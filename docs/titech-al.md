# titech.al: sito albanese

`al/` è un progetto Vercel a sé. Si genera con `python tools/build_albanian_site.py`
partendo dalle pagine inglesi e dal dizionario `tools/al_strings.py`: stesso design, stessi
stili e stesse animazioni. Se una stringa visibile non ha traduzione, la build si ferma.

## Messa online (quando il dominio è comprato)

1. Vercel → Add New Project → stesso repository GitHub.
2. **Root Directory: `al`**. Framework: Other. Production Branch: `main` (dopo il merge).
3. Variabile d'ambiente `RESEND_API_KEY` (la stessa del sito italiano).
4. Domains: `www.titech.al` come principale, `titech.al` con redirect (c'è già nel `vercel.json` di `al/`).
5. Search Console: nuova proprietà per `titech.al`, inviare `https://www.titech.al/sitemap.xml`.
6. Il progetto italiano ignora `al/` (`.vercelignore`), quindi niente copie su titechdigital.it.

## Prima di pubblicare

- Testi albanesi rivisti da un madrelingua (sono una prima bozza).
- Pagine ancora da costruire: servizi (7), come lavoriamo, chi siamo, lavori, settori, blog,
  strumenti, **privacy e cookie** (servono prima del lancio: il modulo raccoglie dati).
  Nel frattempo i link a queste pagine puntano alla versione inglese su titechdigital.it
  (`BUILT` in `tools/build_albanian_site.py`: si aggiorna aggiungendo la pagina in `PAGES`/`BUILT`).
- Scheda Open Graph in albanese (ora usa quella inglese).
- Pagine di sito italiano e inglese: aggiungere l'alternate `sq-AL` (hreflang reciproco), solo a dominio attivo.
- GA4: stesso ID del sito italiano; valutare una proprietà separata.
- Chatbot: non presente sulle pagine albanesi (risponde in italiano e usa un host esterno).

## Stato (25 nov 2026)

Costruite in albanese: home, contatti, `/sherbimet/`, `/tirane/`, 5 pagine di servizio
(`/krijimi-i-faqeve-web-tirane/`, `/dyqan-online-tirane/`, `/softuer-me-porosi-tirane/`,
`/aplikacione-mobile-tirane/`, `/seo-tirane/`), blog con 4 guide. Rigenerazione:
`python tools/build_albanian_site.py && python tools/build_albanian_pages.py`.

Parole chiave: `docs/albania-keywords.csv`. **I volumi non sono verificati**: la sandbox non
raggiunge Keyword Planner. Da compilare a mano prima di decidere le priorità.

## Cosa ha mostrato la ricerca sui risultati

- Per "krijimi i faqeve web Tiranë" e "web design Tiranë" dominano directory (Clutch,
  TechBehemoths, DesignRush) e freelance, non i siti delle agenzie. Le agenzie a Tiranë sono
  decine: il mercato non è vuoto.
- I contenuti in albanese su SEO lokale sono pochi, in gran parte articoli tradotti. Su costi di un
  sito e pagamenti per un e-commerce in Albania non c'è una risposta chiara: lì stanno le guide.
- Shopify Payments e WooPayments non elencano l'Albania (a nov 2026): da ricontrollare prima di
  pubblicare e di ogni modifica.
- Molte ricerche di agenzie sono in inglese: serve una versione `/en/` di titech.al.

## Aggiornamento (25 nov 2026, seconda tornata)

Aggiunte: guida pagamenti online, hotel e B&B (pagina e guida), ristoranti, cliniche, "Automatizim me AI",
guide sui costi di SEO e app, hub settori, Punimet, Si punojmë, Rreth nesh, **Privatësia e Cookie**
(scritte sul trattamento reale: modulo → funzione Vercel → Resend; nessun chatbot su titech.al).
Totale: 28 pagine. La privacy dei siti italiano e inglese è stata corretta: diceva che il modulo
"non passa da un server intermedio", cosa non più vera.

**Aperto, da decidere:** il chatbot sulle pagine italiane e inglesi invia le conversazioni a un servizio
su Render non citato nella privacy: serve sapere cosa conserva e se usa un fornitore AI.

## Prossimi passi

1. Rivedere tutto il testo albanese con un madrelingua.
2. Privacy e cookie in albanese; immagine di condivisione in albanese.
3. Profili sulle directory che dominano i risultati (Clutch, TechBehemoths, DesignRush, GoodFirms).
4. Pagine in inglese per "web design Tirana".
5. Altre città (Durrës, Shkodër, Vlorë, Elbasan, Korçë): una pagina solo quando c'è qualcosa di vero e
   di diverso da dire; altrimenti sono pagine in serie.
