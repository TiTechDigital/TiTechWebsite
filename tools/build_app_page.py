"""Builds the mobile-app service page in both languages from the custom-software pages.

  /servizi/app-mobile/            (Italian)
  /en/services/mobile-apps/       (English twin)

The text says what an app project involves and when an app is the wrong answer.
It claims no delivered app, no technology stack and no price: those are for the
owner to add once they can be shown.

Run: python tools/build_app_page.py
Then: python tools/check_site.py
"""
import html
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://www.titechdigital.it'
DATE = '2026-11-10'

IT_URL = SITE + '/servizi/app-mobile/'
EN_URL = SITE + '/en/services/mobile-apps/'

PAGES = {
    'it': {
        'template': 'servizi/software-su-misura/index.html',
        'old_self': SITE + '/servizi/software-su-misura/',
        'old_twin': SITE + '/en/services/custom-software/',
        'old_twin_path': '/en/services/custom-software/',
        'new_twin_path': '/en/services/mobile-apps/',
        'out': 'servizi/app-mobile/index.html',
        'url': IT_URL, 'lang': 'it-IT',
        'title': 'Sviluppo app mobile iOS e Android | TiTech Digital',
        'description': "Sviluppo di app mobile per aziende: quando serve davvero un'app, native o multipiattaforma, cosa comprende il progetto, tempi, costi e pubblicazione sugli store.",
        'service_name': 'Sviluppo di app mobile',
        'service_type': 'Sviluppo di app mobile per iOS e Android',
        'service_desc': "Progettazione e sviluppo di app mobile per iOS e Android per aziende: analisi delle funzioni, design, sviluppo, test su dispositivi reali, pubblicazione sugli store e aggiornamenti.",
        'crumbs_home': 'Home', 'crumbs_services': 'Servizi', 'crumb': 'App mobile',
        'services_url': SITE + '/servizi/',
        'eyebrow': 'Servizi · 06',
        'h1': 'Sviluppo di app mobile per aziende',
        'lead': "Un'app ha senso quando le persone la usano spesso o quando serve qualcosa che il browser non sa fare: notifiche, fotocamera, funzionamento senza rete. In tutti gli altri casi un sito o una web app costa meno e basta. Partiamo da questa domanda, prima di scegliere come svilupparla.",
        'cta1': ("Racconta cosa deve fare l'app", '/contatti/'),
        'cta2': ('Software su misura', '/servizi/software-su-misura/'),
        'byline_role': 'CEO, TiTech Digital', 'byline_date': 'Aggiornato il 10 novembre 2026',
        'when': ('quando', "Quando serve davvero un'app", "Il primo passo è capire se l'app è la risposta giusta. Spesso lo è, ma non sempre.", [
            ('Uso frequente', "Le persone aprono l'app ogni giorno o ogni settimana: dipendenti sul campo, clienti abituali, abbonati. Un'app guadagna spazio sullo schermo solo con l'uso ripetuto."),
            ('Funzioni del telefono', "Notifiche, fotocamera, posizione, lettura di codici, riconoscimento biometrico. Quando servono davvero, un'app fa più di quanto faccia il browser."),
            ('Uso senza rete', "Magazzino, cantiere, ispezioni: dove la connessione è debole, i dati si salvano sul telefono e si sincronizzano dopo."),
            ('Presenza negli store', "In alcuni settori essere su App Store e Google Play fa parte della credibilità. Da solo, però, non è un motivo sufficiente per fare un'app."),
        ], "<p><strong>Quando basta altro.</strong> Se serve consultare contenuti, prenotare o compilare un modulo, un sito veloce o una web app installabile spesso basta, con un solo codice e senza passare dagli store. Lo diciamo prima di preventivare: se la soluzione giusta è più piccola, lo scriviamo.</p>"),
        'choices': ('scelte', 'Native, multipiattaforma o web app', 'Tre strade, con costi, tempi e limiti diversi. La scelta si fa dopo l’analisi, non prima.', [
            ('App native (iOS e Android)', "Due app separate, scritte per ciascun sistema. Prestazioni massime e accesso completo al telefono. Costano e richiedono più tempo, perché il lavoro si fa due volte."),
            ('App multipiattaforma', "Un solo codice per iOS e Android. Costi e tempi in genere più contenuti, adatta alla maggior parte delle app aziendali. Alcune funzioni molto specifiche possono richiedere parti native."),
            ('Web app installabile (PWA)', "Un'applicazione web che si aggiunge alla schermata del telefono. Nessuno store, aggiornamenti immediati, un solo codice. Le funzioni disponibili dipendono dal sistema e su iPhone sono più limitate."),
        ]),
        'includes': ('comprende', 'Cosa comprende un progetto app', "Cinque parti, nello stesso ordine. Saltarne una è il modo più comune per ottenere un'app che nessuno usa.", [
            ('Funzioni e priorità', "Definiamo cosa deve fare la prima versione e cosa può aspettare. Una prima versione piccola, usata davvero, insegna più di una grande mai finita."),
            ("Design dell'esperienza", "Schermate e percorsi pensati per l'uso con una mano, in movimento, con poco tempo. Un prototipo da provare prima di scrivere il codice."),
            ('Sviluppo e collegamenti', "L'app e, quando serve, il lato server: archivio dei dati, accessi, collegamenti con gestionale, pagamenti e servizi esterni tramite API."),
            ('Test su dispositivi reali', "Prove su telefoni e versioni diverse del sistema, con casi reali, prima di consegnare."),
            ('Pubblicazione e aggiornamenti', "Preparazione e invio agli store, risposta alle revisioni di Apple e Google, e aggiornamenti dopo il rilascio."),
        ]),
        'process': ('svolgimento', 'Come si svolge', 'Per rilasci successivi: ogni fase ha uno scopo chiaro e prepara la successiva.', [
            ('Analisi', "Una call per capire obiettivi, utenti e vincoli, poi un perimetro scritto con funzioni, piattaforme e criteri di riuscita."),
            ('Prototipo', "Schermate cliccabili da provare con chi userà l'app. Le correzioni qui costano poco; dopo costano molto di più."),
            ('Sviluppo a rilasci', "Versioni intermedie da provare ogni poche settimane, così si vede cosa funziona prima della fine."),
            ('Test e pubblicazione', "Prove su dispositivi reali, poi l'invio agli store e la gestione delle revisioni."),
            ('Dopo il rilascio', "Aggiornamenti per i nuovi sistemi operativi, correzioni e nuove funzioni a partire dall'uso reale."),
        ]),
        'limits': ('limiti', 'Cosa non decidiamo noi', 'Tre cose che conviene sapere prima di cominciare.', [
            "<p><strong>La pubblicazione dipende da Apple e Google.</strong> Le loro revisioni hanno regole e tempi che non controlliamo, e un'app può essere respinta e richiedere modifiche prima di essere approvata.</p>",
            "<p><strong>Gli account sviluppatore hanno costi propri.</strong> Apple e Google chiedono una quota a chi pubblica, a carico dell'azienda. Conviene intestare l'account all'azienda, così l'app resta sua.</p>",
            "<p><strong>Un'app va mantenuta.</strong> Ogni anno escono nuove versioni dei sistemi operativi e un'app non aggiornata, prima o poi, smette di funzionare bene. La manutenzione si concorda prima del rilascio.</p>",
        ]),
        'faq_title': 'Domande frequenti',
        'faq': [
            ("Meglio un'app o un sito?", "Dipende da come viene usato. Per consultare e acquistare di rado, un sito veloce o una web app bastano e costano meno. Un'app serve quando l'uso è frequente, servono funzioni del telefono o il lavoro deve funzionare senza rete. Si decide nell'analisi."),
            ("Quanto costa un'app?", "Dipende da quante funzioni ha, da quante piattaforme copre e da quanto si collega ad altri sistemi. Non pubblichiamo un listino: dopo l'analisi ricevi un preventivo scritto con perimetro, tempi e costi."),
            ("Fate anche la parte server?", "Quasi ogni app ha bisogno di un lato server per dati, accessi e notifiche. Lo sviluppiamo insieme all'app, oppure lo colleghiamo a un gestionale esistente tramite API."),
            ("Chi pubblica l'app sugli store?", "L'account sviluppatore deve essere intestato all'azienda, così l'app resta tua. Possiamo seguire la preparazione e l'invio, ma la decisione finale spetta ad Apple e Google."),
            ("L'app può collegarsi al nostro gestionale?", "Sì, se il gestionale offre un modo per scambiare dati (API o file). Se non lo offre, valutiamo alternative prima di stringere compromessi."),
        ],
        'related_title': 'Vicino a questo servizio',
        'related': [
            ('/servizi/software-su-misura/', 'Software su misura', "Gestionali, portali clienti e dashboard sul tuo processo. Spesso è il lato server dell'app."),
            ('/servizi/automazioni-ai/', 'Automazioni e AI', "Meno passaggi manuali e assistenti che rispondono ai clienti, anche dentro un'app."),
            ('/novara/app-mobile/', 'App a Novara', "Per le aziende di Novara e provincia: scenari tipici, zone servite e come lavoriamo dalla sede."),
            ('/servizi/siti-web/', 'Siti web', "Quando basta un sito veloce e ben fatto, senza passare dagli store."),
            ('/settori/', 'Settori', "Cosa cambia quando il lavoro serve un'azienda artigiana, un ristorante o uno studio."),
        ],
        'cta_title': "Cosa deve fare l'app ogni giorno?",
        'cta_text': "Raccontaci chi la userà e cosa deve poter fare. Ti diciamo se serve un'app, una web app o qualcosa di più piccolo.",
        'cta_btn': 'Scrivi a TiTech', 'cta_link': ('Vedi il nostro portfolio', '/lavori/'),
    },
    'en': {
        'template': 'en/services/custom-software/index.html',
        'old_self': SITE + '/en/services/custom-software/',
        'old_twin': SITE + '/servizi/software-su-misura/',
        'old_twin_path': '/servizi/software-su-misura/',
        'new_twin_path': '/servizi/app-mobile/',
        'out': 'en/services/mobile-apps/index.html',
        'url': EN_URL, 'lang': 'en',
        'title': 'Mobile app development for iOS and Android | TiTech Digital',
        'description': 'Mobile app development for companies: when an app is really needed, native or cross-platform, what a project includes, timing, costs and publishing on the stores.',
        'service_name': 'Mobile app development',
        'service_type': 'Mobile app development for iOS and Android',
        'service_desc': 'Design and development of iOS and Android mobile apps for companies: analysis of the features, design, development, testing on real devices, publishing on the stores and updates.',
        'crumbs_home': 'Home', 'crumbs_services': 'Services', 'crumb': 'Mobile apps',
        'services_url': SITE + '/en/services/',
        'eyebrow': 'Services · 06',
        'h1': 'Mobile app development for companies',
        'lead': 'An app makes sense when people use it often, or when you need something a browser cannot do: notifications, the camera, working without a connection. In every other case a website or a web app costs less and is enough. We start from that question, before choosing how to build it.',
        'cta1': ('Tell us what the app should do', '/en/contact/'),
        'cta2': ('Custom software', '/en/services/custom-software/'),
        'byline_role': 'CEO, TiTech Digital', 'byline_date': 'Updated 10 November 2026',
        'when': ('quando', 'When you really need an app', 'The first step is to work out whether an app is the right answer. Often it is, but not always.', [
            ('Frequent use', 'People open the app every day or every week: staff in the field, regular customers, subscribers. An app earns its place on the screen only through repeated use.'),
            ('Phone features', 'Notifications, the camera, location, code scanning, biometric sign-in. When you truly need them, an app can do more than the browser.'),
            ('Working offline', 'Warehouse, building site, inspections: where the connection is weak, data is saved on the phone and synchronised later.'),
            ('Presence on the stores', 'In some sectors being on the App Store and Google Play is part of credibility. On its own, though, it is not enough of a reason to build an app.'),
        ], '<p><strong>When something else is enough.</strong> If people only need to read content, book or fill in a form, a fast website or an installable web app is often enough, with one codebase and no store. We say so before quoting: if the right solution is smaller, we write that down.</p>'),
        'choices': ('scelte', 'Native, cross-platform or web app', 'Three routes, with different costs, timing and limits. The choice is made after the analysis, not before.', [
            ('Native apps (iOS and Android)', 'Two separate apps, each written for its own system. Top performance and full access to the phone. They cost more and take longer, because the work is done twice.'),
            ('Cross-platform apps', 'One codebase for iOS and Android. Costs and timing are usually lower, and it suits most business apps. A few very specific features may need native parts.'),
            ('Installable web app (PWA)', 'A web application added to the phone screen. No store, instant updates, one codebase. The features available depend on the system, and on iPhone they are more limited.'),
        ]),
        'includes': ('comprende', 'What an app project includes', 'Five parts, always in the same order. Skipping one is the most common way to end up with an app nobody uses.', [
            ('Features and priorities', 'We define what the first version must do and what can wait. A small first version that people really use teaches more than a big one that never ships.'),
            ('Experience design', 'Screens and flows designed for one-handed use, on the move, with little time. A prototype to try before any code is written.'),
            ('Development and connections', 'The app and, when needed, the server side: data storage, sign-in, links with your management software, payments and external services through APIs.'),
            ('Testing on real devices', 'Tests on different phones and system versions, with real cases, before delivery.'),
            ('Publishing and updates', 'Preparing and submitting to the stores, answering the Apple and Google reviews, and updates after release.'),
        ]),
        'process': ('svolgimento', 'How it works', 'In successive releases: each phase has a clear purpose and prepares the next.', [
            ('Analysis', 'A call to understand goals, users and constraints, then a written scope with features, platforms and success criteria.'),
            ('Prototype', 'Clickable screens to try with the people who will use the app. Corrections here are cheap; later they cost far more.'),
            ('Releases', 'Intermediate versions to try every few weeks, so you see what works before the end.'),
            ('Testing and publishing', 'Tests on real devices, then submission to the stores and handling of the reviews.'),
            ('After release', 'Updates for new operating systems, fixes and new features based on real use.'),
        ]),
        'limits': ('limiti', 'What we do not decide', 'Three things worth knowing before you start.', [
            '<p><strong>Publishing depends on Apple and Google.</strong> Their reviews follow rules and timing we do not control, and an app can be rejected and need changes before it is approved.</p>',
            '<p><strong>Developer accounts have their own costs.</strong> Apple and Google charge a fee to whoever publishes, paid by the company. The account should be in the company name, so that the app stays yours.</p>',
            '<p><strong>An app has to be maintained.</strong> New versions of the operating systems come out every year, and an app that is not updated sooner or later stops working well. Maintenance is agreed before release.</p>',
        ]),
        'faq_title': 'Frequently asked questions',
        'faq': [
            ('An app or a website?', 'It depends on how it is used. For occasional reading and buying, a fast website or a web app is enough and costs less. An app is needed when use is frequent, phone features matter or the work must run without a connection. It is decided in the analysis.'),
            ('How much does an app cost?', 'It depends on how many features it has, how many platforms it covers and how much it connects to other systems. We do not publish a price list: after the analysis you receive a written quote with scope, timing and costs.'),
            ('Do you also build the server side?', 'Almost every app needs a server side for data, sign-in and notifications. We build it together with the app, or connect it to your existing management software through APIs.'),
            ('Who publishes the app on the stores?', 'The developer account should be in the company name, so the app stays yours. We can handle the preparation and submission, but the final decision belongs to Apple and Google.'),
            ('Can the app connect to our management software?', 'Yes, if that software offers a way to exchange data (an API or files). If it does not, we look at alternatives before settling for compromises.'),
        ],
        'related_title': 'Close to this service',
        'related': [
            ('/en/services/custom-software/', 'Custom software', 'Management tools, client portals and dashboards built on your process. Often the server side of the app.'),
            ('/en/services/ai-automation/', 'AI automation', 'Fewer manual steps and assistants that answer customers, including inside an app.'),
            ('/en/services/website-design/', 'Website design', 'When a fast, well-made website is enough, with no store involved.'),
            ('/en/industries/', 'Industries', 'What changes when the work serves a craft business, a restaurant or a practice.'),
        ],
        'cta_title': 'What should the app do every day?',
        'cta_text': 'Tell us who will use it and what they must be able to do. We will tell you whether you need an app, a web app or something smaller.',
        'cta_btn': 'Write to TiTech', 'cta_link': ('See our work', '/en/work/'),
    },
}


