# -*- coding: utf-8 -*-
"""Builds the Albanian site (al/) for titech.al from the English pages.

The pages keep the English design, styles and animations; every visible string
goes through tools/al_strings.py, and the build stops if one is missing, so no
English text can slip into the Albanian site. Links to pages that are not built
yet fall back to the English page on titechdigital.it (see PENDING below).

al/ is a self-contained Vercel project: create a second Vercel project on the
same repository with Root Directory = al, and attach titech.al to it.

Run: python tools/build_albanian_site.py
"""
import glob
import html
import json
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from al_strings import SQ

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'al')
BASE = 'https://www.titech.al'
IT = 'https://www.titechdigital.it'

# English page -> (file under al/, public path, Italian twin, English twin)
PAGES = {
    'en/index.html': ('index.html', '/', '/', '/en/'),
    'en/contact/index.html': ('kontakt/index.html', '/kontakt/', '/contatti/', '/en/contact/'),
}
# English public path -> Albanian public path, for the pages built so far
BUILT = {'/en/': '/', '/en/contact/': '/kontakt/'}

NOISE = re.compile(r'^[\W\d_]*$|@|^\+?\d')


def sq_url(en_path):
    """Albanian URL for an English path, or the English page on the Italian site while it is pending."""
    clean = en_path.split('#')[0]
    frag = en_path[len(clean):]
    if clean in BUILT:
        return BUILT[clean] + frag
    return IT + clean + frag


def translate_text(raw, misses, where):
    text = html.unescape(raw).strip()
    if not text or NOISE.match(text):
        return raw
    if text in SQ:
        lead = raw[:len(raw) - len(raw.lstrip())]
        trail = raw[len(raw.rstrip()):]
        return lead + html.escape(SQ[text], quote=False) + trail
    misses.add((where, text))
    return raw


def translate_attr(value, misses, where):
    text = html.unescape(value).strip()
    if not text or NOISE.match(text):
        return value
    if text in SQ:
        return html.escape(SQ[text], quote=True)
    misses.add((where, text))
    return value


def rewrite_urls(s):
    # absolute English pages of the Italian site
    def abs_en(m):
        path = m.group(1)
        return (BASE + BUILT[path]) if path in BUILT else (IT + path)
    s = re.sub(r'https://www\.titechdigital\.it(/en/(?:[a-z0-9\-]+/)*)', abs_en, s)
    # root-relative English links
    s = re.sub(r'href="(/en/(?:[a-z0-9\-]+/)*)(#[^"]*)?"', lambda m: 'href="%s"' % sq_url(m.group(1) + (m.group(2) or '')), s)
    s = s.replace('href="/en/"', 'href="%s"' % sq_url('/en/'))
    # the language switcher: Italian
    s = re.sub(r'(<a class="(?:nav__lang|menu__lang)" href=")/(")', r'\g<1>%s/\2' % IT, s)
    # relative asset paths
    s = s.replace('../assets/', '/assets/')
    # WhatsApp: the prefilled message in Albanian
    s = re.sub(r'(https://wa\.me/393509205365)\?text=[^"\s]*',
               r'\1?text=P%C3%ABrsh%C3%ABndetje%20TiTech%2C%20ju%20shkruaj%20nga%20faqja%20juaj.%20Do%20t%C3%AB%20doja%20t%C3%AB%20flisja%20p%C3%ABr%20projektin%20tim.', s)
    return s


