"""Rewrite sitemap.xml so every entry carries the hreflang alternates of its
language pair, the way the pages themselves do.

Ordering is taken from the sitemap that is already on disk (so the Italian tree
keeps the sequence it has always had), the English block is appended in the same
relative order, and any Italian page found on disk but absent from the file is
appended at the end instead of being silently dropped. A page without an English
twin is reported.
Run: python tools/build_sitemap.py
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://www.titechdigital.it'
LASTMOD = '2026-11-04'
CANON = re.compile(r'<link rel="canonical" href="([^"]+)">')
IT_ALT = re.compile(r'<link rel="alternate" hreflang="it-IT" href="([^"]+)">')


# ---- the pairs, again read from the English pages -------------------------
pairs = {}
english = []
for dirpath, _, filenames in os.walk(os.path.join(ROOT, 'en')):
    if 'index.html' not in filenames:
        continue
    raw = open(os.path.join(dirpath, 'index.html'), encoding='utf-8').read()
    canonical, twin = CANON.search(raw), IT_ALT.search(raw)
    if canonical and twin:
        pairs[twin.group(1)] = canonical.group(1)
        english.append(canonical.group(1))
english.sort(key=lambda u: (u.count('/'), u))

# ---- the order the Italian tree already uses in the sitemap --------------
existing = re.findall(r'<loc>([^<]+)</loc>', open(os.path.join(ROOT, 'sitemap.xml'), encoding='utf-8').read())
italian = [u for u in existing if u in pairs]

# New Italian pages (the blog, for example) are appended at the end of the
# Italian block instead of being dropped: the sitemap must list every page
# that exists on disk, or the checker correctly reports a ghost.
added = sorted((u for u in pairs if u not in italian), key=lambda u: (u.count('/'), u))
italian += added

# every page on disk, to catch one that is not in the file at all
stale = [u for u in existing if u not in italian + english]

entries = []
for url in italian + english:
    # pairs is keyed by the Italian URL, so an Italian loc knows its twin at
    # once and an English loc has to look up which key points at it
    if url in pairs:
        it, en = url, pairs[url]
    else:
        it = [k for k, v in pairs.items() if v == url][0]
        en = url
    entries.append(
        '  <url>\n'
        '    <loc>%s</loc>\n'
        '    <lastmod>%s</lastmod>\n'
        '    <xhtml:link rel="alternate" hreflang="it-IT" href="%s"/>\n'
        '    <xhtml:link rel="alternate" hreflang="en" href="%s"/>\n'
        '    <xhtml:link rel="alternate" hreflang="x-default" href="%s"/>\n'
        '  </url>' % (url, LASTMOD, it, en, it))

xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
       '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
       '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
       + '\n'.join(entries) + '\n</urlset>\n')

open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8', newline='\n').write(xml)
print('%d urls: %d italian + %d english' % (len(entries), len(italian), len(english)))
if added:
    print('+ added at the end of the Italian block: %s' % added)
if stale:
    print('! dropped, no English pair: %s' % stale)
