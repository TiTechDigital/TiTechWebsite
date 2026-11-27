# -*- coding: utf-8 -*-
"""Publishes the scheduled articles whose date has come.

Articles waiting for their day live in _scheduled/ (never deployed: .vercelignore skips folders
starting with an underscore) with an entry in _scheduled/manifest.json. For each entry due today
or earlier this script moves the Italian and English pages into blog/ and en/blog/, adds a card and
a ListItem to both blog indexes and both URLs to sitemap.xml, and removes the entry.

A GitHub Action runs it every morning (.github/workflows/publish-scheduled.yml); it can also be run
by hand:   python tools/publish_scheduled.py [--today 2026-11-27]
"""
import datetime
import html
import json
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://www.titechdigital.it'
SCHED = os.path.join(ROOT, '_scheduled')
MANIFEST = os.path.join(SCHED, 'manifest.json')


def urlpath(lang, slug):
    return ('/blog/%s/' if lang == 'it' else '/en/blog/%s/') % slug


def register_index(lang, m):
    f = os.path.join(ROOT, 'blog', 'index.html') if lang == 'it' else os.path.join(ROOT, 'en', 'blog', 'index.html')
    s = open(f, encoding='utf-8').read()
    d = m[lang]
    path = urlpath(lang, d['slug'])
    if path in s:
        return False
    start = s.index('<div class="cards cards--posts">')
    end = s.index('</div>', start)
    line_start = s.rfind('\n', 0, end) + 1
    first = re.search(r'^( *)<article class="card card--link">', s[start:], re.M)
    ind = first.group(1) if first else '        '
    card = ('%(i)s<article class="card card--link">\n%(i)s  <p class="card__meta">%(sec)s · %(min)d min</p>\n'
            '%(i)s  <h3 class="card__title"><a href="%(path)s">%(title)s</a></h3>\n%(i)s  <p class="card__text">%(card)s</p>\n%(i)s</article>\n'
            % {'i': ind, 'sec': html.escape(d['section'], quote=False), 'min': d['minutes'], 'path': path,
               'title': html.escape(d['title'], quote=False), 'card': html.escape(d['card'], quote=False)})
    s = s[:line_start] + card + s[line_start:]

    # structured data: one more item in the list of posts
    m_ld = re.search(r'(<script type="application/ld\+json">)(.*?)(</script>)', s, re.S)
    data = json.loads(m_ld.group(2))

    def find_list(x):
        if isinstance(x, dict):
            if x.get('@type') == 'ItemList' and any(isinstance(i.get('item'), dict) and i['item'].get('@type') == 'BlogPosting' for i in x.get('itemListElement', [])):
                return x
            for v in x.values():
                r = find_list(v)
                if r:
                    return r
        elif isinstance(x, list):
            for v in x:
                r = find_list(v)
                if r:
                    return r
        return None
    lst = find_list(data)
    if lst is not None:
        lst['itemListElement'].append({'@type': 'ListItem', 'position': len(lst['itemListElement']) + 1,
                                       'item': {'@type': 'BlogPosting', '@id': SITE + path + '#article', 'headline': d['title'], 'url': SITE + path}})
        s = s[:m_ld.start(2)] + '\n' + json.dumps(data, ensure_ascii=False, indent=2) + '\n' + s[m_ld.end(2):]
    open(f, 'w', encoding='utf-8', newline='\n').write(s)
    return True


