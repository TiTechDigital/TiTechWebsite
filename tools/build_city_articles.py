"""Builds the three city-angle articles of the blog from the maintenance post as template.

They are guides, not city pages in disguise: each one answers a question the
reader of that area really has, says only what we can defend, and never claims a
client, a project or an office in the city. Italian only (see ITALIAN_ONLY in
tools/check_site.py).

Run: python tools/build_city_articles.py
Then: python tools/check_site.py
"""
import html
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://www.titechdigital.it'
TEMPLATE = os.path.join(ROOT, 'blog', 'manutenzione-sito-web', 'index.html')
DATE = '2026-11-08'
DATE_IT = '8 novembre 2026'

RANGES = ("Le fasce indicative per il mercato italiano: un sito vetrina tra 800 e 2.500 euro, "
          "un sito aziendale tra 2.000 e 6.500 euro, un e-commerce tra 4.000 e 15.000 euro. "
          "Il costo dipende dal perimetro, non dalla città. Per una stima veloce usa il "
          "<a href=\"/strumenti/calcolo-costo-sito-web/\">calcolatore del costo di un sito web</a>.")

ARTICLES = [
    {
        'slug': 'sito-web-aziende-agroalimentari',
        'title': 'Sito web per aziende agroalimentari: cosa serve davvero',
        'description': "Cosa deve avere il sito di un'azienda agricola o agroalimentare: prodotto, origine, richieste dei buyer, vendita diretta. Guida per Vercelli e provincia.",
        'section': 'Settori', 'minutes': 8,
        'keywords': 'sito web azienda agroalimentare, sito web azienda agricola, e-commerce prodotti alimentari, sito web Vercelli',
        'lead': "Un'azienda agricola o agroalimentare non vende un oggetto qualsiasi: vende origine, qualità e fiducia. Il sito deve far capire in pochi secondi cosa produci, per chi e come ordinare. Questa guida è pensata per le aziende di Vercelli e provincia, ma vale per tutta Italia.",
        'cta_link': ('/vercelli/', 'Siti web a Vercelli'),
        'takeaways': [
            ("Prima decidi chi deve capire cosa.", "Un buyer professionale, un ristoratore e un consumatore finale cercano cose diverse. Un sito che parla a tutti non convince nessuno."),
            ("Le pagine giuste sono poche.", "Prodotti, origine e filiera, certificazioni (solo quelle che hai), come ordinare e contatti. Il resto è accessorio."),
            ("Vendere online non è per tutti.", "Dipende da margini, conservazione, spedizione e volumi. Si calcola prima di aprire il negozio."),
            ("Per farsi trovare serve il territorio.", "Scheda Google, una pagina che dice dove sei e cosa fai, testi che citano davvero la zona."),
        ],
        'sections': [
            ('chi', 'Chi legge il sito e cosa cerca',
             "Le aziende agroalimentari parlano in genere a tre pubblici, e conviene sapere quale conta di più prima di disegnare una pagina.",
             ["<p><strong>I clienti professionali</strong> (ristoratori, negozi, distributori, industrie) vogliono sapere se puoi fornire, in che quantità, con quali formati e con quali documenti. Cercano un catalogo, una scheda tecnica e un contatto che risponda. Non vogliono leggere una storia di famiglia prima di trovare il listino.</p>",
              "<p><strong>I consumatori finali</strong> cercano un prodotto buono e un modo semplice per averlo. Contano le foto, la descrizione onesta, il prezzo e i tempi di consegna. La storia dell'azienda aiuta, ma dopo il prodotto.</p>",
              "<p><strong>Chi sta nella filiera</strong> (consorzi, associazioni, partner) usa il sito per verificare che l'azienda esista e sia affidabile. Gli bastano dati chiari: ragione sociale, partita IVA, certificazioni, contatti.</p>",
              "<p>Un sito riuscito sceglie un pubblico principale e dà agli altri una strada breve, per esempio un'area dedicata ai professionisti o un pulsante per l'acquisto diretto.</p>"]),
            ('pagine', 'Le pagine che servono',
             "Poche pagine, ognuna con un compito preciso. Il sito di un'azienda agroalimentare non ha bisogno di venti sezioni.",
             ["<ul class=\"checks\">",
              "<li><strong>Prodotti</strong><span>Una scheda per prodotto o varietà, con formati, caratteristiche e foto vere. Se cambiano con la stagione, si dice.</span></li>",
              "<li><strong>Origine e filiera</strong><span>Dove e come si produce, in modo concreto: zona, lavorazioni, tempi. Le parole generiche (\"tradizione\", \"qualità\") dicono poco.</span></li>",
              "<li><strong>Certificazioni</strong><span>Solo quelle che l'azienda possiede davvero (biologico, marchi di origine, certificazioni di processo), con il riferimento verificabile. Un'etichetta non documentata è un rischio, non un vantaggio.</span></li>",
              "<li><strong>Come ordinare</strong><span>Un percorso chiaro per i clienti professionali (richiesta di listino o preventivo) e uno per i privati (acquisto o punto vendita).</span></li>",
              "<li><strong>Contatti e zona</strong><span>Telefono, email, dove si trova l'azienda e dove consegna. È la pagina che molti cercano per prima.</span></li>",
              "</ul>"]),
            ('vendita', 'Vendere direttamente online: quando ha senso',
             "Il negozio online sembra l'ovvio passo successivo, ma per i prodotti alimentari ha vincoli che altri settori non hanno.",
             ["<p>Prima di costruire un e-commerce conviene fare i conti: prezzo di vendita, costo di imballaggio e spedizione, resi o scarti, commissioni di pagamento, tempo di chi prepara gli ordini. Per un prodotto a lunga conservazione e con un buon margine il conto può tornare. Per un prodotto fresco, fragile o a basso margine spesso no.</p>",
              "<p>Un modo semplice per cominciare è non vendere subito: far arrivare ordini da professionisti con un modulo e valutare il negozio solo dopo, quando i volumi lo giustificano. Per capire cosa resta di ogni vendita puoi usare il <a href=\"/strumenti/calcolo-margine-ecommerce/\">calcolatore del margine e-commerce</a>, e per le scelte di piattaforma vedi <a href=\"/blog/shopify-vs-sito-su-misura/\">Shopify o sito su misura</a>.</p>"]),
            ('contenuti', 'Foto, stagionalità e contenuti che invecchiano',
             "Un prodotto agricolo cambia con le stagioni. Il sito deve poterlo dire senza costare una modifica a ogni raccolto.",
             ["<p>Le foto contano più dei testi: un prodotto ripreso bene, in luce naturale, vale più di una descrizione lunga. Meglio poche immagini reali che molte di repertorio, che i clienti riconoscono.</p>",
              "<p>Le disponibilità stagionali e i listini cambiano: conviene un'area che l'azienda può aggiornare da sola, senza chiedere ogni volta a chi ha fatto il sito. Per questo un sito va costruito perché si possa modificare, e va mantenuto: vedi <a href=\"/blog/manutenzione-sito-web/\">cosa include la manutenzione</a>.</p>"]),
            ('seo', 'Farsi trovare dalle aziende e dalle persone della zona',
             "Chi cerca un fornitore o un produttore spesso aggiunge il nome del territorio. Il sito deve farsi trovare lì.",
             ["<p>Per un'attività che lavora su un territorio, la parte più utile non è il blog: è la scheda Google Business Profile, con categorie corrette, orari, foto reali e recensioni. Poi serve coerenza: nome, indirizzo e telefono uguali ovunque, e una pagina che dica chi sei, dove lavori e cosa fai. Ne parliamo nella <a href=\"/servizi/seo/\">consulenza SEO</a>.</p>",
              "<p>Se la tua azienda è a Vercelli o in provincia, trovi come lavoriamo con le aziende della zona nella pagina <a href=\"/vercelli/\">siti web a Vercelli</a>. Lavoriamo a distanza e, se preferisci, concordiamo un incontro di persona.</p>"]),
        ],
        'faq': [
            ("Un'azienda agricola ha bisogno di un sito?",
             "Se vende o cerca clienti fuori dal passaparola, sì: è il posto dove un buyer o un cliente verifica che l'azienda esista, cosa produca e come contattarla. Può essere piccolo, ma deve essere chiaro e aggiornato."),
            ("Serve un e-commerce per vendere prodotti alimentari?",
             "Non sempre. Dipende da margine, conservazione e spedizione. Spesso conviene partire da un sito con richieste d'ordine e aprire il negozio online solo se i numeri lo giustificano."),
            ("Quanto costa un sito web per un'azienda agroalimentare?", RANGES),
            ("Lavorate con aziende di Vercelli?",
             "Lavoriamo a distanza con aziende di tutta Italia, anche di Vercelli e provincia. Si parte da una videochiamata e, se preferisci, si concorda un incontro di persona. Vedi la pagina <a href=\"/vercelli/\">siti web a Vercelli</a>."),
        ],
        'related': [
            ('/vercelli/', 'Siti web a Vercelli', 'Come lavoriamo con le aziende di Vercelli e provincia.'),
            ('/servizi/e-commerce/', 'Realizzazione e-commerce', 'Se vendi un prodotto direttamente: catalogo, pagamenti, spedizioni.'),
            ('/blog/quanto-costa-sito-web-italia-2026/', 'Quanto costa un sito web in Italia nel 2026', 'Il metodo per leggere un preventivo.'),
        ],
        'cta_title': 'Partiamo da cosa produci e da chi lo compra',
        'cta_text': "Raccontaci cosa produce la tua azienda, a chi vende e cosa non funziona nel sito di oggi. Ti rispondiamo con una prima valutazione.",
    },
    {
        'slug': 'sito-web-hotel-ristoranti-lago-di-como',
        'title': 'Sito web per hotel e ristoranti sul Lago di Como',
        'description': "Come deve essere il sito di un hotel, B&B o ristorante sul lago: prenotazioni dirette, più lingue, scheda Google e foto. Guida per le attività di Como.",
        'section': 'Settori', 'minutes': 8,
        'keywords': 'sito web hotel Lago di Como, sito web ristorante Como, sito web B&B, prenotazioni dirette',
        'lead': "Un hotel, un B&B o un ristorante sul lago vive di visitatori che scelgono in fretta, da telefono e spesso in un'altra lingua. Il sito deve dare le risposte giuste nei primi secondi e portare la prenotazione a te, non a un portale. Una guida per le attività di Como e provincia.",
        'cta_link': ('/como/', 'Siti web a Como'),
        'takeaways': [
            ("Si decide da telefono.", "Camere, menu, prezzi o fasce, orari e come prenotare devono essere visibili senza scorrere in cerca."),
            ("La prenotazione diretta è il vero obiettivo.", "I portali portano ospiti ma trattengono commissioni. Il sito deve rendere semplice prenotare o chiamare direttamente."),
            ("Le lingue vanno progettate, non aggiunte.", "Struttura, indirizzi e collegamenti tra le versioni si decidono all'inizio."),
            ("La scheda Google pesa quanto il sito.", "Chi cerca \"ristorante vicino a me\" spesso non apre nemmeno il sito: guarda la scheda."),
        ],
        'sections': [
            ('chi', 'Chi cerca e da dove arriva',
             "Chi sceglie dove dormire o mangiare sul lago spesso non è del posto e decide guardando poche cose.",
             ["<p>Il visitatore tipico cerca da telefono, spesso in viaggio, e confronta più opzioni in pochi minuti. Guarda le foto, controlla dove si trova la struttura, legge le recensioni e cerca un modo semplice per prenotare o telefonare. Se il sito è lento o confuso, passa alla successiva.</p>",
              "<p>Per questo contano tre cose: velocità da rete mobile, informazioni pratiche subito visibili (posizione, orari, contatti, come arrivare) e un percorso di prenotazione che non richiede di cercare. Il design viene dopo.</p>"]),
            ('diretta', 'Prenotazioni dirette e portali',
             "I portali di prenotazione sono utili per farsi conoscere, ma hanno un costo. Il sito serve a far arrivare chi ti ha già trovato.",
             ["<p>I portali in genere trattengono una commissione su ogni prenotazione. Una prenotazione diretta, invece, arriva senza intermediari e permette di conoscere l'ospite. Per questo conviene che il sito renda il percorso diretto più semplice di quello del portale: disponibilità chiare, un modulo breve o un telefono ben visibile e un motore di prenotazione quando il volume lo giustifica.</p>",
              "<p>Per un ristorante la logica è simile: menu aggiornato, orari, giorni di chiusura e un modo di prenotare un tavolo. Trovi cosa comprende un sito per questo settore nella pagina sui <a href=\"/settori/ristorazione/\">siti per la ristorazione</a>.</p>"]),
            ('lingue', 'Più lingue fatte bene',
             "Sul lago i visitatori parlano lingue diverse. Un sito multilingua fatto male danneggia più di uno monolingua fatto bene.",
             ["<ul class=\"checks\">",
              "<li><strong>Una versione per lingua</strong><span>Ogni lingua ha il suo indirizzo e i suoi testi, collegati tra loro, non una traduzione automatica che cambia al volo.</span></li>",
              "<li><strong>Testi scritti o rivisti da una persona</strong><span>Una traduzione letterale suona male e fa perdere fiducia. Conta più la chiarezza della quantità.</span></li>",
              "<li><strong>Dati pratici nella lingua giusta</strong><span>Orari, politiche di cancellazione, come arrivare, cosa è incluso.</span></li>",
              "<li><strong>Un solo percorso di prenotazione</strong><span>Lo stesso in tutte le lingue, per non avere versioni che si disallineano.</span></li>",
              "</ul>",
              "<p>Questo sito è in italiano e inglese e mostra come collegare le versioni: guarda la <a href=\"/en/\">versione inglese</a> come esempio di struttura. Altre lingue si valutano in base a dove arrivano i tuoi clienti.</p>"]),
            ('google', 'Scheda Google, foto e recensioni',
             "Per chi lavora con i visitatori, la scheda Google è spesso la prima cosa che si vede.",
             ["<p>Una scheda completa (categoria giusta, orari aggiornati, foto reali, sito collegato, servizi) porta più contatti di molte pagine del sito. Le recensioni contano: rispondere a tutte, anche a quelle critiche, mostra attenzione. Non vanno mai scritte da noi né chieste in cambio di sconti.</p>",
              "<p>Le foto devono essere vere e recenti: camere come sono, piatti come arrivano, il lago che si vede davvero. Una foto troppo bella delude chi arriva. La parte tecnica è nella <a href=\"/servizi/seo/\">consulenza SEO</a>.</p>"]),
            ('stagione', 'Stagionalità e aggiornamenti',
             "Chiusure, orari estivi, eventi: un sito che dice cose vecchie fa perdere ospiti.",
             ["<p>Le attività sul lago cambiano con la stagione: orari, giorni di chiusura, menu e offerte. Il sito deve poterle aggiornare in fretta, senza aspettare chi lo ha costruito. Conviene un'area semplice per modificare orari e avvisi e un controllo periodico che tutto funzioni (modulo di contatto, prenotazioni, certificato). Vedi <a href=\"/blog/manutenzione-sito-web/\">cosa include la manutenzione</a>.</p>",
              "<p>Se hai un'attività a Como o in provincia, nella pagina <a href=\"/como/\">siti web a Como</a> trovi come lavoriamo: tutto a distanza, con prototipi online e consegna digitale.</p>"]),
        ],
        'faq': [
            ("Un B&B piccolo ha bisogno di un sito oltre alla scheda dei portali?",
             "Sì, se vuole prenotazioni dirette e non dipendere da un solo canale. Basta un sito semplice, veloce, con foto vere, disponibilità o contatto chiaro e la scheda Google collegata."),
            ("Quante lingue servono?",
             "Dipende da dove arrivano i tuoi ospiti. Italiano e inglese sono la base; altre lingue si aggiungono se i dati lo giustificano. Meglio due lingue fatte bene che cinque fatte male."),
            ("Quanto costa un sito web per un hotel o un ristorante?", RANGES),
            ("Lavorate con attività di Como?",
             "Lavoriamo a distanza con aziende di tutta Italia, anche di Como e provincia: videochiamata iniziale, prototipi online, consegna digitale. Vedi la pagina <a href=\"/como/\">siti web a Como</a>."),
        ],
        'related': [
            ('/como/', 'Siti web a Como', 'Come lavoriamo con le aziende di Como e provincia.'),
            ('/settori/ristorazione/', 'Siti per la ristorazione', 'Menu, prenotazioni e scheda Google collegati al sito.'),
            ('/blog/manutenzione-sito-web/', 'Manutenzione sito web', 'Cosa include e perché non è opzionale.'),
        ],
        'cta_title': 'Partiamo dalle prenotazioni dirette',
        'cta_text': "Raccontaci che tipo di attività hai, da dove arrivano i tuoi ospiti e come prenotano oggi. Ti rispondiamo con una prima valutazione.",
    },
    {
        'slug': 'preventivo-sito-web-milano',
        'title': 'Preventivo sito web a Milano: 8 domande prima di firmare',
        'description': "Otto domande da fare prima di firmare un preventivo per il sito della tua azienda: chi lavora al progetto, cosa è incluso, proprietà, tempi e SEO. Guida per Milano.",
        'section': 'Preventivi', 'minutes': 8,
        'keywords': 'preventivo sito web Milano, realizzazione sito web Milano, web agency Milano, cosa include un preventivo',
        'lead': "Prima di firmare un preventivo per il sito della tua azienda ci sono poche domande che cambiano tutto. Eccone otto, con cosa aspettarsi e come rispondiamo noi, che siamo una web agency di Novara e lavoriamo a distanza con le aziende di Milano.",
        'cta_link': ('/milano/', 'Siti web a Milano'),
        'takeaways': [
            ("Chiedi chi lavora davvero al progetto.", "Un solo referente che sviluppa vale più di una catena di account e project manager."),
            ("Pretendi un perimetro scritto.", "Cosa è incluso, cosa no, quanti giri di modifiche. Senza, il prezzo non si può valutare."),
            ("Verifica di chi è il sito alla fine.", "Dominio, codice e contenuti devono essere tuoi."),
            ("Un preventivo si legge sul perimetro.", "Il totale dice poco: contano le voci incluse, i tempi e cosa succede dopo il lancio."),
        ],
        'sections': [
            ('domande', 'Le otto domande',
             "Per ciascuna: cosa chiedere, cosa dovrebbe esserci nella risposta e come rispondiamo noi.",
             ["<ul class=\"checks\">",
              "<li><strong>1. Chi lavora al mio progetto?</strong><span>Vuoi sapere se parli con chi sviluppa o con un intermediario. Noi lavoriamo con un referente che segue il progetto dall'analisi alla messa online.</span></li>",
              "<li><strong>2. Cosa è incluso e cosa no?</strong><span>Pagine, testi, immagini, lingue, integrazioni, giri di modifiche. Se non è scritto, non è incluso. Il nostro preventivo è scritto e arriva in cinque giorni lavorativi.</span></li>",
              "<li><strong>3. Di chi sono codice, dominio e contenuti?</strong><span>Alla fine devono essere tuoi, con gli accessi in mano. Il sito non deve restare \"in affitto\" senza che sia detto chiaramente.</span></li>",
              "<li><strong>4. Quanto tempo serve e da cosa dipende?</strong><span>Un sito aziendale richiede in genere da quattro a otto settimane; il ritardo più comune sono i contenuti che arrivano tardi, non il codice.</span></li>",
              "<li><strong>5. Come si misura il risultato?</strong><span>Obiettivi chiari (richieste, telefonate, vendite) e strumenti come Search Console e Analytics. Nessuno può promettere una posizione su Google: si misura cosa succede.</span></li>",
              "<li><strong>6. Cosa succede dopo il lancio?</strong><span>Assistenza, aggiornamenti, backup. Noi includiamo trenta giorni di assistenza dopo la messa online e poi si concorda la manutenzione (<a href=\"/blog/manutenzione-sito-web/\">cosa include</a>).</span></li>",
              "<li><strong>7. Come si gestiscono il vecchio sito e la SEO?</strong><span>Un sito nuovo non deve perdere le posizioni che già ha: mappatura degli indirizzi, reindirizzamenti, controllo dell'indicizzazione.</span></li>",
              "<li><strong>8. Posso vedere lavori veri?</strong><span>Un progetto serio si mostra con lavori realizzati, non con immagini di repertorio. Il nostro <a href=\"/lavori/\">portfolio</a> raccoglie i lavori fatti finora.</span></li>",
              "</ul>"]),
            ('lavoriamo', 'Come lavoriamo con le aziende di Milano',
             "Il lavoro è digitale dall'inizio alla fine: conta il metodo, non la distanza.",
             ["<p>Si parte da una videochiamata per capire l'attività, i clienti e cosa non funziona oggi. Poi prototipi online da guardare e commentare, revisioni via messaggio o videochiamata e consegna digitale. Un incontro di persona si valuta caso per caso.</p>",
              "<p>Chi segue il progetto è la stessa persona dall'analisi alla messa online: non ci sono passaggi tra account e sviluppatori. Trovi come lavoriamo nella pagina <a href=\"/milano/\">siti web a Milano</a>.</p>"]),
            ('prezzo', 'Come si legge un preventivo',
             "Un totale senza voci non dice cosa stai comprando.",
             ["<p>Controlla cosa comprende: numero di pagine, testi scritti o da fornire, lingue, SEO tecnica, formazione per aggiornare il sito, assistenza dopo il lancio. Un preventivo molto basso spesso lascia fuori una di queste voci, che poi si paga a parte. Chiedi sempre di vedere le voci per iscritto.</p>",
              "<p>Per orientarti sui costi puoi usare il <a href=\"/strumenti/calcolo-costo-sito-web/\">calcolatore del costo di un sito web</a> e leggere <a href=\"/blog/quanto-costa-sito-web-italia-2026/\">quanto costa un sito web in Italia nel 2026</a>.</p>"]),
            ('seo', 'La SEO a Milano: cosa aspettarsi',
             "A Milano la concorrenza su Google è alta. Un preventivo onesto lo dice.",
             ["<p>Le ricerche generiche come \"agenzia web Milano\" sono tra le più contese: nessuno può garantirti una posizione. Conviene puntare a ricerche specifiche (servizio, settore, problema), a una scheda Google curata e a contenuti che rispondono a domande reali. Misurare con Search Console dice se si sta andando nella direzione giusta. Vedi la <a href=\"/servizi/seo/\">consulenza SEO</a>.</p>"]),
        ],
        'faq': [
            ("Cosa deve contenere un preventivo per un sito web?",
             "Perimetro (pagine, testi, lingue, integrazioni), numero di giri di modifiche, tempi, costi, cosa è incluso dopo il lancio e a chi appartengono codice, dominio e contenuti. Se una voce manca, chiedila per iscritto."),
            ("Quanto tempo serve per avere un preventivo?",
             "Il nostro preventivo scritto arriva in cinque giorni lavorativi dalla prima call. Per un sito aziendale il lavoro richiede poi in genere da quattro a otto settimane."),
            ("Quanto costa un sito web a Milano?", RANGES),
            ("Lavorate con aziende di Milano?",
             "Sì, a distanza: call iniziale, prototipi online, consegna digitale. Un incontro di persona si valuta caso per caso. Vedi la pagina <a href=\"/milano/\">siti web a Milano</a>."),
        ],
        'related': [
            ('/milano/', 'Siti web a Milano', 'Come lavoriamo con le aziende di Milano.'),
            ('/blog/quanto-costa-sito-web-italia-2026/', 'Quanto costa un sito web in Italia nel 2026', 'Il metodo per leggere un preventivo.'),
            ('/servizi/siti-web/', 'Realizzazione siti web', 'Cosa comprende un progetto, passo per passo.'),
        ],
        'cta_title': 'Facci le stesse otto domande',
        'cta_text': "Scrivici cosa ti serve e chiedici cosa è incluso, tempi e proprietà del sito. Ti rispondiamo per iscritto.",
    },
]