def translate_json(block, misses, where):
    m = re.match(r'(<script[^>]*>)(.*?)(</script>)', block, re.S)
    try:
        data = json.loads(m.group(2))
    except ValueError:
        return block
    skip = {'@id', '@type', '@context', 'url', 'item', 'email', 'telephone', 'vatID', 'addressLocality', 'addressCountry',
            'contentUrl', 'image', 'sameAs', 'contactType', 'areaServed'}

    def walk(x, key=None):
        if isinstance(x, dict):
            return {k: walk(v, k) for k, v in x.items()}
        if isinstance(x, list):
            return [walk(v, key) for v in x]
        if isinstance(x, str):
            if key in skip or not re.search(r'[A-Za-z]{3}', x) or x.startswith('http'):
                return x
            if x in ('it', 'en', 'it-IT'):
                return x
            if x in SQ:
                return SQ[x]
            if x in ('TiTech Digital', 'TiTech', 'Novara', 'SEO'):
                return x
            misses.add((where + ' [json-ld]', x))
            return x
        return x
    data = walk(data)

    def langs(x):
        if isinstance(x, dict):
            for k, v in list(x.items()):
                if k == 'inLanguage' and isinstance(v, list):
                    x[k] = ['sq-AL'] + [i for i in v if i != 'sq-AL']
                elif k in ('knowsLanguage', 'availableLanguage') and isinstance(v, list):
                    x[k] = ['sq'] + [i for i in v if i != 'sq']
                elif k == 'areaServed' and isinstance(v, list):
                    x[k] = ['AL'] + [i for i in v if i != 'AL']
                elif k == 'areaServed':
                    x[k] = v
                else:
                    langs(v)
        elif isinstance(x, list):
            for i in x:
                langs(i)
    langs(data)
    out = json.dumps(data, ensure_ascii=False, indent=2)
    out = rewrite_urls(out)
    return m.group(1) + '\n' + out + '\n' + m.group(3)


def build_page(src_rel, dest_rel, path, it_path, en_path, misses):
    s = open(os.path.join(ROOT, src_rel), encoding='utf-8').read()
    parts = re.split(r'(<script\b.*?</script>|<style\b.*?</style>)', s, flags=re.S | re.I)
    out = []
    for p in parts:
        low = p[:200].lower()
        if p.lower().startswith('<script') and 'application/ld+json' in low:
            out.append(translate_json(p, misses, dest_rel))
        elif p.lower().startswith('<script') or p.lower().startswith('<style'):
            out.append(rewrite_urls(p))
        else:
            p = re.sub(r'>([^<>]+)<', lambda m: '>' + translate_text(m.group(1), misses, dest_rel) + '<', p)
            p = re.sub(r'\b(alt|aria-label|placeholder|title|data-msg-[a-z]+)="([^"]*)"',
                       lambda m: '%s="%s"' % (m.group(1), translate_attr(m.group(2), misses, dest_rel)), p)
            p = re.sub(r'(<meta\b[^>]*?\bcontent=")([^"]*)(")',
                       lambda m: m.group(1) + (translate_attr(m.group(2), misses, dest_rel)
                                               if re.search(r'name="(description|twitter:image:alt)"|property="og:(title|description|image:alt)"', m.group(0))
                                               else m.group(2)) + m.group(3), p)
            out.append(rewrite_urls(p))
    s = ''.join(out)
    # the chatbot answers in Italian and sends the conversation to a third-party host: not on the Albanian site
    s = re.sub(r'<script src="https://titechwebsite-chatbot\.onrender\.com/[^"]*"[^>]*></script>\s*', '', s)
    s = s.replace('<html lang="en">', '<html lang="sq">', 1)
    s = s.replace('og:locale" content="en_US"', 'og:locale" content="sq_AL"')
    url = BASE + path
    s = re.sub(r'(<link rel="canonical" href=")[^"]*(")', r'\g<1>%s\2' % url, s)
    s = re.sub(r'(<meta property="og:url" content=")[^"]*(")', r'\g<1>%s\2' % url, s)
    s = re.sub(r'\s*<link rel="alternate" hreflang="[^"]*" href="[^"]*">', '', s)
    alts = ('\n<link rel="alternate" hreflang="sq-AL" href="%s">\n<link rel="alternate" hreflang="it-IT" href="%s">\n'
            '<link rel="alternate" hreflang="en" href="%s">\n<link rel="alternate" hreflang="x-default" href="%s">'
            % (url, IT + it_path, IT + en_path, IT + it_path))
    s = re.sub(r'(<link rel="canonical" href="[^"]*">)', lambda m: m.group(1) + alts, s, count=1)
    # the visible language switcher keeps its label, hidden "Italiano" entry too
    dest = os.path.join(OUT, dest_rel)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    open(dest, 'w', encoding='utf-8', newline='\n').write(s)


