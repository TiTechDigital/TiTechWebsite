# Riscrive le lineette (—) usate come punteggiatura AI-style: virgole, due punti,
# parentesi. Le lineette degli intervalli numerici (800–2.500 €) e i segnaposto
# dei calcolatori restano: quelli sono tipografia, non tic.
import io, sys

EDITS = [
    # ---- home: titolo, og, contatore lavori, oggetto della mail ----
    ('index.html', 'TiTech Digital — Tecnologia e soluzioni digitali per le imprese',
     'TiTech Digital: Tecnologia e soluzioni digitali per le imprese', 2),
    ('index.html', 'TiTech Digital — tecnologia e soluzioni digitali per le imprese',
     'TiTech Digital: tecnologia e soluzioni digitali per le imprese', 2),
    ('index.html', 'dei nostri lavori · 2023\u20142026', 'dei nostri lavori · 2023\u20132026', 1),
    ('index.html', 'Richiesta progetto \u2014 ${topic}', 'Richiesta progetto: ${topic}', 1),
    ('en/index.html', 'TiTech Digital — Technology and digital solutions for businesses',
     'TiTech Digital: Technology and digital solutions for businesses', 2),
    ('en/index.html', 'TiTech Digital — technology and digital solutions for businesses',
     'TiTech Digital: technology and digital solutions for businesses', 2),
    ('en/index.html', 'of our work · 2023\u20142026', 'of our work · 2023\u20132026', 1),
    ('en/index.html', 'Project enquiry \u2014 ${topic}', 'Project enquiry: ${topic}', 1),

    # ---- lavori: intervallo anni ----
    ('lavori/index.html', 'Lavori · 2023\u20142026', 'Lavori · 2023\u20132026', 1),

    # ---- blog: invito a scrivere ----
    ('blog/index.html', 'il prossimo articolo \u2014 e nel frattempo',
     'il prossimo articolo, e nel frattempo', 1),
    ('en/blog/index.html', 'the next article \u2014 and in the meantime',
     'the next article, and in the meantime', 1),

    # ---- cookie ----
    ('cookie/index.html',
     'Esistono tecnologie con effetti simili \u2014 memoria locale del browser, pixel di tracciamento \u2014 e la disciplina è la stessa:',
     'Esistono tecnologie con effetti simili (memoria locale del browser, pixel di tracciamento), e la disciplina è la stessa:', 1),
    ('en/cookies/index.html',
     'There are technologies with similar effects \u2014 local storage inside the browser, tracking pixels \u2014 and the rules are the same:',
     'There are technologies with similar effects (local storage inside the browser, tracking pixels), and the rules are the same:', 1),

    # ---- privacy: voci della lista destinatari ----
    ('privacy/index.html', '<strong>Hosting</strong> \u2014 il sito', '<strong>Hosting</strong>: il sito', 1),
    ('privacy/index.html', '<strong>Posta elettronica</strong> \u2014 il fornitore',
     '<strong>Posta elettronica</strong>: il fornitore', 1),
    ('privacy/index.html', '<strong>Statistica</strong> \u2014 Google Ireland',
     '<strong>Statistica</strong>: Google Ireland', 1),
    ('privacy/index.html', '<strong>Consulenti</strong> \u2014 commercialista',
     '<strong>Consulenti</strong>: commercialista', 1),
    ('privacy/index.html', '<strong>Autorità</strong> \u2014 quando la comunicazione',
     '<strong>Autorità</strong>: quando la comunicazione', 1),
    ('en/privacy/index.html', '<li>Hosting \u2014 the site', '<li>Hosting: the site', 1),
    ('en/privacy/index.html', '<li>Email \u2014 the provider', '<li>Email: the provider', 1),
    ('en/privacy/index.html', '<li>Statistics \u2014 Google Ireland', '<li>Statistics: Google Ireland', 1),
    ('en/privacy/index.html', '<li>Advisers \u2014 accountant', '<li>Advisers: accountant', 1),
    ('en/privacy/index.html', '<li>Authorities \u2014 where disclosure',
     '<li>Authorities: where disclosure', 1),

    # ---- indici servizi ----
    ('servizi/index.html', 'Servizi \u2014 siti web, e-commerce e software su misura | TiTech Digital',
     'Servizi: siti web, e-commerce e software su misura | TiTech Digital', 2),
    ('en/services/index.html', 'Services \u2014 websites, e-commerce and custom software | TiTech Digital',
     'Services: websites, e-commerce and custom software | TiTech Digital', 2),

    # ---- pagine servizio ----
    ('servizi/siti-web/index.html', 'Il resto \u2014 design, tecnologia, animazioni \u2014 esiste per questo.',
     'Il resto (design, tecnologia, animazioni) esiste per questo.', 1),
    ('en/services/website-design/index.html', 'Everything else \u2014 design, technology, motion \u2014 exists for that.',
     'Everything else (design, technology, motion) exists for that.', 1),
    ('en/services/website-design/index.html', 'Structural changes are the exception \u2014 those we handle.',
     'Structural changes are the exception, and those we handle.', 1),
    ('en/services/seo/index.html', 'Vanity metrics \u2014 impressions, average position \u2014 are not enough',
     'Vanity metrics (impressions, average position) are not enough', 1),
    ('en/services/custom-software/index.html', 'the tool is the problem \u2014 not when the process',
     'the tool is the problem, not when the process', 1),
    ('en/services/ai-automation/index.html',
     'Answers to repetitive questions \u2014 opening hours, availability, order status \u2014 with immediate escalation',
     'Answers to repetitive questions (opening hours, availability, order status), with immediate escalation', 1),
    ('servizi/e-commerce/index.html',
     '<strong>Gestione standard (Shopify, WooCommerce)</strong> \u2014 la scelta più sensata',
     '<strong>Gestione standard (Shopify, WooCommerce)</strong>: la scelta più sensata', 1),
    ('servizi/e-commerce/index.html', '<strong>Soluzione su misura</strong> \u2014 ha senso quando',
     '<strong>Soluzione su misura</strong>: ha senso quando', 1),
    ('servizi/e-commerce/index.html',
     'il numero di integrazioni \u2014 magazzino, corriere, fatturazione \u2014 e chi gestirà',
     'il numero di integrazioni (magazzino, corriere, fatturazione) e chi gestirà', 1),
    ('en/services/ecommerce/index.html',
     'What weighs most is the catalogue \u2014 how many products, how many variants \u2014 the number of integrations',
     'What weighs most is the catalogue (how many products, how many variants), the number of integrations', 1),

    # ---- calcolatore costo sito: frasi, non i segnaposto ----
    ('strumenti/calcolo-costo-sito-web/index.html',
     'che nessuno ha ancora documentato \u2014 è la voce che sposta',
     'che nessuno ha ancora documentato: è la voce che sposta', 1),
    ('strumenti/calcolo-costo-sito-web/index.html',
     'fase di analisi, spostano il numero \u2014 di solito più di tutte',
     'fase di analisi, spostano il numero, di solito più di tutte', 1),
    ('en/tools/website-cost-calculator/index.html',
     'one integration nobody has documented yet \u2014 the line item that moves',
     'one integration nobody has documented yet: the line item that moves', 1),
    ('en/tools/website-cost-calculator/index.html',
     'in discovery, move the number \u2014 usually more than everything',
     'in discovery, move the number, usually more than everything', 1),
]

fail = 0
for path, old, new, want in EDITS:
    text = io.open(path, encoding='utf-8', newline='').read()
    got = text.count(old)
    if got != want:
        print('MISS %-45s count=%d want=%d  %s' % (path, got, want, old[:60]))
        fail += 1
        continue
    io.open(path, 'w', encoding='utf-8', newline='').write(text.replace(old, new))
    print('ok   %-45s %d' % (path, got))
print('failures:', fail)
sys.exit(1 if fail else 0)