def esc(t):
    return html.escape(t, quote=False)


def strip_tags(t):
    return html.unescape(re.sub(r'<[^>]+>', '', t))


def build(key):
    c = PAGES[key]
    raw = open(os.path.join(ROOT, c['template']), encoding='utf-8').read()
    head = raw[:raw.index('<script type="application/ld+json">')]
    org = json.loads(re.search(r'\{\s*"@type": "Organization".*?\n    \},', raw, re.S).group(0).rstrip(','))
    person = json.loads(re.search(r'\{\s*"@type": "Person".*?\n    \},', raw, re.S).group(0).rstrip(','))
    header = raw[raw.index('<body>'):raw.index('<main id="main">')]
    footer = raw[raw.index('<footer id="footer"'):]

    url = c['url']
    head = re.sub(r'<title>.*?</title>', '<title>%s</title>' % esc(c['title']), head)
    head = re.sub(r'(<meta name="description" content=")[^"]*(")', r'\g<1>%s\g<2>' % html.escape(c['description']), head)
    head = re.sub(r'(<meta property="og:title" content=")[^"]*(")', r'\g<1>%s\g<2>' % html.escape(c['title']), head)
    head = re.sub(r'(<meta property="og:description" content=")[^"]*(")', r'\g<1>%s\g<2>' % html.escape(c['description']), head)
    head = head.replace(c['old_self'], url).replace(c['old_twin'], EN_URL if key == 'it' else IT_URL)
    header = header.replace(c['old_twin_path'], c['new_twin_path'])

    faq_nodes = [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': strip_tags(a)}} for q, a in c['faq']]
    graph = [org,
        {'@type': 'BreadcrumbList', '@id': url + '#breadcrumb', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': c['crumbs_home'], 'item': SITE + '/'},
            {'@type': 'ListItem', 'position': 2, 'name': c['crumbs_services'], 'item': c['services_url']},
            {'@type': 'ListItem', 'position': 3, 'name': c['crumb'], 'item': url}]},
        {'@type': 'Service', '@id': url + '#service', 'name': c['service_name'], 'serviceType': c['service_type'],
         'description': c['service_desc'], 'url': url, 'provider': {'@id': SITE + '/#organization'},
         'areaServed': ['IT', 'AL'],
         'availableChannel': {'@type': 'ServiceChannel', 'serviceUrl': SITE + ('/contatti/' if key == 'it' else '/en/contact/')}},
        person,
        {'@type': 'WebPage', '@id': url + '#webpage', 'url': url, 'name': c['title'], 'inLanguage': c['lang'],
         'author': {'@id': SITE + '/#enea-muja'}, 'breadcrumb': {'@id': url + '#breadcrumb'},
         'about': {'@id': url + '#service'}, 'datePublished': DATE, 'dateModified': DATE},
        {'@type': 'FAQPage', '@id': url + '#faq', 'isPartOf': {'@id': url + '#webpage'}, 'inLanguage': c['lang'], 'mainEntity': faq_nodes}]
    ld = '<script type="application/ld+json">\n' + json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False, indent=2) + '\n</script>\n</head>\n'

    sid, st, sl, checks, prose = c['when']
    checks_html = '\n'.join('        <li><strong>%s</strong><span>%s</span></li>' % (esc(t), esc(d)) for t, d in checks)
    cid, ct, cl, ctiles = c['choices']
    choices = '\n'.join('        <article class="tile">\n          <span class="tile__num">%02d</span>\n          <h3>%s</h3>\n          <p>%s</p>\n        </article>' % (i + 1, esc(t), esc(d)) for i, (t, d) in enumerate(ctiles))
    iid, it_, il, itiles = c['includes']
    includes = '\n'.join('        <article class="tile">\n          <span class="tile__num">%02d</span>\n          <h3>%s</h3>\n          <p>%s</p>\n        </article>' % (i + 1, esc(t), esc(d)) for i, (t, d) in enumerate(itiles))
    pid, pt, pl, psteps = c['process']
    steps = '\n'.join('        <div class="step">\n          <h3 class="m-text-7">%s</h3>\n          <p class="m-text">%s</p>\n        </div>' % (esc(t), esc(d)) for t, d in psteps)
    lid, lt, ll, lprose = c['limits']
    limits = '\n'.join('        ' + p for p in lprose)
    faq = '\n'.join('        <details>\n          <summary>%s</summary>\n          <p>%s</p>\n        </details>' % (esc(q), a) for q, a in c['faq'])
    related = '\n'.join('        <article class="tile">\n          <h3><a href="%s">%s</a></h3>\n          <p>%s</p>\n        </article>' % (u, esc(t), esc(d)) for u, t, d in c['related'])
    arrow = '<svg class="m-link__arrow" viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8h11M9 3.5 13.5 8 9 12.5"/></svg>'
    home = '/' if key == 'it' else '/en/'
    services = '/servizi/' if key == 'it' else '/en/services/'

    main = '''<main id="main">
  <div class="shell page">
    <nav aria-label="%(navlabel)s">
      <ol class="crumbs">
        <li><a href="%(home)s">%(ch)s</a></li>
        <li><a href="%(services)s">%(cs)s</a></li>
        <li aria-current="page">%(crumb)s</li>
      </ol>
    </nav>
    <div class="head">
      <p class="m-eyebrow">%(eyebrow)s</p>
      <h1 class="m-text-3 head__title">%(h1)s<span class="m-dot" aria-hidden="true"></span></h1>
      <p class="m-text-5 head__lead">%(lead)s</p>
      <div class="head__actions">
        <a class="m-btn" href="%(cta1u)s"><span>%(cta1t)s</span></a>
        <a class="m-link" href="%(cta2u)s"><span class="m-link__label">%(cta2t)s</span>%(arrow)s</a>
      </div>
      <p class="byline"><span class="byline__name">Enea Muja</span><span class="byline__role">%(role)s</span><time class="byline__date" datetime="%(date)s">%(bdate)s</time></p>
    </div>

    <section class="sect" aria-labelledby="%(sid)s-title">
      <div class="sect__top">
        <h2 class="m-text-4" id="%(sid)s-title">%(st)s</h2>
        <p class="m-text">%(sl)s</p>
      </div>
      <ul class="checks">
%(checks)s
      </ul>
      <div class="prose">
        %(prose)s
      </div>
    </section>

    <section class="sect" aria-labelledby="%(cid)s-title">
      <div class="sect__top">
        <h2 class="m-text-4" id="%(cid)s-title">%(ct)s</h2>
        <p class="m-text">%(cl)s</p>
      </div>
      <div class="tiles">
%(choices)s
      </div>
    </section>

    <section class="sect" aria-labelledby="%(iid)s-title">
      <div class="sect__top">
        <h2 class="m-text-4" id="%(iid)s-title">%(it)s</h2>
        <p class="m-text">%(il)s</p>
      </div>
      <div class="tiles">
%(includes)s
      </div>
    </section>

    <section class="sect" aria-labelledby="%(pid)s-title">
      <div class="sect__top">
        <h2 class="m-text-4" id="%(pid)s-title">%(pt)s</h2>
        <p class="m-text">%(pl)s</p>
      </div>
      <div class="steps">
%(steps)s
      </div>
    </section>

    <section class="sect" aria-labelledby="%(lid)s-title">
      <div class="sect__top">
        <h2 class="m-text-4" id="%(lid)s-title">%(lt)s</h2>
        <p class="m-text">%(ll)s</p>
      </div>
      <div class="prose">
%(limits)s
      </div>
    </section>

    <section class="sect sect--paper" aria-labelledby="faq-title">
      <div class="sect__top">
        <h2 class="m-text-4" id="faq-title">%(faqt)s</h2>
      </div>
      <div class="faq">
%(faq)s
      </div>
    </section>

    <section class="sect" aria-labelledby="correlati-title">
      <div class="sect__top">
        <h2 class="m-text-4" id="correlati-title">%(relt)s</h2>
      </div>
      <div class="tiles">
%(related)s
      </div>
    </section>

    <section class="sect" aria-labelledby="cta-title">
      <div class="cta">
        <h2 class="m-text-4 cta__title" id="cta-title">%(ctat)s<span class="m-dot" aria-hidden="true"></span></h2>
        <p class="m-text">%(ctax)s</p>
        <div class="cta__actions">
          <a class="m-btn-2" href="%(cta1u)s"><span>%(ctab)s</span></a>
          <a class="m-link" href="%(ctalu)s" style="color:inherit"><span class="m-link__label">%(ctalt)s</span>%(arrow)s</a>
        </div>
      </div>
    </section>
  </div>
</main>
''' % {'navlabel': 'Percorso' if key == 'it' else 'Breadcrumb', 'home': home, 'services': services,
       'ch': c['crumbs_home'], 'cs': c['crumbs_services'], 'crumb': esc(c['crumb']), 'eyebrow': c['eyebrow'],
       'h1': esc(c['h1']), 'lead': esc(c['lead']), 'cta1u': c['cta1'][1], 'cta1t': esc(c['cta1'][0]),
       'cta2u': c['cta2'][1], 'cta2t': esc(c['cta2'][0]), 'arrow': arrow, 'role': c['byline_role'], 'date': DATE,
       'bdate': c['byline_date'], 'sid': sid, 'st': esc(st), 'sl': esc(sl), 'checks': checks_html, 'prose': prose,
       'cid': cid, 'ct': esc(ct), 'cl': esc(cl), 'choices': choices, 'iid': iid, 'it': esc(it_), 'il': esc(il),
       'includes': includes, 'pid': pid, 'pt': esc(pt), 'pl': esc(pl), 'steps': steps, 'lid': lid, 'lt': esc(lt),
       'll': esc(ll), 'limits': limits, 'faqt': esc(c['faq_title']), 'faq': faq, 'relt': esc(c['related_title']),
       'related': related, 'ctat': esc(c['cta_title']), 'ctax': esc(c['cta_text']), 'ctab': esc(c['cta_btn']),
       'ctalu': c['cta_link'][1], 'ctalt': esc(c['cta_link'][0])}

    out = os.path.join(ROOT, c['out'])
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w', encoding='utf-8', newline='\n').write(head + ld + header + main + footer)
    print('wrote', c['out'])


for k in ('it', 'en'):
    build(k)