def copy_support():
    for d in ('assets', 'api'):
        target = os.path.join(OUT, d)
        if os.path.exists(target):
            shutil.rmtree(target)
        shutil.copytree(os.path.join(ROOT, d), target)
    shutil.copy(os.path.join(ROOT, 'favicon.ico'), os.path.join(OUT, 'favicon.ico'))
    # the form sends the language of the page: anything that is not Italian answers in English
    f = os.path.join(OUT, 'assets', 'js', 'contact-form.js')
    t = open(f, encoding='utf-8').read()
    t = t.replace("document.documentElement.lang === 'en' ? 'en' : 'it'", "document.documentElement.lang === 'it' ? 'it' : 'en'")
    for en, sq in (("'Sending...'", "'Po dërgohet...'"), ("'Enquiry received.'", "'Kërkesa u pranua.'"),
                   ("'Email info@titechdigital.it to send your enquiry.'", "'Shkruani te info@titechdigital.it për të dërguar kërkesën.'"),
                   ("'Please fill in your name, email and message: those are the three fields we need in order to reply.'", "'Plotësoni emrin, emailin dhe mesazhin: janë tre fushat që na duhen për t\\'ju përgjigjur.'"),
                   ("'Please enter a valid email address.'", "'Shkruani një adresë emaili të vlefshme.'")):
        assert en in t, en
        t = t.replace(en, sq)
    open(f, 'w', encoding='utf-8', newline='\n').write(t)
    # experiments.js, pages.js: Albanian wording where the scripts pick text by language
    patches = {
        'experiments.js': [
            ("const isEn = (document.documentElement.lang || '').slice(0, 2) === 'en';",
             "const isEn = (document.documentElement.lang || '').slice(0, 2) === 'en';\n  const isSq = (document.documentElement.lang || '').slice(0, 2) === 'sq';"),
            ("const EXPERIMENTS = isEn ? {",
             "const EXPERIMENTS = isSq ? {\n    'hero_headline': ['Të flasim', 'Të flasim për projektin'],\n    'cta_primary': ['Të flasim', 'Na tregoni për projektin'],\n    'contact_headline': ['Na shkruani', 'Na tregoni problemin']\n  } : isEn ? {"),
            ("const key = (isEn ? 'en' : 'it') + ':' + name;", "const key = (isSq ? 'sq' : isEn ? 'en' : 'it') + ':' + name;"),
            ("assignments[(isEn ? 'en' : 'it') + ':' + name]", "assignments[(isSq ? 'sq' : isEn ? 'en' : 'it') + ':' + name]"),
        ],
        'measure.js': [
            ("const lang = (document.documentElement.lang || 'it').slice(0, 2) === 'en' ? 'en' : 'it';",
             "const lg2 = (document.documentElement.lang || 'it').slice(0, 2);\n  const lang = lg2 === 'en' ? 'en' : lg2 === 'sq' ? 'sq' : 'it';"),
            ("const copy = lang === 'en'\n    ? {",
             "const copy = lang === 'sq'\n    ? {\n      title: 'Matje',\n      text: 'Google Analytics nis vetëm nëse pranoni. Na tregon cilat faqe funksionojnë; pa të dhëna reklamash, pa profil.',\n      accept: 'Pranoj',\n      reject: 'Refuzoj',\n      policy: 'Politika e cookie-ve',\n      policyUrl: 'https://www.titechdigital.it/en/cookies/'\n    }\n    : lang === 'en'\n    ? {"),
        ],
        'pages.js': [
            ("const english = (document.documentElement.lang || 'it').slice(0, 2) === 'en';",
             "const lg = (document.documentElement.lang || 'it').slice(0, 2);\n    const english = lg === 'en';\n    const albanian = lg === 'sq';"),
            ("!/\\/contatti\\/|\\/contact\\//.test(location.pathname)", "!/\\/contatti\\/|\\/contact\\/|\\/kontakt\\//.test(location.pathname)"),
            ("english ? 'Quick contact' : 'Contatto rapido'", "albanian ? 'Kontakt i shpejtë' : english ? 'Quick contact' : 'Contatto rapido'"),
            ("(english ? 'WhatsApp' : 'Scrivi su WhatsApp')", "(albanian ? 'Shkruaj në WhatsApp' : english ? 'WhatsApp' : 'Scrivi su WhatsApp')"),
            ("(english ? 'Call' : 'Chiama')", "(albanian ? 'Telefono' : english ? 'Call' : 'Chiama')"),
        ],
    }
    for name, pairs in patches.items():
        g = os.path.join(OUT, 'assets', 'js', name)
        t = open(g, encoding='utf-8').read()
        for old, new in pairs:
            assert old in t, (name, old)
            t = t.replace(old, new)
        open(g, 'w', encoding='utf-8', newline='\n').write(t)
    pkg = {
        'name': 'titech-al-website', 'version': '1.0.0', 'private': True, 'type': 'module',
        'description': 'TiTech Digital, Albanian site (titech.al)',
        'dependencies': {'resend': '^3.2.0'}, 'engines': {'node': '>=18'},
    }
    open(os.path.join(OUT, 'package.json'), 'w', encoding='utf-8', newline='\n').write(json.dumps(pkg, indent=2) + '\n')
    vercel = {
        '$schema': 'https://openapi.vercel.sh/vercel.json', 'buildCommand': None, 'outputDirectory': '.',
        'cleanUrls': True, 'trailingSlash': True,
        'redirects': [
            {'source': '/(.*)', 'has': [{'type': 'host', 'value': 'titech.al'}], 'destination': BASE + '/$1', 'statusCode': 308},
            {'source': '/index.html', 'destination': '/', 'statusCode': 301},
        ],
        'headers': [
            {'source': '/assets/(.*)', 'headers': [{'key': 'Cache-Control', 'value': 'public, max-age=31536000, immutable'}]},
            {'source': '/(.*)', 'headers': [
                {'key': 'X-Content-Type-Options', 'value': 'nosniff'},
                {'key': 'Referrer-Policy', 'value': 'strict-origin-when-cross-origin'},
                {'key': 'X-Frame-Options', 'value': 'DENY'}]},
        ],
    }
    open(os.path.join(OUT, 'vercel.json'), 'w', encoding='utf-8', newline='\n').write(json.dumps(vercel, indent=2) + '\n')
    open(os.path.join(OUT, 'robots.txt'), 'w', encoding='utf-8', newline='\n').write(
        '# robots.txt per %s\n\nUser-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n' % (BASE, BASE))


