# -*- coding: utf-8 -*-
"""Read Search Console CSV exports and say what to keep, fix or prune.

Usage:
  python tools/gsc_review.py reports/gsc-2026-11-04/pages.csv
  python tools/gsc_review.py pages.csv queries.csv
  python tools/gsc_review.py pages.csv --min-impressions=100
  python tools/gsc_review.py reports/2026-11/pages.csv --previous=reports/2026-10/pages.csv

Accepts the Italian and English column names of the Search Console export.
Cannibalisation can only be detected when the export has both Query and Page
columns (an API or Looker export); the two separate UI exports cannot show it.
--previous takes the same dimension from the period before and reports movers.
The opportunity band (positions 5-20) is read from every export that has a
position column, because that is where the next clicks usually come from.
"""
import csv
import re
import sys
from collections import defaultdict

ALIASES = {
    'page': {'top pages', 'pagine principali', 'page', 'pages', 'pagina', 'pagine'},
    'query': {'top queries', 'ricerche principali', 'query', 'ricerche', 'ricerca'},
    'clicks': {'clicks', 'clic'},
    'impressions': {'impressions', 'impressioni'},
    'ctr': {'ctr'},
    'position': {'position', 'posizione media', 'posizione', 'average position'},
    'date': {'date', 'data'},
}

BANDS = ((1, 3, 0.10), (4, 10, 0.03), (11, 20, 0.01))
# positions 5-20: seen by enough people that a better page moves the number,
# close enough that the next search result is a realistic target
OPPORTUNITY = (5, 20)
# what the band above pays: (highest position still inside this half, the CTR
# the next half better than it tends to hold)
NEXT_TARGET = ((10, 0.10), (20, 0.03))
# a difference this small is the export rounding, not a trend
MIN_IMPRESSION_DELTA = 50
MIN_CLICK_DELTA = 5


# a separator between groups of exactly three digits is a thousands separator,
# whichever of "." or "," the export happened to use
GROUPS = re.compile(r'^\d{1,3}([.,]\d{3})+$')


def field_map(header):
    found = {}
    for name in header:
        clean = ' '.join((name or '').replace('\ufeff', '').strip().lower().split())
        for key, names in ALIASES.items():
            if clean in names and key not in found:
                found[key] = name
    return found


def number(value):
    text = (value or '').strip().replace('\xa0', '').replace(' ', '')
    if not text:
        return 0.0
    if text.endswith('%'):
        return float(text[:-1].replace(',', '.')) / 100
    return float(text.replace(',', '.'))


def integer(value):
    text = (value or '').strip().replace('\xa0', '').replace(' ', '')
    if not text:
        return 0
    if GROUPS.match(text):
        text = text.replace('.', '').replace(',', '')
    return int(float(text.replace(',', '.')))


def from_sitemap(path):
    """the export lists what Google showed; the sitemap lists what we published.
    The difference is the part of the site that is invisible, which the Search
    Console interface can never tell you because it only ever shows rows"""
    with open(path, encoding='utf-8') as handle:
        return [url.strip() for url in re.findall(r'<loc>([^<]+)</loc>', handle.read())]


def invisible(page_rows, sitemap_path):
    seen = {r['page'].rstrip('/') for r in page_rows if r['page']}
    return ['%s: published, and it has no row at all in the export. Open the indexing '
            'report for this URL: a top-1000 export also truncates, so absence is a hint, '
            'not a verdict.' % url
            for url in from_sitemap(sitemap_path) if url.rstrip('/') not in seen]


def kind_of(found):
    return 'query+page' if 'query' in found and 'page' in found else (
        'queries' if 'query' in found else 'pages')


def parse(path):
    with open(path, encoding='utf-8-sig', newline='', errors='replace') as handle:
        sample = handle.read(4096)
        handle.seek(0)
        delimiter = ';' if sample.count(';') > sample.count(',') else ','
        reader = csv.DictReader(handle, delimiter=delimiter)
        found = field_map(reader.fieldnames or [])
        if not {'clicks', 'impressions'} <= set(found):
            raise ValueError('%s: clicks/impressions columns not found (header: %s)'
                             % (path, reader.fieldnames))
        rows = []
        for raw in reader:
            row = {
                'page': (raw.get(found['page']) or '').strip() if 'page' in found else '',
                'query': (raw.get(found['query']) or '').strip() if 'query' in found else '',
                'clicks': integer(raw.get(found['clicks'])),
                'impressions': integer(raw.get(found['impressions'])),
                'ctr': number(raw.get(found['ctr'])) if 'ctr' in found else 0.0,
                'position': number(raw.get(found['position'])) if 'position' in found else 0.0,
            }
            if row['page'] or row['query']:
                rows.append(row)
        return rows, found


