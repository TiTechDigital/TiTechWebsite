# -*- coding: utf-8 -*-
"""Builds the bilingual (Italian + English) articles of the SEO editorial calendar.

Every article is written once with an Italian and an English version (own text, own links,
own slug), built on the real shell of the maintenance article of each language, and written to
_scheduled/ with an entry in _scheduled/manifest.json. tools/publish_scheduled.py moves each one
into place on its publication date and registers it (blog index, sitemap), so nothing goes live
early and nothing needs doing by hand.

Run: python tools/build_calendar_articles.py
"""
import html
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://www.titechdigital.it'
SCHED = os.path.join(ROOT, '_scheduled')
SHELL = {'it': 'blog/manutenzione-sito-web/index.html', 'en': 'en/blog/website-maintenance/index.html'}
SHELL_TWIN = {'it': '/en/blog/website-maintenance/', 'en': '/blog/manutenzione-sito-web/'}
MONTHS = {'it': ['gennaio', 'febbraio', 'marzo', 'aprile', 'maggio', 'giugno', 'luglio', 'agosto', 'settembre', 'ottobre', 'novembre', 'dicembre'],
          'en': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']}
L = {
    'it': dict(home='/', blog='/blog/', crumbs='Percorso', brief='In breve', toc='In questa pagina', faq='Domande frequenti', more='Continua a leggere',
               write='Scrivi a TiTech', talk='Parliamo del tuo progetto', contact='/contatti/', work='/lavori/', work_label='Vedi il nostro portfolio',
               author='/chi-siamo/#enea-muja', role='CEO, TiTech Digital · %d min di lettura', updated='Aggiornato il %s', lang='it-IT', section='Blog'),
    'en': dict(home='/en/', blog='/en/blog/', crumbs='Breadcrumb', brief='In brief', toc='On this page', faq='Frequently asked questions', more='Keep reading',
               write='Write to TiTech', talk='Talk about your project', contact='/en/contact/', work='/en/work/', work_label='See our work',
               author='/en/about/#enea-muja', role='CEO, TiTech Digital · %d min read', updated='Updated %s', lang='en', section='Blog'),
}


def esc(t):
    return html.escape(t, quote=False)


def strip_tags(t):
    return html.unescape(re.sub(r'<[^>]+>', '', t))


def pretty_date(iso, lang):
    y, m, d = iso.split('-')
    return ('%d %s %s' % (int(d), MONTHS[lang][int(m) - 1], y))


def load_shell(lang):
    raw = open(os.path.join(ROOT, SHELL[lang]), encoding='utf-8').read()
    return dict(
        head=raw[:raw.index('<script type="application/ld+json">')],
        org=re.search(r'\{\s*"@type": "Organization".*?\n    \},', raw, re.S).group(0).rstrip(','),
        person=re.search(r'\{\s*"@type": "Person".*?\n    \},', raw, re.S).group(0).rstrip(','),
        header=raw[raw.index('<body>'):raw.index('<main id="main">')],
        footer=raw[raw.index('<footer id="footer"'):])


def paths(a):
    return {lang: ('/blog/%s/' if lang == 'it' else '/en/blog/%s/') % a[lang]['slug'] for lang in ('it', 'en')}


def build(a, lang, shell):
    d = a[lang]
    lb = L[lang]
    twin = 'en' if lang == 'it' else 'it'
    P = paths(a)
    url = SITE + P[lang]
    head = shell['head']
    head = re.sub(r'<title>.*?</title>', '<title>%s</title>' % esc(d['title']), head, flags=re.S)
    head = re.sub(r'(<meta name="description" content=")[^"]*(")', r'\g<1>%s\g<2>' % html.escape(d['description']), head)
    head = re.sub(r'(<meta property="og:title" content=")[^"]*(")', r'\g<1>%s\g<2>' % html.escape(d['title'] + ' | TiTech Digital'), head)
    head = re.sub(r'(<meta property="og:description" content=")[^"]*(")', r'\g<1>%s\g<2>' % html.escape(d['description']), head)
    head = re.sub(r'(<link rel="canonical" href=")[^"]*(")', r'\g<1>%s\2' % url, head)
    head = re.sub(r'(<meta property="og:url" content=")[^"]*(")', r'\g<1>%s\2' % url, head)
    head = re.sub(r'\s*<link rel="alternate" hreflang="[^"]*" href="[^"]*">', '', head)
    head = re.sub(r'(<link rel="canonical" href="[^"]*">)', lambda m: m.group(1) +
                  '\n<link rel="alternate" hreflang="it-IT" href="%s%s">\n<link rel="alternate" hreflang="en" href="%s%s">\n<link rel="alternate" hreflang="x-default" href="%s%s">'
                  % (SITE, P['it'], SITE, P['en'], SITE, P['it']), head, count=1)
    head = re.sub(r'(article:published_time" content=")[^"]*(")', r'\g<1>%s\2' % a['pub'], head)
    head = re.sub(r'(article:modified_time" content=")[^"]*(")', r'\g<1>%s\2' % a['pub'], head)
    head = re.sub(r'(article:section" content=")[^"]*(")', r'\g<1>%s\2' % html.escape(d['section']), head)

    faq_nodes = [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': strip_tags(ans)}} for q, ans in d['faq']]
    graph = [
        json.loads(shell['org']),
        {'@type': 'BreadcrumbList', '@id': url + '#breadcrumb', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE + lb['home']},
            {'@type': 'ListItem', 'position': 2, 'name': 'Blog', 'item': SITE + lb['blog']},
            {'@type': 'ListItem', 'position': 3, 'name': d['title'], 'item': url}]},
        json.loads(shell['person']),
        {'@type': 'BlogPosting', 'image': SITE + '/assets/img/og-card-%s-1200x630.png' % ('it' if lang == 'it' else 'en'), '@id': url + '#article',
         'headline': d['title'], 'description': d['description'], 'url': url, 'mainEntityOfPage': {'@id': url + '#webpage'},
         'inLanguage': lb['lang'], 'datePublished': a['pub'], 'dateModified': a['pub'],
         'author': {'@id': SITE + '/#enea-muja'}, 'publisher': {'@id': SITE + '/#organization'},
         'articleSection': d['section'], 'keywords': d['keywords'],
         'isPartOf': {'@type': 'Blog', '@id': SITE + '/blog/#blog', 'name': 'TiTech Digital Blog', 'url': SITE + lb['blog']}},
        {'@type': 'WebPage', '@id': url + '#webpage', 'url': url, 'name': d['title'], 'inLanguage': lb['lang'],
         'author': {'@id': SITE + '/#enea-muja'}, 'breadcrumb': {'@id': url + '#breadcrumb'}, 'about': {'@id': url + '#article'},
         'datePublished': a['pub'], 'dateModified': a['pub']},
        {'@type': 'FAQPage', '@id': url + '#faq', 'isPartOf': {'@id': url + '#webpage'}, 'inLanguage': lb['lang'], 'mainEntity': faq_nodes},
    ]
    ld = '<script type="application/ld+json">\n' + json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False, indent=2) + '\n</script>\n</head>\n'

    header = shell['header'].replace(SHELL_TWIN[lang], P[twin])
    takeaways = '\n'.join('        <li><strong>%s</strong> %s</li>' % (esc(t), esc(x)) for t, x in d['takeaways'])
    toc = '\n'.join('        <li><a href="#%s"><span class="toc__num">%02d</span><span>%s</span></a></li>' % (sid, i + 1, esc(t))
                    for i, (sid, t, _, _) in enumerate(d['sections']))
    sections = '\n\n'.join(
        '    <section class="sect" id="%s" aria-labelledby="%s-title">\n      <div class="sect__top">\n        <h2 class="m-text-4" id="%s-title">%s</h2>\n        <p class="m-text">%s</p>\n      </div>\n      <div class="prose">\n%s\n      </div>\n    </section>'
        % (sid, sid, sid, esc(t), esc(lead), '\n'.join('        ' + p for p in body)) for sid, t, lead, body in d['sections'])
    faq = '\n'.join('        <details class="faq__item"><summary class="m-text-7">%s<span class="faq__mark" aria-hidden="true"></span></summary><p class="m-text faq__answer">%s</p></details>' % (esc(q), ans) for q, ans in d['faq'])
    cards = '\n'.join('        <article class="card card--link">\n          <h3 class="card__title"><a href="%s">%s</a></h3>\n          <p class="card__text">%s</p>\n        </article>' % (u, esc(t), x) for u, t, x in d['related'])
    link_url, link_label = d['cta_link']
    arrow = '<svg class="m-link__arrow" viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8h11M9 3.5 13.5 8 9 12.5"/></svg>'
    main = '''<main id="main">
  <div class="shell page">
    <nav aria-label="%(crumbs_label)s">
      <ol class="crumbs">
        <li><a href="%(home)s">Home</a></li>
        <li><a href="%(blog)s">Blog</a></li>
        <li aria-current="page">%(title)s</li>
      </ol>
    </nav>
    <div class="head">
      <p class="m-eyebrow">Blog · %(section)s</p>
      <h1 class="m-text-3 head__title">%(title)s<span class="m-dot" aria-hidden="true"></span></h1>
      <p class="m-text-5 head__lead">%(lead)s</p>
      <div class="head__actions">
        <a class="m-btn" href="%(contact)s"><span>%(talk)s</span></a>
        <a class="m-link" href="%(link_url)s"><span class="m-link__label">%(link_label)s</span>%(arrow)s</a>
      </div>
      <p class="byline"><a class="byline__name" href="%(author)s" style="color:inherit">Enea Muja</a><span class="byline__role">%(role)s</span><time class="byline__date" datetime="%(iso)s">%(updated)s</time></p>
    </div>

    <aside class="takeaways" aria-labelledby="takeaways-title">
      <h2 class="m-text-7" id="takeaways-title">%(brief)s</h2>
      <ul>
%(takeaways)s
      </ul>
    </aside>

    <nav class="toc" aria-label="%(toc_label)s">
      <ol>
%(toc)s
      </ol>
    </nav>

%(sections)s

    <section class="sect" id="faq" aria-labelledby="faq-title">
      <div class="sect__top">
        <h2 class="m-text-4" id="faq-title">%(faq_title)s</h2>
      </div>
      <div class="faq">
%(faq)s
      </div>
    </section>

    <section class="sect" id="%(rel_id)s" aria-labelledby="%(rel_id)s-title">
      <div class="sect__top">
        <h2 class="m-text-4" id="%(rel_id)s-title">%(more)s</h2>
      </div>
      <div class="cards">
%(cards)s
      </div>
    </section>

    <section class="sect" aria-labelledby="cta-title">
      <div class="cta">
        <h2 class="m-text-4 cta__title" id="cta-title">%(cta_title)s<span class="m-dot" aria-hidden="true"></span></h2>
        <p class="m-text">%(cta_text)s</p>
        <div class="cta__actions">
          <a class="m-btn-2" href="%(contact)s"><span>%(write)s</span></a>
          <a class="m-link" href="%(work)s" style="color:inherit"><span class="m-link__label">%(work_label)s</span>%(arrow)s</a>
        </div>
      </div>
    </section>
  </div>
</main>
''' % {'crumbs_label': lb['crumbs'], 'home': lb['home'], 'blog': lb['blog'], 'title': esc(d['title']), 'section': esc(d['section']),
       'lead': esc(d['lead']), 'contact': lb['contact'], 'talk': lb['talk'], 'link_url': link_url, 'link_label': esc(link_label), 'arrow': arrow,
       'author': lb['author'], 'role': lb['role'] % d['minutes'], 'iso': a['pub'], 'updated': lb['updated'] % pretty_date(a['pub'], lang),
       'brief': lb['brief'], 'takeaways': takeaways, 'toc_label': lb['toc'], 'toc': toc, 'sections': sections, 'faq_title': lb['faq'], 'faq': faq,
       'more': lb['more'], 'cards': cards, 'cta_title': esc(d['cta_title']), 'cta_text': esc(d['cta_text']), 'write': lb['write'],
       'work': lb['work'], 'work_label': lb['work_label'], 'rel_id': 'correlati' if a.get('en_only') else 'related'}
    return head + ld + header + main + shell['footer']


