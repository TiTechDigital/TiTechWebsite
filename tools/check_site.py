"""Checks the published site in both languages: structure, links, structured
data, hreflang reciprocity, agreement with sitemap.xml, and Italian residue
left in English copy.

Run:  python tools/check_site.py
The exit code is the number of problems, so it can gate a deploy.

    pages  ->  each document is audited on its own
    twins  ->  the two languages are compared with each other
    sitemap->  what the sitemap promises is what the pages declare
    calc   ->  where one calculator exists twice, the two copies still agree
"""
import json
import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://www.titechdigital.it'

VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link',
        'meta', 'param', 'source', 'track', 'wbr'}

# Italian words that must not survive in English prose. Checked on text nodes
# only, so a URL such as /servizi/ or an id such as #lavori does not trigger it.
ITALIAN = ['mesi', 'settimane', 'giorno', 'giorni', 'servizio', 'servizi',
           'azienda', 'aziende', 'preventivo', 'lavori', 'lavoro', 'contatti',
           'settore', 'settori', 'siti web', 'come lavoriamo', 'chi siamo',
           'quanto costa', 'prezzo', 'prezzi', 'perche', 'anche', 'questo',
           'questa', 'molto', 'puo', 'deve', 'viene', 'fatto', 'nella',
           'degli', 'delle', 'presso', 'nostro', 'vostra', 'ciao', 'grazie']

# the blocks that make a page structurally equal to its twin; a component that
# exists in one language and not in the other means the two tell different work
COMPONENTS = ['cta', 'facts', 'byline', 'cases', 'checks', 'tiles', 'steps',
              'prose', 'faq', 'table', 'cards', 'note', 'sect--paper',
              'correlati-title', 'calc', 'chart', 'quotes']

# attributes a reader sees or a screen reader reads out. The residue scan on
# text nodes does not reach them, and an Italian alt text is still Italian.
VISIBLE_ATTRS = ('aria-label', 'alt', 'title', 'placeholder', 'content',
                 'data-msg-subject', 'data-msg-incomplete', 'data-msg-invalid',
                 'data-msg-sent', 'data-mail-label', 'data-idle', 'data-success',
                 'data-error')

# elements whose number is a promise of parity, not a detail of the rewrite:
# the same sections, the same headings, the same FAQ entries, the same table rows
TALLY = ('section', 'h2', 'details', 'tr')


class Page(HTMLParser):
    def __init__(self, rel, raw):
        super().__init__(convert_charrefs=True)
        self.rel, self.raw = rel, raw
        self.stack, self.mismatch = [], []
        self.ids, self.hrefs, self.texts, self.ld = [], [], [], []
        self.in_ld, self.ld_buffer, self.skip = False, '', 0
        self.lang, self.canonical, self.og_url, self.robots = '', '', '', ''
        self.alternates, self.classes = {}, set()
        self.tally, self.marks, self.visible = {}, [], []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'html':
            self.lang = a.get('lang', '')
        if a.get('rel') == 'canonical':
            self.canonical = a.get('href', '')
        if a.get('rel') == 'alternate' and 'hreflang' in a:
            self.alternates[a['hreflang']] = a.get('href', '')
        if a.get('property') == 'og:url':
            self.og_url = a.get('content', '')
        if a.get('name') == 'robots':
            self.robots = a.get('content', '')
        if 'id' in a:
            self.ids.append(a['id'])
        for cls in (a.get('class') or '').split():
            self.classes.add(cls)
        if tag == 'a' and a.get('href'):
            self.hrefs.append(a['href'])
        self.tally[tag] = self.tally.get(tag, 0) + 1
        if 'aria-current' in a:
            self.marks.append((a['aria-current'], a.get('href', '')))
        for name in VISIBLE_ATTRS:
            if a.get(name):
                self.visible.append((tag, name, a[name]))
        if tag == 'script' and a.get('type') == 'application/ld+json':
            self.in_ld, self.ld_buffer = True, ''
        if tag in ('script', 'style', 'template'):
            self.skip += 1
        if tag not in VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if tag == 'script':
            if self.in_ld:
                self.ld.append(self.ld_buffer)
                self.in_ld = False
            self.skip = max(0, self.skip - 1)
        if not self.stack:
            self.mismatch.append('stray </%s>' % tag)
        elif self.stack[-1] != tag:
            if tag in self.stack:
                self.mismatch.append('</%s> closes %s' % (tag, self.stack[-1]))
                while self.stack and self.stack.pop() != tag:
                    pass
            else:
                self.mismatch.append('unexpected </%s>' % tag)
        else:
            self.stack.pop()

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_data(self, data):
        if self.in_ld:
            self.ld_buffer += data
            return
        if self.skip or not data.strip():
            return
        self.texts.append(data.strip())

    # -- conveniences ------------------------------------------------------
    @property
    def inner(self):
        """inner pages share one stylesheet; the homes carry their own inline"""
        return '/assets/css/pages.css' in self.raw

    @property
    def url(self):
        # rel is forward-slash separated, and dirname of a bare index.html is ''
        folder = self.rel.rsplit('/', 1)[0] if '/' in self.rel else ''
        return SITE + ('/' if folder == '' else '/' + folder + '/')

    @property
    def language(self):
        # rel is always forward-slash separated, whatever the platform is
        return 'en' if self.rel.startswith('en/') else 'it'

    @property
    def own_tag(self):
        """the hreflang value that names this page, which is not the same as the
        html lang attribute: the Italian pages say it-IT"""
        return 'it-IT' if self.language == 'it' else 'en'

    @property
    def other_tag(self):
        return 'en' if self.language == 'it' else 'it-IT'


