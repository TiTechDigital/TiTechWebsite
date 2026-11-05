# README, crediti, robots, scheda social e commenti degli script: ultime lineette.
import io, sys

EM = '\u2014'
E = []

R = 'README.md'
E += [
    (R, '# TiTech Digital %s Sito web' % EM, '# TiTech Digital: Sito web', 1),
    (R, '**Siti web ed e-commerce** %s sviluppo' % EM, '**Siti web ed e-commerce**: sviluppo', 1),
    (R, '**Design e identità digitale** %s brand identity' % EM, '**Design e identità digitale**: brand identity', 1),
    (R, '**Software e automazione** %s web app' % EM, '**Software e automazione**: web app', 1),
    (R, '**SEO e crescita digitale** %s SEO tecnica' % EM, '**SEO e crescita digitale**: SEO tecnica', 1),
    (R, '**Supporto continuo** %s manutenzione' % EM, '**Supporto continuo**: manutenzione', 1),
    (R, '`assets/css/pages.css` %s font' % EM, '`assets/css/pages.css`: font', 1),
    (R, '`assets/js/pages.js` %s apertura' % EM, '`assets/js/pages.js`: apertura', 1),
    (R, '`assets/js/motion.js` %s animazioni' % EM, '`assets/js/motion.js`: animazioni', 1),
    (R, '**`h1` con la query, in italiano semplice** %s «Realizzazione' % EM,
       '**`h1` con la query, in italiano semplice**: «Realizzazione', 1),
    (R, '`/` + ventuno pagine interne %s italiano' % EM, '`/` + ventuno pagine interne, in italiano', 1),
    (R, '`/en/` + ventuno pagine interne %s inglese' % EM, '`/en/` + ventuno pagine interne, in inglese', 1),
    (R, '`https://www.titechdigital.it/...` %s italiano' % EM, '`https://www.titechdigital.it/...`: italiano', 1),
    (R, '`https://www.titechdigital.it/en/...` %s inglese' % EM, '`https://www.titechdigital.it/en/...`: inglese', 1),
    (R, '`robots.txt` %s consente' % EM, '`robots.txt`: consente', 1),
    (R, '`sitemap.xml` %s contiene' % EM, '`sitemap.xml`: contiene', 1),
    (R, '`vercel.json` %s configurazione' % EM, '`vercel.json`: configurazione', 1),
    (R, '`.vercelignore` %s esclude' % EM, '`.vercelignore`: esclude', 1),
    (R, '**Testi** %s la home' % EM, '**Testi**: la home', 1),
    (R, '**Email** %s cercare' % EM, '**Email**: cercare', 1),
    (R, '**Logo e favicon** %s il simbolo' % EM, '**Logo e favicon**: il simbolo', 1),
    (R, '**Dati legali** %s copyright' % EM, '**Dati legali**: copyright', 1),
    (R, '**Immagini** %s i WebP' % EM, '**Immagini**: i WebP', 1),
    (R, '**Progetti dimostrativi** %s la sezione' % EM, '**Progetti dimostrativi**: la sezione', 1),
    (R, 'lavori · 2023%s2026' % EM, 'lavori · 2023\u20132026', 1),
    (R, '**Prezzi** %s il sito non pubblica' % EM, '**Prezzi**: il sito non pubblica', 1),
    (R, '**Casi di studio** %s `/lavori/`' % EM, '**Casi di studio**: `/lavori/`', 1),
    (R, '**Meta e anteprima social** %s aggiornare' % EM, '**Meta e anteprima social**: aggiornare', 1),
    (R, '**Dati strutturati** %s l\'head contiene' % EM, '**Dati strutturati**: l\'head contiene', 1),
    (R, 'ora il NAP verificato %s nome, città (Novara), telefono %s e gli stessi valori' % (EM, EM),
     'ora il NAP verificato (nome, città di Novara, telefono) e gli stessi valori', 1),
    (R, '`assets/snippets/footer-credit.txt` %s link' % EM, '`assets/snippets/footer-credit.txt`: link', 1),
    (R, '`assets/snippets/nap-block.txt` %s blocco' % EM, '`assets/snippets/nap-block.txt`: blocco', 1),
    (R, '`assets/snippets/review-schema.txt` %s schema' % EM, '`assets/snippets/review-schema.txt`: schema', 1),
    (R, '`assets/snippets/case-study-en.txt` %s\n' % EM, '`assets/snippets/case-study-en.txt`:\n', 1),
    (R, '`/en/tools/website-cost-calculator/` %s intervallo' % EM,
     '`/en/tools/website-cost-calculator/`: intervallo', 1),
    (R, '`/en/tools/ecommerce-margin-calculator/` %s quanto resta' % EM,
     '`/en/tools/ecommerce-margin-calculator/`: quanto resta', 1),
    (R, 'con medie di settore %s il calcolatore dice «riempi le caselle» invece di inventarle %s e i verdetti' % (EM, EM),
     'con medie di settore: il calcolatore dice «riempi le caselle» invece di inventarle, e i verdetti', 1),
    (R, 'tutto ciò che interrogare un sistema esterno %s audit URL, scrape della SERP, un tool che chiede un dominio e torna un rapporto.' % EM,
     'tutto ciò che richiede di interrogare un sistema esterno (audit URL, scrape della SERP, un tool che chiede un dominio e torna un rapporto).', 1),
]

E += [
    ('CREDITS.md', '- Gabarito %s Google Fonts' % EM, '- Gabarito: Google Fonts', 1),
    ('CREDITS.md', '- Onest %s Google Fonts' % EM, '- Onest: Google Fonts', 1),
    ('CREDITS.md', 'GreenSock %s licenza standard' % EM, 'GreenSock: licenza standard', 1),
    ('CREDITS.md', 'darkroom.engineering %s MIT' % EM, 'darkroom.engineering: MIT', 1),
    ('CREDITS.md', '[8B](https://8b.com/) %s [design studio' % EM, '[8B](https://8b.com/): [design studio', 1),
    ('og-card.html', '<title>TiTech Digital %s social card</title>' % EM,
     '<title>TiTech Digital: social card</title>', 1),
    ('robots.txt', '# robots.txt %s https://www.titechdigital.it' % EM,
     '# robots.txt per https://www.titechdigital.it', 1),
    ('assets/js/article.js', "data.labels[i] + ' %s ' + series.name" % EM,
     "data.labels[i] + ' · ' + series.name", 1),
    ('assets/js/article.js', "labelText + ' %s ' + series.name" % EM,
     "labelText + ' · ' + series.name", 1),
    ('assets/js/article.js', 'Same rule as pages.js %s the file carries' % EM,
     'Same rule as pages.js: the file carries', 1),
    ('assets/js/margin.js', 'looked up %s no market average' % EM, 'looked up: no market average', 1),
]

fail = 0
byfile = {}
for path, old, new, want in E:
    byfile.setdefault(path, []).append((old, new, want))
for path, items in byfile.items():
    text = io.open(path, encoding='utf-8', newline='').read()
    for old, new, want in items:
        got = text.count(old)
        if got != want:
            print('MISS %-22s count=%d want=%d  %s' % (path, got, want, old[:58]))
            fail += 1
            continue
        text = text.replace(old, new)
    io.open(path, 'w', encoding='utf-8', newline='').write(text)
    print('written %-22s remaining em: %d' % (path, text.count(EM)))
print('failures:', fail)
sys.exit(1 if fail else 0)
