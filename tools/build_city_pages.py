"""Builds the Italian-only city pages (/vercelli/, /como/, /milano/) from the
inner-page template (servizi/siti-web/index.html) and the per-city content below.

Each city carries its own territory section, its own FAQ and its own service
links: a page is only worth publishing if it says something the others do not.
Nothing here claims a client, a project or an office in the city. The portfolio
block says plainly that the projects shown are the ones built so far.

Run: python tools/build_city_pages.py
Then: python tools/check_site.py
"""
import html
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://www.titechdigital.it'
TEMPLATE = os.path.join(ROOT, 'servizi', 'siti-web', 'index.html')
TODAY = '2026-11-08'

RANGES = ("Le fasce indicative per il mercato italiano: un sito vetrina tra 800 e 2.500 euro, "
          "un sito aziendale tra 2.000 e 6.500 euro, un e-commerce tra 4.000 e 15.000 euro. "
          "Il costo dipende dal perimetro, non dalla città. Per una stima veloce usa il "
          "<a href=\"/strumenti/calcolo-costo-sito-web/\">calcolatore del costo di un sito web</a>.")

CITIES = [
    {
        'slug': 'vercelli', 'name': 'Vercelli', 'region': 'Piemonte',
        'title': 'Siti web a Vercelli | Web agency TiTech Digital',
        'description': 'Siti web, e-commerce e software per aziende di Vercelli e provincia: agroalimentare, manifattura e professionisti. Web agency di Novara, preventivo scritto.',
        'h1': 'Siti web a Vercelli per aziende e professionisti',
        'lead': "Realizziamo siti web, e-commerce e software per le aziende di Vercelli e della sua provincia. Siamo una web agency con sede a Novara, nella provincia confinante: si parte da una videochiamata e, se preferisci, si concorda un incontro di persona.",
        'territory_title': 'Cosa serve alle aziende di Vercelli e provincia',
        'territory_lead': "Il territorio vercellese è legato alla risicoltura e all'agroalimentare, ma ci sono anche manifattura, logistica, studi professionali e attività di centro. Cambiano le richieste, non il metodo.",
        'territory': [
            ("Aziende agricole e agroalimentari", "Un sito che racconta prodotto, origine e certificazioni, e porta richieste di acquisto all'ingrosso o vendite dirette. Schede chiare, foto vere, un modulo che arriva a chi risponde."),
            ("Piccole imprese manifatturiere", "Catalogo ordinato, schede tecniche scaricabili, una pagina per ogni lavorazione e una richiesta di preventivo che dice subito cosa serve sapere."),
            ("Studi professionali e attività in centro", "Scheda Google curata, servizi spiegati in modo semplice, orari e modo di fissare un appuntamento. Chi cerca vicino a casa decide in pochi secondi."),
            ("Chi ha già un sito vecchio", "Un sito di qualche anno fa che non si aggiorna e si legge male da telefono. Si rifà tenendo gli indirizzi che già portano visite, senza ripartire da zero."),
        ],
        'work_title': "Come lavoriamo con le aziende di Vercelli",
        'work': [
            ("Prima una call", "Venti minuti per capire cosa vendi, a chi e cosa non funziona oggi. Ti diciamo subito se serve un sito nuovo o un intervento più piccolo."),
            ("Preventivo scritto", "Perimetro, tempi e costi su carta prima di iniziare. Con i contenuti pronti un sito aziendale richiede in genere da quattro a otto settimane."),
            ("Un incontro, se serve", "Vercelli confina con la provincia di Novara: per chi preferisce vedersi di persona, si concorda un incontro. Il resto del lavoro corre online."),
        ],
        'services': [
            ('/servizi/siti-web/', 'Realizzazione siti web', 'Dal progetto delle pagine alla pubblicazione, con testi, design e SEO tecnica.'),
            ('/servizi/e-commerce/', 'E-commerce', 'Se vendi un prodotto direttamente: catalogo, pagamenti, spedizioni, integrazioni.'),
            ('/settori/artigianato/', 'Artigianato e manifattura', 'Cosa cambia quando il sito deve spiegare una lavorazione e portare richieste di preventivo.'),
            ('/servizi/seo/', 'Consulenza SEO', 'Scheda Google, pagine che rispondono a domande precise e misurazione con Search Console.'),
        ],
        'faq': [
            ("Lavorate con aziende agricole e agroalimentari di Vercelli?",
             "Lavoriamo con aziende di tutta Italia. Per l'agroalimentare partiamo da cosa deve fare il sito: raccontare il prodotto, ricevere richieste da clienti professionali o vendere direttamente. Nel portfolio trovi i progetti realizzati finora."),
            ("Come ci incontriamo?",
             "Si parte da una videochiamata. Vercelli è nella provincia confinante con Novara, quindi, se preferisci, si concorda un incontro di persona."),
            ("Quanto costa un sito web per un'azienda di Vercelli?", RANGES),
            ("Fate SEO per comparire su Google a Vercelli?",
             "Sì: scheda Google, una pagina che spiega servizi e zona, testi che citano davvero il territorio. Non promettiamo posizioni e non facciamo pagine clonate per ogni comune."),
        ],
        'prov': 'Provincia di Vercelli',
        'others': ['como', 'milano'],
    },
    {
        'slug': 'como', 'name': 'Como', 'region': 'Lombardia',
        'title': 'Siti web a Como | Web agency TiTech Digital',
        'description': 'Siti web, e-commerce e software per aziende e strutture di Como: turismo sul lago, tessile e servizi. Web agency di Novara, lavoro a distanza, preventivo scritto.',
        'h1': 'Siti web a Como per aziende e strutture turistiche',
        'lead': "Realizziamo siti web, e-commerce e software per le aziende di Como e della sua provincia. Siamo una web agency con sede a Novara e lavoriamo a distanza: videochiamate, prototipi online e consegna digitale.",
        'territory_title': 'Cosa serve alle aziende di Como',
        'territory_lead': "Como vive di turismo sul lago, di una lunga tradizione tessile e della vicinanza con la Svizzera. Tre mondi con bisogni diversi, che si riflettono in tre tipi di sito.",
        'territory': [
            ("Turismo e ospitalità sul lago", "Hotel, B&B, ristoranti e attività per i visitatori hanno bisogno di un sito che si legge bene da telefono, che mostri camere o menu e che porti prenotazioni dirette, in più lingue."),
            ("Aziende tessili e manifatturiere", "Como è legata alla seta e al tessile. Un sito per questo settore deve far capire lavorazioni e qualità, con un catalogo chiaro per chi compra da fuori."),
            ("Chi si rivolge a clienti di più Paesi", "Con il confine vicino, molte aziende parlano a clienti di più lingue. Un sito multilingua va progettato dall'inizio, con struttura e indirizzi giusti, non tradotto alla fine."),
            ("Studi e professionisti", "Pagine servizi semplici, scheda Google aggiornata e un modo chiaro per fissare un primo appuntamento, anche da fuori città."),
        ],
        'work_title': "Come lavoriamo con le aziende di Como",
        'work': [
            ("Tutto a distanza", "Videochiamate, prototipi online da guardare e commentare, consegna digitale. Non serve spostarsi per ottenere un sito fatto bene."),
            ("Struttura prima del design", "Decidiamo insieme pagine, lingue e messaggio prima di disegnare. Per chi lavora con i turisti la stagionalità entra nel progetto fin dall'inizio."),
            ("Preventivo scritto", "Perimetro, tempi e costi su carta prima di iniziare, con le lingue e le integrazioni previste già conteggiate."),
        ],
        'services': [
            ('/servizi/siti-web/', 'Realizzazione siti web', 'Siti veloci e accessibili, pensati per essere aggiornati e per più lingue.'),
            ('/settori/ristorazione/', 'Ristorazione e ospitalità', 'Menu, prenotazioni e scheda Google collegati al sito.'),
            ('/servizi/e-commerce/', 'E-commerce', 'Se vendi online a clienti italiani e stranieri: catalogo, pagamenti, spedizioni.'),
            ('/en/', 'Versione inglese del sito', 'Un esempio di sito in italiano e inglese con struttura e hreflang corretti: questo.'),
        ],
        'faq': [
            ("Fate siti in più lingue per turisti e clienti esteri?",
             "Sì. Progettiamo struttura, indirizzi e collegamenti tra le versioni per le lingue che servono, come in questo sito in italiano e inglese. I testi si scrivono o si traducono con chi conosce il mestiere."),
            ("Fate siti per hotel, B&B e ristoranti?",
             "Sì. Si parte da cosa deve fare il sito: far vedere camere o menu, ricevere prenotazioni dirette, comparire su Google Maps. Trovi cosa comprende nella pagina sui siti per la <a href=\"/settori/ristorazione/\">ristorazione</a>."),
            ("Come lavorate con aziende di Como, se siete a Novara?",
             "A distanza: una call per capire il progetto, prototipi online, revisioni via messaggio o videochiamata e consegna digitale. Il metodo è lo stesso per un cliente a Novara e per uno a Como."),
            ("Quanto costa un sito web per un'azienda di Como?", RANGES),
        ],
        'prov': 'Provincia di Como',
        'others': ['vercelli', 'milano'],
    },
    {
        'slug': 'milano', 'name': 'Milano', 'region': 'Lombardia',
        'title': 'Siti web a Milano | Web agency TiTech Digital',
        'description': 'Siti web, e-commerce e software su misura per PMI, studi e aziende B2B di Milano: preventivo scritto e un solo referente. Web agency di Novara, lavoro a distanza.',
        'h1': 'Siti web a Milano per PMI, studi e aziende B2B',
        'lead': "Realizziamo siti web, e-commerce e software su misura per le imprese di Milano. Siamo una web agency di Novara: un solo referente, un preventivo scritto con perimetro, tempi e costi e un sito costruito sul tuo processo, non su un pacchetto uguale per tutti.",
        'territory_title': 'Cosa serve alle aziende di Milano',
        'territory_lead': "A Milano le agenzie sono tante e la concorrenza online è alta. Per questo conta meno promettere tutto e più decidere con precisione cosa serve al tuo caso.",
        'territory': [
            ("PMI e aziende B2B", "Un sito che spiega l'offerta a chi decide, con casi, schede e una richiesta di contatto breve. Se i processi interni rallentano, si valuta anche un gestionale o un'automazione."),
            ("Studi e consulenti", "Pagine servizi chiare, profilo di chi lavora, contatti e un sito che trasmette fiducia nei primi dieci secondi."),
            ("Negozi e brand che vendono online", "Un e-commerce costruito sui margini reali: prima i numeri, poi la piattaforma. Per capire cosa resta di ogni vendita usa il <a href=\"/strumenti/calcolo-margine-ecommerce/\">calcolatore del margine</a>."),
            ("Concorrenza alta su Google", "A Milano rankare su ricerche generiche è difficile per chiunque. Conviene lavorare su ricerche specifiche (servizio, settore, problema) e sulla scheda Google, prima ancora di un blog."),
        ],
        'work_title': "Come lavoriamo con le aziende di Milano",
        'work': [
            ("Un referente solo", "Chi parla con te sul progetto è chi lo sviluppa. Niente passaggi tra account, project manager e sviluppatori."),
            ("Preventivo scritto", "Perimetro, tempi e costi prima di iniziare. Se un numero può cambiare, ti diciamo da cosa dipende."),
            ("Lavoro a distanza", "Call, prototipi online e consegna digitale. Un incontro di persona si valuta caso per caso."),
        ],
        'services': [
            ('/servizi/siti-web/', 'Realizzazione siti web', 'Siti aziendali veloci, con testi, design e SEO tecnica.'),
            ('/servizi/software-su-misura/', 'Software su misura', 'Gestionali, portali clienti e dashboard sul tuo processo.'),
            ('/servizi/automazioni-ai/', 'Automazioni e AI', 'Meno passaggi manuali: documenti, preventivi, sincronizzazione tra sistemi.'),
            ('/servizi/seo/', 'Consulenza SEO', 'Tecnica, contenuti e misurazione, con aspettative chiare.'),
        ],
        'faq': [
            ("Perché scegliere una web agency di Novara per un'azienda di Milano?",
             "Perché il lavoro si fa a distanza comunque: call, prototipi online, consegna digitale. Contano il metodo, un referente chiaro e il preventivo scritto, non la sede. Un incontro di persona si valuta caso per caso."),
            ("Fate SEO per Milano?",
             "Sì, con aspettative chiare. Le ricerche generiche a Milano sono molto competitive: lavoriamo su ricerche specifiche, sulla tecnica e sulla scheda Google, senza promettere posizioni."),
            ("Fate software e automazioni per aziende milanesi?",
             "Sì: gestionali su misura, portali clienti, dashboard e automazioni. Si parte da un solo processo, misurato su casi reali, prima di estendere il lavoro. Vedi <a href=\"/servizi/software-su-misura/\">software su misura</a>."),
            ("Quanto costa un sito web per un'azienda di Milano?", RANGES),
        ],
        'prov': 'Città metropolitana di Milano',
        'others': ['vercelli', 'como'],
    },
]
BY_SLUG = {c['slug']: c for c in CITIES}