def load(rel):
    raw = open(os.path.join(ROOT, rel), encoding='utf-8').read()
    page = Page(rel, raw)
    page.feed(raw)
    page.close()
    return page


def file_for(url):
    """map an absolute site URL to a repository path, forward slashes always"""
    path = url.replace(SITE, '').split('#')[0]
    if path in ('', '/'):
        return 'index.html'
    return path.strip('/') + '/index.html'


def documents():
    rels = []
    # og-card and brand-logo are design aids, not pages: they are ignored by
    # .vercelignore and have no business obeying the rules of a document
    service = {'og-card.html', 'brand-logo.html'}
    for dirpath, dirnames, filenames in os.walk(ROOT):
        # the maintenance folder is skipped, but only the one at the root: the
        # published English site has a /en/tools/ tree of its own
        dirnames[:] = [d for d in dirnames
                       if d not in ('.git', '.vercel', 'node_modules')
                       and not (dirpath == ROOT and d == 'tools')]
        for name in filenames:
            if name.endswith('.html') and name != 'index.original.html' \
                    and name not in service and not name.startswith('_'):
                rels.append(os.path.relpath(os.path.join(dirpath, name), ROOT).replace(os.sep, '/'))
    return sorted(rels)


def audit_page(p):
    """everything one document can be wrong about on its own"""
    problems = []
    if p.stack:
        problems.append('unclosed tags: %s' % p.stack)
    problems += p.mismatch
    dupes = {i for i in p.ids if p.ids.count(i) > 1}
    if dupes:
        problems.append('duplicate ids: %s' % sorted(dupes))

    if p.rel == '404.html':
        # the error page is deliberately not a member of either tree: it is
        # served for unknown addresses in both, so it is excluded from indexing
        if 'noindex' not in p.robots:
            problems.append('404 should be noindex, follow')
        if p.canonical:
            problems.append('404 should carry no canonical')
        if 'lang="en"' not in p.raw:
            problems.append('404 has no English block')
    else:
        if p.canonical != p.url:
            problems.append('canonical %s != %s' % (p.canonical, p.url))
        if p.og_url and p.og_url != p.canonical:
            problems.append('og:url %s != canonical %s' % (p.og_url, p.canonical))
        own = p.alternates.get(p.own_tag, '')
        if own != p.canonical:
            problems.append('hreflang %s does not point at self' % p.own_tag)
        # every indexable page allows large image previews (Discover, rich results)
        if 'max-image-preview:large' not in p.robots:
            problems.append('robots meta lacks max-image-preview:large')
        # a BreadcrumbList with two or more items must have a visible breadcrumb
        # too: the markup has to describe what the reader sees
        crumbs = 0
        for block in p.ld:
            try:
                data = json.loads(block)
            except ValueError:
                continue
            for node in (data.get('@graph', [data]) if isinstance(data, dict) else []):
                if node.get('@type') == 'BreadcrumbList':
                    crumbs = max(crumbs, len(node.get('itemListElement', [])))
        if crumbs >= 2 and not re.search(r'<nav aria-label="(Percorso|Breadcrumb)"', p.raw):
            problems.append('BreadcrumbList without a visible breadcrumb')
        if p.alternates.get('x-default') != p.alternates.get('it-IT'):
            problems.append('x-default should equal the Italian alternate')
        if p.lang != p.language:
            problems.append('html lang is "%s", expected %s' % (p.lang, p.language))

    # structured data must parse and must describe this exact page
    for blob in p.ld:
        try:
            data = json.loads(blob)
        except ValueError as error:
            problems.append('JSON-LD does not parse: %s' % error)
            continue
        dump = json.dumps(data)
        for node in data.get('@graph', []):
            node_url = node.get('url') or node.get('@id', '').split('#')[0]
            if node_url and not node_url.startswith(SITE):
                problems.append('relative URL in structured data: %s' % node_url)
        if p.language == 'en' and 'it-IT' in dump and p.inner:
            problems.append('inLanguage still it-IT')
        if p.language == 'en' and '"en"' not in dump and 'inLanguage' in dump:
            problems.append('inLanguage missing en')

    # English copy must not contain Italian leftovers
    if p.language == 'en':
        joined = ' \n '.join(p.texts).lower()
        for word in ITALIAN:
            match = re.search(r'(?<![a-z])' + re.escape(word) + r'(?![a-z])', joined)
            if match:
                start = max(0, match.start() - 40)
                problems.append('Italian residue "%s" in: ...%s...'
                                % (word, joined[start:match.end() + 30]))
        # the same residue survives in an attribute, where no text node reaches
        for tag, name, value in p.visible:
            low = value.lower()
            for word in ITALIAN:
                if re.search(r'(?<![a-z])' + re.escape(word) + r'(?![a-z])', low):
                    problems.append('Italian residue "%s" in %s %s="%s"'
                                    % (word, tag, name, value[:60]))
                    break

    # aria-current="page" on a link claims that link is the page being read
    if p.canonical:
        here = p.url.replace(SITE, '')
        for value, href in p.marks:
            if value == 'page' and href and href not in (here, p.url):
                problems.append('aria-current="page" on %s, this page is %s'
                                % (href, here))

    # internal links must resolve
    for href in p.hrefs:
        if href.startswith(('mailto:', 'tel:', '//')):
            continue
        if href.startswith('http'):
            if href.startswith(SITE) and not os.path.exists(os.path.join(ROOT, file_for(href))):
                problems.append('dead absolute link: %s' % href)
            continue
        if href.startswith('#'):
            if href != '#' and href[1:] not in p.ids:
                problems.append('dead in-page anchor: %s' % href)
            continue
        if not href.startswith('/'):
            if p.inner:
                problems.append('relative link (inner pages use absolute): %s' % href)
            continue
        path, _, anchor = href.partition('#')
        target = file_for(SITE + path)
        if not os.path.exists(os.path.join(ROOT, target)):
            problems.append('dead link: %s' % href)
        elif anchor and 'id="%s"' % anchor not in open(os.path.join(ROOT, target), encoding='utf-8').read():
            problems.append('missing anchor target: %s' % href)

    if p.inner and 'nav' not in p.classes:
        problems.append('missing component .nav')

    # a name printed on the page has to be a name the structured data knows.
    # looked for in the raw blocks, so a blob that does not parse (already a
    # problem above) cannot crash the check here
    if 'byline' in p.classes and 'person' not in ' '.join(p.ld).lower():
        problems.append('visible byline without a Person node')

    # "no prices published" is a rule of the site, so the euro sign is banned in
    # every shape that renders as one: the character and the entities behind it.
    # Exception: the pricing article legitimately discusses budget ranges and
    # uses euro amounts for transparency; it is the only page allowed to do so.
    euro_allowed = p.rel in ('blog/quanto-costa-sito-web-italia-2026/index.html',
                            'en/blog/website-cost-italy-2026/index.html',
                            'strumenti/calcolo-costo-sito-web/index.html',
                            'en/tools/website-cost-calculator/index.html')
    checks = [(r'\ufffd', 'replacement character (encoding damage)'),
              (r'\ufeff', 'byte order mark')]
    if not euro_allowed:
        checks.insert(0, (r'\u20ac|&euro;|&#0*8364;|&#x0*20ac;', 'euro sign'))
    for pattern, label in checks:
        if re.search(pattern, p.raw, re.I):
            problems.append('%s present' % label)
    tokens = sorted(set(re.findall(r'@@[A-Z_]+@@', p.raw)))
    if tokens:
        problems.append('unfilled template token: %s' % tokens)
    return problems


