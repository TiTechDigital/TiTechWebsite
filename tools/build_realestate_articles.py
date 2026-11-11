"""Builds the five real-estate articles (one general, four with a local angle).

Same rules as build_city_articles.py: each one answers a question the reader of
that area really has, none claims a client, a project or an office we do not
have, and the local ones differ in substance (not only in the city name).
Italian only (see ITALIAN_ONLY in tools/check_site.py).

Run: python tools/build_realestate_articles.py
Then: python tools/check_site.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_city_articles as bc

bc.DATE = '2026-11-11'
bc.DATE_IT = '11 novembre 2026'
RANGES = bc.RANGES


def a(href, text):
    return '<a href="%s">%s</a>' % (href, text)


def checks(items):
    out = ['<ul class="checks">']
    out += ['<li><strong>%s</strong><span>%s</span></li>' % (t, d) for t, d in items]
    out.append('</ul>')
    return out


NOTE_RANKING = ("Nessuno può garantire una posizione su Google: dipende dalla concorrenza, dall'età del sito e dalle recensioni. "
                "Quello che si può fare è costruire basi corrette e misurare i risultati nel tempo.")

ARTICLES = [
    # ------------------------------------------------------------------ general
    {
        'slug': 'sito-web-agenzie-immobiliari',
        'title': 'Sito web per agenzie immobiliari: cosa serve davvero',
        'description': "Pagine, schede immobile, richiesta di valutazione e contatti: cosa deve avere il sito di un'agenzia immobiliare e come affiancarlo ai portali.",
        'section': 'Settori', 'minutes': 9,
        'keywords': 'sito web agenzia immobiliare, creazione sito web immobiliare, sito web per agenti immobiliari, portali immobiliari, scheda immobile',
        'lead': "Il settore si chiama immobiliare. Chi lavora nella compravendita e nelle locazioni è l'agente immobiliare (o mediatore) e di solito opera in un'agenzia immobiliare. Il sito di un'agenzia ha un compito preciso: far vedere gli immobili, dare fiducia e portare telefonate e richieste di valutazione. Una guida pratica, per tutta Italia.",
        'cta_link': ('/servizi/siti-web/', 'Realizzazione siti web'),
        'takeaways': [
            ("Il sito completa i portali, non li sostituisce.", "I portali portano visibilità; il sito è dove il contatto resta tuo e dove dimostri chi sei."),
            ("Le pagine che contano sono poche.", "Immobili, scheda dell'immobile, valutazione, zone dove lavori, chi siete e contatti."),
            ("Ogni immobile è una pagina vera.", "Foto reali, dati completi e un contatto diretto: telefono o WhatsApp a un tocco."),
            ("La fiducia si costruisce con persone e dati.", "Volti, ragione sociale e recensioni vere valgono più di slogan."),
        ],
        'sections': [
            ('portali', 'Portali o sito proprio: non è una scelta',
             "Quasi ogni agenzia pubblica già i propri annunci sui grandi portali. La domanda utile è cosa dà in più un sito.",
             ["<p>I portali portano molte visite, ma tutto si paga per annuncio o per abbonamento e il cliente resta, in pratica, del portale: chi cerca confronta cento annunci e dopo il primo contatto passa al successivo. Sul tuo sito il confronto è tra te e il tuo lavoro: la persona vede come lavori, quali zone conosci e perché dovrebbe affidarti la sua casa.</p>",
              "<p>La strategia più sensata è usare entrambi: i portali per farti trovare da chi cerca un immobile, il sito per far arrivare i proprietari che vogliono vendere, per raccogliere i contatti e per fidelizzare chi ti ha già conosciuto. Nei portali l'annuncio rimanda al tuo sito e al tuo telefono, non a un modulo del portale.</p>"]),
            ('pagine', 'Le pagine che servono',
             "Un sito immobiliare non ha bisogno di venti sezioni. Servono poche pagine, ognuna con un compito.",
             checks([
                 ("Immobili", "L'elenco con filtri essenziali: contratto (vendita o affitto), tipologia, zona, prezzo, camere. Si legge bene da telefono."),
                 ("Scheda dell'immobile", "La pagina più importante: foto, dati, mappa e contatto. Ne parliamo sotto."),
                 ("Valuta la tua casa", "Un modulo breve per i proprietari, con una spiegazione di come si fa la valutazione. È la pagina che porta i mandati di vendita."),
                 ("Zone", "Le zone dove lavori davvero, con informazioni utili scritte da chi le conosce. Non un elenco di nomi di città."),
                 ("Chi siete", "Le persone dell'agenzia, con nome, ruolo e foto vera, e i dati dell'agenzia."),
                 ("Contatti", "Telefono, WhatsApp, email, orari e come arrivare. È la pagina che molti aprono per prima."),
             ])),
            ('scheda', 'La scheda dell\'immobile fatta bene',
             "Chi apre un annuncio vuole decidere in fretta se vale la pena chiamare. La scheda deve rispondere senza farlo cercare.",
             ["<ul><li><strong>Foto reali e ordinate</strong>: ingresso, zona giorno, camere, bagni, esterni. Poche foto buone battono molte foto scure.</li><li><strong>Dati completi</strong>: superficie, locali, piano, riscaldamento, anno, spese condominiali, prezzo.</li><li><strong>Planimetria</strong>, quando c'è: aiuta a capire gli spazi.</li><li><strong>Posizione</strong> sulla mappa, anche approssimata.</li><li><strong>Un modo semplice di contattare</strong>: telefono e WhatsApp a un tocco, non solo un modulo.</li></ul>",
              "<p>Negli annunci commerciali la normativa richiede anche i dati energetici (classe e indice di prestazione energetica dall'attestato APE): verifica con il tuo consulente o con l'associazione di categoria cosa deve comparire e dove.</p>",
              "<p>Un dettaglio che si dimentica: cosa succede quando l'immobile si vende. Cancellare la pagina fa perdere visite e crea errori; conviene lasciarla con lo stato \"venduto\" e proporre immobili simili, oppure reindirizzarla.</p>"]),
            ('gestionale', 'Gestionale e aggiornamento degli annunci',
             "Inserire ogni annuncio due volte, nel gestionale e nel sito, è il modo più sicuro per smettere di aggiornarlo.",
             ["<p>Molte agenzie usano un software gestionale per caricare gli immobili e pubblicarli sui portali. Se il tuo gestionale può esportare gli annunci, il sito può importarli in automatico e restare allineato. Non tutti i gestionali lo permettono e il costo dell'integrazione si valuta a parte, in base a come esporta i dati.</p>",
              "<p>Se l'esportazione non c'è, la soluzione è un pannello semplice dove l'agenzia inserisce gli annunci da sola, con pochi campi chiari. Quello che conviene evitare è un sito che richiede una telefonata a chi l'ha fatto per ogni nuovo immobile. Sul perché un sito va mantenuto vedi " + a('/blog/manutenzione-sito-web/', 'cosa include la manutenzione') + ".</p>"]),
            ('fiducia', 'Fiducia e farsi trovare',
             "Chi affida una casa sceglie una persona prima di un'agenzia. Il sito deve far capire con chi si ha a che fare.",
             ["<p>Mostra i volti e i nomi di chi lavora in agenzia, i dati dell'agenzia (ragione sociale, partita IVA, sede) e le recensioni vere, quelle sulla scheda Google, senza ritoccarle. Se hai venduto immobili in una zona, racconta come è andata, con il permesso del cliente e senza dati che lo rendano riconoscibile.</p>",
              "<p>Per farsi trovare in locale la parte che rende di più è la scheda Google, seguita da una pagina che dica dove lavori e cosa fai e da testi che citano davvero le zone. Ne parliamo nella " + a('/servizi/seo/', 'consulenza SEO') + ". " + NOTE_RANKING + "</p>"]),
        ],
        'faq': [
            ("Come si chiama chi vende e affitta case?",
             "In Italia si parla di agente immobiliare o mediatore immobiliare, e di agenzia immobiliare per l'attività. Chi cerca online usa soprattutto \"agenzia immobiliare\" e \"agente immobiliare\" seguiti dalla città, ed è per questo che il sito deve citare dove lavori."),
            ("Serve un sito se pubblico già gli annunci sui portali?",
             "Sì, perché sui portali gli annunci sono tutti simili e il cliente resta del portale. Il sito è dove spieghi come lavori, raccogli le richieste di valutazione dei proprietari e fai conoscere le persone dell'agenzia."),
            ("Quanto costa un sito web per un'agenzia immobiliare?", RANGES + " Un'eventuale integrazione con il gestionale per importare gli annunci si valuta a parte."),
            ("Quanto tempo serve per comparire su Google?",
             "Dipende dalla concorrenza della zona. Per ricerche locali poco affollate possono bastare alcune settimane o mesi, per le città grandi serve di più. " + NOTE_RANKING),
        ],
        'related': [
            ('/blog/sito-web-agenzie-immobiliari-novara/', 'Sito web per agenzie immobiliari a Novara', 'Il taglio per le agenzie di Novara e provincia.'),
            ('/blog/sito-web-agenzie-immobiliari-milano/', 'Sito web per agenzie immobiliari a Milano', 'Come distinguersi in un mercato pieno di portali e reti.'),
            ('/blog/sito-web-agenzie-immobiliari-como/', 'Sito web per agenzie immobiliari a Como', 'Più lingue e immobili di pregio sul lago.'),
        ],
        'cta_title': 'Parliamo del sito della tua agenzia',
        'cta_text': "Raccontaci dove lavori, che immobili tratti e come gestisci gli annunci oggi. Ti rispondiamo con una prima valutazione e un preventivo scritto.",
    },
    # ------------------------------------------------------------------ Novara
    {
        'slug': 'sito-web-agenzie-immobiliari-novara',
        'title': 'Sito web per agenzie immobiliari a Novara: come farsi scegliere',
        'description': "Come deve essere il sito di un'agenzia immobiliare di Novara: zone, scheda Google, richiesta di valutazione e annunci. Guida per Novara e provincia.",
        'section': 'Settori', 'minutes': 8,
        'keywords': 'agenzia immobiliare Novara, sito web agenzia immobiliare Novara, creazione sito immobiliare Novara, valutazione immobile Novara',
        'lead': "Un'agenzia immobiliare di Novara compete con le altre agenzie della città e dei comuni intorno, oltre che con i portali. Il sito deve far capire in pochi secondi dove lavori, cosa tratti e perché fidarsi. Una guida per le agenzie di Novara e provincia.",
        'cta_link': ('/novara/', 'Siti web a Novara'),
        'takeaways': [
            ("A Novara si compete sulla conoscenza della zona.", "Il sito deve mostrare che conosci davvero i quartieri e i comuni dove lavori."),
            ("La scheda Google viene prima del sito.", "Chi cerca \"agenzia immobiliare Novara\" vede prima la mappa con le schede."),
            ("La valutazione è la pagina che porta mandati.", "Un modulo breve e una spiegazione chiara di come si valuta."),
            ("Pagine per zona solo se reali.", "Un testo fotocopia con il nome del comune cambiato non serve a nessuno."),
        ],
        'sections': [
            ('mercato', 'Chi cerca casa a Novara e come',
             "Prima di disegnare il sito, conviene chiedersi chi sono le persone che chiamano la tua agenzia.",
             ["<p>Chi cerca casa in zona è di solito una famiglia della città o dei comuni vicini, ma c'è anche chi lavora a Milano o a Torino e cerca vicino alla stazione, sfruttando i collegamenti ferroviari. Ci sono proprietari che vogliono vendere e chi cerca in affitto. Sono profili che puoi verificare con le tue richieste: non sono dati statistici, ma un modo per decidere cosa mettere in primo piano.</p>",
              "<p>Se la maggior parte delle tue chiamate viene da proprietari, la prima schermata del sito deve parlare di valutazione; se vengono da chi cerca, deve mostrare subito gli immobili e un filtro semplice. Un sito che fa tutte e due le cose allo stesso peso non convince nessuno.</p>"]),
            ('zone', 'Zone e comuni: scrivi solo quelle che conosci',
             "La tentazione è creare una pagina per ogni comune della provincia. Funziona solo se hai qualcosa di vero da dire.",
             ["<p>Una pagina di zona è utile quando racconta cose che solo chi lavora lì sa: che tipo di immobili prevalgono, come sono i collegamenti, quali servizi ci sono, come si muove il mercato. Se non hai immobili né esperienza in un comune, non scrivere la pagina: Google riconosce i testi ripetuti e il lettore anche.</p>",
              "<p>Per le agenzie dei comuni più piccoli intorno a Novara abbiamo scritto una guida a parte: " + a('/blog/sito-web-agenzia-immobiliare-piccoli-comuni/', 'sito web per l\'agenzia di un piccolo comune') + ".</p>"]),
            ('google', 'La scheda Google e la ricerca locale',
             "Chi cerca un'agenzia a Novara vede per prima la mappa con tre schede. È lì che si decide la prima chiamata.",
             ["<ul><li>Categoria corretta (\"agenzia immobiliare\") e orari reali.</li><li>Foto vere dell'ufficio e della squadra.</li><li>Recensioni di clienti reali, chieste a tutti, senza sconti o incentivi: le recensioni comprate o scritte da altri sono vietate da Google e danneggiano la scheda.</li><li>Un sito che dice le stesse cose della scheda: stesso nome, stesso indirizzo, stesso telefono.</li></ul>",
              "<p>Come lavoriamo con le attività di zona è spiegato nella pagina " + a('/novara/', 'siti web a Novara') + ".</p>"]),
            ('valutazione', 'La richiesta di valutazione che porta mandati',
             "Il proprietario che vuole sapere quanto vale la sua casa è il cliente più prezioso: porta un mandato di vendita.",
             ["<p>La pagina deve spiegare in poche righe come si fa la valutazione (confronto con le vendite recenti, sopralluogo, tempi di risposta) e offrire un modulo breve: indirizzo o zona, tipologia, telefono, consenso al trattamento dei dati. Più campi si chiedono, meno persone arrivano in fondo.</p>",
              "<p>Rispondere in giornata fa più della grafica. Conviene anche decidere in anticipo chi risponde alla richiesta e come viene registrata, così nessun contatto si perde.</p>"]),
            ('limiti', 'Cosa può fare il sito e cosa no',
             "Un sito ben fatto è una base. Il resto è lavoro di agenzia, e di tempo.",
             ["<p>Il sito aiuta a farsi trovare, a dare fiducia e a raccogliere contatti; non vende al posto tuo e non porta clienti da un giorno all'altro. " + NOTE_RANKING + "</p>",
              "<p>Noi siamo a Novara: se preferisci ci si incontra di persona in città, altrimenti si lavora in videochiamata. Prima di iniziare ricevi un preventivo scritto con perimetro, tempi e costi.</p>"]),
        ],
        'faq': [
            ("Quanto costa un sito web per un'agenzia immobiliare a Novara?", RANGES),
            ("Meglio i portali o un sito mio?",
             "Entrambi: i portali per farti trovare da chi cerca casa, il sito per i proprietari e per far conoscere come lavori. Il contatto sul sito resta tuo. Vedi la " + a('/blog/sito-web-agenzie-immobiliari/', 'guida generale per le agenzie immobiliari') + "."),
            ("Serve una pagina per ogni comune della provincia?",
             "No. Serve una pagina per le zone dove lavori davvero e dove hai qualcosa di concreto da dire. Le pagine fotocopia non aiutano e possono danneggiare il sito."),
            ("Lavorate con agenzie di Novara?",
             "Lavoriamo a distanza con attività di tutta Italia e abbiamo sede a Novara, quindi è facile anche incontrarsi. Si parte da una videochiamata e da un preventivo scritto."),
        ],
        'related': [
            ('/blog/sito-web-agenzie-immobiliari/', 'Sito web per agenzie immobiliari', 'La guida generale: pagine, schede e contatti.'),
            ('/blog/sito-web-agenzia-immobiliare-piccoli-comuni/', 'Sito per l\'agenzia di un piccolo comune', 'Da dove cominciare fuori dalle città grandi.'),
            ('/novara/', 'Siti web a Novara', 'Come lavoriamo con le attività di Novara e provincia.'),
        ],
        'cta_title': 'Partiamo da dove lavora la tua agenzia',
        'cta_text': "Dicci in quali zone lavori, che immobili tratti e come ricevi le richieste oggi. Ti rispondiamo per iscritto con una prima valutazione.",
    },
    # ------------------------------------------------------------------ Milano
    {
        'slug': 'sito-web-agenzie-immobiliari-milano',
        'title': 'Sito web per agenzie immobiliari a Milano: come distinguersi',
        'description': "A Milano portali e grandi reti occupano tutto: come scegliere una nicchia, quali contenuti pubblicare e cosa aspettarsi da Google per un'agenzia immobiliare.",
        'section': 'Settori', 'minutes': 9,
        'keywords': 'agenzia immobiliare Milano, sito web agenzia immobiliare Milano, sito web immobiliare Milano, agente immobiliare Milano',
        'lead': "Milano è il mercato immobiliare più affollato: portali, grandi reti e agenzie di quartiere. Un nuovo sito non vince scrivendo \"agenzia immobiliare Milano\" in tutte le pagine: vince dicendo chiaramente cosa fai meglio e per chi. Una guida per le agenzie milanesi.",
        'cta_link': ('/milano/', 'Siti web a Milano'),
        'takeaways': [
            ("Contro chi giochi.", "Portali e reti dominano le ricerche generiche: serve una nicchia."),
            ("Una nicchia è un quartiere, un tipo di immobile o un servizio.", "E il sito la dice nella prima schermata."),
            ("Contenuti che un portale non ha.", "Guide di zona scritte da chi la conosce e processo di vendita spiegato."),
            ("Le aspettative vanno misurate.", "Le ricerche generiche richiedono tempo; quelle specifiche portano prima."),
        ],
        'sections': [
            ('concorrenza', 'Contro chi giochi davvero',
             "Per la ricerca \"agenzia immobiliare Milano\" compaiono i portali, le grandi reti e centinaia di agenzie. Un sito nuovo non è il favorito.",
             ["<p>Dichiararlo non è pessimismo: è il punto di partenza per scegliere dove investire. Competere sulle parole più generiche richiede anni, recensioni e molti collegamenti da altri siti. Più conviene puntare dove puoi arrivare prima: una zona precisa, un tipo di immobile, un tipo di cliente.</p>"]),
            ('nicchia', 'Scegliere una nicchia e dirla subito',
             "Una nicchia non è una limitazione: è il motivo per cui qualcuno ti chiama invece di chiamare un'altra agenzia.",
             checks([
                 ("Una zona", "Un quartiere o un gruppo di quartieri che conosci a fondo: scuole, trasporti, edifici, prezzi, come cambia la domanda."),
                 ("Un tipo di immobile", "Bilocali per investimento, ville, uffici, immobili da ristrutturare: ciò in cui hai esperienza vera."),
                 ("Un servizio", "Gestione degli affitti, vendite con consulenza sulla ristrutturazione, assistenza a chi compra da fuori città."),
                 ("Un tipo di cliente", "Chi vende, chi investe, chi si trasferisce per lavoro. La prima schermata dice a chi parli."),
             ])),
            ('contenuti', 'Contenuti che un portale non ha',
             "I portali hanno gli annunci di tutti. Tu puoi avere ciò che un annuncio non dice.",
             ["<ul><li><strong>Guide di zona</strong> scritte da chi lavora lì: com'è vivere nel quartiere, cosa si trova, che tipo di immobili ci sono.</li><li><strong>Dati di mercato con la fonte</strong>: per i valori di zona esistono rilevazioni pubbliche (per esempio quelle dell'Osservatorio del Mercato Immobiliare dell'Agenzia delle Entrate). Cita la fonte e non inventare cifre.</li><li><strong>Il processo spiegato</strong>: valutazione, mandato, visite, proposta, rogito, tempi e costi, senza gergo.</li><li><strong>Storie di vendita</strong>, con il permesso del cliente e senza dati riconoscibili.</li></ul>",
              "<p>Questi contenuti non vanno ripetuti identici per ogni quartiere: una guida utile per uno vale per uno. Se i testi sono fotocopie con il nome cambiato, i motori li riconoscono come pagine inutili.</p>"]),
            ('lingue', 'Una versione in inglese solo se serve',
             "Milano attira acquirenti e affittuari da fuori Italia, ma non tutte le agenzie hanno bisogno di un sito bilingue.",
             ["<p>Se parte dei tuoi clienti è straniera e tu parli con loro in inglese, una versione inglese è sensata: una vera, scritta o rivista da una persona, con un indirizzo suo e collegata alla versione italiana. Se invece non ricevi richieste in inglese, una traduzione affrettata danneggia più che aiutare. Su come si costruisce un sito in due lingue vedi la " + a('/en/', 'versione inglese di questo sito') + " come esempio di struttura.</p>"]),
            ('velocita', 'Velocità: gli annunci hanno molte foto',
             "Un annuncio con trenta foto pesanti su una connessione mobile è lento, e chi aspetta passa oltre.",
             ["<p>Le immagini vanno compresse e caricate man mano, le mappe non devono bloccare la pagina e l'elenco deve aprirsi subito. È una questione tecnica che si vede in pochi secondi: prova il sito di un'agenzia su telefono e vedi quanto ci mette a mostrare il primo immobile.</p>"]),
            ('aspettative', 'Tempi e aspettative',
             "Cosa è realistico, e cosa no.",
             ["<p>Per ricerche molto specifiche (un tipo di immobile in un quartiere) un sito curato può comparire in alcune settimane o mesi. Per le ricerche generiche della città serve molto di più. " + NOTE_RANKING + " Se un fornitore ti promette la prima pagina in poco tempo, vedi i segnali d'allarme in " + a('/blog/come-scegliere-una-web-agency/', 'come scegliere una web agency') + ".</p>"]),
        ],
        'faq': [
            ("Conviene a Milano avere un sito se uso già i portali?",
             "Sì, ma con uno scopo chiaro: far arrivare i proprietari e mostrare la tua nicchia. Come sito generico, che dice solo \"agenzia a Milano\", si perde tra migliaia di concorrenti."),
            ("Quanto costa un sito web per un'agenzia immobiliare a Milano?", RANGES + " L'integrazione con il gestionale si valuta a parte."),
            ("Come si fa a posizionarsi su Google a Milano?",
             "Scegliendo ricerche specifiche (zona, tipo di immobile), curando la scheda Google, raccogliendo recensioni vere e pubblicando contenuti utili. Per le ricerche generiche serve tempo. " + NOTE_RANKING),
            ("Lavorate con agenzie di Milano?",
             "Lavoriamo a distanza con attività di tutta Italia, anche milanesi. Si parte da una videochiamata e da un preventivo scritto. Vedi la pagina " + a('/milano/', 'siti web a Milano') + "."),
        ],
        'related': [
            ('/blog/sito-web-agenzie-immobiliari/', 'Sito web per agenzie immobiliari', 'La guida generale: pagine, schede e contatti.'),
            ('/blog/preventivo-sito-web-milano/', 'Preventivo sito web: 8 domande', 'Cosa chiedere prima di firmare un preventivo.'),
            ('/milano/', 'Siti web a Milano', 'Come lavoriamo con le attività milanesi.'),
        ],
        'cta_title': 'Troviamo la nicchia della tua agenzia',
        'cta_text': "Raccontaci dove lavori, che immobili tratti e a chi ti rivolgi. Ti rispondiamo con una prima valutazione, senza promesse di posizione.",
    },
    # ------------------------------------------------------------------ Como
    {
        'slug': 'sito-web-agenzie-immobiliari-como',
        'title': 'Sito web per agenzie immobiliari a Como e sul lago',
        'description': "Case sul lago, seconde case e acquirenti stranieri: come deve essere il sito di un'agenzia immobiliare di Como, tra più lingue, foto e contatto a distanza.",
        'section': 'Settori', 'minutes': 8,
        'keywords': 'agenzia immobiliare Como, sito web agenzia immobiliare Como, case sul lago di Como, ville lago di Como in vendita',
        'lead': "Sul Lago di Como chi compra o affitta spesso non è del posto: seconde case, ville, acquirenti stranieri e dalla vicina Svizzera, che decidono a distanza. Il sito di un'agenzia deve funzionare per chi non può venire a visitare. Una guida per le agenzie di Como e provincia.",
        'cta_link': ('/como/', 'Siti web a Como'),
        'takeaways': [
            ("Molti clienti decidono da lontano.", "Foto, video e descrizioni devono sostituire la prima visita."),
            ("Le lingue vanno progettate.", "Una versione vera per ogni lingua, non una traduzione automatica."),
            ("Il contatto deve essere facile da lontano.", "WhatsApp, modulo breve, videochiamata per vedere l'immobile."),
            ("La scheda Google resta il primo punto di contatto.", "Anche per chi cerca in inglese."),
        ],
        'sections': [
            ('clienti', 'Chi compra e chi affitta sul lago',
             "Il cliente tipico del lago non è quello di una città di provincia: cambia come cerca e cosa vuole sapere.",
             ["<p>Accanto ai residenti, una parte del mercato è fatta di seconde case, di ville e di acquirenti che arrivano da altre regioni e da altri Paesi, tra cui la vicina Svizzera. Sono clienti che confrontano da lontano, spesso da telefono, e vogliono capire in poco tempo dove si trova l'immobile, com'è e come ci si arriva.</p>",
              "<p>Sapere chi sono i tuoi clienti dalla tua agenda decide cosa mostrare: se vendi soprattutto a stranieri, il sito parte in inglese o nella lingua principale; se vendi a residenti, la priorità sono le zone e i servizi.</p>"]),
            ('lingue', 'Italiano, inglese e le altre lingue',
             "Un sito in più lingue fatto male danneggia più di uno in una lingua fatto bene.",
             checks([
                 ("Una versione per lingua", "Ogni lingua ha il suo indirizzo e i suoi testi, collegati tra loro."),
                 ("Testi scritti o rivisti da una persona", "Un annuncio tradotto alla lettera fa perdere fiducia. Conta più la chiarezza della quantità."),
                 ("Dati pratici nella lingua giusta", "Superficie, locali, spese, distanza dal lago e dai servizi, come arrivare."),
                 ("Un solo elenco di immobili", "Lo stesso in tutte le lingue, per non avere versioni che si disallineano."),
             ]) + ["<p>Come si collegano le versioni lo puoi vedere in questo sito, che è in italiano e inglese, e nella guida " + a('/blog/sito-web-hotel-ristoranti-lago-di-como/', 'sito web per hotel e ristoranti sul Lago di Como') + ", che tratta lo stesso tema per un altro settore.</p>"]),
            ('presentazione', 'Foto, video e tour per chi non può visitare',
             "Per chi decide da lontano, la scheda è la visita.",
             ["<ul><li><strong>Foto professionali</strong> in luce naturale: la vista, l'accesso al lago, il giardino, l'esterno e l'interno.</li><li><strong>Video</strong> o tour virtuale, se l'agenzia lo produce.</li><li><strong>Dati chiari</strong>: superficie, locali, stato dei lavori, parcheggio, spese, anno.</li><li><strong>Posizione e distanze</strong>: dal centro, dalla stazione, da Milano e dai servizi.</li></ul>",
              "<p>Se l'immobile ha caratteristiche particolari (vincoli, giardino, pontile o accesso privato), la scheda deve dirlo con chiarezza e rimandare ai documenti, senza promesse che non puoi mantenere.</p>"]),
            ('contatto', 'Rispondere a chi è lontano',
             "Un cliente che scrive da un altro Paese non aspetta: contatta tre agenzie e risponde chi arriva prima.",
             ["<p>Servono un modulo breve, un numero WhatsApp visibile, orari chiari (e il fuso orario se lavori con l'estero) e la possibilità di una visita in videochiamata. Conviene anche decidere in anticipo chi risponde in inglese e in quanto tempo.</p>"]),
            ('google', 'Scheda Google e pagine per località',
             "Come per le altre città, la mappa viene prima del sito: la scheda va curata.",
             ["<p>Categoria corretta, foto vere, orari e recensioni di clienti reali, senza incentivi. Per le pagine di località (Como città, i comuni del lago) vale la regola di sempre: una pagina solo dove hai immobili e conoscenza reale, con testi scritti apposta. " + NOTE_RANKING + "</p>"]),
        ],
        'faq': [
            ("Quanto costa un sito web per un'agenzia immobiliare a Como?", RANGES + " Ogni lingua in più aumenta il lavoro, perché testi e schede vanno scritti o rivisti."),
            ("Serve il sito in inglese?",
             "Serve se parte dei tuoi clienti lo è e se puoi rispondere in inglese. Un sito in inglese senza qualcuno che risponde è peggio di nessuno."),
            ("Quali lingue conviene aggiungere?",
             "Quelle dei clienti che hai già e che puoi servire davvero. Si parte da una, ben fatta, e si aggiungono le altre solo se arrivano richieste."),
            ("Lavorate con agenzie di Como?",
             "Lavoriamo a distanza con attività di tutta Italia, anche di Como e dintorni. Si parte da una videochiamata. Vedi la pagina " + a('/como/', 'siti web a Como') + "."),
        ],
        'related': [
            ('/blog/sito-web-agenzie-immobiliari/', 'Sito web per agenzie immobiliari', 'La guida generale: pagine, schede e contatti.'),
            ('/blog/sito-web-hotel-ristoranti-lago-di-como/', 'Sito web per hotel e ristoranti sul lago', 'Più lingue e prenotazioni dirette.'),
            ('/como/', 'Siti web a Como', 'Come lavoriamo con le attività di Como.'),
        ],
        'cta_title': 'Raccontaci i clienti della tua agenzia',
        'cta_text': "Dicci chi compra da te, da dove arriva e in quali lingue rispondi. Ti rispondiamo con una prima valutazione e un preventivo scritto.",
    },
    # ------------------------------------------------------------------ small towns
    {
        'slug': 'sito-web-agenzia-immobiliare-piccoli-comuni',
        'title': "Sito web per l'agenzia immobiliare di un piccolo comune",
        'description': "Un'agenzia immobiliare di paese ha bisogno di un sito? Cosa mettere, quanto spendere e come farsi trovare nei comuni intorno. Guida per Novara e provincia.",
        'section': 'Settori', 'minutes': 7,
        'keywords': 'sito web piccola agenzia immobiliare, agenzia immobiliare comune piccolo, sito web agente immobiliare, agenzia immobiliare Galliate Trecate Borgomanero',
        'lead': "Se la tua agenzia immobiliare è in un comune della provincia (per esempio Galliate, Trecate, Oleggio, Arona, Borgomanero e simili) il tuo vantaggio è conoscere le persone e le strade. Il sito non deve sembrare quello di una grande rete: deve trasformare quel vantaggio in qualcosa che si vede online.",
        'cta_link': ('/novara/', 'Siti web a Novara'),
        'takeaways': [
            ("Il vantaggio è essere del posto.", "Il sito lo dice con nomi, volti e conoscenza della zona."),
            ("Il sito minimo basta.", "Home, immobili, scheda, valutazione, chi siamo, contatti."),
            ("Una pagina per comune solo se vera.", "Evita pagine fotocopia con il nome cambiato."),
            ("La scheda Google rende di più del sito.", "È dove si decide la prima telefonata."),
        ],
        'sections': [
            ('vantaggio', 'Il vantaggio di essere del posto',
             "Nelle ricerche locali piccole la concorrenza è più bassa e il passaparola conta ancora molto.",
             ["<p>Un'agenzia di paese ha un vantaggio che le reti non hanno: sa chi sono i vicini, quali case sono in vendita da anni e come si muove la zona. Il passaparola funziona, ma funziona di più se chi lo riceve trova online le stesse persone che gli hanno raccomandato: foto vere, nomi, recensioni.</p>"]),
            ('minimo', 'Il sito minimo che funziona',
             "Non servono venti pagine. Servono poche pagine che si leggono bene da telefono.",
             checks([
                 ("Home", "Cosa fate, dove, e due pulsanti: vedi gli immobili e valuta la tua casa."),
                 ("Immobili e scheda", "Elenco semplice e una scheda per immobile con foto, dati e telefono."),
                 ("Valuta la tua casa", "Un modulo breve e come si fa la valutazione."),
                 ("Chi siamo", "Le persone, con foto vere, e i dati dell'agenzia."),
                 ("Contatti", "Telefono, WhatsApp, orari e mappa."),
             ])),
            ('comuni', 'I comuni intorno: una pagina solo se è vera',
             "Una pagina per ogni comune della zona sembra una buona idea. Dipende da cosa ci scrivi.",
             ["<p>Se vendi anche nei comuni vicini e li conosci, una pagina per ciascuno con informazioni vere (che immobili ci sono, come sono i collegamenti, cosa c'è nei dintorni) è utile. Se invece è lo stesso testo con il nome cambiato, è una pagina che serve solo a comparire: Google la riconosce, il lettore pure, e il sito perde credibilità. Meglio due pagine ottime che dieci uguali.</p>"]),
            ('google', 'La scheda Google: la parte che rende di più',
             "Per \"agenzia immobiliare\" più il nome del paese, Google mostra prima la mappa.",
             ["<ul><li>Categoria e orari corretti, telefono uguale a quello del sito.</li><li>Foto vere dell'ufficio, della vetrina e della squadra.</li><li>Recensioni dei clienti reali, chieste a tutti, senza regali o sconti: Google non le vuole e possono sparire.</li><li>Risposta a ogni recensione, anche quella brutta, con calma.</li></ul>",
              "<p>Su come impostarla vedi la " + a('/servizi/seo/', 'consulenza SEO') + ". Una scheda ben curata dà più telefonate di un sito bellissimo ma senza segnali.</p>"]),
            ('aggiornare', 'Aggiornare senza dipendere da nessuno',
             "Il sito di un'agenzia piccola muore quando smette di essere aggiornato.",
             ["<p>Un annuncio venduto da mesi che resta online fa perdere credibilità. Il sito deve consentire di aggiungere, modificare e segnare come venduto un immobile in pochi minuti, da soli. Se dipendi da una telefonata per ogni modifica, non lo aggiornerai. Cosa include la manutenzione: " + a('/blog/manutenzione-sito-web/', 'manutenzione sito web') + ".</p>"]),
            ('costi', 'Quanto spendere',
             "Il budget dipende dal perimetro, non dal paese.",
             ["<p>Un sito semplice per un'agenzia piccola sta nella fascia più bassa dei prezzi, e si può far crescere dopo (più zone, versione in inglese, collegamento al gestionale). Per un'idea dei costi usa il " + a('/strumenti/calcolo-costo-sito-web/', 'calcolatore del costo di un sito web') + " e leggi " + a('/blog/quanto-costa-sito-web-italia-2026/', 'quanto costa un sito web in Italia') + ".</p>"]),
        ],
        'faq': [
            ("Un'agenzia immobiliare di paese ha bisogno di un sito?",
             "Se vuoi essere trovata da chi non ti conosce e dimostrare come lavori, sì. Può essere semplice, ma deve avere immobili aggiornati, volti reali e contatti chiari."),
            ("Quanto costa un sito web per una piccola agenzia immobiliare?", RANGES),
            ("Posso aggiornare io gli annunci?",
             "Sì, deve essere così: un pannello semplice con pochi campi, senza chiedere a nessuno. Se usi un gestionale, si valuta l'importazione automatica."),
            ("Lavorate con agenzie dei comuni intorno a Novara?",
             "Sì, lavoriamo con attività di tutta Italia e siamo a Novara: si può anche incontrarsi di persona. Si parte da una videochiamata e da un preventivo scritto."),
        ],
        'related': [
            ('/blog/sito-web-agenzie-immobiliari/', 'Sito web per agenzie immobiliari', 'La guida generale: pagine, schede e contatti.'),
            ('/blog/sito-web-agenzie-immobiliari-novara/', 'Sito web per agenzie immobiliari a Novara', 'Il taglio per le agenzie della città.'),
            ('/blog/quanto-costa-sito-web-italia-2026/', 'Quanto costa un sito web in Italia nel 2026', 'Il metodo per leggere un preventivo.'),
        ],
        'cta_title': 'Un sito semplice per la tua agenzia',
        'cta_text': "Dicci dove lavori e come tratti gli annunci oggi. Ti rispondiamo con una proposta semplice e un preventivo scritto.",
    },
]

bc.ARTICLES = ARTICLES

if __name__ == '__main__':
    bc.main()
