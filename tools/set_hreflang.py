"""Give every Italian page the hreflang trio its English twin already declares.

The pairs are read from the English tree instead of typed here, so the two
languages cannot drift apart: the English pages already say which Italian URL
they are the English version of, and this script just answers the call. It also
points the language switch of each Italian page at its twin.
Run: python tools/set_hreflang.py   (re-runable: pages already done are left alone)
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://titechdigital.it'
CANON = re.compile(r'<link rel="canonical" href="([^"]+)">')
IT_ALT = re.compile(r'<link rel="alternate" hreflang="it-IT" href="([^"]+)">')


def file_for(url):
    """map an absolute site URL to a file on disk"""
    path = url.replace(SITE, '').split('#')[0]
    if path.endswith('/'):
        return os.path.join(ROOT, path.lstrip('/'), 'index.html')
    return os.path.join(ROOT, path.lstrip('/'))


def read(path):
    # newline='' keeps whatever line ending the file already uses
    return open(path, encoding='utf-8', newline='').read()


# ---- the pairs, taken from the English side -------------------------------
pairs = {}
for dirpath, _, filenames in os.walk(os.path.join(ROOT, 'en')):
    if 'index.html' not in filenames:
        continue
    path = os.path.join(dirpath, 'index.html')
    raw = read(path)
    canonical, twin = CANON.search(raw), IT_ALT.search(raw)
    if not (canonical and twin):
        print('  ! %s has no canonical or no it-IT alternate' % os.path.relpath(path, ROOT))
        continue
    pairs[twin.group(1)] = canonical.group(1)

print('%d English pages declare %d Italian twins' % (
    sum(1 for d, _, f in os.walk(os.path.join(ROOT, 'en')) if 'index.html' in f), len(pairs)))

# ---- answer them ---------------------------------------------------------
# two jobs per page: the hreflang trio in the head, and a language switch that
# lands on the twin rather than on the English home
patched, already, rewired, missing = [], [], [], []
for it_url in sorted(pairs):
    path = file_for(it_url)
    if not os.path.exists(path):
        missing.append(it_url)
        continue
    raw = read(path)
    en_url = pairs[it_url]
    changed = raw

    # the language switch in the nav is an <a hreflang="en"> too, so the guard
    # has to name the element: only a <link rel="alternate"> is a declaration
    if 'rel="alternate" hreflang="en"' not in changed:
        canonical = CANON.search(changed)
        if not canonical:
            missing.append(it_url + '  (no canonical)')
            continue
        eol = '\r\n' if '\r\n' in changed else '\n'
        trio = ''.join('%s<link rel="alternate" hreflang="%s" href="%s">' % (eol, lang, href)
                       for lang, href in (('it-IT', it_url), ('en', en_url), ('x-default', it_url)))
        changed = changed[:canonical.end()] + trio + changed[canonical.end():]
        patched.append(it_url)
    else:
        already.append(it_url)

    for cls in ('nav__lang', 'menu__lang'):
        before = '<a class="%s" href="/en/"' % cls
        # the switch keeps the root-relative style of the surrounding markup
        after = '<a class="%s" href="%s"' % (cls, en_url.replace(SITE, '') or '/')
        if before in changed:
            changed = changed.replace(before, after)
            if it_url != SITE + '/' and rewired.count(it_url) == 0:
                rewired.append(it_url)

    if changed != raw:
        with open(path, 'w', encoding='utf-8', newline='') as handle:
            handle.write(changed)

for url in patched:
    print('  + %-46s -> %s' % (url, pairs[url]))
if already:
    print('  = hreflang already declared: %d pages' % len(already))
print('  > language switch pointed at the twin: %d pages' % len(rewired))
if missing:
    print('  ! not found on disk: %s' % missing)

# ---- the other direction: Italian pages nobody declared a twin for -------
declared = set(pairs)
print('\nItalian pages with no English twin:')
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in ('en', '.git', '.vercel', 'node_modules')]
    if 'index.html' not in filenames:
        continue
    rel = os.path.relpath(dirpath, ROOT).replace(os.sep, '/')
    slug = '' if rel == '.' else rel + '/'
    url = SITE + '/' + slug
    if url not in declared:
        print('  ', url)