# Italian-only by design: local landing pages and the case study have no English
# twin, and must not pretend to have one (hreflang would point at a missing page).
ITALIAN_ONLY = {
    'novara/index.html', 'vercelli/index.html', 'como/index.html', 'milano/index.html',
    'blog/case-study-sartoria-novara/index.html',
    'blog/sito-web-aziende-agroalimentari/index.html',
    'blog/sito-web-hotel-ristoranti-lago-di-como/index.html',
    'blog/preventivo-sito-web-milano/index.html',
    'novara/app-mobile/index.html',
    'blog/come-scegliere-una-web-agency/index.html',
    'blog/sito-web-agenzie-immobiliari/index.html',
    'blog/sito-web-agenzie-immobiliari-novara/index.html',
    'blog/sito-web-agenzie-immobiliari-milano/index.html',
    'blog/sito-web-agenzie-immobiliari-como/index.html',
    'blog/sito-web-agenzia-immobiliare-piccoli-comuni/index.html',
    'blog/sito-web-studio-dentistico/index.html',
    'blog/sito-web-dentista-novara/index.html',
    'blog/sito-web-studio-legale-commercialista/index.html',
    'blog/sito-web-estetista-parrucchiere-centro-benessere/index.html',
    'blog/sito-web-idraulico-elettricista-impresa-edile/index.html',
    'blog/sito-web-fisioterapista-osteopata-psicologo/index.html',
    'blog/sito-web-veterinario/index.html',
    'blog/sito-web-autofficina-carrozzeria-gommista/index.html',
    'blog/sito-web-notaio-geometra-architetto-ingegnere/index.html',
    'blog/sito-web-palestra/index.html',
    'blog/sito-web-agenzia-viaggi-fotografo-wedding-planner/index.html',
    'blog/sito-web-aziende-artigiane-manifatturiere/index.html',
    'blog/sito-web-idraulico-elettricista-novara/index.html',
    'blog/sito-web-parrucchiere-estetista-novara/index.html',
    'blog/sito-web-fisioterapista-novara/index.html',
    'blog/sito-web-palestra-novara/index.html',
    'blog/sito-web-parrucchiere-estetista-vercelli/index.html',
    'blog/sito-web-parrucchiere-estetista-como/index.html',
    'blog/sito-web-parrucchiere-estetista-milano/index.html',
    'blog/sito-web-idraulico-elettricista-vercelli/index.html',
    'blog/sito-web-idraulico-elettricista-como/index.html',
    'blog/sito-web-idraulico-elettricista-milano/index.html',
    'blog/sito-web-fisioterapista-vercelli/index.html',
    'blog/sito-web-fisioterapista-como/index.html',
    'blog/sito-web-fisioterapista-milano/index.html',
    'blog/sito-web-veterinario-vercelli/index.html',
    'blog/sito-web-veterinario-como/index.html',
    'blog/sito-web-veterinario-milano/index.html',
    'blog/sito-web-veterinario-novara/index.html',
    'blog/sito-web-autofficina-carrozzeria-vercelli/index.html',
    'blog/sito-web-autofficina-carrozzeria-como/index.html',
    'blog/sito-web-autofficina-carrozzeria-milano/index.html',
    'blog/sito-web-autofficina-carrozzeria-novara/index.html',
    'blog/sito-web-architetto-geometra-vercelli/index.html',
    'blog/sito-web-architetto-geometra-como/index.html',
    'blog/sito-web-architetto-geometra-milano/index.html',
    'blog/sito-web-architetto-geometra-novara/index.html',
    'blog/sito-web-palestra-vercelli/index.html',
    'blog/sito-web-palestra-como/index.html',
    'blog/sito-web-palestra-milano/index.html',
    'blog/sito-web-fotografo-wedding-planner-vercelli/index.html',
    'blog/sito-web-fotografo-wedding-planner-como/index.html',
    'blog/sito-web-fotografo-wedding-planner-milano/index.html',
    'blog/sito-web-fotografo-wedding-planner-novara/index.html',
    'blog/sito-web-azienda-artigiana-vercelli/index.html',
    'blog/sito-web-azienda-artigiana-como/index.html',
    'blog/sito-web-azienda-artigiana-milano/index.html',
    'blog/sito-web-azienda-artigiana-novara/index.html',
}


