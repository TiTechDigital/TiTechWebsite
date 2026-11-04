# Le due lineette dei due articoli lunghi. Stessa regola del primo intervento:
# virgola, due punti o parentesi a seconda della frase; il trattino che fa da
# segnaposto nei risultati del calcolatore non si tocca.
import io, sys

EM = '\u2014'

IT = 'blog/quanto-costa-sito-web-italia-2026/index.html'
EN = 'en/blog/website-cost-italy-2026/index.html'

EDITS = [
    (IT, 'Tra le voci ricorrenti più comuni %s hosting, dominio, aggiornamenti, backup, monitoraggio e assistenza %s' % (EM, EM),
     'Tra le voci ricorrenti più comuni (hosting, dominio, aggiornamenti, backup, monitoraggio e assistenza)', 2),
    (IT, 'spostano davvero un preventivo %s perimetro, template, contenuti, integrazioni, multilingua %s ma non conosce il tuo progetto' % (EM, EM),
     'spostano davvero un preventivo (perimetro, template, contenuti, integrazioni, multilingua), ma non conosce il tuo progetto', 2),
    (IT, 'ciò che muove %s o nasconde %s un preventivo' % (EM, EM), 'ciò che muove, o nasconde, un preventivo', 1),
    (IT, 'La stessa richiesta %s «un sito nuovo» %s può nascondere' % (EM, EM),
     'La stessa richiesta, «un sito nuovo», può nascondere', 1),
    (IT, 'un\'offerta è fuori scala %s verso il basso o verso l\'alto %s prima di firmarla' % (EM, EM),
     'un\'offerta è fuori scala, verso il basso o verso l\'alto, prima di firmarla', 1),
    (IT, '<h3>Numero di pagine %s e di template</h3>' % EM, '<h3>Numero di pagine e di template</h3>', 1),
    (IT, 'Un\'identità disegnata da zero %s griglia tipografica, componenti, micro-interazioni %s è un lavoro diverso' % (EM, EM),
     'Un\'identità disegnata da zero (griglia tipografica, componenti, micro-interazioni) è un lavoro diverso', 1),
    (IT, 'E ogni collegamento esterno %s CRM, gestionale, pagamenti, newsletter, fatturazione %s ha un costo' % (EM, EM),
     'E ogni collegamento esterno (CRM, gestionale, pagamenti, newsletter, fatturazione) ha un costo', 1),
    (IT, '<p>La base %s struttura URLs, heading, sitemap, dati strutturati, performance %s oggi è mestiere' % (EM, EM),
     '<p>La base (struttura URLs, heading, sitemap, dati strutturati, performance) oggi è mestiere', 1),
    (IT, 'Se li scrive l\'agenzia si pagano %s in genere tra 80 e 200 € a pagina per i testi %s se li fornisci tu' % (EM, EM),
     'Se li scrive l\'agenzia si pagano, in genere tra 80 e 200 € a pagina per i testi; se li fornisci tu', 1),
    (IT, 'un progetto semplice e uno molto articolato %s la colonna a destra ti dice di quanto' % EM,
     'un progetto semplice e uno molto articolato: la colonna a destra ti dice di quanto', 1),
    (IT, 'le fasce si sovrappongono di proposito %s un sito aziendale ricco' % EM,
     'le fasce si sovrappongono di proposito: un sito aziendale ricco', 1),
    (IT, 'La stima è un ordine di grandezza %s considerala affidabile entro il 30%% %s non un preventivo' % (EM, EM),
     'La stima è un ordine di grandezza, considerala affidabile entro il 30%, non un preventivo', 1),
    (IT, 'in fase di analisi, spostano il numero %s di solito più di tutte' % EM,
     'in fase di analisi, spostano il numero, di solito più di tutte', 1),
    (IT, 'Quello che un sito professionale fa %s e i numeri qui sotto lo mostrano in forma illustrativa %s è rendere' % (EM, EM),
     'Quello che un sito professionale fa, e i numeri qui sotto lo mostrano in forma illustrativa, è rendere', 1),
    (IT, 'Osteria Verde %s ristorante</h3>' % EM, 'Osteria Verde, ristorante</h3>', 1),
    (IT, '<caption>Osteria Verde %s prima e dopo' % EM, '<caption>Osteria Verde, prima e dopo', 1),
    (IT, 'Artigiano Casa %s laboratorio artigiano</h3>' % EM, 'Artigiano Casa, laboratorio artigiano</h3>', 1),
    (IT, '<caption>Artigiano Casa %s prima e dopo' % EM, '<caption>Artigiano Casa, prima e dopo', 1),
    (IT, 'misura, spazio e scadenza %s così la richiesta che arriva' % EM,
     'misura, spazio e scadenza: così la richiesta che arriva', 1),
    (IT, 'Studio Nova %s servizi professionali</h3>' % EM, 'Studio Nova, servizi professionali</h3>', 1),
    (IT, '<caption>Studio Nova %s prima e dopo' % EM, '<caption>Studio Nova, prima e dopo', 1),
    (IT, 'filtrano il traffico %s arrivano richieste più pertinenti, non solo più numerose %s ed è per questo' % (EM, EM),
     'filtrano il traffico: arrivano richieste più pertinenti, non solo più numerose, ed è per questo', 1),
    (IT, 'richieste mensili prima e dopo %s Osteria Verde' % EM, 'richieste mensili prima e dopo: Osteria Verde', 1),
    (IT, 'punteggio PageSpeed mobile prima e dopo %s Osteria Verde' % EM,
     'punteggio PageSpeed mobile prima e dopo: Osteria Verde', 1),
    (IT, 'misura prestazionale %s non una classifica' % EM, 'misura prestazionale, non una classifica', 1),
    (IT, 'conversion rate prima e dopo %s Osteria Verde' % EM, 'conversion rate prima e dopo: Osteria Verde', 1),
    (IT, 'click organici mensili prima e dopo %s Osteria Verde' % EM, 'click organici mensili prima e dopo: Osteria Verde', 1),
    (IT, 'settore ristorazione %s ruolo inventato' % EM, 'settore ristorazione, ruolo inventato', 1),
    (IT, 'laboratorio artigiano %s ruolo inventato' % EM, 'laboratorio artigiano, ruolo inventato', 1),
    (IT, 'studio professionale %s ruolo inventato' % EM, 'studio professionale, ruolo inventato', 1),
    (IT, 'Esempio di testimonianza %s testo dimostrativo' % EM, 'Esempio di testimonianza: testo dimostrativo', 3),
    (IT, 'quanto costa esportare il sito %s il vero margine' % EM, 'quanto costa esportare il sito: il vero margine', 1),
    (IT, '<strong>Prepara i contenuti prima</strong> %s testi, foto' % EM,
     '<strong>Prepara i contenuti prima</strong>: testi, foto', 1),
    (IT, '<strong>Riduci i template, non per forza le pagine</strong> %s riusare' % EM,
     '<strong>Riduci i template, non per forza le pagine</strong>: riusare', 1),
    (IT, '<strong>Parti da un MVP</strong> %s metti online' % EM, '<strong>Parti da un MVP</strong>: metti online', 1),
    (IT, '<strong>Nomina un decisore unico</strong> %s le decisioni' % EM,
     '<strong>Nomina un decisore unico</strong>: le decisioni', 1),
    (IT, '<strong>Non cambiare perimetro a metà</strong> %s ogni aggiunta' % EM,
     '<strong>Non cambiare perimetro a metà</strong>: ogni aggiunta', 1),
    (IT, 'se quel lavoro serve davvero %s e quella domanda va fatta' % EM,
     'se quel lavoro serve davvero, e quella domanda va fatta', 1),
    (IT, 'quanto tempo richiede %s con una forbice di costo onesta' % EM,
     'quanto tempo richiede, con una forbice di costo onesta', 1),

    (EN, 'Counting the most common recurring items %s hosting, domain, updates, backups, monitoring and support %s' % (EM, EM),
     'Counting the most common recurring items (hosting, domain, updates, backups, monitoring and support)', 2),
    (EN, 'genuinely move a quote %s scope, templates, content, integrations, multilingual %s but it does not know your project' % (EM, EM),
     'genuinely move a quote (scope, templates, content, integrations, multilingual), but it does not know your project', 2),
    (EN, 'what moves %s or hides %s a quote' % (EM, EM), 'what moves, or hides, a quote', 1),
    (EN, 'The same request %s "a new website" %s can hide' % (EM, EM),
     'The same request ("a new website") can hide', 1),
    (EN, 'recurring costs %s all VAT excluded, all labelled as estimates' % EM,
     'recurring costs, all VAT excluded, all labelled as estimates', 1),
    (EN, 'an offer is off scale %s downward or upward %s before signing it' % (EM, EM),
     'an offer is off scale, downward or upward, before signing it', 1),
    (EN, '<h3>Number of pages %s and of templates</h3>' % EM, '<h3>Number of pages and of templates</h3>', 1),
    (EN, 'An identity drawn from scratch %s type grid, components, micro-interactions %s is a different job' % (EM, EM),
     'An identity drawn from scratch (type grid, components, micro-interactions) is a different job', 1),
    (EN, 'every external connection %s CRM, ERP, payments, newsletter, invoicing %s carries analysis' % (EM, EM),
     'every external connection (CRM, ERP, payments, newsletter, invoicing) carries analysis', 1),
    (EN, '<p>The basics %s URL structure, headings, sitemap, structured data, performance %s are craft today' % (EM, EM),
     '<p>The basics (URL structure, headings, sitemap, structured data, performance) are craft today', 1),
    (EN, 'If the agency writes them you pay %s typically between 80 and 200 € per page for copy %s if you supply them' % (EM, EM),
     'If the agency writes them you pay, typically between 80 and 200 € per page for copy; if you supply them', 1),
    (EN, 'a simple project and a very intricate one %s the right-hand column tells you by how much' % EM,
     'a simple project and a very intricate one: the right-hand column tells you by how much', 1),
    (EN, 'the ranges overlap on purpose %s a rich business site' % EM,
     'the ranges overlap on purpose: a rich business site', 1),
    (EN, 'The estimate is an order of magnitude %s treat it as reliable within 30%% %s not a quote' % (EM, EM),
     'The estimate is an order of magnitude, treat it as reliable within 30%, not a quote', 1),
    (EN, 'in discovery, move the number %s usually more than everything' % EM,
     'in discovery, move the number, usually more than everything', 1),
    (EN, 'What a professional website does %s and the numbers below show this in illustrative form %s is make' % (EM, EM),
     'What a professional website does, and the numbers below show this in illustrative form, is make', 1),
    (EN, 'Osteria Verde %s restaurant</h3>' % EM, 'Osteria Verde, restaurant</h3>', 1),
    (EN, '<caption>Osteria Verde %s before and after' % EM, '<caption>Osteria Verde, before and after', 1),
    (EN, 'not all reservations %s some are "are you open tonight?" %s and those count too' % (EM, EM),
     'not all reservations: some are "are you open tonight?", and those count too', 1),
    (EN, 'Artigiano Casa %s artisan workshop</h3>' % EM, 'Artigiano Casa, artisan workshop</h3>', 1),
    (EN, '<caption>Artigiano Casa %s before and after' % EM, '<caption>Artigiano Casa, before and after', 1),
    (EN, 'space and deadline %s so the enquiry that arrives' % EM, 'space and deadline, so the enquiry that arrives', 1),
    (EN, 'Studio Nova %s professional services</h3>' % EM, 'Studio Nova, professional services</h3>', 1),
    (EN, '<caption>Studio Nova %s before and after' % EM, '<caption>Studio Nova, before and after', 1),
    (EN, 'filter the traffic %s enquiries arrive more relevant, not merely more numerous %s which is why' % (EM, EM),
     'filter the traffic: enquiries arrive more relevant, not merely more numerous, which is why', 1),
    (EN, 'monthly enquiries before and after %s Osteria Verde' % EM, 'monthly enquiries before and after: Osteria Verde', 1),
    (EN, 'mobile PageSpeed score before and after %s Osteria Verde' % EM,
     'mobile PageSpeed score before and after: Osteria Verde', 1),
    (EN, 'performance scale %s not a ranking' % EM, 'performance scale, not a ranking', 1),
    (EN, 'conversion rate before and after %s Osteria Verde' % EM, 'conversion rate before and after: Osteria Verde', 1),
    (EN, 'monthly organic clicks before and after %s Osteria Verde' % EM,
     'monthly organic clicks before and after: Osteria Verde', 1),
    (EN, 'restaurant sector %s invented role' % EM, 'restaurant sector, invented role', 1),
    (EN, 'artisan workshop %s invented role' % EM, 'artisan workshop, invented role', 1),
    (EN, 'professional practice %s invented role' % EM, 'professional practice, invented role', 1),
    # la riga sotto era rimasta in italiano nella pagina inglese
    (EN, '<p class="quote__demo">Esempio di testimonianza %s testo dimostrativo, non dichiarazione di un cliente reale.</p>' % EM,
     '<p class="quote__demo">Testimonial example: demonstration text, not a statement from a real client.</p>', 3),
    (EN, 'ask what an export costs %s the real margin' % EM, 'ask what an export costs: the real margin', 1),
    (EN, '<strong>Prepare the content first</strong> %s texts, photos' % EM,
     '<strong>Prepare the content first</strong>: texts, photos', 1),
    (EN, '<strong>Cut templates, not necessarily pages</strong> %s reusing' % EM,
     '<strong>Cut templates, not necessarily pages</strong>: reusing', 1),
    (EN, '<strong>Start from an MVP</strong> %s ship what is needed' % EM,
     '<strong>Start from an MVP</strong>: ship what is needed', 1),
    (EN, '<strong>Name a single decision-maker</strong> %s decisions taken' % EM,
     '<strong>Name a single decision-maker</strong>: decisions taken', 1),
    (EN, '<strong>Do not change scope mid-project</strong> %s every addition' % EM,
     '<strong>Do not change scope mid-project</strong>: every addition', 1),
    (EN, 'whether that work is genuinely needed %s and asking yourself' % EM,
     'whether that work is genuinely needed, and asking yourself', 1),
    (EN, 'what can wait and how long it takes %s with an honest cost range' % EM,
     'what can wait and how long it takes, with an honest cost range', 1),
]

fail = 0
byfile = {}
for path, old, new, want in EDITS:
    byfile.setdefault(path, []).append((old, new, want))
for path, items in byfile.items():
    text = io.open(path, encoding='utf-8', newline='').read()
    for old, new, want in items:
        got = text.count(old)
        if got != want:
            print('MISS %-52s count=%d want=%d  %s' % (path, got, want, old[:56]))
            fail += 1
            continue
        text = text.replace(old, new)
    io.open(path, 'w', encoding='utf-8', newline='').write(text)
    print('written %-52s remaining em: %d' % (path, text.count(EM)))
print('failures:', fail)
sys.exit(1 if fail else 0)