def percent(value):
    return ('%.2f' % (value * 100)).rstrip('0').rstrip('.') + '%'


def section(title, items, limit=15):
    print('\n## ' + title)
    if not items:
        print('\nNone.')
        return
    for line in items[:limit]:
        print('\n- ' + line)
    if len(items) > limit:
        print('\n- ... and %d more in the export.' % (len(items) - limit))


def summarise(rows):
    clicks = sum(r['clicks'] for r in rows)
    impressions = sum(r['impressions'] for r in rows)
    weighted = sum(r['position'] * r['impressions'] for r in rows)
    position = weighted / impressions if impressions else 0
    ctr = clicks / impressions if impressions else 0
    return ('%d clicks, %d impressions, CTR %s, average position %.1f'
            % (clicks, impressions, percent(ctr), position))


def merge(rows, key):
    """one line per page or per query. An export broken down by day repeats every
    page once per day, and an average position only means something weighted by
    the impressions it arrived with"""
    merged = {}
    for r in rows:
        name = r[key]
        if not name:
            continue
        line = merged.setdefault(name, {'name': name, 'clicks': 0,
                                        'impressions': 0, 'weighted': 0.0})
        line['clicks'] += r['clicks']
        line['impressions'] += r['impressions']
        line['weighted'] += r['position'] * r['impressions']
    out = []
    for line in merged.values():
        line['position'] = line['weighted'] / line['impressions'] if line['impressions'] else 0
        line['ctr'] = line['clicks'] / line['impressions'] if line['impressions'] else 0
        out.append(line)
    return out


def opportunity(lines, what):
    """the band the month is won in: not position 40, and not the page you
    already own. What is offered is the order, not a promise of clicks"""
    items = []
    for r in lines:
        if not OPPORTUNITY[0] <= r['position'] <= OPPORTUNITY[1]:
            continue
        floor = next(value for upper, value in NEXT_TARGET if r['position'] <= upper)
        gain = r['impressions'] * (floor - r['ctr'])
        if r['impressions'] < MIN_IMPRESSION_DELTA or gain <= 0:
            continue
        items.append((r['impressions'], '"%s" (%s): position %.1f, CTR %s on %d impressions. '
                      'If it answered as well as the band above, roughly %d more clicks '
                      'in the same period.'
                      % (r['name'], what, r['position'], percent(r['ctr']), r['impressions'],
                         int(round(gain)))))
    items.sort(reverse=True)
    return [line for _, line in items]


