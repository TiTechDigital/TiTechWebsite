"""Builds four Novara-specific sector guides.

Unlike the sector guides, each of these takes a different angle that only makes
sense for that trade in that town (who calls, when, through which channel), so
they are not the same page with another name. No client or project is claimed.
Italian only (see ITALIAN_ONLY in tools/check_site.py).

Run: python tools/build_novara_sector_articles.py
Then: python tools/check_site.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_city_articles as bc
from build_realestate_articles import a, checks, NOTE_RANKING, RANGES
from build_sector_articles import art, SMALL, faq_work

bc.DATE = '2026-11-12'
bc.DATE_IT = '12 novembre 2026'

NOV = ('/novara/', 'Siti web a Novara')

ARTICLES = [
    art('sito-web-idraulico-elettricista-novara',
        'Sito web per idraulici ed elettricisti a Novara: come essere chiamati per primi',
        "Come far trovare un idraulico o un elettricista di Novara: zone servite, condomìni e amministratori, manutenzioni programmate e scheda Google.",
        8, 'idraulico Novara, elettricista Novara, sito web idraulico Novara, sito web elettricista Novara, impresa edile Novara',
        'sito web idraulico novara',
        "A Novara chi chiama un idraulico o un elettricista di solito sceglie tra i primi due o tre nomi che trova sulla mappa, e spesso vive in un appartamento o in un condominio. Il sito non serve a convincere con lunghi testi: serve a farsi trovare, a dire dove arrivi e a far chiamare subito.",
        [("Vince chi compare sulla mappa.", "\"Idraulico Novara\" mostra prima le schede Google: nome, orari, telefono e recensioni decidono la chiamata."),
         ("Condomìni e amministratori sono un cliente a parte.", "Una pagina dedicata a chi gestisce più edifici porta lavori ricorrenti."),
         ("La manutenzione programmata è lavoro ripetibile.", "Controlli periodici degli impianti evitano le emergenze e fanno tornare i clienti."),
         ("La zona va detta con onestà.", "Novara città, frazioni e comuni vicini: dove arrivi davvero e in quanto tempo.")],
        [('mappa', 'La mappa viene prima del sito',
          "La maggior parte delle chiamate arriva da qui, specialmente da telefono e specialmente quando c'è fretta.",
          ["<p>Per un idraulico o un elettricista di Novara la prima cosa da curare è la scheda Google: categoria giusta, orari veri (compresa la reperibilità, se la offri), telefono uguale a quello del sito, foto di lavori e furgone, recensioni di clienti reali. Il sito conferma ciò che la scheda promette e porta chi vuole saperne di più. " + SMALL + "</p>"]),
         ('condomini', 'Condomìni e amministratori',
          "Un'impresa che lavora con gli amministratori ha lavori ricorrenti e meno concorrenza di prezzo sul singolo intervento.",
          ["<p>Una pagina per gli amministratori di condominio, scritta per loro, dice che interventi fai (guasti, manutenzioni, messa a norma degli impianti comuni), come gestisci le chiamate urgenti, come rilasci preventivi e documenti, e come lo contattano. Gli amministratori cercano un fornitore affidabile e rapido: la serietà si vede nella chiarezza.</p>"]),
         ('manutenzione', 'Manutenzioni programmate e controlli periodici',
          "Molti clienti chiamano solo quando c'è un guasto. Il sito può spiegare perché conviene prevenire.",
          ["<p>Una pagina sulla manutenzione periodica (controlli degli impianti, verifiche prima della stagione fredda, sostituzione di parti usurate) con cosa si controlla e ogni quanto, senza allarmismo, serve a far tornare il cliente prima dell'emergenza. Se offri contratti di manutenzione, dì cosa comprendono e come si disdicono. Ogni obbligo di legge sugli impianti va verificato per il tipo di impianto: non fare affermazioni generiche.</p>"]),
         ('zone', 'Novara città, frazioni e comuni vicini',
          "Dire dove lavori è la parte di sito che più riduce le chiamate inutili.",
          ["<p>Indica la città, le frazioni e i comuni che copri davvero, con tempi di intervento realistici per l'urgenza. Se un comune è fuori dal tuo raggio, meglio dirlo che perdere tempo al telefono. Una pagina per comune ha senso solo se hai lavori e referenze lì; per il resto, una frase chiara basta. Per capire come impostiamo la presenza locale vedi " + a('/novara/', 'siti web a Novara') + " e la guida generale " + a('/blog/sito-web-idraulico-elettricista-impresa-edile/', 'per idraulici, elettricisti e imprese edili') + ".</p>"])],
        [('Quanto costa un sito per un idraulico o un elettricista a Novara?', RANGES),
         ('Serve la scheda Google anche con il sito?', "Sì: per \"idraulico Novara\" è la scheda a portare la prima chiamata. Sito e scheda devono avere lo stesso nome, indirizzo, telefono e orari."),
         ('Conviene una pagina per gli amministratori di condominio?', "Se lavori o vuoi lavorare con i condomìni, sì: è un cliente con esigenze diverse da quelle del privato e vale la pena parlargli direttamente."),
         faq_work('idraulici ed elettricisti di Novara')],
        [('/blog/sito-web-idraulico-elettricista-impresa-edile/', 'Sito web per idraulici, elettricisti e imprese edili', 'La guida generale per le imprese di impianti.'),
         ('/settori/artigianato/', 'Siti per artigiani', 'Un sito semplice per chi lavora con le mani.'),
         ('/novara/', 'Siti web a Novara', 'Come lavoriamo con le attività di Novara.')],
        'Partiamo da dove lavori',
        "Dicci quali interventi fai, in che zone e come ti chiamano oggi. Ti rispondiamo con una prima valutazione e un preventivo scritto.",
        cta_link=NOV),

    art('sito-web-parrucchiere-estetista-novara',
        'Sito web per parrucchieri ed estetiste a Novara: dal passaparola alla prenotazione',
        "Come far trovare un salone o un centro estetico di Novara: orari per chi lavora, prenotazione WhatsApp, cerimonie e servizi stagionali, scheda Google.",
        8, 'parrucchiere Novara, estetista Novara, centro estetico Novara, sito web parrucchiere Novara, prenotazione online parrucchiere Novara',
        'sito web parrucchiere novara',
        "A Novara molti saloni e centri estetici vivono di clienti fedeli e di passaparola. Il sito serve a far trovare il salone a chi non lo conosce e a rendere facile prenotare a chi lo conosce già: soprattutto se lavora in orari difficili e prenota dal telefono la sera.",
        [("Si prenota da telefono, spesso la sera.", "Un pulsante WhatsApp con messaggio già pronto toglie attrito."),
         ("Gli orari contano quanto i servizi.", "Chi lavora cerca aperture comode: sabato, pausa pranzo, sera."),
         ("Cerimonie e stagioni sono picchi.", "Sposa, comunioni, feste e preparazione all'estate vanno gestiti con anticipo."),
         ("Instagram porta, il sito conferma.", "Listino e prenotazione stanno nel sito, le foto anche sui social.")],
        [('orari', 'Orari e comodità: la prima cosa che si controlla',
          "Chi lavora fuori città o fa i turni sceglie il salone che riesce a raggiungere.",
          ["<p>Mettete orari reali e visibili, indicazioni per arrivare e dove parcheggiare, e dite se offrite aperture in orari comodi (sera, sabato, pausa pranzo). Sono dettagli che sembrano ovvi, ma nel sito di molti saloni mancano o sono nascosti in una pagina di contatti. Gli stessi orari devono comparire identici sulla scheda Google, che è dove la maggior parte delle persone li legge.</p>"]),
         ('whatsapp', 'Prenotare con WhatsApp',
          "Per un salone di dimensioni medio-piccole è il canale più usato dalle clienti.",
          ["<p>Un pulsante \"Prenota su WhatsApp\" con il messaggio già compilato (servizio, giorno preferito) riduce i passaggi. Dite chi risponde, in quali orari e in quanto tempo: una cliente che non riceve risposta in giornata prenota altrove. Se il volume cresce, si può passare a un'agenda online collegata al software del salone; si valuta a parte.</p>"]),
         ('cerimonie', 'Cerimonie, sposa e servizi stagionali',
          "Alcuni servizi si prenotano con settimane di anticipo e valgono più di una messa in piega.",
          ["<p>Una pagina per la sposa e per le cerimonie (come si svolge la prova, quanto tempo serve, quanto prima si prenota, che servizi comprende) porta richieste di valore. Lo stesso vale per i trattamenti stagionali (preparazione all'estate, cura dopo le vacanze): una pagina scritta per tempo, con come prenotare, distribuisce meglio gli appuntamenti. Mostra solo foto di lavori tuoi e, quando le clienti sono riconoscibili, con il loro consenso.</p>"]),
         ('instagram', 'Instagram e scheda Google insieme',
          "Le tre cose non si sostituiscono: si completano.",
          ["<p>Instagram mostra lo stile; la scheda Google fa trovare il salone da chi cerca \"parrucchiere Novara\"; il sito dà listino, orari e prenotazione in un posto stabile. Tieni coerenti nome, indirizzo e telefono. " + SMALL + " Per il quadro generale vedi la guida per " + a('/blog/sito-web-estetista-parrucchiere-centro-benessere/', 'centri estetici e saloni') + " e la pagina " + a('/novara/', 'siti web a Novara') + ".</p>"])],
        [('Quanto costa un sito web per un salone di Novara?', RANGES + " Un'agenda online collegata al software di gestione si valuta a parte."),
         ('Conviene mettere il listino con i prezzi?', "In genere sì: chi non vede i prezzi tende a non chiamare. Basta un \"da\" accanto a ogni servizio, con la spiegazione di cosa comprende."),
         ('Posso usare le foto dei lavori fatti alle clienti?', "Con il loro consenso quando sono riconoscibili. Per le altre foto, meglio quelle tue che immagini d'archivio."),
         faq_work('saloni e centri estetici di Novara')],
        [('/blog/sito-web-estetista-parrucchiere-centro-benessere/', 'Sito web per estetiste, parrucchieri e centri benessere', 'La guida generale.'),
         ('/blog/sito-web-palestra-novara/', 'Sito web per palestre a Novara', 'Iscrizioni e orari per chi lavora.'),
         ('/novara/', 'Siti web a Novara', 'Come lavoriamo con le attività di Novara.')],
        'Partiamo dal tuo salone',
        "Dicci che servizi fai, quando sei aperta e come ti prenotano oggi. Ti rispondiamo con una prima valutazione.",
        cta_link=NOV),

    art('sito-web-fisioterapista-novara',
        'Sito web per fisioterapisti a Novara: farsi trovare da chi ha un dolore',
        "Come far trovare lo studio di fisioterapia di Novara: sportivi, postura da ufficio, riabilitazione, rapporto con i medici e primo contatto riservato.",
        8, 'fisioterapista Novara, sito web fisioterapista Novara, studio di fisioterapia Novara, osteopata Novara, riabilitazione Novara',
        'sito web fisioterapista novara',
        "Chi cerca un fisioterapista a Novara spesso ha un dolore che dura da giorni o un problema dopo un infortunio, e vuole sapere in fretta se lo studio fa al caso suo, quando può andare e quanto costa la prima seduta. Il sito deve dare queste risposte e, per un professionista sanitario, nel rispetto delle regole di comunicazione.",
        [("Si cerca per problema.", "Schiena, collo, spalla, ginocchio, dopo un intervento: le pagine partono da lì."),
         ("Tre pubblici ricorrenti.", "Sportivi, chi lavora seduto per molte ore, persone in riabilitazione."),
         ("Anche i medici sono un pubblico.", "Medici e specialisti che indirizzano i pazienti vogliono capire chi sei e come lavori."),
         ("Il primo contatto è riservato.", "Un modulo breve, senza dettagli clinici.")],
        [('problemi', 'Parti dal problema, non dal titolo',
          "Una persona con la schiena bloccata non cerca \"studio di fisioterapia\": cerca di capire se puoi aiutarla.",
          ["<p>Una pagina per ciascun problema che tratti davvero (dolore lombare o cervicale, spalla, ginocchio, riabilitazione dopo un intervento), scritta in modo semplice: cosa si valuta alla prima seduta, come si lavora, quante sedute servono in genere, senza promettere guarigioni. Le regole di comunicazione sanitaria vanno verificate con il tuo Ordine: noi scriviamo il sito, ma cosa si può dire lo decidi tu.</p>"]),
         ('pubblici', 'Sportivi, chi lavora al computer, chi si riabilita',
          "Tre persone diverse con bisogni diversi: il sito può parlare a ciascuna con una pagina.",
          checks([("Sportivi", "Chi corre, gioca o frequenta la palestra: ritorno allo sport dopo un infortunio, prevenzione, valutazione del movimento."),
                  ("Chi lavora seduto", "Postura, collo e schiena: percorsi brevi e consigli pratici, senza esagerare."),
                  ("Riabilitazione", "Dopo un intervento o un trauma: come si lavora con il medico, quante sedute, come si prosegue a casa.")])),
         ('medici', 'Parlare anche a chi indirizza i pazienti',
          "Una parte dei pazienti arriva su consiglio di un medico di base, di uno specialista o di un altro professionista.",
          ["<p>Una pagina per i colleghi, sobria, che spiega chi sei, quali ambiti segui, come si prenota una valutazione e come comunichi gli esiti, fa capire che sei una persona seria. Non è pubblicità: è un riferimento chiaro. Evita ogni forma di incentivo o accordo non dichiarato e verifica le regole del tuo Ordine su collaborazioni e comunicazione.</p>"]),
         ('contatto', 'Primo contatto e scheda Google',
          "Chi ha un dolore vuole una risposta in giornata.",
          ["<p>Telefono a un tocco, WhatsApp, orari reali e un modulo con nome, telefono e fascia oraria. Chiedi di non inviare dettagli clinici nel primo messaggio, con informativa privacy e consenso chiari: i dati sulla salute hanno regole più rigide. " + SMALL + " Il quadro generale è nella guida " + a('/blog/sito-web-fisioterapista-osteopata-psicologo/', 'per fisioterapisti, osteopati e psicologi') + ".</p>"])],
        [('Quanto costa un sito web per un fisioterapista a Novara?', RANGES),
         ('Posso mostrare le recensioni dei pazienti?', "Le recensioni vere sulla scheda Google sono la strada più semplice. Per testimonianze sul sito servono il consenso scritto e il rispetto delle regole della professione."),
         ('Posso scrivere che il trattamento guarisce?', "No: le promesse di risultato non sono ammesse nella comunicazione sanitaria. Si descrivono il metodo e il percorso, senza garantire esiti."),
         faq_work('fisioterapisti di Novara')],
        [('/blog/sito-web-fisioterapista-osteopata-psicologo/', 'Sito web per fisioterapisti, osteopati e psicologi', 'La guida generale.'),
         ('/blog/sito-web-dentista-novara/', 'Sito web per dentisti a Novara', 'Un caso simile per gli studi sanitari.'),
         ('/novara/', 'Siti web a Novara', 'Come lavoriamo con le attività di Novara.')],
        'Partiamo dal tuo studio',
        "Dicci per quali problemi lavori e come ti trovano i pazienti oggi. Ti rispondiamo con una prima valutazione.",
        cta_link=NOV),

    art('sito-web-palestra-novara',
        'Sito web per palestre a Novara: orari, iscrizioni e prova gratuita',
        "Come far trovare una palestra di Novara: orari per chi lavora, corsi per fasce d'età, picchi di iscrizioni, prova gratuita e scheda Google.",
        8, 'palestra Novara, sito web palestra Novara, centro fitness Novara, iscrizione palestra Novara',
        'sito web palestra novara',
        "Chi cerca una palestra a Novara controlla prima gli orari, la distanza da casa o dal lavoro e il prezzo, poi cerca di capire com'è l'ambiente. Il sito deve rispondere subito alle prime tre cose e invogliare a provare: una visita, una lezione di prova, una telefonata.",
        [("Gli orari decidono.", "Chi lavora vuole sapere se riesce ad andarci: mattina presto, pausa pranzo, sera."),
         ("Corsi diversi per età diverse.", "Famiglie, adulti, over: ciascuno vuole vedersi nella proposta."),
         ("Le iscrizioni hanno i loro picchi.", "Settembre e gennaio sono i momenti dell'anno in cui più persone decidono: il sito va pronto prima."),
         ("La prova toglie la paura.", "Un primo passo semplice vale più di un listino lungo.")],
        [('orari', 'Orari e distanza: i due filtri veri',
          "Il primo criterio non è l'attrezzatura: è se riesci ad andarci.",
          ["<p>Mettete in evidenza indirizzo, mappa, parcheggio, orari di apertura e il calendario dei corsi, e tenete tutto aggiornato. Un calendario fermo all'anno scorso è peggio di nessuno. Se avete orari adatti a chi lavora o a chi fa i turni, scrivetelo nella prima schermata, non in fondo.</p>"]),
         ('fasce', "Corsi per fasce d'età e obiettivi",
          "Una palestra ha clienti molto diversi: il sito può parlare a ciascuno.",
          checks([("Adulti che iniziano", "Cosa succede alla prima volta, come si sceglie il percorso, chi li segue."),
                  ("Chi ha poco tempo", "Corsi brevi o a orari compressi, abbonamenti flessibili."),
                  ("Famiglie e ragazzi", "Se avete corsi per loro, con orari e requisiti scritti."),
                  ("Over e percorsi dolci", "Attività adatte, con istruttori formati: senza promettere effetti medici.")])),
         ('picchi', 'I picchi di iscrizione',
          "Le iscrizioni si concentrano in alcuni momenti dell'anno, tipicamente a settembre e dopo le feste.",
          ["<p>Preparare prima una pagina con le formule, le condizioni e il modo di iscriversi permette di essere pronti quando le persone cercano. Se offrite promozioni, scrivete per quanto valgono e cosa comprendono, senza condizioni nascoste: le formule poco chiare producono recensioni negative.</p>"]),
         ('prova', 'Prova gratuita e scheda Google',
          "Il pulsante \"Vieni a provare\" fa più di un testo.",
          ["<p>Se offrite una lezione di prova o una visita, rendetela evidente e chiara (cosa si porta, quanto dura, come si prenota). " + SMALL + " Il quadro generale è nella guida " + a('/blog/sito-web-palestra/', 'per palestre e centri fitness') + " e nella pagina " + a('/novara/', 'siti web a Novara') + ".</p>"])],
        [('Quanto costa un sito web per una palestra a Novara?', RANGES + " L'iscrizione online con pagamenti si valuta a parte."),
         ('Conviene mettere i prezzi?', "In genere sì: chi non trova le formule tende a non chiamare. Scrivi condizioni, durata e disdetta per intero."),
         ('Serve un sito se ho già Instagram?', "Sì, per orari, corsi, prezzi e iscrizione in un posto stabile e per essere trovati su Google. Instagram resta la vetrina."),
         faq_work('palestre di Novara')],
        [('/blog/sito-web-palestra/', 'Sito web per palestre e centri fitness', 'La guida generale.'),
         ('/blog/sito-web-parrucchiere-estetista-novara/', 'Sito web per parrucchieri ed estetiste a Novara', 'Prenotazione e orari.'),
         ('/novara/', 'Siti web a Novara', 'Come lavoriamo con le attività di Novara.')],
        'Partiamo dalla tua palestra',
        "Dicci che corsi hai, quando sei aperto e come si iscrivono le persone oggi. Ti rispondiamo con una prima valutazione.",
        cta_link=NOV),
]

bc.ARTICLES = ARTICLES

if __name__ == '__main__':
    bc.main()