def esc(t):
    return html.escape(t, quote=False)


def strip_tags(t):
    return html.unescape(re.sub(r'<[^>]+>', '', t))


raw = open(TEMPLATE, encoding='utf-8').read()
head_end = raw.index('<script type="application/ld+json">')
head_prefix = raw[:head_end]
org_node = re.search(r'\{\s*"@type": "Organization".*?\n    \},', raw, re.S).group(0).rstrip(',')
body_start = raw.index('<body>')
header_block = raw[body_start:raw.index('<main id="main">')]
footer_block = raw[raw.index('<footer id="footer"'):]
cases = re.search(r'(<div class="cases">.*?</div>\n)\s*\n?\s*</section>', raw, re.S).group(1)

# the template header points at the English twin of the service page; these pages have none
header_block = header_block.replace('/en/services/website-design/', '/en/')
header_block = header_block.replace(' aria-current="true"', '')


def page(c):
    url = '%s/%s/' % (SITE, c['slug'])
    name = c['name']
    head = head_prefix
    head = re.sub(r'<title>.*?</title>', '<title>%s</title>' % esc(c['title']), head)
    head = re.sub(r'(<meta name="description" content=")[^"]*(")', r'\g<1>%s\g<2>' % html.escape(c['description']), head)
    head = re.sub(r'(<meta property="og:title" content=")[^"]*(")', r'\g<1>%s\g<2>' % html.escape(c['title']), head)
    head = re.sub(r'(<meta property="og:description" content=")[^"]*(")', r'\g<1>%s\g<2>' % html.escape(c['description']), head)
    head = head.replace('https://www.titechdigital.it/servizi/siti-web/', url)
    head = re.sub(r'\s*<link rel="alternate" hreflang="en"[^>]*>', '', head)
    head = head.replace('<link rel="alternate" hreflang="it-IT" href="%s">' % url,
                        '<link rel="alternate" hreflang="it-IT" href="%s">' % url)

    faq_nodes = [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': strip_tags(a)}} for q, a in c['faq']]
    graph = [
        json.loads(org_node),
        {'@type': 'BreadcrumbList', '@id': url + '#breadcrumb', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE + '/'},
            {'@type': 'ListItem', 'position': 2, 'name': 'Siti web a ' + name, 'item': url}]},
        {'@type': 'Service', '@id': url + '#service', 'name': 'Realizzazione siti web a ' + name,
         'serviceType': 'Sviluppo di siti web aziendali', 'url': url,
         'provider': {'@id': SITE + '/#organization'},
         'areaServed': {'@type': 'City', 'name': name, 'containedInPlace': {'@type': 'AdministrativeArea', 'name': c['prov']}},
         'availableChannel': {'@type': 'ServiceChannel', 'serviceUrl': SITE + '/contatti/'}},
        {'@type': 'WebPage', '@id': url + '#webpage', 'url': url, 'name': c['title'], 'description': c['description'],
         'inLanguage': 'it-IT', 'isPartOf': {'@id': SITE + '/#website'},
         'breadcrumb': {'@id': url + '#breadcrumb'}, 'about': {'@id': url + '#service'},
         'datePublished': TODAY, 'dateModified': TODAY},
        {'@type': 'FAQPage', '@id': url + '#faq', 'isPartOf': {'@id': url + '#webpage'}, 'inLanguage': 'it-IT', 'mainEntity': faq_nodes},
    ]
    ld = '<script type="application/ld+json">\n' + json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False, indent=2) + '\n</script>\n</head>\n'

    checks = '\n'.join('        <li><strong>%s</strong><span>%s</span></li>' % (esc(t), d) for t, d in c['territory'])
    steps = '\n'.join('        <div class="step">\n          <h3 class="m-text-7">%s</h3>\n          <p class="m-text">%s</p>\n        </div>' % (esc(t), d) for t, d in c['work'])
    tiles = '\n'.join('        <article class="tile">\n          <h3><a href="%s">%s</a></h3>\n          <p>%s</p>\n        </article>' % (u, esc(t), d) for u, t, d in c['services'])
    faq = '\n'.join('        <details>\n          <summary>%s</summary>\n          <p>%s</p>\n        </details>' % (esc(q), a) for q, a in c['faq'])
    near = '\n'.join(
        '        <article class="tile">\n          <h3><a href="/%s/">Siti web a %s</a></h3>\n          <p>%s</p>\n        </article>' % (s, BY_SLUG[s]['name'], BY_SLUG[s]['territory_lead'])
        for s in c['others'])

    main = '''<main id="main">
  <div class="shell page">
    <nav aria-label="Percorso">
      <ol class="crumbs">
        <li><a href="/">Home</a></li>
        <li aria-current="page">Siti web a %(name)s</li>
      </ol>
    </nav>
    <div class="head">
      <p class="m-eyebrow">Siti web · %(name)s</p>
      <h1 class="m-text-3 head__title">%(h1)s<span class="m-dot" aria-hidden="true"></span></h1>
      <p class="m-text-5 head__lead">%(lead)s</p>
      <div class="head__actions">
        <a class="m-btn" href="/contatti/"><span>Raccontaci il progetto</span></a>
        <a class="m-btn-2" href="/lavori/"><span>Vedi il nostro portfolio</span></a>
      </div>
    </div>

    <section class="sect" aria-labelledby="territorio-title">
      <div class="sect__top">
        <h2 class="m-text-4" id="territorio-title">%(territory_title)s</h2>
        <p class="m-text">%(territory_lead)s</p>
      </div>
      <ul class="checks">
%(checks)s
      </ul>
    </section>

    <section class="sect" aria-labelledby="metodo-title">
      <div class="sect__top">
        <h2 class="m-text-4" id="metodo-title">%(work_title)s</h2>
      </div>
      <div class="steps">
%(steps)s
      </div>
    </section>

    <section class="sect" aria-labelledby="servizi-title">
      <div class="sect__top">
        <h2 class="m-text-4" id="servizi-title">Cosa possiamo fare per te a %(name)s</h2>
      </div>
      <div class="tiles">
%(tiles)s
      </div>
    </section>

    <section class="sect" aria-labelledby="lavori-title">
      <div class="sect__top">
        <h2 class="m-text-4" id="lavori-title">I nostri lavori</h2>
        <p class="m-text">Ti mostriamo solo progetti che abbiamo realizzato: questi sono quelli fatti finora, in settori diversi. Il portfolio completo è qui sotto.</p>
      </div>
      <div class="cases">
%(cases)s
      </div>
      <div class="head__actions">
        <a class="m-btn" href="/lavori/"><span>Vedi il nostro portfolio</span></a>
      </div>
    </section>

    <section class="sect sect--paper" aria-labelledby="faq-title">
      <div class="sect__top">
        <h2 class="m-text-4" id="faq-title">Domande frequenti</h2>
      </div>
      <div class="faq">
%(faq)s
      </div>
    </section>

    <section class="sect" aria-labelledby="correlati-title">
      <div class="sect__top">
        <h2 class="m-text-4" id="correlati-title">Vicino a questa pagina</h2>
      </div>
      <div class="tiles">
        <article class="tile">
          <h3><a href="/novara/">Sviluppo siti web a Novara</a></h3>
          <p>La nostra sede: incontri di persona, SEO locale e Google Business Profile nello stesso progetto.</p>
        </article>
%(near)s
      </div>
    </section>

    <section class="sect" aria-labelledby="cta-title">
      <div class="cta">
        <h2 class="m-text-4 cta__title" id="cta-title">Partiamo da cosa ti serve a %(name)s<span class="m-dot" aria-hidden="true"></span></h2>
        <p class="m-text">Raccontaci cosa fa la tua attività, a chi si rivolge e cosa non funziona oggi. Ti rispondiamo con una prima valutazione e, se serve, un preventivo scritto.</p>
        <div class="cta__actions">
          <a class="m-btn-2" href="/contatti/"><span>Scrivi a TiTech</span></a>
          <a class="m-link" href="/lavori/" style="color:inherit"><span class="m-link__label">Vedi il nostro portfolio</span><svg class="m-link__arrow" viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8h11M9 3.5 13.5 8 9 12.5"/></svg></a>
        </div>
      </div>
    </section>
  </div>
</main>
''' % {'name': name, 'h1': esc(c['h1']), 'lead': c['lead'], 'territory_title': esc(c['territory_title']),
       'territory_lead': c['territory_lead'], 'checks': checks, 'work_title': esc(c['work_title']),
       'steps': steps, 'tiles': tiles, 'cases': cases_inner,
       'faq': faq, 'near': near}
    return head + ld + header_block + main + footer_block


cases_inner = re.sub(r'^<div class="cases">\n|</div>\n$', '', cases).rstrip('\n')

for c in CITIES:
    out = os.path.join(ROOT, c['slug'])
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, 'index.html'), 'w', encoding='utf-8', newline='\n').write(page(c))
    print('wrote', c['slug'] + '/index.html')