def audit_twin(p):
    """what the other language has to look like for this page to be honest"""
    if p.rel in ITALIAN_ONLY:
        return []
    problems = []
    other = p.other_tag
    twin_url = p.alternates.get(other)
    if not twin_url:
        return ['no %s alternate' % other]
    twin_rel = file_for(twin_url)
    if not os.path.exists(os.path.join(ROOT, twin_rel)):
        return ['hreflang target missing on disk: %s' % twin_url]
    twin = load(twin_rel)
    if twin.alternates.get(p.own_tag) != p.canonical:
        problems.append('%s twin does not point back: %s' % (other, twin_url))

    # the two languages should describe the same amount of work
    if p.inner and twin.inner:
        for component in COMPONENTS:
            here = 'class="%s"' % component in p.raw or 'id="%s"' % component in p.raw
            there = 'class="%s"' % component in twin.raw or 'id="%s"' % component in twin.raw
            if here != there:
                problems.append('component .%s here: %s, in the twin: %s'
                                % (component, here, there))
    # component names can match while the page is shorter: count the blocks too
    for tag in TALLY:
        if p.tally.get(tag, 0) != twin.tally.get(tag, 0):
            problems.append('<%s> count: %d here, %d in the twin'
                            % (tag, p.tally.get(tag, 0), twin.tally.get(tag, 0)))
    # and mark the same places as "you are here"
    if len(p.marks) != len(twin.marks):
        problems.append('aria-current marks: %d here, %d in the twin'
                        % (len(p.marks), len(twin.marks)))
    # a language switch that lands on the home instead of the twin loses the
    # reader where they were
    for cls in ('nav__lang', 'menu__lang'):
        match = re.search(r'<a class="%s" href="([^"]+)"' % cls, p.raw)
        if match and match.group(1) != twin_url.replace(SITE, ''):
            problems.append('%s goes to %s, not to the twin %s'
                            % (cls, match.group(1), twin_url.replace(SITE, '')))
    return problems


