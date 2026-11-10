"""Builds /novara/app-mobile/, the local page for app development around Novara.

It is a child of /novara/ and of /servizi/app-mobile/, not a copy of either: it
lists where an app serves a business in Novara and its province, how the work
runs from Novara and which towns are covered. The scenarios are examples, not
clients; no project in the area is claimed. Italian only (see ITALIAN_ONLY in
tools/check_site.py).

Run after tools/build_app_page.py:  python tools/build_novara_app_page.py
"""
import html
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://www.titechdigital.it'
URL = SITE + '/novara/app-mobile/'
DATE = '2026-11-10'
OUT = 'novara/app-mobile/index.html'

TITLE = 'Sviluppo app a Novara | App iOS e Android | TiTech Digital'
DESC = "Sviluppo di app per iOS e Android a Novara e provincia: quando serve un'app, esempi per logistica, turismo, agroalimentare e studi, come lavoriamo e zone servite."
H1 = 'Sviluppo di app a Novara per aziende e professionisti'
LEAD = "Sviluppiamo app per iOS e Android per le aziende di Novara e provincia. La sede è a Novara: si parte da una videochiamata o da un incontro di persona e, prima di scrivere codice, verifichiamo se un'app è davvero la risposta giusta."

SCENARIOS = [
    ('Logistica e trasporti', "Novara è un nodo logistico, con il suo interporto. Per autisti, magazzinieri e operatori sul campo un'app può gestire presa in carico, firma di consegna e foto dei colli, anche dove la rete è debole."),
    ('Turismo e ospitalità sui laghi', "In provincia ci sono il Lago Maggiore e il Lago d'Orta. Per strutture e attività con ospiti di più Paesi e stagionalità forte, un'app o una web app può gestire prenotazioni, informazioni e avvisi in più lingue."),
    ('Agroalimentare e filiera del riso', "Nelle campagne del Novarese, aziende agricole e di trasformazione possono usare un'app per rilievi in campo, registro delle attività e tracciabilità dei lotti, con i dati sincronizzati quando c'è connessione."),
    ('Studi, centri e servizi alla persona', "Prenotazione di appuntamenti, promemoria e documenti. Spesso basta una web app; un'app ha senso quando servono notifiche e un legame frequente con chi la usa."),
    ('Commercio e attività locali', "Ordini, prenotazioni e fidelizzazione dei clienti abituali. Prima valutiamo se serve un'app o se una pagina ben fatta risolve lo stesso problema con meno costi."),
]

STEPS = [
    ('Primo incontro a Novara o in videochiamata', "Capiamo l'attività, chi userà l'app e cosa non funziona oggi. Se preferisci vederci di persona, ci incontriamo a Novara."),
    ('Analisi e preventivo scritto', "Funzioni, piattaforme e criteri di riuscita messi per iscritto, con tempi e costi, prima di iniziare."),
    ('Prototipo da provare', "Schermate cliccabili da provare con chi userà l'app, prima di scrivere il codice."),
    ('Sviluppo per rilasci', "Versioni intermedie da provare ogni poche settimane, poi test su dispositivi reali."),
    ('Pubblicazione e assistenza', "Invio agli store, gestione delle revisioni di Apple e Google e aggiornamenti dopo il rilascio."),
]

FAQ = [
    ("Sviluppate app a Novara?", "Sì. TiTech Digital ha sede a Novara e sviluppa app per iOS e Android per aziende e professionisti di Novara e provincia, e lavora anche a distanza con clienti di tutta Italia."),
    ("Dove ci si incontra?", "A Novara, oppure in videochiamata. Per clienti della provincia (Galliate, Trecate, Arona, Borgomanero, Oleggio e comuni vicini) si concorda l'incontro più comodo."),
    ("Per un'attività locale è meglio un'app o un sito?", "Dipende da come viene usato. Se i clienti consultano, prenotano o ordinano di rado, un sito veloce o una web app bastano e costano meno. Un'app serve quando l'uso è frequente, servono funzioni del telefono o il lavoro deve funzionare senza rete. Si decide nell'analisi: trovi i criteri nella pagina <a href=\"/servizi/app-mobile/\">sviluppo di app mobile</a>."),
    ("Quanto costa un'app?", "Dipende da quante funzioni ha, da quante piattaforme copre e da quanto si collega ad altri sistemi. Non pubblichiamo un listino: dopo l'analisi ricevi un preventivo scritto con perimetro, tempi e costi."),
]

RELATED = [
    ('/servizi/app-mobile/', 'Sviluppo di app mobile', "La guida completa: native, multipiattaforma o web app, cosa comprende il progetto e cosa decidono gli store."),
    ('/novara/', 'Sviluppo siti web a Novara', "Siti, e-commerce, software e SEO locale per le imprese di Novara e provincia."),
    ('/servizi/software-su-misura/', 'Software su misura', "Gestionali, portali clienti e dashboard: spesso il lato server dell'app."),
    ('/servizi/automazioni-ai/', 'Automazioni e AI', "Assistenti e flussi automatici, anche dentro un'app."),
]

