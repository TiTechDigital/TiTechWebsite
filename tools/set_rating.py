"""Sets the Google rating shown in every footer and declared in the structured data.

The numbers must be the ones on the Google Business Profile, and must be
updated by hand whenever they change: a rating on the site that no longer
matches the profile is exactly the kind of mismatch to avoid.

  - footer of every published page: a visible line linking to the profile
  - aggregateRating on the local business node of the home pages and /novara/
    (the visible line is on the same page, as the guidelines ask)

Usage:  python tools/set_rating.py 5.0 3
        python tools/set_rating.py 4.9 20
        python tools/set_rating.py off        (removes both)
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAP = 'https://maps.app.goo.gl/D2tHJGsZuTfMurwo6'
NODE_PAGES = {'index.html', 'en/index.html', 'novara/index.html'}
ANCHOR = re.compile(r'<a class="m-link-2"[^>]*href="%s"[^>]*>[^<]*</a>' % re.escape(MAP))


def label(rating, count, english):
    if english:
        return '★ %s on Google · %d review%s' % (('%.1f' % rating), count, '' if count == 1 else 's')
    return '★ %s su Google · %d recension%s' % (('%.1f' % rating).replace('.', ','), count, 'e' if count == 1 else 'i')


def main():
    args = sys.argv[1:]
    if args == ['off']:
        rating = count = None
    elif len(args) == 2:
        rating, count = float(args[0]), int(args[1])
        if not (1 <= rating <= 5) or count < 1:
            sys.exit('rating between 1 and 5, count at least 1')
    else:
        sys.exit(__doc__)

    pages = footers = nodes = 0
    for path in sorted(glob.glob(os.path.join(ROOT, '**', 'index.html'), recursive=True)):
        rel = os.path.relpath(path, ROOT).replace(os.sep, '/')
        text = open(path, encoding='utf-8').read()
        original = text
        english = rel.startswith('en/')
        i = text.find('<footer id="footer"')
        if i >= 0:
            head, foot = text[:i], text[i:]
            if rating is None:
                new = '<a class="m-link-2" href="%s" rel="noopener" target="_blank">Google Maps</a>' % MAP
            else:
                new = '<a class="m-link-2" href="%s" rel="noopener" target="_blank">%s</a>' % (MAP, label(rating, count, english))
            foot, n = ANCHOR.subn(new, foot, count=1)
            footers += n
            text = head + foot
        if rel in NODE_PAGES:
            def fix(m):
                nonlocal nodes
                try:
                    data = json.loads(m.group(2))
                except ValueError:
                    return m.group(0)
                changed = False
                for node in data.get('@graph', [data]):
                    if node.get('@id') == 'https://www.titechdigital.it/#localbusiness':
                        if rating is None:
                            changed = node.pop('aggregateRating', None) is not None or changed
                        else:
                            node['aggregateRating'] = {'@type': 'AggregateRating', 'ratingValue': rating,
                                                       'reviewCount': count, 'bestRating': 5, 'worstRating': 1}
                            changed = True
                if not changed:
                    return m.group(0)
                nodes += 1
                return m.group(1) + '\n' + json.dumps(data, ensure_ascii=False, indent=2) + '\n' + m.group(3)
            text = re.sub(r'(<script type="application/ld\+json">)(.*?)(</script>)', fix, text, flags=re.S)
        if text != original:
            open(path, 'w', encoding='utf-8', newline='\n').write(text)
            pages += 1
    print('pages changed: %d, footers: %d, structured-data nodes: %d' % (pages, footers, nodes))


if __name__ == '__main__':
    main()