def write_sitemap():
    rows = []
    for _, (dest, path, it_path, en_path) in PAGES.items():
        u = BASE + path
        rows.append('  <url>\n    <loc>%s</loc>\n    <lastmod>2026-11-25</lastmod>\n'
                    '    <xhtml:link rel="alternate" hreflang="sq-AL" href="%s"/>\n'
                    '    <xhtml:link rel="alternate" hreflang="it-IT" href="%s"/>\n'
                    '    <xhtml:link rel="alternate" hreflang="en" href="%s"/>\n'
                    '    <xhtml:link rel="alternate" hreflang="x-default" href="%s"/>\n  </url>' % (u, u, IT + it_path, IT + en_path, IT + it_path))
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
           'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + '\n'.join(rows) + '\n</urlset>\n')
    open(os.path.join(OUT, 'sitemap.xml'), 'w', encoding='utf-8', newline='\n').write(xml)


def main():
    misses = set()
    for src, (dest, path, it_path, en_path) in PAGES.items():
        build_page(src, dest, path, it_path, en_path, misses)
    copy_support()
    write_sitemap()
    if misses:
        print('MISSING TRANSLATIONS (%d):' % len(misses))
        for where, text in sorted(misses):
            print('  [%s] %s' % (where, text[:140]))
        sys.exit(1)
    print('built %d pages in al/' % len(PAGES))


if __name__ == '__main__':
    main()