def audit_sitemap(pages):
    problems = []
    path = os.path.join(ROOT, 'sitemap.xml')
    if not os.path.exists(path):
        return ['sitemap.xml missing']
    xml = open(path, encoding='utf-8').read()
    blocks = re.findall(r'<url>(.*?)</url>', xml, re.S)
    listed = [re.search(r'<loc>([^<]+)</loc>', b).group(1) for b in blocks]
    if len(set(listed)) != len(listed):
        problems.append('sitemap has duplicate locs')
    published = {p.canonical for p in pages if p.canonical and 'noindex' not in p.robots}
    for missing in sorted(published - set(listed)):
        problems.append('page not in the sitemap: %s' % missing)
    for ghost in sorted(set(listed) - published):
        problems.append('sitemap entry with no page behind it: %s' % ghost)
    for block, loc in zip(blocks, listed):
        page = [p for p in pages if p.canonical == loc]
        if not page:
            continue
        declared = {(lang, href) for lang, href in page[0].alternates.items()}
        in_sitemap = {(m.group(1), m.group(2)) for m in
                      re.finditer(r'hreflang="([A-Za-z-]+)" href="([^"]+)"', block)}
        if declared != in_sitemap:
            problems.append('%s: sitemap alternates %s, the page declares %s'
                            % (loc, sorted(in_sitemap), sorted(declared)))
    return problems


def calc_signature(form):
    """the arithmetic of one calculator: every attribute article.js and margin.js
    read, plus the control names, in document order, with the prose thrown away.
    Copy is allowed to differ between the article and the standalone tool page;
    the maths is not, because two copies that disagree are two wrong answers.
    The locale is not part of the maths: the Italian and the English copy of one
    tool have to compute the same number, so the attribute that says which
    thousands separator to use is dropped here and compared nowhere."""
    out = []
    for tag, attrs in re.findall(r'<(\w+)([^>]*)>', form):
        pairs = re.findall(r'([\w-]+)="([^"]*)"', attrs)
        kept = sorted(k for k, _ in pairs if k.startswith('data-')
                      and not k.endswith('-locale'))
        kept += [k for k, _ in pairs if k in ('name', 'type', 'value', 'min',
                                            'max', 'step') ]
        if not kept:
            continue
        out.append((tag, tuple((k, dict(pairs)[k]) for k in sorted(set(kept)))))
    return tuple(out)


