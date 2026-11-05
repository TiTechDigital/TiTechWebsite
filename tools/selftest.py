"""Proves tools/check_site.py can fail. A checker that always says ok is worth
nothing, so this plants pages with known defects, runs the checker over the
whole site, and insists every defect shows up in the report of the page that
carries it.

Run:  python tools/selftest.py
The planted pages are written to _selftest_planted/ and removed again, whatever
happens in between. Files starting with _ are excluded by .vercelignore.

Two pages are planted because one defect hides another: stripping the hreflang
trio stops the twin comparison before it can look at parity, so the parity
defects live on a second page that keeps its trio. The rule about Italian inside
an attribute is fed a page of its own, because the language of a page is read
from its path and nothing under _selftest_planted/ can be an English page. The
copy rule for calculators is fed two forms in memory instead of two planted files,
because the pages that really carry them are published and must not be moved.
"""
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STAGE = os.path.join(ROOT, '_selftest_planted')


def write(rel, body):
    path = os.path.join(STAGE, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8', newline='').write(body)


def plant():
    source = open(os.path.join(ROOT, 'settori', 'index.html'), encoding='utf-8').read()
    broken = source
    # 1. a canonical that does not match the address it sits on
    broken = broken.replace('<link rel="canonical" href="https://www.titechdigital.it/settori/">',
                            '<link rel="canonical" href="https://www.titechdigital.it/settore/">', 1)
    # 2. a link to a page that does not exist
    broken = broken.replace('href="/come-lavoriamo/"', 'href="/come-lavoriam/"', 1)
    # 3. a tag left open
    broken = broken.replace('<div class="tiles">', '<div class="tiles"><div>', 1)
    # 4. the hreflang trio removed, which also breaks the reciprocity check
    broken = re.sub(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*">\n', '', broken)
    # 5. a euro sign, which the site promises never to publish
    broken = broken.replace('</h1>', '</h1><p>\u20ac</p>', 1)

    # a second page, which keeps its trio so the twin comparison runs to the end
    parity = source
    # 6. "you are here" set on a link that goes somewhere else
    parity = parity.replace('</h1>', '</h1><a href="/lavori/" aria-current="page">Lavori</a>', 1)
    # 7. one section more than the twin has
    parity = parity.replace('</h1>', '</h1><section></section>', 1)
    # 8. a euro sign written as an entity, which a character-only ban would miss
    parity = parity.replace('</h1>', '</h1><p>da 1.500 &euro;</p>', 1)

    write('index.html', broken)
    write(os.path.join('bis', 'index.html'), parity)


def report():
    run = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'check_site.py')],
                         capture_output=True, text=True)
    return run.stdout


def page_block(out, name):
    """the lines the checker printed about one page"""
    lines = out.splitlines()
    start = [n for n, line in enumerate(lines) if line.startswith(name)]
    if not start:
        return ''
    end = len(lines)
    for n in range(start[0] + 1, len(lines)):
        if lines[n] and not lines[n].startswith(' '):
            end = n
            break
    return '\n'.join(lines[start[0]:end])


PAGES = {
    '_selftest_planted/index.html': {
        'wrong canonical': 'canonical',
        'dead link': 'dead link',
        'tag left open': 'closes',
        'hreflang removed': 'no en alternate',
        'euro sign': 'euro sign',
    },
    '_selftest_planted/bis/index.html': {
        'aria-current on the wrong link': 'aria-current="page" on',
        'aria-current count differs from the twin': 'aria-current marks',
        'one section more than the twin': '<section> count',
        'euro sign written as an entity': 'euro sign',
    },
}

# the residue rule reads attributes a screen reader meets, on an English page only
ATTRIBUTE_HTML = ('<html lang="en"><head><title>Proof</title></head><body>'
                  '<img alt="I nostri servizi" src="/assets/img/logo.svg"></body></html>')


def attribute_rule():
    sys.path.insert(0, os.path.join(ROOT, 'tools'))
    sys.dont_write_bytecode = True   # importing must not leave a __pycache__ behind
    import check_site
    page = check_site.Page('en/prova/index.html', ATTRIBUTE_HTML)
    page.feed(ATTRIBUTE_HTML)
    page.close()
    found = check_site.audit_page(page)
    print('attribute residue rule: %s' % (found or 'NOTHING REPORTED'))
    return any('Italian residue' in line and 'alt=' in line for line in found)


