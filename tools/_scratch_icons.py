# -*- coding: utf-8 -*-
"""Scratch: three icons in the homepage contact block, one prefilled WhatsApp
message in every wa.me link on the site. Dry run by default."""
import pathlib
import re
import sys
from urllib.parse import quote

ROOT = pathlib.Path(__file__).resolve().parents[1]
APPLY = '--apply' in sys.argv
APPLY_PATH = pathlib.Path('tools', '_wa.svg')
SKIP = {'.git', '.vercel', 'node_modules'}

IT_TEXT = 'Ciao TiTech, vi scrivo dal sito web. Vorrei parlare del mio progetto.'
EN_TEXT = "Hi TiTech, I'm writing from your website. I'd like to talk about my project."

WA_PATHS = [m.group(1) for m in
            re.finditer(r'<path d="([^"]+)"', (ROOT / APPLY_PATH).read_text(encoding='utf-8'))]
assert len(WA_PATHS) == 1, len(WA_PATHS)

MAIL = ('<path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6'
        'c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/>')
PHONE = ('<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5'
         ' 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 '
         '1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 '
         '0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 '
         '22 16.92z"/>')


def icon(kind):
    if kind == 'wa':
        inner = ''.join('<path d="%s"/>' % d for d in WA_PATHS)
        attrs = ' fill="currentColor"'
    else:
        inner = MAIL if kind == 'mail' else PHONE
        attrs = (' fill="none" stroke="currentColor" stroke-width="1.7"'
                 ' stroke-linecap="round" stroke-linejoin="round"')
    return ('<svg class="contact__icon" viewBox="0 0 24 24" width="17" height="17"%s'
            ' aria-hidden="true" focusable="false">%s</svg>' % (attrs, inner))


def documents():
    for path in sorted(ROOT.rglob('*.html')):
        rel = path.relative_to(ROOT)
        if set(rel.parts) & SKIP or rel.parts[0] == 'tools':
            continue
        if rel.name in ('index.original.html', 'og-card.html', 'brand-logo.html') \
                or rel.name.startswith('_'):
            continue
        yield rel.as_posix(), path


reports = []
for rel, path in documents():
    raw = path.read_text(encoding='utf-8')
    english = rel.startswith('en/')
    text = quote(EN_TEXT if english else IT_TEXT, safe=',')
    new = raw

    # 1. one prefilled message, everywhere the number is offered
    new, wa = re.subn(r'https://wa\.me/393761024080(?!\?text=)',
                      'https://wa.me/393761024080?text=' + text, new)

    # 2. icons: only the homepage contact block, in both languages
    if rel in ('index.html', 'en/index.html'):
        # the footer carries the same three hrefs, so the rewrite is fenced to the
        # contact section instead of matching every m-link-2 on the page
        start = new.index('<section id="contact"')
        end = new.index('</section>', start)
        block = new[start:end]

        def anchor(m):
            href = m.group(2)
            kind = ('mail' if href.startswith('mailto:') else
                    'phone' if href.startswith('tel:') else 'wa')
            return '%s<a class="m-link-2" href="%s">%s%s</a>' % (
                m.group(1), href, icon(kind), m.group(3))
        block, icons = re.subn(r'([ \t]*)<a class="m-link-2" '
                             r'href="(mailto:info@titechdigital\.it|tel:\+393761024080|'
                             r'https://wa\.me/393761024080\?text=[^"]*)">([^<]*)</a>',
                             anchor, block)
        new = new[:start] + block + new[end:]
        if icons != 3:
            reports.append('%s: expected 3 contact anchors, replaced %d' % (rel, icons))
        css_anchor = '#contact .contact__links { display: grid; justify-items: start; gap: 0; }'
        css_new = (css_anchor + '\n#contact .contact__links a { display: inline-flex; '
                   'align-items: center; gap: 9px; }\n'
                   '#contact .contact__links .contact__icon { flex: none; width: 17px; '
                   'height: 17px; color: var(--color-3); }')
        if css_anchor in new:
            new = new.replace(css_anchor, css_new, 1)
        else:
            reports.append('%s: CSS anchor line not found' % rel)
        reports.append('%s: wa.me %d, icons %d' % (rel, wa, icons))
        if not APPLY and rel == 'index.html':
            print('\n--- preview ---\n' +
                  block[:block.index('<form class="contact__form')] + '\n--- end ---\n')

    # everything else: just the message
    elif wa:
        reports.append('%s: wa.me %d' % (rel, wa))

    if new != raw and APPLY:
        path.write_text(new, encoding='utf-8', newline='')

print('APPLY' if APPLY else 'DRY RUN', '-', len(reports), 'notes')
for line in reports:
    print('   ', line)