def audit_calculators(pages):
    """the same calculator can legitimately appear on more than one page - the
    tool and the article that quotes it, or its Italian and its English copy.
    Wherever it appears, it must still compute the same number from the same
    input, so copies are grouped by the controls they expose"""
    groups = {}
    for p in pages:
        for form in re.findall(r'<form class="calc".*?</form>', p.raw, re.S):
            names = tuple(sorted(set(re.findall(r'name="([^"]+)"', form))))
            groups.setdefault(names, []).append(
                (p.rel, calc_signature(form)))
    problems = []
    for names, copies in sorted(groups.items()):
        if len(copies) < 2:
            continue
        by_signature = {}
        for rel, sig in copies:
            by_signature.setdefault(sig, []).append(rel)
        if len(by_signature) > 1:
            problems.append('calculator is not the same in every copy (%s): %s'
                            % ('+'.join(names[:3]),
                               '; '.join(', '.join(r)
                                         for r in by_signature.values())))
    return problems


CASE = re.compile(r'^(lavori|en/work)/([^/]+)/index\.html$')


def audit_case(p):
    """a project page is the one place where this site can quietly sell an
    invention: a result nobody measured, a testimonial nobody approved. Each
    requirement below turns one of the seven promised outputs into something a
    build can refuse, instead of a promise a client has to take on faith."""
    if not CASE.match(p.rel):
        return []
    english = p.language == 'en'
    problems = []

    # 5. results: either verified, with the measurement named, or declared absent
    status = re.search(r'data-results="([^"]+)"', p.raw)
    if not status:
        problems.append('no data-results marker: say "verified" or "not-measured"')
    elif status.group(1) not in ('verified', 'not-measured'):
        problems.append('data-results="%s" is neither verified nor not-measured'
                        % status.group(1))
    elif status.group(1) == 'verified' and 'class="facts"' not in p.raw:
        problems.append('results claimed as verified without a .facts block to '
                        'carry where they came from')

    # 3. before and after, as two images a screen reader can name
    wanted = ('before', 'after') if english else ('prima', 'dopo')
    alts = ' '.join(v for tag, name, v in p.visible if tag == 'img' and name == 'alt').lower()
    for word in wanted:
        if word not in alts:
            problems.append('no image alt mentions "%s"' % word)

    # 4. technical implementation details, as a table
    if 'class="table"' not in p.raw:
        problems.append('no .table with the technical specifics of the build')

    # 7. a way to the service that was actually sold
    prefix = '/en/services/' if english else '/servizi/'
    if prefix not in p.raw:
        problems.append('no link to %s' % prefix)

    # 6. a testimonial needs either a written permission or the demo label
    if 'class="quote"' in p.raw and 'data-permission' not in p.raw \
            and 'class="tag-demo"' not in p.raw:
        problems.append('a quote with no data-permission and no demo disclaimer')
    return problems


def main():
    pages = [load(rel) for rel in documents()]
    total = 0
    for p in pages:
        problems = audit_page(p) + audit_case(p)
        if p.canonical:
            problems += audit_twin(p)
        total += len(problems)
        print('%-46s %s' % (p.rel, 'ok' if not problems else '%d PROBLEMS' % len(problems)))
        for problem in problems:
            print('    - ' + problem)
    problems = audit_sitemap(pages)
    total += len(problems)
    print('\nsitemap: %s' % ('ok' if not problems else '%d PROBLEMS' % len(problems)))
    for problem in problems:
        print('    - ' + problem)
    problems = audit_calculators(pages)
    total += len(problems)
    print('\ncalculators: %s' % ('ok' if not problems else '%d PROBLEMS' % len(problems)))
    for problem in problems:
        print('    - ' + problem)
    trees = sum(1 for p in pages if p.canonical and 'noindex' not in p.robots)
    print('\n%d documents checked (%d published pages), %d problems'
          % (len(pages), trees, total))
    return 1 if total else 0


if __name__ == '__main__':
    sys.exit(main())