def movers(current, previous, what):
    """two exports of the same dimension, one period each. Only lines present in
    both are compared: a page that appears for the first time is new, not rising"""
    before = {r['name']: r for r in previous}
    gains, losses = [], []
    for r in current:
        p = before.get(r['name'])
        if not p:
            continue
        impressions = r['impressions'] - p['impressions']
        clicks = r['clicks'] - p['clicks']
        label = ('"%s" (%s): %d to %d impressions, %d to %d clicks, position %.1f to %.1f'
                 % (r['name'], what, p['impressions'], r['impressions'],
                    p['clicks'], r['clicks'], p['position'], r['position']))
        if impressions >= MIN_IMPRESSION_DELTA:
            gains.append((impressions, label + '. Whatever changed, it worked: do the same to '
                          'a page that is not moving.'))
        if clicks <= -MIN_CLICK_DELTA:
            losses.append((clicks, label + '. Losing clicks while still seen is a snippet '
                           'problem first, a content problem second.'))
    gains.sort(reverse=True)
    losses.sort()
    return ([line for _, line in gains], [line for _, line in losses])


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    options = [a for a in sys.argv[1:] if a.startswith('--')]
    minimum = 50
    previous_path = ''
    sitemap_path = 'sitemap.xml'
    for option in options:
        if option.startswith('--min-impressions='):
            try:
                minimum = int(option.split('=', 1)[1])
            except ValueError:
                print('--min-impressions needs a number')
                return 2
        elif option.startswith('--previous='):
            previous_path = option.split('=', 1)[1]
        elif option.startswith('--sitemap='):
            sitemap_path = option.split('=', 1)[1]
        else:
            print('unknown option: ' + option)
            return 2
    if not args:
        print('\n'.join(__doc__.strip().splitlines()[2:4]))
        return 2

    rows, page_rows, query_rows = [], [], []
    page_files, query_files = [], []
    for path in args:
        try:
            parsed, found = parse(path)
        except (OSError, ValueError) as error:
            print(error)
            return 1
        kind = kind_of(found)
        print('# %s - %d rows (%s)' % (path, len(parsed), kind))
        print('  Totals: ' + summarise(parsed))
        rows.extend(parsed)
        if kind in ('pages', 'query+page'):
            page_files.append(path)
            page_rows.extend(parsed)
        if kind in ('queries', 'query+page'):
            query_files.append(path)
            query_rows.extend(parsed)

    if len(page_files) > 1 or len(query_files) > 1:
        print('\nWARNING: more than one export feeds the same dimension, so the lines below add '
              'the same traffic together. Pass the older period with --previous instead.')

    per_page = merge(page_rows, 'page')
    per_query = merge(query_rows, 'query')

    dead = ['%s: 0 impressions in the period. Check the indexing report before touching it; '
            'a hub or a legal page stays even without traffic.' % r['name']
            for r in sorted(per_page, key=lambda r: r['name']) if r['impressions'] == 0]

    ctr = []
    for r in per_page:
        if r['impressions'] < minimum:
            continue
        for low, high, floor in BANDS:
            if low <= r['position'] <= high and r['ctr'] < floor:
                ctr.append('%s: position %.1f, CTR %s on %d impressions. The page is seen and not '
                           'chosen: rewrite title and description before the body.'
                           % (r['name'], r['position'], percent(r['ctr']), r['impressions']))
                break
    ctr.sort()

    quiet = ['%s: %d clicks on %d impressions. Review, do not delete: it may be the only page '
             'for that intent.' % (r['name'], r['clicks'], r['impressions'])
             for r in per_page if r['clicks'] < 2 and r['impressions'] > 0]

    query_ctr = ['"%s": position %.1f, CTR %s on %d impressions. The query is close; the answer in '
                 'the snippet is not.' % (r['name'], r['position'], percent(r['ctr']), r['impressions'])
                 for r in per_query
                 if r['position'] <= 10 and r['ctr'] < 0.02 and r['impressions'] >= 30]

    paired = defaultdict(set)
    for r in rows:
        if r['query'] and r['page'] and r['impressions'] >= 10:
            paired[r['query']].add(r['page'])
    shared = ['"%s": %d pages: %s. Pick one target, link the others to it, merge or rewrite '
              'the rest.' % (query, len(pages), ', '.join(sorted(pages)))
              for query, pages in sorted(paired.items()) if len(pages) > 1]

    section('Pages with no impressions', dead)
    if page_rows:
        try:
            section('Published pages missing from the export',
                    invisible(page_rows, sitemap_path))
        except OSError:
            print('\n## Published pages missing from the export\n\nSkipped: %s not found, '
                  'so the export cannot be diffed against what the site publishes.'
                  % sitemap_path)
    section('Opportunity band, positions 5-20',
            opportunity(per_page, 'page') + opportunity(per_query, 'query'))
    section('CTR below the position band (min %d impressions)' % minimum, ctr)
    section('Queries in the top 10 with a low CTR', query_ctr)
    section('Queries served by more than one page', shared)
    section('Pages with almost no clicks', quiet)

    if previous_path:
        try:
            before_rows, before_found = parse(previous_path)
        except (OSError, ValueError) as error:
            print(error)
            return 1
        before_kind = kind_of(before_found)
        print('\n# %s - previous period, %d rows (%s)'
              % (previous_path, len(before_rows), before_kind))
        print('  Totals: ' + summarise(before_rows))
        compared = {'query+page': ('page', 'query'), 'pages': ('page',), 'queries': ('query',)}
        dimensions = [d for d in compared[before_kind]
                      if (d == 'page' and page_rows) or (d == 'query' and query_rows)]
        if not dimensions:
            print('\nThe previous export reports a dimension this period does not have. '
                  'Export the same report twice, once per period.')
            return 0
        gains, losses = [], []
        for key in dimensions:
            current = per_page if key == 'page' else per_query
            moved = movers(current, merge(before_rows, key), key)
            gains += moved[0]
            losses += moved[1]
        section('Gaining impressions since the previous period', gains)
        section('Losing clicks since the previous period', losses)

    print('\n**Rule of thumb:** fix the snippet first, then the body. Merge only after 90 days of '
          'stable data, and never delete a page that has produced a real enquiry in the last year.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