TOWNS = ['Novara', 'Galliate', 'Trecate', 'Arona', 'Borgomanero', 'Oleggio', 'Altri comuni della provincia']


def esc(t):
    return html.escape(t, quote=False)


def strip_tags(t):
    return html.unescape(re.sub(r'<[^>]+>', '', t))


raw = open(os.path.join(ROOT, 'servizi', 'app-mobile', 'index.html'), encoding='utf-8').read()
head = raw[:raw.index('<script type="application/ld+json">')]
org = json.loads(re.search(r'\{\s*"@type": "Organization".*?\n    \},', raw, re.S).group(0).rstrip(','))
person = json.loads(re.search(r'\{\s*"@type": "Person".*?\n    \},', raw, re.S).group(0).rstrip(','))
header = raw[raw.index('<body>'):raw.index('<main id="main">')]
footer = raw[raw.index('<footer id="footer"'):]

SELF = SITE + '/servizi/app-mobile/'
head = re.sub(r'<title>.*?</title>', '<title>%s</title>' % esc(TITLE), head)
head = re.sub(r'(<meta name="description" content=")[^"]*(")', r'\g<1>%s\g<2>' % html.escape(DESC), head)
head = re.sub(r'(<meta property="og:title" content=")[^"]*(")', r'\g<1>%s\g<2>' % html.escape(TITLE), head)
head = re.sub(r'(<meta property="og:description" content=")[^"]*(")', r'\g<1>%s\g<2>' % html.escape(DESC), head)
head = head.replace(SELF, URL)
head = re.sub(r'\s*<link rel="alternate" hreflang="en"[^>]*>', '', head)
header = header.replace('/en/services/mobile-apps/', '/en/')

faq_nodes = [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': strip_tags(a)}} for q, a in FAQ]
prov = {'@type': 'AdministrativeArea', 'name': 'Provincia di Novara', 'containedInPlace': {'@type': 'AdministrativeArea', 'name': 'Piemonte'}}
graph = [org,
    {'@type': 'BreadcrumbList', '@id': URL + '#breadcrumb', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE + '/'},
        {'@type': 'ListItem', 'position': 2, 'name': 'Siti web a Novara', 'item': SITE + '/novara/'},
        {'@type': 'ListItem', 'position': 3, 'name': 'App a Novara', 'item': URL}]},
    {'@type': 'Service', '@id': URL + '#service', 'name': 'Sviluppo di app a Novara',
     'serviceType': 'Sviluppo di app mobile per iOS e Android', 'url': URL,
     'description': "Sviluppo di app per iOS e Android per aziende e professionisti di Novara e provincia: analisi, design, sviluppo, test, pubblicazione sugli store e aggiornamenti.",
     'provider': {'@id': SITE + '/#organization'},
     'areaServed': [{'@type': 'City', 'name': 'Novara', 'containedInPlace': prov}] +
                   [{'@type': 'City', 'name': t, 'containedInPlace': prov} for t in ('Galliate', 'Trecate', 'Arona', 'Borgomanero', 'Oleggio')],
     'availableChannel': {'@type': 'ServiceChannel', 'serviceUrl': SITE + '/contatti/'}},
    person,
    {'@type': 'WebPage', '@id': URL + '#webpage', 'url': URL, 'name': TITLE, 'description': DESC, 'inLanguage': 'it-IT',
     'isPartOf': {'@id': SITE + '/#website'}, 'author': {'@id': SITE + '/#enea-muja'},
     'breadcrumb': {'@id': URL + '#breadcrumb'}, 'about': {'@id': URL + '#service'}, 'datePublished': DATE, 'dateModified': DATE},
    {'@type': 'FAQPage', '@id': URL + '#faq', 'isPartOf': {'@id': URL + '#webpage'}, 'inLanguage': 'it-IT', 'mainEntity': faq_nodes}]
ld = '<script type="application/ld+json">\n' + json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False, indent=2) + '\n</script>\n</head>\n'

