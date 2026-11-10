# -*- coding: utf-8 -*-
"""Validate docs/keywords.csv against the site that is actually published.

A keyword list drifts the moment a URL changes. This keeps the twenty tracked
terms pointing at live, canonical pages in the right language.
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / 'docs' / 'keywords.csv'
SITEMAP = ROOT / 'sitemap.xml'
EXPECTED = 39
COLUMNS = ['keyword', 'language', 'intent', 'priority', 'target_url', 'notes']
LANGUAGES = {'it', 'en'}
INTENTS = {'commercial', 'transactional', 'informational'}


def main():
    problems = []
    global CSV_PATH
    if len(sys.argv) > 1:
        CSV_PATH = Path(sys.argv[1]).resolve()
    if not CSV_PATH.exists():
        print('missing %s' % CSV_PATH)
        return 1

    with CSV_PATH.open(encoding='utf-8-sig', newline='') as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != COLUMNS:
            print('header must be: %s' % ', '.join(COLUMNS))
            return 1
        rows = list(reader)

    if len(rows) != EXPECTED:
        problems.append('%d keywords, expected %d' % (len(rows), EXPECTED))

    sitemap = SITEMAP.read_text(encoding='utf-8')
    locs = set(re.findall(r'<loc>(.*?)</loc>', sitemap))
    seen = set()

    for number, row in enumerate(rows, start=2):
        keyword = (row['keyword'] or '').strip()
        language = (row['language'] or '').strip()
        intent = (row['intent'] or '').strip()
        priority = (row['priority'] or '').strip()
        url = (row['target_url'] or '').strip()
        where = 'line %d (%s)' % (number, keyword or 'no keyword')

        if not keyword:
            problems.append('%s: empty keyword' % where)
            continue
        key = (keyword.casefold(), language)
        if key in seen:
            problems.append('%s: duplicate keyword in the same language' % where)
        seen.add(key)

        if language not in LANGUAGES:
            problems.append('%s: language must be it or en' % where)
        if intent not in INTENTS:
            problems.append('%s: intent must be one of %s' % (where, ', '.join(sorted(INTENTS))))
        if priority not in {'1', '2', '3'}:
            problems.append('%s: priority must be 1, 2 or 3' % where)

        if not (url.startswith('/') and url.endswith('/')) or '//' in url[1:] or '://' in url:
            problems.append('%s: target must be a path such as /servizi/seo/' % where)
            continue
        if language == 'en' and not url.startswith('/en/'):
            problems.append('%s: English keyword must point inside /en/' % where)
        if language == 'it' and url.startswith('/en/'):
            problems.append('%s: Italian keyword must not point inside /en/' % where)

        if 'https://www.titechdigital.it' + url not in locs:
            problems.append('%s: %s is not in sitemap.xml' % (where, url))
        page = ROOT / url.strip('/') / 'index.html' if url != '/' else ROOT / 'index.html'
        if not page.exists():
            problems.append('%s: %s does not exist' % (where, page.relative_to(ROOT)))
            continue
        html = page.read_text(encoding='utf-8')
        match = re.search(r'<html[^>]*\blang="([^"]+)"', html)
        page_language = match.group(1)[:2] if match else ''
        if page_language != language:
            problems.append('%s: %s declares lang="%s"' % (where, url, page_language))

    for problem in problems:
        print(problem)
    print('%d keywords, %d live targets, %d problems'
          % (len(rows), len(rows) - sum('does not exist' in p or 'sitemap' in p for p in problems), len(problems)))
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main())