def calculator_rule():
    """the same calculator legitimately sits on two pages. The copies must still
    agree: proved both ways, so a signature that ignored every number would fail
    the first case and a signature that read the prose would fail the second"""
    from types import SimpleNamespace
    sys.path.insert(0, os.path.join(ROOT, 'tools'))
    sys.dont_write_bytecode = True
    import check_site
    copies = [SimpleNamespace(rel='a/index.html', raw=CALC_A),
              SimpleNamespace(rel='b/index.html', raw=CALC_B)]
    drift = any('calculator is not the same in every copy' in line
                for line in check_site.audit_calculators(copies))
    faithful = any('calculator is not the same in every copy' in line
                   for line in check_site.audit_calculators(
                       [copies[0], SimpleNamespace(rel='c/index.html', raw=CALC_A.replace(
                           'Estimate of the cheapest configuration',
                           'Estimate of the most expensive configuration'))]))
    print('calculator copy rule: drift caught: %s, prose-only difference allowed: %s'
          % (drift, not faithful))
    return drift and not faithful


CALC_A = """<form class="calc" data-calc data-calc-locale="it-IT" data-calc-integration-cost="650">
<select data-calc-kind name="kind"><option value="onepage" data-base="900" data-included="1">One page</option></select>
<input type="range" data-calc-pages name="pages" min="1" max="60" value="10">
<p class="calc__meta">Estimate of the cheapest configuration</p></form>"""

CALC_B = CALC_A.replace('data-base="900"', 'data-base="1200"')


CASE_OK = '''<html lang="it"><body>
<img src="/a.webp" alt="Il sito prima del restyling">
<img src="/b.webp" alt="Il sito dopo la messa online">
<div class="facts" data-results="verified"><p>Fonte: analytics del cliente, 1 marzo – 1 ottobre.</p></div>
<table class="table"><tr><td>WordPress, hosting gestito, checkout Stripe</td></tr></table>
<a href="/servizi/e-commerce/">E-commerce</a>
<blockquote class="quote" data-permission="email del 3 marzo">...</blockquote>
</body></html>'''

CASE_BAD = '''<html lang="it"><body>
<img src="/a.webp" alt="Una schermata del progetto">
<div data-results="verified"></div>
<a href="/chi-siamo/">Chi siamo</a>
<blockquote class="quote">Cliente entusiasta</blockquote>
</body></html>'''


def case_rule():
    """the contract a project page has to keep: proved on a page that satisfies
    it and on one that invents results, skips the before/after pair, has no
    technical table, no service link and an unapproved testimonial"""
    sys.path.insert(0, os.path.join(ROOT, 'tools'))
    sys.dont_write_bytecode = True
    import check_site
    clean = check_site.Page('lavori/verde-casa/index.html', CASE_OK)
    clean.feed(CASE_OK)
    clean.close()
    quiet = check_site.audit_case(clean)
    invented = check_site.Page('lavori/ristorante-xyz/index.html', CASE_BAD)
    invented.feed(CASE_BAD)
    invented.close()
    found = check_site.audit_case(invented)
    wanted = ('.facts block', 'prima', 'dopo', '.table', '/servizi/', 'data-permission')
    caught = [needle for needle in wanted if any(needle in line for line in found)]
    print('case study rule: clean page reported %s, incomplete page caught %d of %d'
          % (quiet or 'nothing', len(caught), len(wanted)))
    return not quiet and len(caught) == len(wanted)


if __name__ == '__main__':
    plant()
    try:
        out = report()
    finally:
        shutil.rmtree(STAGE, ignore_errors=True)

    missed = []
    for name, expected in PAGES.items():
        block = page_block(out, name)
        print(block or '(%s was not reported at all)' % name)
        print()
        missed += [defect for defect, needle in expected.items() if needle not in block]

    caught = sum(len(e) for e in PAGES.values()) + int(attribute_rule())
    caught += int(calculator_rule())
    caught += int(case_rule())
    total = sum(len(e) for e in PAGES.values()) + 3
    if caught < total:
        missed.append('one of the extra rules (attribute residue, copy drift, case contract)')
    print('\n%d of %d defects caught' % (caught, total))
    for defect in missed:
        print('  missed: %s' % defect)
    sys.exit(1 if missed else 0)