arrow = '<svg class="m-link__arrow" viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8h11M9 3.5 13.5 8 9 12.5"/></svg>'
scen = '\n'.join('        <li><strong>%s</strong><span>%s</span></li>' % (esc(t), esc(d)) for t, d in SCENARIOS)
steps = '\n'.join('        <div class="step">\n          <h3 class="m-text-7">%s</h3>\n          <p class="m-text">%s</p>\n        </div>' % (esc(t), esc(d)) for t, d in STEPS)
faq = '\n'.join('        <details>\n          <summary>%s</summary>\n          <p>%s</p>\n        </details>' % (esc(q), a) for q, a in FAQ)
related = '\n'.join('        <article class="tile">\n          <h3><a href="%s">%s</a></h3>\n          <p>%s</p>\n        </article>' % (u, esc(t), esc(d)) for u, t, d in RELATED)
CHIP = 'padding:7px 14px;border:1px solid rgba(247,248,246,.32);border-radius:999px;font-size:14px;font-weight:600'
towns = ''.join('<li style="%s">%s</li>' % (CHIP, esc(t)) for t in TOWNS)

main = '''<main id="main">
  <div class="shell page">
    <nav aria-label="Percorso">
      <ol class="crumbs">
        <li><a href="/">Home</a></li>
        <li><a href="/novara/">Siti web a Novara</a></li>
        <li aria-current="page">App a Novara</li>
      </ol>
    </nav>
    <div class="head">
      <p class="m-eyebrow">App · Novara</p>
      <h1 class="m-text-3 head__title">%(h1)s<span class="m-dot" aria-hidden="true"></span></h1>
      <p class="m-text-5 head__lead">%(lead)s</p>
      <div class="head__actions">
        <a class="m-btn" href="/contatti/"><span>Raccontaci cosa deve fare l'app</span></a>
        <a class="m-link" href="/servizi/app-mobile/"><span class="m-link__label">Come lavoriamo sulle app</span>%(arrow)s</a>
      </div>
      <p class="byline"><span class="byline__name">Enea Muja</span><span class="byline__role">CEO, TiTech Digital</span><time class="byline__date" datetime="%(date)s">Aggiornato il 10 novembre 2026</time></p>
    </div>

    <section class="sect" aria-labelledby="dove-title">
      <div class="sect__top">
        <h2 class="m-text-4" id="dove-title">Dove un'app serve alle aziende di Novara e provincia</h2>
        <p class="m-text">Cinque scenari tipici del territorio. Sono esempi di dove un'app può servire, non clienti: prima di proporla verifichiamo che serva davvero.</p>
      </div>
      <ul class="checks">
%(scen)s
      </ul>
      <div class="prose">
        <p>Se la tua attività non è in questo elenco, il metodo è lo stesso: partiamo da chi usa l'app, da quanto spesso e da cosa deve poter fare. Se un sito o una web app risolvono il problema con meno costi, lo scriviamo nel preventivo.</p>
      </div>
    </section>

    <section class="sect" aria-labelledby="metodo-title">
      <div class="sect__top">
        <h2 class="m-text-4" id="metodo-title">Come lavoriamo da Novara</h2>
        <p class="m-text">Un solo referente, un preventivo scritto e rilasci a pezzi, così si vede cosa funziona prima della fine.</p>
      </div>
      <div class="steps">
%(steps)s
      </div>
    </section>

    <section class="sect" aria-labelledby="zone-title">
      <div class="sect__top">
        <h2 class="m-text-4" id="zone-title">Zone servite</h2>
        <p class="m-text">La sede è a Novara. Ci incontriamo di persona a Novara e in provincia, e lavoriamo a distanza con clienti di tutta Italia.</p>
      </div>
      <ul class="zone-list" style="display:flex;flex-wrap:wrap;gap:10px;list-style:none">%(towns)s</ul>
    </section>

    <section class="sect sect--paper" aria-labelledby="faq-title">
      <div class="sect__top">
        <h2 class="m-text-4" id="faq-title">Domande frequenti sulle app a Novara</h2>
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
%(related)s
      </div>
    </section>

    <section class="sect" aria-labelledby="cta-title">
      <div class="cta">
        <h2 class="m-text-4 cta__title" id="cta-title">Parliamone a Novara<span class="m-dot" aria-hidden="true"></span></h2>
        <p class="m-text">Raccontaci chi userà l'app e cosa deve poter fare. Ti rispondiamo con una prima valutazione e, se serve, un preventivo scritto.</p>
        <div class="cta__actions">
          <a class="m-btn-2" href="/contatti/"><span>Scrivi a TiTech</span></a>
          <a class="m-link" href="/lavori/" style="color:inherit"><span class="m-link__label">Vedi il nostro portfolio</span>%(arrow)s</a>
        </div>
      </div>
    </section>
  </div>
</main>
''' % {'h1': esc(H1), 'lead': esc(LEAD), 'arrow': arrow, 'date': DATE, 'scen': scen, 'steps': steps, 'towns': towns, 'faq': faq, 'related': related}

out = os.path.join(ROOT, OUT)
os.makedirs(os.path.dirname(out), exist_ok=True)
open(out, 'w', encoding='utf-8', newline='\n').write(head + ld + header + main + footer)
print('wrote', OUT)
