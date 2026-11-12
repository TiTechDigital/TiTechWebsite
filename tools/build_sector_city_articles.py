"""Builds sector-by-city guides: nine trades and professions in Vercelli, Como,
Milano (and Novara for the five sectors that had no Novara guide yet).

Each page is written for that combination: its own angle, its own situations,
its own checklist and its own questions. Local facts are kept general and
verifiable (lake, rice fields, border, size of the market); anything the owner
knows better than we do is phrased as an example to check. No client or
project is claimed. Italian only (see ITALIAN_ONLY in tools/check_site.py).

Run: python tools/build_sector_city_articles.py
Then: python tools/check_site.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_city_articles as bc
from build_realestate_articles import a, checks, NOTE_RANKING, RANGES
from build_sector_articles import art, SMALL, RULES, faq_work

bc.DATE = '2026-11-12'
bc.DATE_IT = '12 novembre 2026'

CITIES = ['vercelli', 'como', 'milano', 'novara']
CITY = {'vercelli': 'Vercelli', 'como': 'Como', 'milano': 'Milano', 'novara': 'Novara'}

SECTOR = {
    'beauty': dict(label='parrucchieri ed estetiste', slug='parrucchiere-estetista', kw='parrucchiere', reg=False,
                   guide='sito-web-estetista-parrucchiere-centro-benessere', gtitle='Sito web per estetiste, parrucchieri e centri benessere'),
    'trades': dict(label='idraulici ed elettricisti', slug='idraulico-elettricista', kw='idraulico', reg=False,
                   guide='sito-web-idraulico-elettricista-impresa-edile', gtitle='Sito web per idraulici, elettricisti e imprese edili'),
    'physio': dict(label='fisioterapisti', slug='fisioterapista', kw='fisioterapista', reg=True,
                   guide='sito-web-fisioterapista-osteopata-psicologo', gtitle='Sito web per fisioterapisti, osteopati e psicologi'),
    'vet': dict(label='veterinari', slug='veterinario', kw='veterinario', reg=True,
                guide='sito-web-veterinario', gtitle='Sito web per veterinari e ambulatori veterinari'),
    'auto': dict(label='autofficine e carrozzerie', slug='autofficina-carrozzeria', kw='autofficina', reg=False,
                 guide='sito-web-autofficina-carrozzeria-gommista', gtitle='Sito web per autofficine, carrozzerie e gommisti'),
    'tech': dict(label='architetti e studi tecnici', slug='architetto-geometra', kw='architetto', reg=True,
                 guide='sito-web-notaio-geometra-architetto-ingegnere', gtitle='Sito web per notai, geometri, architetti e ingegneri'),
    'gym': dict(label='palestre', slug='palestra', kw='palestra', reg=False,
                guide='sito-web-palestra', gtitle='Sito web per palestre e centri fitness'),
    'creative': dict(label='fotografi e wedding planner', slug='fotografo-wedding-planner', kw='fotografo', reg=False,
                     guide='sito-web-agenzia-viaggi-fotografo-wedding-planner', gtitle='Sito web per agenzie di viaggio, fotografi e wedding planner'),
    'artisan': dict(label='aziende artigiane', slug='azienda-artigiana', kw='azienda artigiana', reg=False,
                    guide='sito-web-aziende-artigiane-manifatturiere', gtitle='Sito web per aziende artigiane e piccole manifatture'),
}

# Existing Novara guides for these four sectors: not rebuilt here.
SKIP = {('trades', 'novara'), ('beauty', 'novara'), ('physio', 'novara'), ('gym', 'novara')}

# (sector, city) -> angle, lead, A, B, checks, C, faq, takeaways
D = {}


def put(sector, city, angle, lead, A, B, checks_, C, faq, tk):
    D[(sector, city)] = dict(angle=angle, lead=lead, A=A, B=B, checks=checks_, C=C, faq=faq, tk=tk)


# ------------------------------------------------------------------ beauty
put('beauty', 'vercelli', "clienti fedeli e studenti",
    "A Vercelli un salone vive soprattutto di clienti che tornano, ma in una città universitaria c'è anche chi arriva per un periodo e cerca un posto dove fidarsi in fretta. Il sito serve a farsi scegliere da chi non conosce nessuno.",
    "Chi vive in città da anni sceglie per consiglio. Chi è arrivato da poco, per studio o per lavoro, cerca su Google e sulla mappa, guarda le foto e decide in pochi minuti. Sono due modi di scegliere diversi e il sito deve servirli entrambi.",
    "Per i clienti nuovi servono listino chiaro, orari, come arrivare a piedi o in bici dal centro e un modo semplice di prenotare. Per i fedeli serve poter spostare un appuntamento con un messaggio. Le due cose si risolvono con lo stesso pulsante WhatsApp.",
    [("Listino con prezzi", "Chi si è appena trasferito non ha termini di paragone: il prezzo scritto toglie imbarazzo."),
     ("Orari compatibili con lezioni e lavoro", "Aperture a ora di pranzo o a fine giornata, se le fate."),
     ("Come arrivare", "Indirizzo, mappa e parcheggio o fermate vicine."),
     ("Chi vi lavora", "Nomi e foto vere: in un posto dove ci si conosce, si sceglie la persona.")],
    "Una pagina per le cerimonie (sposa, feste, eventi) con quanto prima prenotare e come funziona la prova è il servizio a più alto valore. Non usare foto d'archivio.",
    [("Serve il sito se i clienti vengono dal passaparola?", "Sì: chi riceve un consiglio cerca il nome online. Un sito e una scheda curati confermano il consiglio."),
     ("Come faccio a farmi trovare da chi si è appena trasferito?", "Con una scheda Google completa, foto vere e orari corretti: è lì che questa persona cerca.")],
    [("Si sceglie su consiglio e su Google.", "Il sito deve servire entrambi."), ("WhatsApp per spostare e prenotare.", "Un solo canale per clienti nuovi e fedeli."), ("Cerimonie, il servizio più prezioso.", "Una pagina con tempi e prove.")])
put('beauty', 'como', "turisti, hotel e stagioni",
    "A Como un salone o un centro estetico lavora con residenti e con chi è di passaggio: turisti, ospiti di hotel, spose che arrivano da fuori. Il sito deve funzionare in due lingue e dire con chiarezza quando e come si prenota.",
    "I residenti prenotano con i loro tempi; i visitatori prenotano in poche ore, spesso da telefono, per un trattamento prima di un evento o di una cena. Se parte della clientela è straniera, un sito solo in italiano ne perde una parte.",
    "Una versione in inglese, vera, con i servizi principali, i prezzi, gli orari e un contatto WhatsApp è più utile di molte pagine. Gli ospiti di hotel e le spose cercano anche un servizio a domicilio o in struttura: se lo fate, scrivete dove e a che condizioni.",
    [("Versione inglese", "Servizi, prezzi e prenotazione, scritti da una persona e non tradotti alla lettera."),
     ("Orari stagionali", "Aperture estive o festive diverse dal resto dell'anno, scritte sul sito e sulla scheda."),
     ("Servizio in hotel o a domicilio", "Dove andate, con che anticipo e quanto costa."),
     ("Cerimonie e matrimoni", "Prova, durata, anticipo: per chi viene da fuori, un'informazione indispensabile.")],
    "Collega il sito alla scheda Google e rispondi alle recensioni in italiano e, quando serve, in inglese: chi guarda da fuori si fida di chi risponde.",
    [("Serve il sito in inglese?", "Se hai già clienti stranieri o lavori con hotel e matrimoni, sì. Una versione fatta bene vale più di una traduzione automatica."),
     ("Posso proporre servizi a domicilio?", "Sì, se li fai davvero: scrivi dove arrivi, con che anticipo e a che condizioni.")],
    [("Due pubblici: residenti e visitatori.", "Due tempi di prenotazione."), ("Inglese vero o niente.", "Meglio una versione ben fatta."), ("Stagionalità dichiarata.", "Orari estivi e festivi sul sito e sulla scheda.")])
put('beauty', 'milano', "specializzarsi in un mercato affollato",
    "A Milano i saloni e i centri estetici sono moltissimi e per un nuovo cliente la scelta è già fatta dalla mappa e dalle recensioni. Il sito non serve a dire \"siamo bravi\": serve a dire in cosa siete speciali.",
    "Chi cerca \"parrucchiere Milano\" trova centinaia di schede. Chi cerca \"colore per capelli ricci\" o \"epilazione laser\" più la zona trova molto meno. Una specializzazione chiara e ripetuta nel sito fa trovare e fa scegliere.",
    "Scegli un'area in cui hai esperienza reale (un tipo di colore, di taglio, un trattamento, una clientela) e costruisci intorno ad essa le pagine, le foto e le recensioni. In una città di orari lunghi contano anche l'apertura serale e la prenotazione dal telefono in due minuti.",
    [("Una specializzazione detta subito", "Nella prima schermata, con una frase e due foto reali."),
     ("Prenotazione rapida", "WhatsApp o un'agenda online: chi cerca a Milano non aspetta."),
     ("Quartiere e come arrivare", "Fermata di metro o tram, parcheggio, tempi di percorrenza."),
     ("Recensioni specifiche", "Chiedi ai clienti di raccontare cosa hanno fatto: aiutano chi cerca proprio quel servizio.")],
    "Evita il listino infinito: tre o quattro servizi forti convincono più di venti generici. " + NOTE_RANKING,
    [("Come emergere tra tanti saloni?", "Specializzandosi e dicendolo ovunque: sito, scheda Google, recensioni e foto. Le ricerche generiche richiedono tempo."),
     ("Conviene un'agenda online?", "Se i clienti prenotano spesso e fuori orario, sì. Si collega al software di gestione e si valuta a parte.")],
    [("La mappa ha già deciso.", "Il sito spiega perché voi."), ("Una specializzazione batte venti servizi.", "Dilla subito."), ("Orari e prenotazione veloce.", "A Milano si decide in minuti.")])
# ------------------------------------------------------------------ trades
put('trades', 'vercelli', "case di campagna e cascine",
    "A Vercelli e nei comuni intorno un idraulico o un elettricista lavora tra case in città, cascine e immobili di campagna. Le distanze cambiano i tempi e i costi, e il sito deve dirlo con onestà.",
    "Chi chiama da una cascina o da una casa isolata vuole sapere se arrivi, in quanto tempo e a che condizioni. Chi chiama dal centro vuole un intervento rapido. Sono due richieste diverse e conviene dire chiaramente come le gestisci.",
    "Indica la zona che copri (città, frazioni, comuni intorno) e come calcoli lo spostamento, se lo applichi. Per gli immobili di campagna conta spiegare che tipi di impianti gestisci: elettrici, idraulici, pompe, impianti con sistemi autonomi; e se offri sopralluoghi preliminari.",
    [("Raggio d'azione", "Elenco dei comuni che copri davvero, con tempi realistici."),
     ("Costo dello spostamento", "Se c'è, scrivilo: evita discussioni al telefono."),
     ("Impianti di cascine e case isolate", "Cosa tratti e cosa no, senza promettere tutto."),
     ("Reperibilità", "Se fai urgenze, quando e come.")],
    "Per i lavori programmati (ristrutturazioni, impianti nuovi) aggiungi qualche lavoro vero in foto, con il permesso del cliente. Per il quadro generale vedi la " + a('/blog/sito-web-idraulico-elettricista-impresa-edile/', 'guida per idraulici, elettricisti e imprese edili') + ".",
    [("Devo elencare tutti i comuni?", "No: solo quelli che copri davvero, con tempi onesti. Meglio pochi veri che tanti che poi non servi."),
     ("Posso scrivere un prezzo di uscita?", "Sì, se lo applichi sempre: toglie incertezza a chi chiama.")],
    [("Le distanze fanno la differenza.", "Dichiarale."), ("Cascine e case isolate sono un cliente a sé.", "Dì cosa tratti."), ("Zona vera, non lista lunga.", "Poche, onesta.")])
put('trades', 'como', "ville, seconde case e accessi difficili",
    "Sul lago molte case sono seconde case, ville o edifici su terreni in pendenza, con accessi non semplici. Un idraulico o un elettricista di Como lavora spesso su immobili vuoti per parte dell'anno e con clienti che non abitano lì.",
    "Chi ha una seconda casa cerca qualcuno di fiducia che controlli l'impianto prima della stagione, intervenga se qualcosa si guasta in sua assenza e gli mandi foto e preventivi da lontano. Il sito deve dire che offri questo servizio, se lo offri.",
    "Una pagina sulla manutenzione delle seconde case (controlli prima e dopo la stagione, interventi su richiesta, relazione con foto) è più preziosa di un elenco di servizi. Specifica quando le chiavi si consegnano e come si gestiscono: sono dettagli che fanno scegliere.",
    [("Manutenzione stagionale", "Controlli prima dell'estate e prima dell'inverno, con cosa si verifica."),
     ("Gestione delle chiavi e degli accessi", "Come si concorda, come si registra, chi risponde."),
     ("Preventivi da lontano", "Foto e descrizione via WhatsApp, poi sopralluogo."),
     ("Tempi di intervento onesti", "Accessi difficili o strade strette cambiano i tempi: dillo.")],
    "Se lavori con clienti stranieri, una versione in inglese dei servizi principali evita fraintendimenti e porta richieste più utili.",
    [("Come far capire che seguo le seconde case?", "Con una pagina dedicata: cosa controlli, quando, come informi il proprietario."),
     ("Serve l'inglese?", "Se hai clienti che non parlano italiano, sì: servizi principali e contatto bastano.")],
    [("Il cliente spesso non c'è.", "Il servizio è la relazione a distanza."), ("Gli accessi cambiano i tempi.", "Dillo prima."), ("Seconde case, un servizio a sé.", "Una pagina dedicata.")])
put('trades', 'milano', "condomìni grandi e pronto intervento",
    "A Milano molti interventi riguardano condomìni, appartamenti in edifici d'epoca e uffici. I clienti sono spesso amministratori professionali o inquilini che chiamano con urgenza. Il sito deve far capire in pochi secondi che sei affidabile e rapido.",
    "Un amministratore di condominio cerca un fornitore che risponda, intervenga e documenti il lavoro. Un inquilino cerca qualcuno che arrivi oggi. Le due richieste vanno gestite con due percorsi: una pagina per amministratori e un numero ben visibile per l'urgenza.",
    "Per gli amministratori: come richiedere un preventivo, come si documentano gli interventi, tempi di risposta. Per l'urgenza: orari, reperibilità, cosa fare nel frattempo. Per gli edifici d'epoca: se hai esperienza con impianti vecchi, dillo, perché è un'esperienza che non tutti hanno.",
    [("Pagina per amministratori", "Servizi, documenti, tempi di risposta."),
     ("Urgenza", "Numero cliccabile e orari reali, senza promettere ciò che non puoi garantire."),
     ("Impianti in edifici d'epoca", "Se hai esperienza, mostralo con esempi veri."),
     ("Zone che copri a Milano", "Quartieri o municipi dove arrivi davvero e in quanto tempo.")],
    "Un mercato così affollato premia la specializzazione: manutenzione condominiale, ristrutturazioni di bagni, impianti elettrici per uffici. Scegline una e dillo subito. " + NOTE_RANKING,
    [("Come emergere tra tanti idraulici a Milano?", "Con una specializzazione chiara, la scheda Google curata e recensioni di clienti veri. Le ricerche generiche richiedono tempo."),
     ("Devo promettere interventi in un'ora?", "No, se non puoi garantirli: è la prima causa di recensioni negative.")],
    [("Amministratori e inquilini, due percorsi.", "Servono pagine diverse."), ("Specializzarsi paga.", "Più che promettere tutto."), ("Zone vere.", "Municipi e tempi onesti.")])
# ------------------------------------------------------------------ physio
put('physio', 'vercelli', "lavori manuali, sport e over 65",
    "A Vercelli e provincia molte persone lavorano nei campi, nelle aziende agricole e nell'artigianato, con schiena, spalle e ginocchia sotto sforzo. Chi cerca un fisioterapista spesso vuole tornare a lavorare in fretta e capire cosa può fare nel frattempo.",
    "Il paziente tipico non cerca una teoria: cerca di capire se la schiena che si blocca ogni stagione di raccolta ha una soluzione e quando può tornare a lavorare. Una pagina per i lavori manuali e ripetitivi, scritta con parole semplici, fa sentire capiti.",
    "Mettete accanto le fasce di età: chi lavora, chi pratica sport, chi è anziano e cerca di mantenersi autonomo. Per gli over 65 contano accessibilità, parcheggio, orari al mattino e la possibilità di essere accompagnati.",
    [("Lavori manuali e ripetitivi", "Schiena, spalla, polso: cosa si valuta e come si lavora, senza promettere guarigioni."),
     ("Sportivi amatori", "Ritorno all'attività dopo un infortunio, prevenzione."),
     ("Over 65", "Mobilità, equilibrio, accessibilità dello studio."),
     ("Orari comodi", "Presto al mattino o fine giornata, per chi lavora.")],
    RULES + " Evita testimonianze scritte sul sito e preferisci le recensioni vere sulla scheda Google.",
    [("Posso scrivere che il trattamento risolve il mal di schiena?", "No: le promesse di risultato non sono ammesse. Descrivi il metodo e il percorso, non l'esito."),
     ("Cosa devo avere nel modulo di contatto?", "Pochi campi e nessun dettaglio clinico: la privacy sui dati sulla salute è più rigorosa.")],
    [("Chi lavora con le mani cerca tempi di recupero.", "Parlagli di lavoro."), ("Accessibilità e orari per gli over 65.", "Dettagli decisivi."), ("Niente promesse di guarigione.", "Metodo e percorso.")])
put('physio', 'como', "sport all'aperto e chi lavora seduto",
    "A Como molte persone praticano sport all'aperto (corsa, ciclismo, vela, trekking) e altre passano le giornate seduto, compresi i pendolari verso la Svizzera. Sono due pubblici che arrivano da fisioterapisti per problemi diversi.",
    "Lo sportivo cerca di tornare a muoversi e di non ricadere nello stesso infortunio. Chi lavora seduto cerca sollievo da collo e schiena e un modo di non peggiorare. Il sito può parlare a entrambi con pagine distinte.",
    "Per gli sportivi: valutazione del gesto, ritorno all'attività, prevenzione. Per chi lavora seduto: percorsi brevi, esercizi per l'ufficio e gli orari fuori dal lavoro. Se hai pazienti stranieri, una versione in inglese dei contatti e dei servizi evita incomprensioni.",
    [("Sport all'aperto", "Corsa, ciclismo, sport sull'acqua: cosa si valuta, senza promettere risultati."),
     ("Chi lavora seduto o fa il pendolare", "Postura, collo, schiena: percorsi pratici."),
     ("Orari per chi lavora lontano", "Mattina presto o sera, se li offri."),
     ("Pazienti stranieri", "Informazioni in inglese su prima visita e contatti.")],
    RULES,
    [("Posso mostrare foto di pazienti sportivi?", "Solo con il consenso scritto e nel rispetto delle regole della professione: è un punto da verificare con il tuo Ordine."),
     ("Serve una versione in inglese?", "Se visiti pazienti stranieri sì, anche solo con servizi e contatti.")],
    [("Sportivi e sedentari, due pagine.", "Problemi diversi."), ("Orari per chi lavora lontano.", "Un dettaglio che decide."), ("Inglese essenziale.", "Per i pazienti che non parlano italiano.")])
put('physio', 'milano', "specializzazione, aziende e assicurazioni",
    "A Milano i fisioterapisti sono molti e molti pazienti arrivano tramite il lavoro, l'assicurazione o il medico. Il sito serve a far capire in cosa sei specializzato e come lavori con chi paga la seduta, che sia il paziente o un fondo.",
    "Chi cerca \"fisioterapista Milano\" trova centinaia di studi. Chi cerca \"riabilitazione spalla\" o \"fisioterapia per runner\" più la zona ne trova molti meno. La specializzazione è il modo di farsi scegliere.",
    "Dì chiaramente cosa tratti meglio, con quale formazione e quale metodo. Se lavori con fondi sanitari, assicurazioni o welfare aziendale, spiega come funziona la procedura (cosa serve, come si prenota) senza promesse sui rimborsi, che dipendono dal fondo.",
    [("Una specializzazione chiara", "Un ambito, con formazione e metodo, in prima schermata."),
     ("Fondi, assicurazioni e welfare", "Se esistono convenzioni, descrivi come funzionano senza promettere rimborsi."),
     ("Zona e collegamenti", "Fermata, parcheggio, tempi di percorrenza."),
     ("Orari per chi esce tardi dal lavoro", "Sera e primo mattino, se li offri.")],
    RULES + " " + NOTE_RANKING,
    [("Posso scrivere che le sedute sono rimborsabili?", "Solo se è vero per ciascun fondo e se lo spieghi con precisione: la copertura dipende dal fondo e dal paziente."),
     ("Come emergere tra tanti studi?", "Con una specializzazione, la scheda Google curata e contenuti utili. Le ricerche generiche richiedono tempo.")],
    [("Specializzarsi è il modo di farsi scegliere.", "Dilla subito."), ("Fondi e assicurazioni: spiega la procedura.", "Senza promettere rimborsi."), ("Orari per chi lavora.", "Sera e mattina presto.")])
put('physio', 'novara', "-", "-", "-", "-", [], "-", [], [])  # placeholder removed below
del D[('physio', 'novara')]
# ------------------------------------------------------------------ vet
put('vet', 'vercelli', "animali da compagnia e animali da reddito",
    "Nella provincia di Vercelli, accanto ai cani e ai gatti di città, ci sono aziende agricole e allevamenti. Un veterinario che segue anche animali da reddito o cavalli deve dirlo con chiarezza, perché sono servizi che il proprietario cerca in modo diverso.",
    "Chi ha un cane cerca un ambulatorio vicino e orari comodi. Chi ha animali da reddito cerca un professionista che venga in azienda, risponda presto e conosca il lavoro. Due pubblici, due modi di cercare.",
    "Un'unica pagina che mescola tutto confonde. Meglio una sezione per gli animali da compagnia (ambulatorio, orari, prenotazione) e una per le aziende (zone di intervento, reperibilità, tipo di servizi), con un numero diverso o un modo diverso di chiamare.",
    [("Ambulatorio e visite", "Orari, prenotazione, servizi per cani, gatti ed esotici."),
     ("Interventi in azienda", "Zone che copri, tempi di arrivo, come si chiama."),
     ("Reperibilità", "Quando e a quali condizioni: la domanda più importante."),
     ("Specie seguite", "Bovini, equini, ovini o altro: solo quelle che segui davvero.")],
    RULES,
    [("Serve un numero diverso per le aziende?", "Conviene distinguere almeno il modo di chiamare e gli orari: le urgenze in azienda seguono tempi diversi."),
     ("Posso mostrare foto degli animali curati?", "Con il consenso dei proprietari. Meglio foto dello studio e del team.")],
    [("Due clienti, due richieste.", "Ambulatorio e azienda."), ("La reperibilità è l'informazione chiave.", "Dilla chiaramente."), ("Specie vere, non tutte.", "Solo quelle che segui.")])
put('vet', 'como', "turisti, viaggi e pratiche per l'estero",
    "A Como molti proprietari viaggiano con i loro animali, anche verso la Svizzera, e i turisti si trovano con un cane che sta male lontano da casa. Il sito di un veterinario deve rispondere a chi cerca un aiuto in fretta e a chi si prepara a partire.",
    "Il turista con un cane che sta male cerca orari, un numero e un posto dove andare, spesso in inglese. Il residente che viaggia cerca informazioni su documenti, microchip e vaccinazioni richieste per l'espatrio.",
    "Una pagina in inglese con le urgenze, gli orari e come arrivare è la più utile ai visitatori. Una pagina sui viaggi con gli animali (microchip, vaccinazioni, documenti: cosa si fa in studio, cosa va verificato presso le autorità) è utile ai residenti. Non elencare regole che cambiano senza rimandare a fonti ufficiali.",
    [("Urgenze in inglese", "Orari, telefono e indicazioni per arrivare."),
     ("Viaggi con animali", "Cosa fai tu (microchip, vaccini, certificati) e dove verificare i requisiti del Paese di destinazione."),
     ("Orari stagionali", "Aperture estive diverse dal resto dell'anno."),
     ("Accessibilità", "Parcheggio e accesso per chi arriva con animali grandi.")],
    RULES,
    [("Posso scrivere le regole per viaggiare in Svizzera?", "Meglio rimandare alle fonti ufficiali, perché cambiano: indica cosa fai tu e dove verificare."),
     ("Serve una versione in inglese?", "Se hai visitatori stranieri sì, almeno per urgenze e contatti.")],
    [("Turisti con urgenze.", "Inglese, orari e mappa."), ("Residenti che viaggiano.", "Una pagina sui documenti."), ("Regole ufficiali, non copiate.", "Rimanda alle fonti.")])
put('vet', 'milano', "cani in appartamento, specialità e urgenze",
    "A Milano molti animali vivono in appartamento e molti proprietari cercano uno specialista (dermatologia, cardiologia, ortopedia) oltre al veterinario di fiducia. Il sito serve a far capire cosa fai meglio e come si arriva da te.",
    "Chi cerca un veterinario a Milano spesso confronta più strutture, guarda recensioni e cerca la più vicina alla fermata o al parcheggio. Chi ha un caso specifico cerca la specialità. Il sito deve dirlo subito.",
    "Dichiara le specialità che segui davvero, con titoli e formazione, e come si accede (su appuntamento, su invio di un collega). Per le urgenze, orari e numero visibili, e un'informazione onesta su cosa puoi fare e cosa richiede un invio ad altra struttura.",
    [("Specialità", "Quelle che segui davvero, con formazione e titoli."),
     ("Come si accede", "Appuntamento, invio da un collega, urgenze."),
     ("Mezzi e parcheggio", "A Milano come si arriva conta quanto la cura."),
     ("Specie seguite", "Cani, gatti, esotici, solo quelli che segui.")],
    RULES + " " + NOTE_RANKING,
    [("Come emergere tra tante strutture?", "Con una specialità chiara, titoli visibili, scheda Google curata e recensioni vere."),
     ("Devo scrivere che faccio urgenze?", "Solo se è vero e con orari precisi. Se invii altrove, dillo e indica come.")],
    [("Specialità e titoli prima di tutto.", "Il proprietario cerca competenza."), ("Mezzi e parcheggio contano.", "Scrivili."), ("Urgenze oneste.", "Solo se le fai.")])
put('vet', 'novara', "vicinanza, urgenze e passaparola",
    "A Novara molti proprietari scelgono il veterinario vicino a casa e su consiglio. Il sito serve a confermare quel consiglio, a far trovare gli orari giusti in un momento di apprensione e a spiegare cosa si fa in prima visita.",
    "Un cane che sta male non aspetta: il proprietario cerca da telefono un numero, un orario e se si può andare oggi. Il sito e la scheda Google devono dire la stessa cosa e dirla in modo chiaro.",
    "Metti in evidenza urgenze e orari, come funziona la prima visita (cosa portare, quanto dura), come si prenota e le specie che segui. Aggiungi qualche riga su cosa fare in attesa dell'appuntamento, senza dare consigli clinici dettagliati online.",
    [("Urgenze e orari", "Numero cliccabile e orari identici a quelli della scheda Google."),
     ("Prima visita", "Cosa portare (libretto, esami), quanto dura, come prenotare."),
     ("Il team", "Titoli e foto vere dei veterinari."),
     ("Come arrivare", "Parcheggio e accesso per animali grandi o in difficoltà.")],
    RULES + " La guida generale è " + a('/blog/sito-web-veterinario/', 'sito web per veterinari') + " e come lavoriamo a Novara è nella pagina " + a('/novara/', 'siti web a Novara') + ".",
    [("Posso dare consigli clinici sul sito?", "Meglio di no: il sito informa su servizi e orari; la diagnosi si fa in visita."),
     ("Serve la scheda Google?", "Sì: è dove la maggior parte dei proprietari trova orari e telefono in un momento di urgenza.")],
    [("Urgenza: numero e orari.", "In prima schermata."), ("Prima visita spiegata.", "Meno paura, meno telefonate."), ("Scheda Google allineata.", "Stessi orari, stesso numero.")])
# ------------------------------------------------------------------ auto
put('auto', 'vercelli', "mezzi agricoli, furgoni e pendolari",
    "A Vercelli un'officina o una carrozzeria lavora con auto di privati, pendolari verso Torino e Milano e mezzi di aziende agricole e artigiane. Il sito deve dire quali veicoli trattate e quanto tempo servono.",
    "Chi ha un'azienda non può restare senza mezzo: cerca un'officina che sappia stimare i tempi, che offra un'auto di cortesia o un ritiro, e che lavori su furgoni e veicoli commerciali. Il privato cerca prezzo chiaro e un appuntamento comodo.",
    "Una sezione per le aziende (veicoli commerciali, flotte piccole, mezzi da lavoro) con tempi di fermo realistici e un contatto diretto. Una per i privati con servizi e prezzi di massima. Se tratti anche trattori e macchine agricole, scrivilo senza esagerare: non tutte le officine possono.",
    [("Veicoli commerciali e da lavoro", "Furgoni, mezzi aziendali, tempi di fermo, auto di cortesia."),
     ("Mezzi agricoli", "Solo se li tratti davvero."),
     ("Pendolari", "Orari di ritiro e consegna comodi, tagliandi veloci."),
     ("Gomme stagionali", "Prenotazione per il cambio stagionale.")],
    "Per un quadro più ampio vedi la " + a('/blog/sito-web-autofficina-carrozzeria-gommista/', 'guida per autofficine, carrozzerie e gommisti') + ".",
    [("Serve parlare alle aziende?", "Sì: i clienti aziendali tornano e portano più lavoro del singolo privato."),
     ("Posso scrivere che tratto mezzi agricoli?", "Solo se hai attrezzature e competenze: altrimenti rischi richieste che non puoi soddisfare.")],
    [("Aziende e privati, due percorsi.", "Tempi di fermo contano."), ("Mezzi agricoli solo se veri.", "Non promettere tutto."), ("Gomme stagionali.", "Prenotazione anticipata.")])
put('auto', 'como', "frontalieri, turisti e orari lunghi",
    "A Como molti automobilisti fanno molti chilometri ogni giorno, anche verso la Svizzera, e molti visitatori arrivano in auto con problemi in viaggio. Un'officina o un gommista deve dire quando e come può ricevere.",
    "Il frontaliere cerca orari che gli permettano di lasciare l'auto prima di andare al lavoro e riprenderla dopo, o un ritiro e riconsegna. Il turista in difficoltà cerca un numero e un intervento rapido, spesso in inglese.",
    "Orari lunghi o su appuntamento, servizio di ritiro e consegna, auto di cortesia e tempi reali sono le informazioni che fanno scegliere. Per i visitatori, una pagina in inglese con il numero e cosa fai in urgenza (gomme, batteria, diagnosi) basta.",
    [("Orari per chi viaggia molto", "Apertura anticipata o ritiro e riconsegna, se li offri."),
     ("Auto con molti chilometri", "Tagliandi e controlli pensati per chi guida molto."),
     ("Interventi per turisti", "Gomme, batteria, diagnosi, in inglese e con numero ben visibile."),
     ("Gomme stagionali", "Prenotazioni anticipate.")],
    "Nei periodi di punta turistici gli appuntamenti si saturano: un avviso chiaro sui tempi evita recensioni negative.",
    [("Serve il sito in inglese?", "Per gli interventi urgenti ai turisti sì, in forma breve: numero, orari, servizi."),
     ("Posso offrire il ritiro dell'auto?", "Se lo fai davvero, mettilo in evidenza: per chi lavora lontano è un motivo di scelta.")],
    [("Chi guida molto ha esigenze di orari.", "Ritiro e consegna."), ("Turisti in difficoltà.", "Numero e inglese essenziale."), ("Periodi di punta.", "Avviso sui tempi.")])
put('auto', 'milano', "auto elettriche, parcheggio e ritiro",
    "A Milano molti automobilisti hanno meno spazio e meno tempo, e molte auto sono ibride o elettriche. Un'officina o una carrozzeria che lavora bene qui ritira, consegna e dice chiaramente cosa sa fare.",
    "Il cliente milanese non vuole perdere mezza giornata: cerca ritiro e riconsegna, auto sostitutiva, tempi certi e preventivi chiari. Chi ha un'auto ibrida o elettrica cerca un'officina che la sappia trattare.",
    "Dichiara tipologie e marchi che tratti, con le competenze reali sulle auto ibride ed elettriche (se le hai), e i servizi che riducono il tempo perso: ritiro, riconsegna, tempi dichiarati, foto del lavoro. Per la carrozzeria, preventivo di massima con foto e tempi di consegna.",
    [("Auto ibride ed elettriche", "Solo se hai formazione e attrezzature."),
     ("Ritiro e riconsegna", "Zone servite, costi, orari."),
     ("Preventivo con foto", "Per carrozzeria, con specifica che il definitivo si fa in sede."),
     ("Parcheggio e accesso", "Dove si lascia l'auto e come si arriva.")],
    "Un mercato molto concorrenziale premia la specializzazione e le recensioni vere: scegli un ambito, dillo e curane la scheda Google. " + NOTE_RANKING,
    [("Conviene specializzarsi?", "Sì: una specializzazione chiara (elettriche, marchi, carrozzeria) è più facile da trovare e da scegliere."),
     ("Posso promettere tempi di riparazione?", "Solo se puoi rispettarli: i tempi sbagliati sono la causa principale di recensioni negative.")],
    [("Il tempo perso è il costo vero.", "Ritiro e riconsegna."), ("Ibride ed elettriche solo se vere.", "Competenze dichiarate."), ("Preventivo con foto.", "Riduce i viaggi inutili.")])
put('auto', 'novara', "pendolari, flotte piccole e gomme stagionali",
    "A Novara molte persone usano l'auto tutti i giorni per spostarsi verso Milano e Torino o per lavoro, e molte piccole imprese hanno veicoli da tenere in strada. Un'officina o un gommista che dice orari, tempi e prezzi di massima si fa scegliere.",
    "Il pendolare cerca un'officina che gli faccia il tagliando senza fargli perdere la giornata, e un gommista che prenoti il cambio gomme prima dell'ingorgo di stagione. Le piccole imprese cercano un referente che risponda.",
    "Metti in evidenza i servizi principali (tagliando, freni, gomme, carrozzeria), gli orari, la prenotazione con WhatsApp e un modo per richiedere un preventivo con la targa o le foto. Per le piccole flotte, una frase chiara su come gestisci i mezzi aziendali.",
    [("Tagliando in giornata", "Se lo offri, dillo con i tempi reali."),
     ("Gomme stagionali", "Prenotazione, cosa serve, tempi."),
     ("Mezzi aziendali", "Un referente e un modo semplice di prenotare più veicoli."),
     ("Preventivo con targa o foto", "Meno telefonate inutili.")],
    "Come lavoriamo con le attività di Novara: " + a('/novara/', 'siti web a Novara') + ". Il quadro generale è nella " + a('/blog/sito-web-autofficina-carrozzeria-gommista/', 'guida per autofficine, carrozzerie e gommisti') + ".",
    [("Serve il sito se ho la scheda Google?", "Sì: la scheda porta la prima telefonata, il sito dà servizi, prezzi e prenotazione."),
     ("Come far prenotare il cambio gomme?", "Con un modulo o un messaggio WhatsApp già pronto e un avviso ad inizio stagione.")],
    [("Pendolari: tempo e orari.", "Tagliando senza perdere la giornata."), ("Gomme: prenotare prima.", "Evita le code."), ("Flotte piccole: un referente.", "Un solo contatto.")])
# ------------------------------------------------------------------ tech
put('tech', 'vercelli', "cascine, edifici storici e pratiche",
    "A Vercelli e nel territorio intorno si lavora spesso su cascine, edifici rurali e immobili storici, con ristrutturazioni e pratiche che richiedono esperienza particolare. Un architetto o un geometra che lo sa fare deve dirlo.",
    "Chi ha una cascina da recuperare o un edificio in centro cerca un professionista che conosca le regole, i vincoli e i tempi, e che sappia spiegarli. Non cerca slogan: cerca qualcuno che abbia già fatto qualcosa di simile.",
    "Mostra pochi progetti di recupero, raccontando il problema, la soluzione e i tempi (con il permesso del committente). Spiega le fasi di una pratica tipica (sopralluogo, progetto, pratiche, direzione lavori) con parole semplici e senza promettere tempi che dipendono dagli enti.",
    [("Recupero di cascine e immobili rurali", "Pochi progetti ben raccontati."),
     ("Edifici storici e vincoli", "Se hai esperienza con le procedure, spiegala senza promettere tempi."),
     ("Pratiche edilizie e catastali", "Cosa serve, quanto tempo richiede in genere."),
     ("Chi sei", "Titoli, iscrizione, foto vera.")],
    RULES,
    [("Posso promettere i tempi delle pratiche?", "No: dipendono dagli enti. Descrivi le fasi e cosa dipende da te."),
     ("Come mostro i progetti?", "Pochi, con il permesso del committente e una breve storia di ciascuno.")],
    [("Il recupero è la specialità del territorio.", "Mostralo."), ("Vincoli e procedure da spiegare.", "Senza promesse di tempi."), ("Pochi progetti, raccontati.", "Più di una galleria.")])
put('tech', 'como', "ville, vincoli paesaggistici e clienti da fuori",
    "Sul lago molti progetti riguardano ville, edifici di pregio e terreni con vincoli paesaggistici, spesso per clienti che non vivono lì. Un architetto o un ingegnere di Como lavora con regole più complesse e committenti più lontani.",
    "Il cliente che compra o ristruttura una casa sul lago vuole sapere se hai già affrontato vincoli e pratiche paesaggistiche, come gestisci il cantiere a distanza e come lo tieni informato. Spesso parla un'altra lingua.",
    "Una pagina sui progetti sul lago, con esempi veri e permessi, e una sul modo in cui lavori a distanza (aggiornamenti, foto, riunioni in videochiamata) rassicura. Una versione in inglese dei servizi e del modo di lavorare apre il mercato di chi cerca da fuori.",
    [("Vincoli paesaggistici", "Spiega l'esperienza, senza promettere esiti sulle autorizzazioni."),
     ("Lavoro a distanza", "Come si seguono cantiere, aggiornamenti e decisioni."),
     ("Progetti sul lago", "Pochi, ben fotografati e con il permesso."),
     ("Inglese", "Servizi e metodo di lavoro per chi cerca da fuori.")],
    RULES,
    [("Posso promettere le autorizzazioni?", "No: dipendono dagli enti. Descrivi il percorso e la tua esperienza."),
     ("Serve il sito in inglese?", "Se lavori con clienti stranieri sì: servizi e come lavori basta.")],
    [("Vincoli e autorizzazioni: esperienza, non promesse.", "Dilla bene."), ("Clienti lontani.", "Lavoro a distanza spiegato."), ("Inglese per chi cerca da fuori.", "Versione breve.")])
put('tech', 'milano', "ristrutturazioni di interni e pratiche complesse",
    "A Milano un architetto o un geometra lavora spesso su appartamenti, uffici e condomìni, con pratiche complesse e clienti esigenti. In un mercato molto affollato, la specializzazione e i progetti mostrati fanno la differenza.",
    "Chi ristruttura un appartamento a Milano cerca qualcuno che gestisca progetto, pratiche e cantiere, con tempi e costi chiari. Un investitore cerca analisi e fattibilità. Un amministratore cerca un tecnico per le parti comuni.",
    "Scegli uno o due ambiti (interni residenziali, uffici, condomìni, immobili da mettere a reddito) e costruisci intorno ad essi la tua presenza: progetti, processo, tempi. Racconta in modo onesto cosa comprende il tuo servizio (progetto, pratiche, direzione lavori) e cosa no.",
    [("Ambiti scelti", "Uno o due, dichiarati subito."),
     ("Il processo", "Dal sopralluogo alla consegna, con tempi e responsabilità."),
     ("Pratiche in condominio", "Se gestisci autorizzazioni e rapporti con l'amministratore."),
     ("Progetti mostrati", "Pochi, con permesso e senza dati riconoscibili.")],
    RULES + " " + NOTE_RANKING,
    [("Come emergere tra tanti studi?", "Con una specializzazione chiara, progetti veri e recensioni di clienti reali."),
     ("Cosa devo dire sui costi?", "Come si arriva a un preventivo e cosa comprende: le cifre dipendono dal progetto e dalle regole della professione.")],
    [("Un mercato di specialisti.", "Scegli un ambito."), ("Il processo rassicura.", "Fasi e tempi chiari."), ("Cosa comprende il servizio.", "E cosa no.")])
put('tech', 'novara', "ristrutturazioni, pratiche e passaggi di proprietà",
    "A Novara un geometra o un architetto lavora per lo più su case, condomìni e piccole attività, con pratiche edilizie, catastali e di ristrutturazione. Il sito serve a far capire quali pratiche segui e come si comincia.",
    "Chi compra o ristruttura casa a Novara cerca qualcuno che lo guidi nel percorso e che risponda al telefono. Chi deve fare una pratica catastale o un cambio di destinazione cerca un riferimento che gli spieghi i passaggi.",
    "Una pagina per ciascun tipo di pratica che segui, scritta per chi non è del mestiere: cosa serve, in quali casi, come si svolge, quanto tempo richiede in genere senza promettere tempi che dipendono dagli enti. Un modulo breve per il primo contatto e un incontro a Novara.",
    [("Pratiche edilizie e catastali", "Una pagina per tipo, con cosa serve e come funziona."),
     ("Ristrutturazioni", "Progetto, pratiche, direzione lavori: cosa comprendi."),
     ("Passaggi di proprietà", "Se segui compravendite, con cosa serve e come ti si contatta."),
     ("Primo incontro", "Come si svolge e come si chiede.")],
    RULES + " Il quadro generale è nella " + a('/blog/sito-web-notaio-geometra-architetto-ingegnere/', 'guida per studi tecnici e notarili') + " e le pagine locali nella " + a('/novara/', 'pagina su Novara') + ".",
    [("Posso scrivere quanto costa una pratica?", "Dipende dalla pratica e dalle regole della professione: spiega come si arriva a un preventivo."),
     ("Serve la scheda Google?", "Sì: molti clienti la guardano prima di chiamare.")],
    [("Pratiche spiegate in parole semplici.", "Una pagina per tipo."), ("Tempi: fasi, non promesse.", "Dipendono dagli enti."), ("Primo incontro semplice.", "Modulo e telefono.")])
# ------------------------------------------------------------------ gym
put('gym', 'vercelli', "studenti, lavoratori e orari",
    "A Vercelli una palestra ha clienti molto diversi: studenti universitari, lavoratori, famiglie. Cambiano gli orari, i budget e le aspettative, e il sito deve parlare a ciascuno.",
    "Lo studente cerca una formula flessibile e un prezzo chiaro, spesso da settembre. Chi lavora cerca orari compatibili. La famiglia cerca corsi per più età. Un sito che mostra le tre strade fa scegliere prima.",
    "Una pagina con le formule (mensile, trimestrale, brevi periodi), una con orari e corsi divisi per fasce, e un invito a provare. Se ci sono sconti per studenti, scrivi come si ottengono e per quanto valgono, senza condizioni nascoste.",
    [("Formule flessibili", "Brevi periodi o mensili per chi sta in città per l'anno accademico."),
     ("Orari per chi lavora", "Mattina presto, pausa pranzo, sera."),
     ("Corsi per fasce d'età", "Famiglie e ragazzi con orari scritti."),
     ("Prova gratuita", "Se la offri, come si prenota.")],
    "Il picco di iscrizioni cade di solito a settembre e dopo le feste: prepara prima le formule e la pagina per iscriversi. Il quadro generale è nella " + a('/blog/sito-web-palestra/', 'guida per palestre') + ".",
    [("Conviene scrivere gli sconti per studenti?", "Sì, se li fai, con le condizioni: evita malintesi e porta iscrizioni."),
     ("Quando serve il sito più aggiornato?", "A settembre e dopo le feste, quando le persone decidono di iscriversi.")],
    [("Tre pubblici: studenti, lavoratori, famiglie.", "Tre percorsi."), ("Formule scritte per intero.", "Prezzo, durata, disdetta."), ("Picchi di iscrizione.", "Preparati prima.")])
put('gym', 'como', "orari lunghi, outdoor e turisti",
    "A Como molte persone lavorano lontano, anche in Svizzera, e molti praticano sport all'aperto; in più ci sono turisti che cercano un posto per allenarsi per pochi giorni. Una palestra che dice chiaramente orari e formule giornaliere trova più clienti.",
    "Il frontaliere cerca orari molto presto o molto tardi. Chi pratica sport all'aperto cerca un allenamento complementare. Il turista cerca un ingresso giornaliero o settimanale e istruzioni in inglese.",
    "Una pagina con orari estesi (se li hai), una con i corsi e le formule brevi e un modo di prenotare un ingresso di prova. Se hai clienti stranieri, una versione in inglese di orari, prezzi e come arrivare è più utile di molte pagine tradotte.",
    [("Orari estesi", "Se li offri, in primo piano."),
     ("Formule giornaliere e settimanali", "Prezzi e condizioni, anche in inglese."),
     ("Allenamento per chi pratica sport", "Corsi o programmi complementari, senza promesse di prestazione."),
     ("Informazioni in inglese", "Orari, prezzi, indirizzo e contatto.")],
    SMALL,
    [("Serve il sito in inglese?", "Se hai clienti stranieri sì, anche solo per orari, prezzi e contatti."),
     ("Conviene offrire un ingresso di prova?", "Se puoi farlo, sì: abbassa la barriera, soprattutto per chi viene da fuori.")],
    [("Orari estremi per chi lavora lontano.", "Mettili in evidenza."), ("Turisti: ingresso breve.", "Formule giornaliere."), ("Inglese essenziale.", "Orari, prezzi, contatti.")])
put('gym', 'milano', "specializzarsi contro le catene",
    "A Milano le palestre sono moltissime e le catene occupano le ricerche generiche. Una palestra o uno studio di allenamento si fa scegliere con una specializzazione chiara, un ambiente riconoscibile e un percorso per iniziare.",
    "Chi cerca \"palestra Milano\" trova decine di schede. Chi cerca \"allenamento funzionale\", \"personal training\" o \"corso per principianti\" più il quartiere ne trova molte meno. Una specializzazione dichiarata è più utile di un'attrezzatura più grande.",
    "Scegli un metodo o un pubblico (principianti, donne, over, atleti, allenamento a piccoli gruppi), scrivi come si lavora, chi segue i clienti e quanto dura un percorso. Per chi lavora vicino, proponi formule per la pausa pranzo.",
    [("Una specializzazione", "Metodo e pubblico, in prima schermata."),
     ("Piccoli gruppi e personal training", "Come funziona, quante persone, chi segue."),
     ("Formule per la pausa pranzo", "Se le offri, con orari e durata."),
     ("Il quartiere e come arrivare", "Fermata, parcheggio, tempi di percorrenza.")],
    NOTE_RANKING,
    [("Come competere con le catene?", "Specializzandosi e curando relazione e risultati misurabili senza promesse esagerate. Le ricerche generiche sono dominate dalle catene."),
     ("Conviene un'agenda online?", "Per corsi su prenotazione sì: si collega al software e si valuta a parte.")],
    [("Le catene dominano le ricerche generiche.", "Specializzarsi è la strada."), ("Piccoli gruppi e seguiti.", "Mostralo."), ("Pausa pranzo.", "Un'offerta per chi lavora vicino.")])
# ------------------------------------------------------------------ creative
put('creative', 'vercelli', "matrimoni di campagna e aziende agricole",
    "A Vercelli e dintorni molte cerimonie si fanno in cascine, dimore storiche e location di campagna, e molte aziende agricole hanno bisogno di foto del prodotto e della produzione. Un fotografo o un wedding planner del territorio ha due strade.",
    "Le coppie cercano un fotografo che conosca le location e la luce di campagna e un wedding planner che sappia organizzare cerimonie fuori dai circuiti più noti. Le aziende agricole cercano foto per sito, catalogo e confezioni.",
    "Mostra due portfolio separati: matrimoni in location di campagna e foto per aziende agricole e alimentari. Per i wedding planner, racconta come lavori con le location del territorio e quali servizi comprendi (logistica, fornitori, coordinamento).",
    [("Portfolio matrimoni", "Cascine, dimore storiche e location locali, con il permesso delle coppie."),
     ("Portfolio aziende agricole", "Prodotti, lavorazioni, persone, per sito e cataloghi."),
     ("Come lavori", "Sopralluogo, tempi di consegna, cosa è incluso."),
     ("Preventivo mirato", "Data, luogo e tipo di servizio.")],
    "Per un taglio sulle aziende agricole vedi anche la guida " + a('/blog/sito-web-aziende-agroalimentari/', 'sito web per aziende agroalimentari') + ".",
    [("Posso mostrare le foto dei matrimoni?", "Con il consenso delle coppie e senza dati che le rendano riconoscibili se non vogliono."),
     ("Conviene mostrare anche foto per aziende?", "Sì, se è un servizio che vuoi vendere: è un cliente con budget e continuità.")],
    [("Due mercati: coppie e aziende.", "Due portfolio."), ("Location locali, un punto di forza.", "Mostrale."), ("Preventivo mirato.", "Meno richieste inutili.")])
put('creative', 'como', "matrimoni sul lago e clienti stranieri",
    "Il Lago di Como è una meta per matrimoni e cerimonie, anche di coppie straniere che sposano a distanza. Un fotografo o un wedding planner di Como lavora con clienti che non conoscono il posto e decidono su internet.",
    "Una coppia che sposa sul lago da un altro Paese sceglie guardando portfolio, lingue, esperienza con le location e capacità di organizzare a distanza. Spesso non si incontra prima, quindi il sito è il primo e talvolta l'unico incontro.",
    "Un sito in inglese vero, con portfolio di matrimoni sul lago, descrizione di come si lavora a distanza (videochiamate, sopralluoghi, tempi), una pagina per le location e le procedure principali e un preventivo con data, luogo e numero di invitati.",
    [("Inglese vero", "Testi scritti o rivisti da una persona, non tradotti alla lettera."),
     ("Portfolio sul lago", "Pochi matrimoni ben raccontati, con permesso."),
     ("Lavoro a distanza", "Come si organizza senza incontrarsi prima."),
     ("Pagina sulle location", "Cosa conosci e con chi lavori.")],
    "Le regole per sposarsi in Italia da stranieri cambiano: rimanda a fonti ufficiali e specifica cosa fai tu. Il quadro per gli altri settori turistici è nella guida " + a('/blog/sito-web-hotel-ristoranti-lago-di-como/', 'hotel e ristoranti sul Lago di Como') + ".",
    [("Serve il sito in inglese?", "Se lavori con coppie straniere, è la parte più importante del sito."),
     ("Posso spiegare le procedure per sposarsi?", "Solo in modo generale, rimandando alle fonti ufficiali perché cambiano.")],
    [("Il sito è il primo incontro.", "Inglese e portfolio."), ("Lavoro a distanza spiegato.", "Rassicura."), ("Procedure: rimanda alle fonti.", "Non copiarle.")])
put('creative', 'milano', "stile riconoscibile, aziende e moda",
    "A Milano un fotografo o un wedding planner compete con un mercato molto ampio, che comprende anche fotografia aziendale, di moda e di eventi. Un sito che dichiara uno stile e un pubblico è più utile di un portfolio generico.",
    "I clienti milanesi cercano un fotografo per un ritratto professionale, un evento, un catalogo, un servizio. Le coppie cercano matrimoni anche fuori città. I wedding planner competono su stile e organizzazione, non solo su prezzo.",
    "Scegli uno o due ambiti (ritratti aziendali, eventi, prodotto, matrimoni) e costruisci il sito intorno ad essi, con portfolio ordinato per tipo di servizio e una descrizione del processo. Per i clienti aziendali, aggiungi tempi, formati di consegna e licenze.",
    [("Ambito e stile", "Uno o due, dichiarati subito."),
     ("Fotografia per aziende", "Ritratti, eventi, prodotto: tempi, formati, uso delle immagini."),
     ("Matrimoni fuori città", "Disponibilità a viaggiare e come si gestisce."),
     ("Processo", "Dal primo contatto alla consegna.")],
    NOTE_RANKING,
    [("Come emergere a Milano?", "Con uno stile riconoscibile, un ambito dichiarato e un portfolio selezionato. Le ricerche generiche richiedono tempo."),
     ("Cosa devo scrivere sulle licenze?", "Come si possono usare le immagini (siti, stampa, social) e per quanto tempo: è un'informazione che i clienti aziendali cercano.")],
    [("Uno stile riconoscibile.", "Meglio di un portfolio generico."), ("Aziende: formati e licenze.", "Dettagli che fanno scegliere."), ("Disponibilità a viaggiare.", "Per i matrimoni fuori città.")])
put('creative', 'novara', "coppie, famiglie ed eventi della zona",
    "A Novara e provincia un fotografo o un wedding planner lavora con coppie della zona, famiglie, aziende locali ed eventi. Il passaparola conta molto, e il sito deve confermare ciò che i conoscenti hanno detto.",
    "Chi riceve il consiglio di un fotografo cerca il suo nome, guarda il portfolio e decide se chiamare. Chi non ha consigli cerca \"fotografo Novara\" o \"wedding planner Novara\" e sceglie guardando foto e recensioni.",
    "Mostra pochi lavori ben raccontati per tipo (matrimoni, famiglie, eventi, aziende), indica le zone in cui lavori, i tempi di consegna e come si prenota. Per i wedding planner, descrivi i servizi (coordinamento, fornitori, giorno del matrimonio) e quando conviene contattarti.",
    [("Portfolio per tipo di servizio", "Matrimoni, famiglie, eventi, aziende: ciascuno con pochi lavori scelti."),
     ("Zone e disponibilità", "Dove lavori, se viaggi, a che condizioni."),
     ("Tempi di consegna", "Quanto serve per ricevere le foto o per organizzare."),
     ("Preventivo", "Data, luogo, tipo di servizio.")],
    "Come lavoriamo con le attività di Novara: " + a('/novara/', 'siti web a Novara') + ". La guida generale è per " + a('/blog/sito-web-agenzia-viaggi-fotografo-wedding-planner/', 'fotografi, wedding planner e agenzie di viaggio') + ".",
    [("Un fotografo di zona ha bisogno di un sito?", "Sì: per confermare il passaparola, farsi trovare su Google e ricevere richieste ordinate."),
     ("Quante foto mostro?", "Poche e scelte: meglio dieci lavori raccontati che cento foto in fila.")],
    [("Il passaparola va confermato online.", "Portfolio e recensioni."), ("Zone e tempi chiari.", "Meno telefonate."), ("Preventivo mirato.", "Data, luogo, tipo.")])
# ------------------------------------------------------------------ artisan
put('artisan', 'vercelli', "filiera agricola e attrezzature su misura",
    "A Vercelli molte aziende artigiane lavorano per l'agricoltura e per la filiera alimentare: carpenteria, attrezzature, impianti, manutenzioni, lavorazioni su misura. Chi cerca queste aziende è un'impresa agricola o un'azienda di trasformazione.",
    "L'acquirente è un tecnico o un titolare che ha un problema specifico: serve un componente, un impianto, una riparazione. Cerca un fornitore vicino, che conosca il settore e risponda presto, e controlla il sito per capire se fai quel tipo di lavoro.",
    "Una pagina per ciascuna lavorazione (carpenteria, lavorazioni su misura, riparazioni, manutenzioni), con materiali, dimensioni, tempi tipici e come chiedere un preventivo con foto o disegno. Per le urgenze (rotture in stagione), spiega come gestisci le chiamate.",
    [("Lavorazioni per aziende agricole", "Cosa fai, con quali materiali e dimensioni."),
     ("Manutenzione e riparazioni", "Interventi in azienda o in officina, tempi e urgenze."),
     ("Preventivo con foto o disegno", "Un modulo che accetta allegati."),
     ("Referenze", "Solo con il consenso delle aziende.")],
    "Per un caso simile sul lato del prodotto vedi la guida " + a('/blog/sito-web-aziende-agroalimentari/', 'aziende agroalimentari') + ".",
    [("Posso citare le aziende per cui lavoro?", "Solo con il loro consenso: molte non vogliono essere citate. Mostra il lavoro senza il nome."),
     ("Serve un catalogo?", "Se hai prodotti standard sì; per i lavori su misura bastano pagine per lavorazione e un modulo per il preventivo.")],
    [("L'acquirente è un tecnico.", "Dati, non slogan."), ("Urgenze di stagione.", "Spiega come le gestisci."), ("Preventivo con allegati.", "Foto o disegno.")])
put('artisan', 'como', "tessile, arredo e committenze di pregio",
    "Il territorio comasco ha una tradizione tessile e produttiva e molte aziende artigiane lavorano per l'arredo, per hotel e ville di pregio. Chi cerca queste aziende cerca qualità, tempi rispettati e capacità di realizzare pezzi su misura.",
    "Un architetto o un designer che cerca un fornitore per un lavoro su misura valuta il portfolio, i materiali, le tolleranze e la capacità di seguire un progetto. Spesso lavora con committenti stranieri o con studi che chiedono documentazione in inglese.",
    "Pagine per lavorazione e materiale, con foto vere e tempi realistici; una pagina sul processo (dal disegno al pezzo finito, con campioni e approvazioni) e un modo di inviare un progetto. Una versione in inglese per i committenti stranieri rende più facile il contatto.",
    [("Lavorazioni e materiali", "Cosa fai, con cosa, a che livello di qualità."),
     ("Processo su misura", "Dal disegno al pezzo finito, con campioni e approvazioni."),
     ("Foto dei lavori", "Veri, con il permesso dei committenti."),
     ("Inglese per studi e committenti", "Servizi e processo in forma essenziale.")],
    "Evita parole generiche come \"eccellenza\" e \"tradizione\": servono dati, materiali e processi.",
    [("Posso citare le ville o gli hotel per cui ho lavorato?", "Solo con il consenso del committente: molti non vogliono comparire."),
     ("Serve il sito in inglese?", "Se lavori con studi o committenti stranieri sì, anche in forma essenziale.")],
    [("Qualità si dimostra con dati.", "Materiali e processi."), ("Su misura: processo chiaro.", "Campioni e approvazioni."), ("Inglese per i committenti stranieri.", "Versione essenziale.")])
put('artisan', 'milano', "studi di design, prototipi e piccole serie",
    "A Milano molte aziende artigiane lavorano per studi di design, brand e architetti che cercano prototipi, piccole serie e lavorazioni su misura. Un'azienda che dice chiaramente cosa sa fare e in che tempi si fa trovare da chi progetta.",
    "Chi progetta cerca un fornitore con cui dialogare: capace di consigliare sui materiali, di realizzare un prototipo e di mantenere la qualità in piccola serie. Guarda foto di lavori, tempi e come si invia un progetto.",
    "Pagine per lavorazioni e materiali, una pagina sui prototipi e le piccole serie (quantità minime, tempi, costi indicativi senza cifre inventate), un modo di inviare un progetto con disegni, e un contatto diretto con un tecnico. Una versione in inglese serve se lavori con brand internazionali.",
    [("Prototipi e piccole serie", "Quantità, tempi, come si avvia un progetto."),
     ("Materiali e consulenza", "Cosa consigli e perché."),
     ("Invio del progetto", "Disegni, specifiche e un referente."),
     ("Foto dei lavori", "Con il consenso dei clienti.")],
    NOTE_RANKING,
    [("Come farmi trovare dagli studi di design?", "Con pagine chiare per lavorazione, foto vere e un modo semplice di inviare un progetto. Le ricerche generiche richiedono tempo."),
     ("Posso scrivere dei prezzi?", "Meglio spiegare cosa influisce sul costo e come si ottiene un preventivo.")],
    [("Chi progetta cerca un interlocutore.", "Un tecnico di riferimento."), ("Prototipo e piccola serie.", "Come si parte."), ("Foto vere.", "Con consenso.")])
put('artisan', 'novara', "fornitori per imprese di zona",
    "A Novara e provincia un'azienda artigiana lavora spesso per altre imprese della zona: carpenteria, lavorazioni, manutenzioni, falegnameria su misura. Chi cerca ha un problema tecnico e vuole un fornitore vicino e rapido.",
    "La prossimità è un vantaggio che il sito deve dire: arrivi presto, puoi visitare l'azienda e vedere il lavoro, rispondi al telefono. Chi cerca vuole conferme tecniche, non slogan.",
    "Pagine per lavorazione con materiali, dimensioni e tempi; una pagina sull'azienda con foto vere dell'officina; un modulo per chiedere un preventivo con disegno o foto; dati dell'azienda e come visitarla. Come lavoriamo con le attività di Novara è nella " + a('/novara/', 'pagina dedicata') + ".",
    [("Lavorazioni e materiali", "Cosa fai, con cosa, a quali dimensioni."),
     ("Visita in azienda", "Come concordarla, dove siete."),
     ("Preventivo con allegati", "Disegno o foto, quantità, tempi desiderati."),
     ("Tempi di risposta", "Chi risponde e in quanto tempo.")],
    "Il quadro generale è nella " + a('/blog/sito-web-aziende-artigiane-manifatturiere/', 'guida per aziende artigiane') + " e nei " + a('/settori/artigianato/', 'siti per artigiani') + ".",
    [("Serve un sito se lavoro per poche aziende?", "Sì: chi deve scegliere un fornitore lo cerca online e controlla il sito prima di chiamare."),
     ("Posso mostrare i lavori fatti per altre aziende?", "Solo con il consenso del cliente: puoi mostrare il prodotto senza il nome.")],
    [("La vicinanza è un vantaggio.", "Dillo."), ("Chi cerca è un tecnico.", "Dati e foto vere."), ("Preventivo con allegati.", "Meno telefonate.")])


def build_articles():
    out = []
    for sector, info in SECTOR.items():
        order = [c for c in CITIES if (sector, c) in D]
        for i, city in enumerate(order):
            if (sector, city) in SKIP:
                continue
            d = D[(sector, city)]
            name = CITY[city]
            slug = 'sito-web-%s-%s' % (info['slug'], city)
            title = 'Sito web per %s a %s: %s' % (info['label'], name, d['angle'])
            desc = 'Guida per %s di %s: %s. Cosa mettere nel sito, scheda Google e cosa evitare.' % (info['label'], name, d['angle'])
            if len(desc) > 158:
                desc = 'Guida per %s di %s: %s.' % (info['label'], name, d['angle'])
            nxt = order[(i + 1) % len(order)]
            sib_slug = 'sito-web-%s-%s' % (info['slug'], nxt)
            c_text = d['C'].replace(NOTE_RANKING, '').strip()
            tk = d['tk']
            sections = [
                ('chi', 'Chi cerca a %s' % name, tk[0][0] + ' ' + tk[0][1], ["<p>%s</p>" % d['A']]),
                ('cosa', 'Cosa mettere nel sito', tk[1][0] + ' ' + tk[1][1], ["<p>%s</p>" % d['B']] + checks(d['checks'])),
                ('extra', 'Da curare a %s' % name, tk[2][0] + ' ' + tk[2][1],
                 ["<p>%s</p>" % c_text,
                  "<p>La scheda Google di %s è il primo punto di contatto: orari, foto vere e recensioni di clienti reali, senza incentivi.</p>" % info['label']]),
            ]
            faq = d['faq'] + [('Quanto costa un sito per questa attività?',
                               "Dipende dal perimetro, non dalla città: fasce e metodo sono nella " + a('/blog/quanto-costa-sito-web-italia-2026/', 'guida ai costi') + ".")]
            related = [
                ('/blog/%s/' % info['guide'], info['gtitle'], 'La guida generale per questo settore.'),
                ('/%s/' % city, 'Siti web a %s' % name, 'Come lavoriamo con le attività di %s.' % name),
                ('/blog/%s/' % sib_slug, 'Lo stesso settore a %s' % CITY[nxt], 'Cosa cambia in un\'altra città.'),
            ]
            x = art(slug, title, desc, 6, 'sito web %s %s, %s %s, %s' % (info['kw'], city, info['kw'], city, info['label']),
                    'sito web %s %s' % (info['kw'], city), d['lead'], [(t, s) for t, s in d['tk']], sections, faq, related,
                    'Parliamo della tua attività a %s' % name, "Raccontaci cosa fai e come ti trovano i clienti oggi: ti rispondiamo con una prima valutazione.",
                    cta_link=('/%s/' % city, 'Siti web a %s' % name))
            out.append(x)
    return out


ARTICLES = build_articles()
bc.ARTICLES = ARTICLES

if __name__ == '__main__':
    bc.main()