raw = open(TEMPLATE, encoding='utf-8').read()
head_prefix = raw[:raw.index('<script type="application/ld+json">')]
org_node = re.search(r'\{\s*"@type": "Organization".*?\n    \},', raw, re.S).group(0).rstrip(',')
person_node = re.search(r'\{\s*"@type": "Person".*?\n    \},', raw, re.S).group(0).rstrip(',')
header_block = raw[raw.index('<body>'):raw.index('<main id="main">')].replace('/en/blog/website-maintenance/', '/en/blog/')
footer_block = raw[raw.index('<footer id="footer"'):]


def esc(t):
    return html.escape(t, quote=False)


def strip_tags(t):
    return html.unescape(re.sub(r'<[^>]+>', '', t))


def build(a):
    url = '%s/blog/%s/' % (SITE, a['slug'])
    head = head_prefix
    head = re.sub(r'<title>.*?</title>', '<title>%s</title>' % esc(a['title']), head)
    head = re.sub(r'(<meta name="description" content=")[^"]*(")', r'\g<1>%s\g<2>' % html.escape(a['description']), head)
    head = re.sub(r'(<meta property="og:title" content=")[^"]*(")', r'\g<1>%s\g<2>' % html.escape(a['title'] + ' | TiTech Digital'), head)
    head = re.sub(r'(<meta property="og:description" content=")[^"]*(")', r'\g<1>%s\g<2>' % html.escape(a['description']), head)
    head = head.replace('https://www.titechdigital.it/blog/manutenzione-sito-web/', url)
    head = re.sub(r'\s*<link rel="alternate" hreflang="en"[^>]*>', '', head)
    head = re.sub(r'(article:published_time" content=")[^"]*(")', r'\g<1>%s\g<2>' % DATE, head)
    head = re.sub(r'(article:modified_time" content=")[^"]*(")', r'\g<1>%s\g<2>' % DATE, head)
    head = re.sub(r'(article:section" content=")[^"]*(")', r'\g<1>%s\g<2>' % html.escape(a['section']), head)

    faq_nodes = [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': strip_tags(ans)}} for q, ans in a['faq']]
    graph = [
        json.loads(org_node),
        {'@type': 'BreadcrumbList', '@id': url + '#breadcrumb', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE + '/'},
            {'@type': 'ListItem', 'position': 2, 'name': 'Blog', 'item': SITE + '/blog/'},
            {'@type': 'ListItem', 'position': 3, 'name': a['title'], 'item': url}]},
        json.loads(person_node),
        {'@type': 'BlogPosting', 'image': SITE + '/assets/img/og-card-it-1200x630.png', '@id': url + '#article',
         'headline': a['title'], 'description': a['description'], 'url': url,
         'mainEntityOfPage': {'@id': url + '#webpage'}, 'inLanguage': 'it-IT',
         'datePublished': DATE, 'dateModified': DATE,
         'author': {'@id': SITE + '/#enea-muja'}, 'publisher': {'@id': SITE + '/#organization'},
         'articleSection': a['section'], 'keywords': a['keywords'],
         'isPartOf': {'@type': 'Blog', '@id': SITE + '/blog/#blog', 'name': 'TiTech Digital Blog', 'url': SITE + '/blog/'}},
        {'@type': 'WebPage', '@id': url + '#webpage', 'url': url, 'name': a['title'], 'inLanguage': 'it-IT',
         'author': {'@id': SITE + '/#enea-muja'}, 'breadcrumb': {'@id': url + '#breadcrumb'},
         'about': {'@id': url + '#article'}, 'datePublished': DATE, 'dateModified': DATE},
        {'@type': 'FAQPage', '@id': url + '#faq', 'isPartOf': {'@id': url + '#webpage'}, 'inLanguage': 'it-IT', 'mainEntity': faq_nodes},
    ]
    ld = '<script type="application/ld+json">\n' + json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False, indent=2) + '\n</script>\n</head>\n'

    takeaways = '\n'.join('        <li><strong>%s</strong> %s</li>' % (esc(t), esc(d)) for t, d in a['takeaways'])
    toc = '\n'.join('        <li><a href="#%s"><span class="toc__num">%02d</span><span>%s</span></a></li>' % (sid, i + 1, esc(t))
                    for i, (sid, t, _, _) in enumerate(a['sections']))
    sections = '\n\n'.join(
        '    <section class="sect" id="%s" aria-labelledby="%s-title">\n      <div class="sect__top">\n        <h2 class="m-text-4" id="%s-title">%s</h2>\n        <p class="m-text">%s</p>\n      </div>\n      <div class="prose">\n%s\n      </div>\n    </section>'
        % (sid, sid, sid, esc(t), esc(lead), '\n'.join('        ' + p for p in body))
        for sid, t, lead, body in a['sections'])
    faq = '\n'.join('        <details class="faq__item"><summary class="m-text-7">%s<span class="faq__mark" aria-hidden="true"></span></summary><p class="m-text faq__answer">%s</p></details>' % (esc(q), ans) for q, ans in a['faq'])
    cards = '\n'.join('        <article class="card card--link">\n          <h3 class="card__title"><a href="%s">%s</a></h3>\n          <p class="card__text">%s</p>\n        </article>' % (u, esc(t), d) for u, t, d in a['related'])
    link_url, link_label = a['cta_link']

    main = '''<main id="main">
  <div class="shell page">
    <nav aria-label="Percorso">
      <ol class="crumbs">
        <li><a href="/">Home</a></li>
        <li><a href="/blog/">Blog</a></li>
        <li aria-current="page">%(crumb)s</li>
      </ol>
    </nav>
    <div class="head">
      <p class="m-eyebrow">Blog · %(section)s</p>
      <h1 class="m-text-3 head__title">%(title)s<span class="m-dot" aria-hidden="true"></span></h1>
      <p class="m-text-5 head__lead">%(lead)s</p>
      <div class="head__actions">
        <a class="m-btn" href="/contatti/"><span>Parliamo del tuo progetto</span></a>
        <a class="m-link" href="%(link_url)s"><span class="m-link__label">%(link_label)s</span><svg class="m-link__arrow" viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8h11M9 3.5 13.5 8 9 12.5"/></svg></a>
      </div>
      <p class="byline"><span class="byline__name">Enea Muja</span><span class="byline__role">CEO, TiTech Digital · %(minutes)s min di lettura</span><time class="byline__date" datetime="%(date)s">Aggiornato il %(date_it)s</time></p>
    </div>

    <aside class="takeaways" aria-labelledby="takeaways-title">
      <h2 class="m-text-7" id="takeaways-title">In breve</h2>
      <ul>
%(takeaways)s
      </ul>
    </aside>

    <nav class="toc" aria-label="In questa pagina">
      <ol>
%(toc)s
      </ol>
    </nav>

%(sections)s

    <section class="sect" id="faq" aria-labelledby="faq-title">
      <div class="sect__top">
        <h2 class="m-text-4" id="faq-title">Domande frequenti</h2>
      </div>
      <div class="faq">
%(faq)s
      </div>
    </section>

    <section class="sect" id="correlati" aria-labelledby="correlati-title">
      <div class="sect__top">
        <h2 class="m-text-4" id="correlati-title">Continua a leggere</h2>
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
          <a class="m-btn-2" href="/contatti/"><span>Scrivi a TiTech</span></a>
          <a class="m-link" href="/lavori/" style="color:inherit"><span class="m-link__label">Vedi il nostro portfolio</span><svg class="m-link__arrow" viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8h11M9 3.5 13.5 8 9 12.5"/></svg></a>
        </div>
      </div>
    </section>
  </div>
</main>
''' % {'crumb': esc(a['title']), 'section': esc(a['section']), 'title': esc(a['title']), 'lead': esc(a['lead']),
       'link_url': link_url, 'link_label': esc(link_label), 'minutes': a['minutes'], 'date': DATE, 'date_it': DATE_IT,
       'takeaways': takeaways, 'toc': toc, 'sections': sections, 'faq': faq, 'cards': cards,
       'cta_title': esc(a['cta_title']), 'cta_text': esc(a['cta_text'])}
    return head + ld + header_block + main + footer_block


for a in ARTICLES:
    out = os.path.join(ROOT, 'blog', a['slug'])
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, 'index.html'), 'w', encoding='utf-8', newline='\n').write(build(a))
    words = len(re.sub(r'<[^>]+>', ' ', open(os.path.join(out, 'index.html'), encoding='utf-8').read().split('<main')[1].split('</main>')[0]).split())
    print('wrote blog/%s/index.html (%d words)' % (a['slug'], words))