def write_all(articles):
    shells = {lang: load_shell(lang) for lang in ('it', 'en')}
    manifest_path = os.path.join(SCHED, 'manifest.json')
    manifest = json.load(open(manifest_path, encoding='utf-8')) if os.path.exists(manifest_path) else []
    done = {m['day'] for m in manifest}
    for a in articles:
        P = paths(a)
        for lang in (('en',) if a.get('en_only') else ('it', 'en')):
            out = os.path.join(SCHED, P[lang].strip('/'))
            os.makedirs(out, exist_ok=True)
            open(os.path.join(out, 'index.html'), 'w', encoding='utf-8', newline='\n').write(build(a, lang, shells[lang]))
            words = len(re.sub(r'<[^>]+>', ' ', open(os.path.join(out, 'index.html'), encoding='utf-8').read().split('<main')[1].split('</main>')[0]).split())
            print('%s  %s  %s  (%d words)' % (a['pub'], lang, P[lang], words))
        keys = ('slug', 'title', 'description', 'section', 'minutes', 'card')
        entry = {'day': a['day'], 'pub': a['pub'], 'slot': a['slot'],
                 'it': {'slug': a['it']['slug']} if a.get('en_only') else {k: a['it'][k] for k in keys},
                 'en': {k: a['en'][k] for k in keys}}
        if a.get('en_only'):
            entry['en_only'] = True
        manifest = [m for m in manifest if m['day'] != a['day']] + [entry]
    manifest.sort(key=lambda m: (m['pub'], m['slot'], m['day']))
    open(manifest_path, 'w', encoding='utf-8', newline='\n').write(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    import calendar_content, calendar_content_b, calendar_content_c, calendar_content_d, calendar_content_e, calendar_content_f
    allarticles = []
    for mod in (calendar_content, calendar_content_b, calendar_content_c, calendar_content_d, calendar_content_e, calendar_content_f):
        allarticles += mod.ARTICLES
    write_all(allarticles)
