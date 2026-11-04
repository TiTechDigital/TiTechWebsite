# TiTech Digital: Sito web

Sito bilingue in italiano e inglese per **TiTech Digital**, partner tecnologico per imprese. Il progetto parte dal template design studio di 8B e ne conserva layout, sistema visivo, tipografia e animazioni: il contenuto è stato riscritto per raccontare posizionamento, servizi e metodo di TiTech Digital.

Alla home si affianca un albero di **pagine interne**, in italiano (`/servizi/`, `/settori/`, `/lavori/`, `/come-lavoriamo/`, `/chi-siamo/`, `/contatti/`, `/privacy/`, `/cookie/`) e nella sua versione inglese (`/en/...`), costruito per intercettare le ricerche commerciali che una one-page non può coprire. A questo si aggiunge il **blog**, con un hub e quattro articoli per lingua. Vedi [Pagine interne](#pagine-interne) e [Il blog](#il-blog).

## Contenuto

La pagina copre:

- **Siti web ed e-commerce**: sviluppo su misura, prestazioni, accessibilità e gestione.
- **Design e identità digitale**: brand identity, UI/UX, design di prodotto e direzione creativa.
- **Software e automazione**: web app, dashboard, API, integrazioni, AI e automazione.
- **SEO e crescita digitale**: SEO tecnica, performance, contenuti e CRO.
- **Supporto continuo**: manutenzione, hosting, assistenza e partnership nel tempo.

Il posizionamento è quello di un partner serio e concreto: competenza tecnica, scelte motivate, attenzione alla qualità e continuità dopo il lancio. La sede è in Italia, con un orizzonte internazionale e un'attenzione particolare al mercato albanese.

## Struttura della pagina

1. Hero con immagine rotonda e parola di apertura.
2. Statement in due righe.
3. Cinque card di servizio su binario orizzontale (siti ed e-commerce, design, software, SEO, supporto).
4. Sei card della ruota dei principi.
5. Metodo in quattro fasi con anello animato.
6. Collage dello studio con competenze integrate.
7. I nostri lavori, con una sequenza a storia: una card per progetto, avanti con lo scroll.
8. Sei domande frequenti in `<details>`.
9. Contatti con modulo.
10. Footer con saluto, link, email, dati legali e credito Design e sito web: titechdigital.it.

Le animazioni GSAP/ScrollTrigger e lo smooth scrolling Lenis sono quelli originali del template. La sezione lavori segue lo stesso schema delle altre scene: sezione alta `100svh + var(--run)`, stage `position: sticky` e timeline agganciata allo scroll con `scrollTrigger: { scrub: true }`. Con `prefers-reduced-motion` attivo la pagina resta completa e statica e i lavori tornano una griglia.

## Pagine interne

La home presenta l'azienda; sotto di essa ci sono **due alberi paralleli**, uno italiano e uno inglese, con lo stesso numero di pagine e di sezioni. Ogni albero è costruito **una pagina per intento di ricerca**, senza duplicati per città.

| URL | Gemella inglese | Intento di ricerca | Ruolo |
| --- | --- | --- | --- |
| `/servizi/` | `/en/services/` | «servizi web agency» | hub, distribuisce i link ai servizi |
| `/servizi/siti-web/` | `/en/services/website-design/` | «realizzazione siti web», «sito web aziendale» | pagina commerciale principale |
| `/servizi/e-commerce/` | `/en/services/ecommerce/` | «creare e-commerce», «negozio online» | ticket più alto |
| `/servizi/software-su-misura/` | `/en/services/custom-software/` | «software gestionale su misura» | margine alto, concorrenza bassa |
| `/servizi/automazioni-ai/` | `/en/services/ai-automation/` | «automazione processi aziendali AI» | query in crescita, offerta scarsa |
| `/servizi/seo/` | `/en/services/seo/` | «consulenza SEO» | dimostra la competenza |
| `/settori/` | `/en/industries/` | «sito web per settore» | hub dei tre settori |
| `/settori/artigianato/` | `/en/industries/craft-manufacturing/` | «sito web per artigiani» | long-tail difendibile |
| `/settori/ristorazione/` | `/en/industries/restaurants/` | «sito web per ristoranti» | long-tail difendibile |
| `/settori/professionisti/` | `/en/industries/professional-services/` | «sito web per professionisti» | long-tail difendibile |
| `/lavori/` | `/en/work/` | «case study», brand + settore | asset di conversione |
| `/come-lavoriamo/` | `/en/how-we-work/` | «come lavoriamo», «fasi di un progetto» | processo chiaro = fiducia, poi contatto |
| `/chi-siamo/` | `/en/about/` | brand, E-E-A-T | fiducia prima del contatto |
| `/contatti/` | `/en/contact/` | «web agency» + area servita | pagina di conversione |
| `/privacy/`, `/cookie/` | `/en/privacy/`, `/en/cookies/` | — | conformità GDPR |
| `/blog/` | `/en/blog/` | «blog siti web», «costi sito web» | hub editoriale, distribuisce i quattro articoli |
| `/blog/quanto-costa-sito-web-italia-2026/` | `/en/blog/website-cost-italy-2026/` | «quanto costa un sito web» | metodo del preventivo, senza pubblicare cifre |
| `/blog/e-commerce-b2b-quando-conviene/` | `/en/blog/b2b-ecommerce-when-it-pays-off/` | «e-commerce B2B» | decisione e modello operativo |
| `/blog/automazione-ai-pmi-5-processi/` | `/en/blog/ai-automation-smes-5-processes/` | «automazione AI PMI» | cinque processi e pilota misurabile |
| `/blog/shopify-vs-sito-su-misura/` | `/en/blog/shopify-vs-custom-website/` | «Shopify o sito su misura» | confronto per costo totale e controllo |
| `404.html` | — | risposta per URL inesistenti (Vercel la serve da sola) | bilingue per necessità: un solo file risponde a `/...` e a `/en/...` |

Regole rispettate nell'albero:

- **Una pagina per intento.** Nessuna pagina «servizio + città»: i cloni locali sono doorway page, Google li ignora. Il lavoro locale si fa con la scheda Google Business Profile e con la pagina contatti.
- **Italiano come lingua principale, inglese come specchio.** L'italiano è la versione predefinita e `x-default`; l'inglese riproduce pagina per pagina la stessa struttura. Gli slug inglesi **non** ricalcano quelli italiani (`/servizi/siti-web/` → `/en/services/website-design/`): un indirizzo in lingua si legge meglio di una traduzione letterale, e la scelta è definitiva perché una URL indicizzata conviene non moverla più.
- **Percorsi assoluti.** Dentro le pagine interne le risorse si richiamano da `/assets/...`, così la stessa riga funziona a qualsiasi profondità.
- **Nessun prezzo pubblicato.** Il sito non espone tariffe né fasce di prezzo: il preventivo si comunica solo dopo la prima conversazione. Le pagine servizio descrivono cosa determina il lavoro, non quanto costa.

### Il blog

Il blog è un albero editoriale, non una raccolta di pagine servizio travestite. Parte con quattro coppie di articoli: costo di un sito, e-commerce B2B, automazione AI per PMI e Shopify contro sito su misura. Ogni pezzo parte da una domanda, dichiara una tesi e lascia al lettore una decisione.

Il pezzo sui costi è deliberatamente un metodo, non un listino: spiega perché non pubblichiamo cifre e come si costruisce un preventivo. Nessun articolo promette posizioni su Google, inventa casi o usa screenshot finti. Il componente `.figure` è pronto per le immagini reali, che si aggiungono solo quando esistono; fino ad allora le pagine restano testuali.

Ogni articolo ha firma e data visibili, nodi `BlogPosting` e `WebPage` nel JSON-LD, un indice `.toc` con ancore, il box `.takeaways` e categoria e tempo di lettura in `.card__meta`. L'hub `/blog/` presenta gli articoli in `.cards--posts` (due colonne da 760px in su) e dichiara la lista in un `ItemList`; i post correlati usano `.cards`.

### Come è fatta una pagina interna

Le pagine interne sono documenti di lettura e condividono tre file. Il motore di animazione gira con le stesse librerie della home, ma su pochi gesti: l'intestazione sale in rivelazione mascherata, le righe di `.tiles` e `.steps` disegnano un filo blu una alla volta, le immagini di `.cards` entrano da una tendina. Il testo di lettura, le tabelle, i moduli e le FAQ non si animano mai, ed è una scelta: chi arriva da una ricerca vuole leggere, non aspettare. Ogni tween nasce dentro un `onEnter`, quindi se il ticker si blocca il contenuto resta visibile.

- `assets/css/pages.css`: font (subset latino), token della home, tipografia, componenti e barra di navigazione. Non contiene CSS specifico di una pagina.
- `assets/js/pages.js`: apertura del menu mobile, anno corrente del footer e composizione del modulo di contatto. Circa quaranta righe, nessuna dipendenza.
- `assets/js/motion.js`: animazioni, caricate con `defer`: aggiungono `html.motion` solo a librerie caricate, così senza JS la pagina resta completa e statica.

Componenti disponibili: `.crumbs` (breadcrumb), `.head` (testata), `.byline` (firma con autore e data), `.sect` e `.sect__top` (sezione), `.prose` (testo lungo), `.tiles` (indice numerato, una riga per voce), `.cards` (progetti e post, con `.card__meta` per categoria e tempo di lettura), `.cards--posts` (hub del blog, due colonne da 760px), `.takeaways` (punti chiave), `.toc` (indice con ancore), `.figure` (immagine reale con didascalia), `.checks` (distinta a due colonne), `.steps` (fasi numerate), `.facts` (tre numeri verificabili), `.cases` (casi come righe, non riquadri), `.table` con `.table-wrap` (tabella dati, mai listini), `.faq` (`<details>` con `+`/`–`), `.cards` (progetti), `.form` (modulo), `.note` (avvertenza), `.cta` (chiamata finale, a tutta larghezza), `.footer` (footer identico alla home), `.lost` (404).

### Il template di pagina servizio

Le cinque pagine `/servizi/...` seguono tutte la stessa sequenza. È l'ordine in cui un cliente decide, non un ordine decorativo:

1. **`h1` con la query, in italiano semplice**: «Realizzazione di siti web per aziende», non uno slogan. Il posizionamento emotivo sta nel `head__lead`, che è la promessa in una riga.
2. **Firma** (`.byline`): nome, ruolo e data di aggiornamento visibili, agganciata al nodo `Person` con `@id` `#enea-muja`. Un autore inventato vale meno di nessun autore: se cambia la persona, si aggiornano insieme il testo visibile e il `jobTitle` nei dati strutturati.
3. **Prova** (`.facts` + `.cases`): tre impegni verificabili del progetto (tempi, giorni per il preventivo, assistenza inclusa) e due casi che rimandano a `/lavori/#caso-...`. Niente loghi di clienti e niente metriche: non esistono ancora, e inventarle è il modo più rapido per perdere la fiducia di chi legge.
4. **Cosa comprende**, **come si svolge**, poi le **domande frequenti**.
5. **Rimandi** (`.tiles`) verso due servizi vicini e un settore.
6. **CTA**.

Sui prezzi vale una regola sola: **non se ne pubblicano**. Il posto dove il visitatore se lo aspetta è occupato da una FAQ sul costo che spiega da cosa dipende e rimanda alla prima conversazione. Le fasce in euro sono state rimosse apposta: un numero pubblicato invita al confronto con il preventivo del concorrente, mentre la conversazione è l'unico posto in cui il numero ha un contesto.

Ogni pagina di entrambi gli alberi dichiara il trio di alternati: `hreflang="it-IT"` sulla gemella italiana, `hreflang="en"` su sé stessa, `hreflang="x-default"` sulla gemella italiana, con la `canonical` sulla pagina che si sta leggendo. Il rimando deve essere **reciproco**: un alternato che punta a una pagina inesistente, o che non viene ricambiato, è un segnale rotto. L'unica eccezione è `404.html`, che ha `noindex, follow` e quindi non partecipa all'indicizzazione. Le pagine istituzionali e legali ripetono i nodi `Organization` (`#organization`) e, dove serve, `Person` (`#enea-muja`) con `@id` assoluti radicati sulla versione italiana: due lingue, un solo soggetto giuridico.

Le date nei casi di studio si aggiungono quando i progetti saranno reali. Fino a quel momento la nota «Progetti dimostrativi» resta visibile sopra le immagini: datare un lavoro mai fatto è il contrario di un segnale di esperienza.

### Aggiungere una pagina

1. Creare `<cartella>/index.html` (lo slash finale è garantito da `trailingSlash: true` in `vercel.json`).
2. Copiare l'intestazione di una pagina esistente e cambiare `title`, `description`, `canonical`, `og:url` e `og:title`/`og:description`: restano poche righe da modificare e il resto (favicon, font, CSS, Open Graph) è già corretto. L'immagine Open Graph segue la lingua: `og-card-it-1200x630.png` sull'italiano, `og-card-en-1200x630.png` sull'inglese, con `og:locale` `it_IT` e `en_US` rispettivamente.
3. Aggiornare il blocco JSON-LD: la `BreadcrumbList` deve essere contigua e coerente con i `.crumbs` visibili; il nodo specifico è `Service` per una pagina servizio, `CollectionPage` per un hub, `AboutPage` o `ContactPage` per le pagine istituzionali. Ogni pagina ripete i nodi `Organization` (`#organization`) e `Person` (`#enea-muja`), e il nodo `WebPage` lega autore, breadcrumb e servizio con `@id` assoluti: senza quei nodi i riferimenti restano appesi. Nella pagina inglese i nodi condivisi si **referenziano** con `@id` assoluti sulla versione italiana invece di ripeterli: le due lingue descrivono la stessa entità.
4. Impostare `aria-current` sulla voce di navigazione pertinente: `page` quando il link porta alla pagina stessa (vedi `/contatti/`), `true` quando la pagina è figlia di una sezione e il link porta alla sezione (vedi `/servizi/seo/`, che non è `/servizi/`). I due valori sono stilati allo stesso modo da `pages.css`.
5. Creare la gemella inglese. **Non è una traduzione riga per riga**: è una riscrittura nativa, che però mantiene lo stesso numero di sezioni, gli stessi componenti (`.facts`, `.checks`, `.tiles`, `.steps`, `.faq`, `.table`...) e gli stessi tipi di nodo JSON-LD. Una pagina inglese che perde un blocco racconta un lavoro diverso da quello italiano.
6. Aggiungere il trio `hreflang` **su entrambe le pagine**, reciproco. Se si inserisce solo da una parte, il segnale è mezzo e il validatore lo segnala.
7. Aggiungere entrambe le URL a `sitemap.xml` con la data di pubblicazione e i relativi `<xhtml:link>`: gli alternati in sitemap devono coincidere con quelli dichiarati nelle pagine.

### Aggiungere un articolo

1. Creare la coppia di URL, una italiana e una inglese, con lo stesso numero di sezioni e gli stessi componenti. Il titolo può differire, la struttura no.
2. Nel JSON-LD usare `BlogPosting` per l'articolo e `WebPage` per la pagina, con `datePublished` e `dateModified` in formato ISO, autore `#enea-muja` e `isPartOf` il nodo `Blog` dell'hub. La `BreadcrumbList` diventa Home → Blog → articolo.
3. Mantenere visibili firma, data e tempo di lettura. Aggiungere categoria e tempo anche in `.card__meta` dell'hub.
4. Aggiornare l'hub in entrambe le lingue: card dell'articolo, `ItemList` nel JSON-LD e conteggio negli eventuali `.facts`. Un articolo che non compare nell'hub è un vicolo cieco.
5. Rigenerare `sitemap.xml` con `python tools/build_sitemap.py` e rilanciare `python tools/check_site.py`.

## Lingue

La versione italiana è quella predefinita, l'inglese ne è lo specchio completo:

- `/` + ventuno pagine interne, in italiano
- `/en/` + ventuno pagine interne, in inglese

Il pulsante `EN` nella barra di navigazione porta alla versione inglese nella stessa pagina (`/servizi/seo/` ↔ `/en/services/seo/`), non alla home: chi sta leggendo una scheda tecnica in italiano la ritrova equivalente, non un punto di partenza diverso. Su mobile lo stesso cambio è disponibile come `English` / `Italiano` nel menu.

Una visita inglese non attraversa mai una pagina italiana: home, navigation, menu, footer e modulo di contatto della versione `/en/` rimandano solo dentro `/en/`. Le uniche uscite verso l'italiano sono il pulsante `IT` e, su `404.html`, i due blocchi di link marcati `lang`.

Le due home condividono struttura, animazioni e attributi `data-8b-*`; cambiano testi, metadati e percorsi delle risorse (`../assets/` nella home inglese, che resta un documento autonomo con il CSS inline). Le pagine interne di entrambe le lingue usano percorsi assoluti `/assets/...` e sono lo stesso tipo di documento a due profondità diverse. Non è presente un selettore automatico basato sulla lingua del browser: la scelta resta manuale.

## URL canonici, robots e sitemap

Il dominio di riferimento è **`https://titechdigital.it`**, pubblicato su **Vercel**. Ogni pagina pubblicata esiste nelle due lingue, per un totale di **quarantaquattro URL**:

- `https://titechdigital.it/...`: italiano, `canonical` su sé stessa, `hreflang` `it-IT` e `x-default`
- `https://titechdigital.it/en/...`: inglese, `canonical` su sé stessa, `hreflang` `en`

Il nome file `index.html` non compare mai nelle URL canoniche. Il pulsante `EN`/`IT` non riporta alla home dell'altra lingua ma alla **pagina equivalente**: chi cambia lingua resta sullo stesso argomento (`/servizi/seo/` ↔ `/en/services/seo/`).

- `robots.txt`: consente la scansione completa, esclude la copia del template (`index.original.html`) e indica la posizione della sitemap.
- `sitemap.xml`: contiene le quarantaquattro URL pubblicate, ognuna con i tre `<xhtml:link>` `hreflang` della propria coppia. Gli alternati in sitemap devono coincidere con quelli dichiarati nelle pagine: quando si aggiunge una pagina, si aggiornano entrambi i posti.
- `vercel.json`: configurazione dell'hosting: `trailingSlash: true` mantiene lo slash finale (`/en/services/seo/`) coerente con `canonical` e sitemap; due redirect **301** portano `/index.html` su `/` e `/en/index.html` su `/en/`; gli header impostano la cache degli asset e tre opzioni di sicurezza. Il redirect `www` → apex e il certificato HTTPS si gestiscono in Vercel (Project → Settings → Domains), non nel file.
- `.vercelignore`: esclude dal deploy la copia del template, i due file di servizio (`og-card.html`, `brand-logo.html`), la documentazione e i file di lavorazione (`_*`), che restano nel repository ma non vengono pubblicati.

I redirect valgono solo su Vercel: l'anteprima con `python -m http.server` li ignora e serve `/` e `/en/` leggendo i rispettivi `index.html`. Dopo il deploy verificare con `curl -I https://titechdigital.it/index.html`: deve rispondere `301` verso `/`.

## Controlli

In `tools/` ci sono sette script che non fanno parte del sito (esclusi da `.vercelignore`) ma ne tengono in piedi le regole.

| Script | Cosa fa |
| --- | --- |
| `check_site.py` | audita tutti i documenti: tag chiusi, `id` duplicati, link e ancore morte, JSON-LD che non si interpreta o descrive un'altra pagina, `canonical`/`og:url` incoerenti, `hreflang` non reciproci, parità dei componenti fra le due lingue, parità del numero di sezioni, titoli, voci di FAQ e righe di tabella, `aria-current` sulla pagina sbagliata o presente in numero diverso dalla gemella, interruttori di lingua che atterrano sulla home invece che sulla gemella, coerenza con `sitemap.xml`, parole italiane nei testi inglesi **e** negli attributi che uno screen reader legge (`alt`, `aria-label`, `placeholder`, messaggi del modulo), simbolo dell'euro in qualsiasi forma (carattere e entità). Esce con il numero dei problemi. |
| `selftest.py` | pianta nove difetti noti su due pagine e ne verifica un decimo a parte, poi controlla che `check_site.py` li veda tutti: un validatore che dice sempre «ok» non vale nulla. Servono due pagine perché un difetto ne nasconde un altro: togliere il trio `hreflang` ferma il confronto con la gemella prima che guardi la parità. |
| `set_hreflang.py` | aggiunge il trio `hreflang` alle pagine italiane leggendo le coppie dagli specchi inglesi (non da una tabella a mano) e punta il loro pulsante `EN` sulla gemella. Ripetibile: chi è già a posto viene lasciato stare. |
| `build_sitemap.py` | rigenera `sitemap.xml` con una voce per pagina e i tre `<xhtml:link>` di ciascuna coppia. Conserva l'ordine già presente e accoda le pagine italiane nuove, blog compreso, invece di scartarle; segnala quelle senza gemella inglese. |
| `check_keywords.py` | verifica `docs/keywords.csv`: venti righe, nessun duplicato, ogni URL esistente, presente in `sitemap.xml` e nella lingua dichiarata. |
| `gsc_review.py` | legge gli export CSV di Search Console (intestazioni italiane o inglesi) e propone cosa correggere: pagine senza impression, CTR sotto la fascia della posizione, query con CTR basso, query servite da più URL, pagine senza clic. |
| `set_ga4.py` | accende o spegne l'ID GA4 in `<meta name="ga4-id">` su tutte le pagine pubblicate; `--check` mostra i valori presenti, `--off` li azzera. |

Dopo una modifica, l'ordine utile è: `python tools/check_site.py`, e se si sono toccati lingue o URL anche `python tools/set_hreflang.py` e `python tools/build_sitemap.py`. Se cambiano le keyword, `python tools/check_keywords.py`.

## Anteprima locale

Dalla cartella del progetto:

```bash
python -m http.server 8080 --bind 127.0.0.1
```

Poi aprire `http://127.0.0.1:8080/` (italiano) oppure `http://127.0.0.1:8080/en/` (inglese).

Non serve alcun build step. La home e la pagina inglese sono un singolo `index.html` con CSS e JavaScript inline; le pagine interne sono un `index.html` per cartella che carica `assets/css/pages.css` e `assets/js/pages.js`. Le risorse esterne (font, GSAP, Lenis, immagini) sono condivise.

## Modulo di contatto

Non è configurato un backend. I moduli sono quattro, due per lingua: uno nella sezione `#contact` di ciascuna home e uno nella pagina contatti (`/contatti/` e `/en/contact/`), tutti con lo stesso comportamento:

1. valida nome, email e descrizione;
2. compone una richiesta con nome, email, azienda, area di interesse e messaggio;
3. apre il programma di posta dell'utente tramite `mailto:` verso `info@titechdigital.it`.

I moduli delle pagine interne sono gestiti da `assets/js/pages.js` (`[data-mailto-form]`) e non inviano nulla a un server: nessun dato personale transita da un intermediario. I messaggi letti dall'utente (oggetto, errori, conferma) stanno negli attributi `data-msg-*` e `data-mail-label` del markup, quindi ogni pagina porta la propria lingua senza che lo script conosca il sito. Se in futuro si vuole un invio vero (Formspree, un endpoint proprio), va sostituito quel blocco e aggiunta la stessa logica di validazione lato server, oltre all'informativa aggiornata.

L'indirizzo `info@titechdigital.it` è un **segnaposto**: va sostituito con l'indirizzo reale prima della pubblicazione. Per usare un servizio di invio (Formspree, Netlify Forms o un endpoint proprio) basta modificare lo script `section-script:contact` e il markup del form.

## Personalizzazione

- **Testi**: la home è in `index.html` (italiano) e `en/index.html` (inglese); le pagine interne sono in `<cartella>/index.html` per l'italiano e `<cartella>/index.html` sotto `en/` per l'inglese. Quando si modifica una pagina, aggiornare anche la gemella: stesso numero di sezioni e stessi componenti, o `tools/check_site.py` lo segnala.
- **Email**: cercare `info@titechdigital.it` e sostituirla in contatti, footer e script.
- **Logo e favicon**: il simbolo è in `assets/img/logo.svg`; la versione per la scheda del browser è in `assets/img/favicon.svg`. La navbar usa il simbolo accanto al nome TiTech, mentre il menu mobile lo ripete in alto.
- **Dati legali**: copyright, P. IVA e crediti sono nella riga finale del footer, presente in entrambe le pagine. Aggiornarli insieme se cambiano.
- **Immagini**: i WebP ottimizzati sono in `assets/img` e referenziati da entrambe le pagine; le attribuzioni sono in [CREDITS.md](CREDITS.md). Le foto sono illustrative e non rappresentano clienti o progetti reali.
- **Progetti dimostrativi**: la sezione `#lavori` contiene sei casi fittizi (nomi, testi e immagini di esempio) con una nota visibile in fondo alla sezione. Sostituire le card `<li class="project">` dentro `.story__stack` con i progetti reali, aggiornare il contatore `Solo alcuni dei nostri lavori · 2023–2026` e rimuovere la nota `lavori__note` prima della pubblicazione. La riga di contesto e l'apertura della sezione dichiarano che si tratta di una parte dei lavori svolti dal 2023 al 2026: allineare anni e conteggi ai casi reali e aggiornare i badge `.project__year` di ogni card. Il numero di card può cambiare: `scene:lavori` conta le card e calcola da solo durata dello scroll (`--run`) incroci e riempimento delle barre, ma le barre di avanzamento `.story__fill` vanno aggiunte o tolte a mano per restare una per progetto. Sopra le barre resta visibile l'avviso `.story__hint` («Scorri per sfogliare i progetti» / «Scroll to browse the projects»): serve perché le barre di avanzamento fanno pensare a una storia che avanza da sola, mentre qui l'avanzamento dipende solo dallo scroll. È nascosto quando la scena non è attiva (JS assente o `prefers-reduced-motion`), quindi non compare nella griglia statica.
- **Prezzi**: il sito non pubblica prezzi: la tabella con le fasce indicative che stava in `/come-lavoriamo/` è stata rimossa, insieme al titolo, alle meta e al collegamento in `/servizi/` che promettevano «quanto costa». La pagina ora racconta il processo (come si forma un preventivo, cosa è compreso, le fasi) senza cifre. Anche l'articolo `/blog/quanto-costa-sito-web-italia-2026/` è un metodo, non un listino: spiega da cosa dipende il preventivo e perché non pubblichiamo numeri. La regola vale anche per le entità (`&euro;`, `&#8364;`), che `tools/check_site.py` tratta come il carattere. Se in futuro servisse una pagina prezzi, va creata da zero con valori reali confermati dal cliente: nessun'altra pagina ripete cifre, quindi si aggiunge in un punto solo.
- **Casi di studio**: `/lavori/` elenca gli stessi sei progetti dimostrativi della home, con la stessa nota visibile (`.note`). Le pagine `/lavori/<cliente>/` non sono state create: nomi, testi e immagini sono di esempio e pubblicare URL di casi inesistenti sarebbe peggio che non averli. Lo stampo però esiste ed è completo: `assets/snippets/case-study-it.txt` e `assets/snippets/case-study-en.txt`, con la procedura e la richiesta di consenso scritte in `docs/phase-9-case-studies.md`. `tools/check_site.py` rifiuta una pagina `/lavori/<slug>/` a cui manchi uno dei sette pezzi promessi: gemello inglese, schermate prima/dopo, tabella tecnica, marcatore `data-results`, link alla pagina del servizio venduto e prova scritta del consenso per la testimonianza.
- **Meta e anteprima social**: aggiornare `description`, `og:title` e `og:description` quando saranno disponibili contenuti definitivi. Le card social 1200×630 sono `assets/img/og-card-it-1200x630.png` e `assets/img/og-card-en-1200x630.png`, dichiarate con URL assolute in `og:image` e `twitter:image` (Open Graph richiede URL assoluti, quindi funzionano solo sul dominio). Si rigenerano da `og-card.html`, che non viene pubblicato: `chrome --headless=new --window-size=1200,630 --force-device-scale-factor=1 --screenshot=assets/img/og-card-it-1200x630.png "http://127.0.0.1:8080/og-card.html"` e con `?lang=en` per la versione inglese. Le pagine interne riusano la card italiana: se servirà un'immagine per singolo servizio, è un file in più da dichiarare nel loro `og:image`.
- **Dati strutturati**: l'head contiene un unico blocco JSON-LD con `@graph`: `Organization` (nome, URL, logo raster, email, telefono, indirizzo a livello città, partita IVA, aree servite, competenze, `contactPoint`), `WebSite` (editore, lingue) e `ProfessionalService` (immagine, indirizzo, catalogo servizi), più una `BreadcrumbList`. I nodi sono collegati tramite `@id` assoluti (`#organization`, `#logo`, `#website`, `#service`, `#breadcrumb`), quindi i riferimenti funzionano solo con il dominio reale. Mancano di proposito `sameAs` (profili social), `streetAddress`/`postalCode`/`addressRegion` e `priceRange`: aggiungere solo dati verificati, altrimenti Google mostra dati errati nel pannello. Il logo dei dati strutturati deve essere raster: `assets/img/logo-512x512.png` si rigenera da `brand-logo.html` (non pubblicato) con `chrome --headless=new --window-size=512,512 --force-device-scale-factor=1 --screenshot=assets/img/logo-512x512.png "http://127.0.0.1:8080/brand-logo.html"`. La `BreadcrumbList` della home ha una sola voce (Home); nelle pagine interne diventa un percorso di due o tre livelli, allineato ai `.crumbs` visibili. Tenere i due elementi sincronizzati: se una pagina cambia posizione, cambiano entrambi.

Non rimuovere gli attributi `data-8b-*`, gli ID delle sezioni, i punti decorativi nelle intestazioni, il commento del template e il `<meta name="generator">`: servono al funzionamento delle animazioni. Il credito visibile nel footer è **Design e sito web: titechdigital.it**.

## Font e tecnologie

- **Gabarito** e **Onest** da Google Fonts.
- **GSAP 3.13.0** e **ScrollTrigger** da jsDelivr.
- **Lenis 1.3.4** per lo smooth scrolling.
- CSS con cascade layers, `color-mix()` e unità viewport moderne.

Browser supportati: Chrome/Edge 111+, Safari 16.2+, Firefox 113+.

## Phase 5 (authority)
La parte operativa è in `docs/phase-5-authority.md`: record NAP canonico, checklist directory, richiesta recensioni, portfolio, LinkedIn e digital PR, con l'elenco di ciò che resta bloccato.

Il footer di ogni pagina pubblica ora il NAP verificato (nome, città di Novara, telefono) e gli stessi valori sono nei dati strutturati `Organization` e `ProfessionalService`. Restano da confermare indirizzo civico e CAP.

Snippet pronti da incollare, mai caricati dal sito:
- `assets/snippets/footer-credit.txt`: link «Realizzato da TiTech Digital» per i siti clienti.
- `assets/snippets/nap-block.txt`: blocco NAP consistente.
- `assets/snippets/review-schema.txt`: schema per recensioni reali. I valori sono token (`@@MEDIA_VALUTAZIONE@@`, `@@NUMERO_RECENSIONI@@`), non un 5,0 già scritto: si incolla solo quando il conteggio coincide con le recensioni pubblicate sulla pagina.
- `assets/snippets/case-study-it.txt` e `assets/snippets/case-study-en.txt`:
  lo stampo completo di una pagina caso studio, una per lingua.

Nessuno di questi file viene incluso dalle pagine: non aggiungono markup, link o dati strutturati al sito.

## Phase 6 (misurazione)

Il piano operativo è in `docs/phase-6-measurement.md`: definizioni, cadenza settimanale e mensile, target a 90 giorni / 6 mesi / 12 mesi, venti keyword in `docs/keywords.csv`, regole di potatura e checklist di attivazione GA4.

`assets/js/measure.js` è caricato da tutte le pagine pubblicate. Il ID `G-1XHPFBBW5Z` è dichiarato in `<meta name="ga4-id">` su ogni pagina, quindi l'impianto è attivo; il banner di consenso però non compare (`askForConsent = false` in testa al file). Senza un modo per dare il consenso non viene caricato `gtag.js`, non viene scritto alcun cookie e nessuna richiesta parte: è l'unica lettura compatibile col GDPR di «GA4 senza banner». Gli eventi restano registrati in `window.titechEvents`, quindi l'impianto si verifica anche senza property. Per vedere i dati propri in GA4 prima di decidere, l'owner attiva il consenso nel proprio browser con `?misura=on` (e lo toglie con `?misura=off`): il parametro viene rimosso dall'indirizzo dopo la scelta, cosi il link non si diffonde da solo. Nessun altro viene mai interpellato e nessun altro acconsente.

Gli eventi inviati sono tre: `contact_click` con `method` (`phone`, `email`, `whatsapp`) e `placement` (barra mobile, footer, CTA, corpo pagina), `contact_submit` e `generate_lead`, che scattano insieme nel momento in cui il modulo passa il messaggio al client di posta. Come chiave di conversione in GA4 si segna solo `generate_lead`.

Gli eventi non sono lead: `contact_submit` dice che il messaggio è stato consegnato al programma di posta, non che sia arrivato. I lead si contano a mano in `docs/scorecard.csv`, che ora tiene anche `organic_sessions` e `lead_rate`.

Strumenti: `tools/set_ga4.py` accende o spegne l'ID su tutte le pagine; `tools/check_keywords.py` verifica che le venti keyword puntino a URL vivi, in sitemap e nella lingua giusta; `tools/gsc_review.py` legge gli export di Search Console e propone cosa correggere o unire. Gli export finiscono in `reports/`, che non viene pubblicato né versionato.

## Phase 7 (autorità tematica)

Il piano dei cluster è in `docs/phase-7-topical-authority.md`: cinque pillar, ventisei articoli pianificati, regole di linking e criteri di scrittura. Ogni articolo risponde a una domanda distinta; nessuna pagina per variazione di keyword.

Il primo cluster avviato è "Realizzazione siti web": gli articoli esistenti (`quanto-costa-sito-web-italia-2026`, `manutenzione-sito-web`) e i pillar relativi (`/servizi/siti-web/`, `/en/services/website-design/`) sono collegati in entrambe le direzioni. Gli altri quattro cluster seguono lo stesso schema.

Strumento: `tools/check_clusters.py` valida l'integrità dei cluster (esistenza bilingue, sitemap, hreflang, link pillar↔articolo).

## Phase 8 (conversion intelligence)

Il piano operativo è in `docs/phase-8-conversion.md`: metrica chiave (ricavo organico / costo di acquisizione organico), A/B test, attribuzione first-touch, integrazione CRM, automazione follow-up, tracking dei deal chiusi.

`assets/js/attribution.js` è caricato da tutte le pagine: cattura UTM, referrer e landing alla prima visita, li salva in `localStorage` e li allega a ogni modulo (campi nascosti + blocco testo nell'email). `assets/js/experiments.js` assegna varianti deterministiche per visitatore e traccia esposizione e conversione. `measure.js` invia source, medium e campaign con ogni evento.

Tre esperimenti attivi: `hero_headline`, `cta_primary`, `contact_headline`. I risultati si misurano sui lead qualificati, non sui clic.

I punti di contatto costruiti in questa fase:

- **Barra mobile** (`assets/js/pages.js` + `.mbar` in `assets/css/pages.css`): sotto i 960px, dopo il 60% dell'altezza della finestra, compaiono «Scrivi su WhatsApp» e «Chiama». Il numero non è duplicato nel JS: viene letto dal NAP del footer, quindi resta un fatto solo. La barra non esiste sulle pagine dei contatti, dove il modulo è già la chiamata all'azione.
- **WhatsApp nel NAP del footer** di tutti i 49 documenti, lo stesso numero del `tel:`. È il contatto WhatsApp per chi legge da desktop, dove la barra mobile non compare.
- **`generate_lead`** emesso insieme a `contact_submit`, con la nota in `docs/phase-6-measurement.md` su quale dei due segnare come key event e su come costruire in GA4 il rapporto lead / sessioni organiche.

Due voci del piano restano fuori, non rinviate: la trasparenza dei prezzi collide con la regola del sito («nessun listino pubblicato») e aspetta una decisione dell'owner; l'automazione dei lead richiede un backend che un sito statico su Vercel senza funzioni non ha.

## Phase 9 (casi studio)

Il piano operativo è in `docs/phase-9-case-studies.md`: i sette output che ogni progetto concluso deve produrre, la tabella dei token dello stampo, la procedura in dodici passi, il testo da mandare al cliente per chiedere il consenso alla testimonianza e l'elenco di ciò che non si può scrivere.

Lo stampo è `assets/snippets/case-study-it.txt` (italiano) e `assets/snippets/case-study-en.txt` (inglese): una pagina interna completa, non un frammento di markup. `audit_case()` in `tools/check_site.py` trasforma i sette punti in cinque rifiuti: una pagina `/lavori/<slug>/` senza gemello inglese, senza schermate prima/dopo, senza tabella tecnica, senza `data-results` o con una testimonianza che non dichiara il consenso non passa. `case_rule()` in `tools/selftest.py` verifica che la regola scatti davvero.

Nessun caso studio è pubblicabile oggi: i sei progetti in `/lavori/` sono dimostrativi e dichiarati tali. Manca l'unica materia prima, cioè un progetto reale concluso.

## Phase 10 (strumenti gratuiti)

Due calcolatori che fanno un calcolo, non due form travestiti da calcolatore.

- `/strumenti/calcolo-costo-sito-web/` e `/en/tools/website-cost-calculator/`: intervallo di investimento e settimane.
- `/strumenti/calcolo-margine-ecommerce/` e `/en/tools/ecommerce-margin-calculator/`: quanto resta su ogni ordine, costo di acquisizione massimo sostenibile, ROAS di pareggio, ordini per coprire i costi fissi.

`assets/js/margin.js` è il motore del secondo: ogni aliquota vive negli attributi `data-*` dei controlli, il file fa solo aritmetica e tutte le frasi che il lettore vede restano nell'HTML. Le caselle non sono precompilate con medie di settore: il calcolatore dice «riempi le caselle» invece di inventarle, e i verdetti sono cinque stati distinti (`incomplete`, `loss`, `uncovered`, `thin`, `ok`), perché un ordine può stare in piedi e il mese no.

Scopribilità: prima gli strumenti erano raggiungibili solo da un articolo del blog. Ora `/servizi/e-commerce/` linka il calcolatore del margine nella sezione «Quando conviene, e quando no» e `/servizi/siti-web/` linka quello del costo nella FAQ «Quanto costa un sito web?», in entrambe le lingue.

Il checker confronta le copie dello stesso calcolatore (pagina dedicata, articolo che lo cita, versione inglese) su nomi dei controlli e attributi `data-*`, ignorando gli attributi `*-locale`: due copie che calcolano numeri diversi sono due risposte sbagliate. `audit_calculators()` stampa `calculators: ok`.

Resta fuori, non rinviato: tutto ciò che richiede di interrogare un sistema esterno (audit URL, scrape della SERP, un tool che chiede un dominio e torna un rapporto). Un sito statico su Vercel senza funzioni non può farlo senza un backend, e un frontend che finge il risultato è il peggior modo di chiedere un link.

## Phase 11 (loop mensile SEO)

Il metodo è in `docs/phase-11-monthly-loop.md`: cosa esportare da Search Console, come nominare i file, il comando da lanciare e cosa fare di ogni sezione che stampa.

La regola del mese: prima le pagine in posizione 5–20, poi tutto il resto; massimo tre pagine modificate e nessun articolo nuovo nella stessa settimana di una riscrittura, perché dopo due effetti non si distinguono più.

`tools/gsc_review.py` legge export italiani o inglesi (`;` o `,`, `2.500` o `2,500`), cerca le pagine pubblicate assenti dall'export confrontandole con `sitemap.xml`, mette in cima la fascia 5–20 con l'ordine di grandezza dei clic recuperabili e, con `--previous=<file>`, dice cosa sale e cosa perde clic fra due periodi.

Bloccato lato owner: la property di Search Console non è verificata e `reports/` è vuoto, quindi il loop è descritto ma non ha ancora mai girato. `docs/scorecard.csv` non ha righe.

## Licenza

Il codice del template è distribuito con licenza MIT: vedere [LICENSE](LICENSE). Foto, font e librerie mantengono le proprie licenze: vedere [CREDITS.md](CREDITS.md).

Template originale: [8B](https://8b.com/templates/).