def link_existing_italian_page(m):
    """An English twin of a page that already existed in Italian: the Italian page and its sitemap entry learn about it."""
    it_path, en_path = urlpath('it', m['it']['slug']), urlpath('en', m['en']['slug'])
    page = os.path.join(ROOT, it_path.strip('/'), 'index.html')
    s = open(page, encoding='utf-8').read()
    en_url = SITE + en_path
    if 'hreflang="en" href="%s"' % en_url not in s:
        s = s.replace('<link rel="alternate" hreflang="x-default"', '<link rel="alternate" hreflang="en" href="%s">\n<link rel="alternate" hreflang="x-default"' % en_url, 1)
    s = re.sub(r'(<a class="(?:nav__lang|menu__lang)" href=")/en/blog/(" hreflang="en")', lambda x: x.group(1) + en_path + x.group(2), s)
    open(page, 'w', encoding='utf-8', newline='\n').write(s)
    f = os.path.join(ROOT, 'sitemap.xml')
    t = open(f, encoding='utf-8').read()
    it_loc = '<loc>%s</loc>' % (SITE + it_path)
    i = t.index(it_loc)
    j = t.index('</url>', i)
    if 'hreflang="en"' not in t[i:j]:
        t = t[:j] + '    <xhtml:link rel="alternate" hreflang="en" href="%s"/>\n  ' % en_url + t[j:]
    open(f, 'w', encoding='utf-8', newline='\n').write(t)


def register_sitemap(m):
    f = os.path.join(ROOT, 'sitemap.xml')
    s = open(f, encoding='utf-8').read()
    it, en = SITE + urlpath('it', m['it']['slug']), SITE + urlpath('en', m['en']['slug'])
    if en in s:
        return
    if m.get('en_only'):
        link_existing_italian_page(m)
        s = open(f, encoding='utf-8').read()
    rows = ''
    for loc in ((en,) if m.get('en_only') else (it, en)):
        rows += ('  <url>\n    <loc>%s</loc>\n    <lastmod>%s</lastmod>\n'
                 '    <xhtml:link rel="alternate" hreflang="it-IT" href="%s"/>\n    <xhtml:link rel="alternate" hreflang="en" href="%s"/>\n'
                 '    <xhtml:link rel="alternate" hreflang="x-default" href="%s"/>\n  </url>\n' % (loc, m['pub'], it, en, it))
    open(f, 'w', encoding='utf-8', newline='\n').write(s.replace('</urlset>', rows + '</urlset>'))


def publish(today):
    if not os.path.exists(MANIFEST):
        print('nothing scheduled')
        return []
    manifest = json.load(open(MANIFEST, encoding='utf-8'))
    due = [m for m in manifest if m['pub'] <= today]
    left = [m for m in manifest if m['pub'] > today]
    done = []
    for m in sorted(due, key=lambda x: (x['pub'], x['slot'], x['day'])):
        ok = True
        for lang in (('en',) if m.get('en_only') else ('it', 'en')):
            rel = urlpath(lang, m[lang]['slug']).strip('/')
            src, dst = os.path.join(SCHED, rel), os.path.join(ROOT, rel)
            if os.path.exists(dst):
                print('already published, skipped: /%s/' % rel)
                continue
            if not os.path.exists(os.path.join(src, 'index.html')):
                print('MISSING FILE for the due article: %s' % src)
                ok = False
                continue
            shutil.move(src, dst)
        if ok:
            if not m.get('en_only'):
                register_index('it', m)
            register_index('en', m)
            register_sitemap(m)
            done.append(m)
            print('published day %d: %s | %s' % (m['day'], m['it'].get('title', '(existing Italian page)'), m['en']['title']))
        else:
            left.append(m)
    open(MANIFEST, 'w', encoding='utf-8', newline='\n').write(json.dumps(sorted(left, key=lambda x: (x['pub'], x['slot'], x['day'])), ensure_ascii=False, indent=2) + '\n')
    # empty folders left behind in _scheduled
    for base, dirs, files in os.walk(SCHED, topdown=False):
        if base != SCHED and not os.listdir(base):
            os.rmdir(base)
    return done


if __name__ == '__main__':
    today = datetime.date.today().isoformat()
    if '--today' in sys.argv:
        today = sys.argv[sys.argv.index('--today') + 1]
    done = publish(today)
    print('%d published, %s' % (len(done), today))
