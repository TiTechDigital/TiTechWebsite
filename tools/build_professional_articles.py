"""Builds three guides for professional practices: dentists (general and Novara)
and law/accounting firms.

Same rules as the other article builders: each answers a real question, none
claims a client or project we do not have, and every rule of professional
advertising is stated as "check with your professional body", never as legal
advice. Italian only (see ITALIAN_ONLY in tools/check_site.py).

Run: python tools/build_professional_articles.py
Then: python tools/check_site.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_city_articles as bc
from build_realestate_articles import a, checks, NOTE_RANKING, RANGES

bc.DATE = '2026-11-12'
bc.DATE_IT = '12 novembre 2026'

RULES = ("Le regole sulla pubblicità cambiano per ogni professione e vanno verificate con il proprio Ordine o la propria associazione: "
         "noi scriviamo il sito, ma cosa si può dire lo decide chi risponde del titolo.")

ARTICLES = [
    # ---------------------------------------------------------------- dentists, general
    {
        'slug': 'sito-web-studio-dentistico',
        'title': 'Sito web per studi dentistici: cosa serve e cosa si può dire',
        'description': "Le pagine che servono a uno studio dentistico, come prenotare, cosa dice la pubblicità sanitaria e come gestire recensioni e dati dei pazienti.",
        'section': 'Settori', 'minutes': 9,
        'keywords': 'sito web studio dentistico, sito web dentista, creazione sito web studio odontoiatrico, prenotazione online dentista',
        'lead': "Chi cerca un dentista lo fa da telefono, spesso con un dolore o con timore, e sceglie chi gli ispira fiducia. Il sito di uno studio non deve essere una brochure: deve dire chi siete, cosa fate, come si prenota e cosa succede alla prima visita, nel rispetto delle regole della pubblicità sanitaria.",
        'cta_link': ('/settori/professionisti/', 'Siti per professionisti'),
        'takeaways': [
            ("Due tipi di paziente.", "Chi ha un'urgenza vuole un telefono subito; chi programma confronta e legge con calma."),
            ("Poche pagine, vere.", "Trattamenti che fate davvero, il team con titoli, lo studio con foto vere, prima visita, contatti."),
            ("La pubblicità sanitaria ha dei limiti.", "Niente confronti, superlativi o promesse di risultato: verifica con il tuo Ordine."),
            ("I dati dei pazienti sono dati sensibili.", "Un modulo breve, un'informativa chiara e nessun dettaglio clinico nei messaggi."),
        ],
        'sections': [
            ('pazienti', 'Due pazienti, due modi di cercare',
             "La stessa ricerca \"dentista\" nasconde bisogni molto diversi: il sito deve rispondere a entrambi.",
             ["<p><strong>Chi ha un'urgenza</strong> (dolore, un dente rotto) non legge: cerca un numero da chiamare, l'orario e se c'è posto oggi. Per lui contano il telefono a un tocco, gli orari in evidenza e la scheda Google corretta.</p>",
              "<p><strong>Chi programma</strong> (igiene, ortodonzia, implantologia) confronta più studi: legge i trattamenti, guarda chi siete, cerca di capire come si svolge la prima visita e quanto può costare. Per lui contano contenuti chiari, il team e la fiducia.</p>"]),
            ('pagine', 'Le pagine che servono',
             "Uno studio non ha bisogno di venti sezioni: servono poche pagine con un compito preciso.",
             checks([
                 ("Trattamenti", "Una pagina per ciascun trattamento che fate davvero (igiene, conservativa, ortodonzia, implantologia, pedodonzia): cos'è, come si svolge, per chi, tempi. Solo quelli che offrite."),
                 ("Il team", "Nome, titolo e ambito di ciascun professionista, con foto vera. È la pagina che molti pazienti guardano per fidarsi."),
                 ("Lo studio", "Foto reali di accoglienza e sala operativa, orari, accessibilità, come arrivare e dove parcheggiare."),
                 ("La prima visita", "Cosa succede, quanto dura, cosa portare. Toglie paura e riduce le telefonate di chiarimento."),
                 ("Costi", "Come si arriva a un preventivo e cosa comprende. Dare cifre o fasce è una scelta da valutare con le regole della professione."),
                 ("Contatti e prenotazione", "Telefono, WhatsApp, modulo breve, orari e mappa."),
             ])),
            ('regole', 'Cosa si può dire e cosa no',
             "La pubblicità sanitaria è regolata: un sito vistoso può diventare un problema con l'Ordine.",
             ["<p>In generale la comunicazione di uno studio deve essere informativa e corretta: titoli e servizi veri, niente confronti con altri studi, niente superlativi (\"il migliore\") né promesse di risultato, e attenzione alle offerte che possono trarre in inganno. Le strutture sanitarie hanno inoltre obblighi di indicazione (per esempio del direttore sanitario). Fotografie prima e dopo e testimonianze dei pazienti richiedono particolare attenzione e il consenso scritto della persona.</p>",
              "<p>" + RULES + "</p>"]),
            ('prenotazione', 'Prenotare senza telefonare, senza raccogliere troppo',
             "Un modulo di prenotazione fa arrivare più persone, ma ogni campo in più è un dato che dovrai proteggere.",
             ["<ul><li><strong>Pochi campi</strong>: nome, telefono, motivo in poche parole (visita, igiene, urgenza), fascia oraria preferita.</li><li><strong>Nessun dettaglio clinico</strong> nel modulo o nei messaggi: dati sulla salute sono una categoria particolare di dati personali, con regole più rigide.</li><li><strong>Informativa e consenso</strong> chiari, con un link alla privacy policy.</li><li><strong>WhatsApp e telefono</strong> restano il modo preferito da molti: mettili in evidenza.</li></ul>",
              "<p>Se in futuro vorrai una prenotazione online con agenda, si può collegare al software dello studio: dipende dal gestionale che usi e si valuta a parte.</p>"]),
            ('google', 'Scheda Google e recensioni dei pazienti',
             "Chi cerca \"dentista\" più la città vede per prima la mappa con le schede: è lì che si decide la telefonata.",
             ["<p>Categoria corretta, orari reali, foto vere dello studio e recensioni di pazienti veri, chieste a tutti e senza incentivi. Quando rispondi a una recensione non rivelare mai se la persona è o non è un tuo paziente né dettagli sulle cure: basta un ringraziamento o un invito a chiamare lo studio.</p>",
              "<p>Come si imposta la presenza locale lo trovi nella " + a('/servizi/seo/', 'consulenza SEO') + ". " + NOTE_RANKING + "</p>"]),
        ],
        'faq': [
            ("Un dentista ha bisogno di un sito web?",
             "Se vuole essere trovato da chi non lo conosce e dare fiducia prima della prima visita, sì. Può essere semplice, ma con team, trattamenti, orari e contatti chiari e aggiornati."),
            ("Quanto costa un sito web per uno studio dentistico?", RANGES + " La prenotazione online collegata all'agenda dello studio si valuta a parte."),
            ("Posso pubblicare i prezzi dei trattamenti?",
             "Dipende dalle regole della professione e da come presenti le cifre (informazione corretta, non offerte ingannevoli). Chiedi al tuo Ordine: il sito si adatta a quello che puoi dire."),
            ("Posso mostrare foto prima e dopo?",
             "Solo con il consenso scritto del paziente e nel rispetto delle regole sulla pubblicità sanitaria. Va deciso con attenzione; non lo facciamo senza che tu l'abbia verificato."),
        ],
        'related': [
            ('/blog/sito-web-dentista-novara/', 'Sito web per dentisti a Novara', 'Il taglio per gli studi di Novara e provincia.'),
            ('/blog/sito-web-studio-legale-commercialista/', 'Sito web per studi legali e commercialisti', 'Fiducia, aree di attività e regole.'),
            ('/blog/manutenzione-sito-web/', 'Manutenzione sito web', 'Cosa include e perché non è opzionale.'),
        ],
        'cta_title': 'Parliamo del sito del tuo studio',
        'cta_text': "Raccontaci i trattamenti che fate, come si prenota oggi e cosa non funziona nel sito attuale. Ti rispondiamo con una prima valutazione e un preventivo scritto.",
    },
    # ---------------------------------------------------------------- dentists, Novara
    {
        'slug': 'sito-web-dentista-novara',
        'title': 'Sito web per dentisti a Novara: farsi trovare dai pazienti della zona',
        'description': "Come far trovare lo studio dentistico di Novara: scheda Google, orari, accessibilità, prima visita e prenotazione, nel rispetto della pubblicità sanitaria.",
        'section': 'Settori', 'minutes': 8,
        'keywords': 'dentista Novara, sito web dentista Novara, studio dentistico Novara, dentista urgente Novara',
        'lead': "Lo studio dentistico di Novara parla a pazienti della città e dei comuni intorno, che scelgono vicino a casa o al lavoro e spesso si fidano del consiglio di qualcuno. Il sito deve confermare quel consiglio, rendere facile arrivare e far prenotare senza fatica. Una guida per gli studi di Novara e provincia.",
        'cta_link': ('/novara/', 'Siti web a Novara'),
        'takeaways': [
            ("Si sceglie vicino.", "Dove siete, come si arriva, dove si parcheggia e quanto è comodo l'orario contano come i trattamenti."),
            ("Il passaparola va confermato online.", "Chi riceve un consiglio cerca lo studio e verifica: team, foto, recensioni."),
            ("L'urgenza è una ricerca a sé.", "\"Dentista urgente\" richiede orari chiari, telefono e una scheda Google corretta."),
            ("Pagine per i comuni vicini solo se vere.", "Un testo identico con il nome del paese cambiato non aiuta."),
        ],
        'sections': [
            ('vicinanza', 'Si sceglie vicino a casa o al lavoro',
             "Per le cure di tutti i giorni la comodità è un criterio forte: lo studio vicino, aperto all'ora giusta, con un posto dove lasciare l'auto.",
             ["<p>Chi cerca un dentista a Novara spesso guarda prima di tutto dove si trova lo studio e quando è aperto. Metti in evidenza l'indirizzo e la mappa, le indicazioni per arrivare (parcheggio, mezzi pubblici), l'accessibilità per chi ha difficoltà motorie e gli orari, comprese eventuali aperture in orari comodi per chi lavora. Sono dettagli che sembrano ovvi ma che nel sito di molti studi mancano o sono nascosti.</p>"]),
            ('passaparola', 'Il passaparola va confermato online',
             "In una città di provincia molti pazienti arrivano da un consiglio. Prima di chiamare, quasi tutti controllano.",
             ["<p>Cercano il nome dello studio e guardano tre cose: la scheda Google con le recensioni, il sito con le persone e le foto dello studio, e se le informazioni coincidono. Una scheda con orari sbagliati o un sito fermo a cinque anni fa trasformano un consiglio in un dubbio.</p>",
              "<ul><li>Stesso nome, indirizzo e telefono ovunque.</li><li>Foto vere dello studio e del team, non immagini generiche.</li><li>Recensioni di pazienti reali, chieste a tutti e senza regali o sconti.</li></ul>"]),
            ('urgenze', 'Dentista urgente: la ricerca che non aspetta',
             "Chi ha un dolore alle undici di sera non legge una pagina: cerca un numero e un orario.",
             ["<p>Se lo studio gestisce le urgenze, dillo in modo preciso: quando, come, a quale numero. Se non le gestisce, è meglio non promettere. Una pagina dedicata con orari, telefono e cosa fare nel frattempo serve più di un banner generico. Il numero deve essere cliccabile da telefono e uguale a quello della scheda Google.</p>"]),
            ('prima-visita', 'La prima visita e la prenotazione',
             "Molte persone rimandano la visita per paura o per non sapere cosa aspettarsi.",
             ["<p>Una pagina che spiega la prima visita (durata, cosa si fa, cosa portare, come si arriva al preventivo) toglie paura e riduce le telefonate. Per prenotare servono un modulo breve, WhatsApp e telefono; nel modulo niente dettagli clinici, con informativa e consenso chiari, perché i dati sulla salute hanno regole più rigide. Il quadro generale è nella " + a('/blog/sito-web-studio-dentistico/', 'guida per gli studi dentistici') + ".</p>",
              "<p>" + RULES + "</p>"]),
            ('zone', 'Comuni vicini: una pagina solo se è vera',
             "Una pagina per ogni comune sembra una buona idea. Dipende da cosa ci scrivi.",
             ["<p>Se molti tuoi pazienti vengono da un comune vicino, una pagina che spiega come arrivare da lì può servire. Se invece è lo stesso testo con il nome cambiato, è un riempitivo che i motori riconoscono. Come lavoriamo con le attività della zona: " + a('/novara/', 'siti web a Novara') + ". " + NOTE_RANKING + "</p>"]),
        ],
        'faq': [
            ("Quanto costa un sito web per uno studio dentistico a Novara?", RANGES),
            ("Serve la scheda Google anche con un sito?",
             "Sì: per \"dentista Novara\" Google mostra per prima la mappa con le schede, e lì i pazienti decidono. Il sito e la scheda devono dire le stesse cose."),
            ("Posso rispondere alle recensioni?",
             "Sì, ma senza rivelare se la persona è un paziente né dettagli sulle cure. Un ringraziamento o un invito a chiamare lo studio bastano."),
            ("Lavorate con studi di Novara?",
             "Lavoriamo a distanza con attività di tutta Italia e abbiamo sede a Novara, quindi si può anche incontrarsi di persona. Si parte da una videochiamata e da un preventivo scritto."),
        ],
        'related': [
            ('/blog/sito-web-studio-dentistico/', 'Sito web per studi dentistici', 'La guida generale: pagine, regole e prenotazione.'),
            ('/novara/', 'Siti web a Novara', 'Come lavoriamo con le attività di Novara e provincia.'),
            ('/settori/professionisti/', 'Siti per professionisti', 'Studi e liberi professionisti.'),
        ],
        'cta_title': 'Partiamo dal tuo studio',
        'cta_text': "Dicci dove si trova lo studio, quali trattamenti fate e come si prenota oggi. Ti rispondiamo per iscritto con una prima valutazione.",
    },
    # ---------------------------------------------------------------- law and accounting
    {
        'slug': 'sito-web-studio-legale-commercialista',
        'title': 'Sito web per studi legali e commercialisti: fiducia prima di tutto',
        'description': "Aree di attività, profili dei professionisti, primo contatto e regole di comunicazione: cosa deve avere il sito di uno studio legale o di un commercialista.",
        'section': 'Settori', 'minutes': 8,
        'keywords': 'sito web studio legale, sito web avvocato, sito web commercialista, sito web studio professionale',
        'lead': "Chi cerca un avvocato o un commercialista di solito ha un problema e poco tempo: vuole capire in fretta se sei la persona giusta per quel problema e come fare il primo passo. Il sito di uno studio professionale vende fiducia e chiarezza, non slogan. Una guida per studi legali e commercialisti.",
        'cta_link': ('/settori/professionisti/', 'Siti per professionisti'),
        'takeaways': [
            ("Si cerca un problema, non uno studio.", "Le pagine devono partire da cosa risolvi, non da come ti chiami."),
            ("Il professionista è il prodotto.", "Profilo, titoli, ambiti e foto vera valgono più della grafica."),
            ("Il primo contatto deve essere facile e riservato.", "Telefono, email e un modulo breve, senza chiedere i dettagli del caso."),
            ("Niente promesse di risultato.", "E niente confronti: le regole di comunicazione vanno verificate con il proprio Ordine."),
        ],
        'sections': [
            ('problemi', 'Parti dal problema del cliente',
             "Chi cerca un avvocato scrive \"separazione\" o \"recupero crediti\", non \"studio legale\".",
             ["<p>Il sito funziona meglio se organizzato per aree di attività e per le domande che i clienti fanno davvero: una pagina per ogni ambito in cui lavori, con cosa fai, in quali casi, come si svolge il primo incontro. Lo stesso vale per un commercialista: apertura attività, dichiarazioni, consulenza per le imprese, ciascuna con parole semplici.</p>",
              "<p>Mettere troppi ambiti fa sembrare lo studio un generalista; meglio pochi e veri.</p>"]),
            ('persone', 'Le persone prima dello studio',
             "Per un servizio fondato sulla fiducia, chi sei conta più di come è fatto il sito.",
             checks([
                 ("Profilo del professionista", "Nome, titoli, ordine di iscrizione, ambiti e un breve profilo in prima persona o neutro, senza elenchi di sigle."),
                 ("Foto vera", "Una foto curata, non d'archivio: mostra che dietro il sito c'è una persona."),
                 ("Come si lavora", "Primo incontro, preventivo, tempi di risposta, come si seguono le pratiche."),
                 ("Contatti completi", "Sede, telefono, email, orari, indicazioni per arrivare."),
             ])),
            ('regole', 'Cosa si può dire e cosa no',
             "Le professioni regolamentate hanno regole di comunicazione. Un sito troppo commerciale può creare problemi.",
             ["<p>In generale la comunicazione di uno studio professionale deve essere informativa, veritiera e decorosa: niente promesse di risultato, niente confronti con altri professionisti, attenzione a dichiarazioni sulle proprie qualità e alle offerte promozionali. Se pubblichi casi o testimonianze, serve il consenso del cliente e il rispetto del segreto professionale.</p>",
              "<p>" + RULES + "</p>"]),
            ('contatto', 'Il primo contatto, senza raccogliere troppo',
             "Chi scrive a uno studio spesso racconta più di quanto serva. Il modulo non deve invitarlo a farlo.",
             ["<p>Un modulo breve (nome, telefono o email, ambito, poche righe) è sufficiente. Specifica che per ragioni di riservatezza è meglio non inviare documenti né dettagli del caso con il primo messaggio: se ne parla nel primo incontro. Aggiungi un'informativa chiara e il consenso al trattamento dei dati, e prevedi chi risponde e in quanto tempo.</p>"]),
            ('contenuti', 'Contenuti utili e scheda Google',
             "Un approfondimento utile fa fiducia più di dieci slogan.",
             ["<p>Un articolo che spiega con parole semplici una procedura, una scadenza o un diritto mostra come lavori e porta persone che cercano proprio quella risposta. Va scritto da chi la sa e tenuto aggiornato: un contenuto fermo a vecchie norme fa danno. Per la ricerca locale, cura la scheda Google (categoria, orari, recensioni vere) e fai coincidere i dati con il sito. Vedi la " + a('/servizi/seo/', 'consulenza SEO') + ". " + NOTE_RANKING + "</p>"]),
        ],
        'faq': [
            ("Un avvocato o un commercialista ha bisogno di un sito web?",
             "Se vuole essere trovato da chi non lo conosce e dare fiducia prima del primo incontro, sì. Può essere semplice: ambiti, profilo, contatti e qualche approfondimento utile."),
            ("Quanto costa un sito web per uno studio professionale?", RANGES),
            ("Posso pubblicare recensioni o casi di clienti?",
             "Con attenzione: serve il consenso del cliente, il rispetto del segreto professionale e delle regole della professione. Le recensioni vere sulla scheda Google sono la strada più semplice."),
            ("Lavorate con studi professionali?",
             "Lavoriamo a distanza con attività di tutta Italia e abbiamo sede a Novara. Si parte da una videochiamata e da un preventivo scritto. Vedi la pagina " + a('/settori/professionisti/', 'siti per professionisti') + "."),
        ],
        'related': [
            ('/blog/sito-web-studio-dentistico/', 'Sito web per studi dentistici', 'Pagine, regole e prenotazione per gli studi sanitari.'),
            ('/settori/professionisti/', 'Siti per professionisti', 'Cosa include un sito per uno studio.'),
            ('/blog/quanto-costa-sito-web-italia-2026/', 'Quanto costa un sito web in Italia nel 2026', 'Il metodo per leggere un preventivo.'),
        ],
        'cta_title': 'Parliamo del sito del tuo studio',
        'cta_text': "Raccontaci gli ambiti in cui lavori e come ti trovano i clienti oggi. Ti rispondiamo con una prima valutazione e un preventivo scritto.",
    },
]

bc.ARTICLES = ARTICLES

if __name__ == '__main__':
    bc.main()
