# Calendario editoriale SEO, 10 novembre - 10 dicembre 2026

Stato: EN-MISSING 1, EXISTS 2, MISSING 23, PARTIAL 5

| Giorno | Pubblica | Stato | Titolo | Keyword principale (IT / EN) |
|---|---|---|---|---|
| 1 (11-10) | -  | EXISTS | Quanto costa un sito web in Italia nel 2026 | costo sito web / website cost |
| 2 (11-11) | 2026-12-12 B | EN-MISSING | Come scegliere una web agency: 7 aspetti da valutare | come scegliere una web agency / how to choose a web agency |
| 3 (11-12) | 2026-11-28 B | MISSING | Sito web per piccole imprese: perché è fondamentale nel 2026 | sito web per piccole imprese / website for small businesses |
| 4 (11-13) | 2026-12-10 B | PARTIAL | Sito web aziendale: cosa include il prezzo e come leggere il preventivo | prezzo sito web aziendale / business website price |
| 5 (11-14) | 2026-11-29 B | MISSING | Sito web o social network: cosa conviene alla tua attività? | sito web o social network / website or social media |
| 6 (11-15) | 2026-11-30 B | MISSING | Come trovare clienti online: strategie per le piccole imprese | trovare clienti online / find customers online |
| 7 (11-16) | 2026-12-01 B | MISSING | Come creare un sito web professionale che trasforma visitatori in clienti | sito web professionale / professional website |
| 8 (11-17) | 2026-12-02 B | MISSING | Quanto costa sviluppare un software gestionale personalizzato? | costo software gestionale / custom management software cost |
| 9 (11-18) | 2026-12-03 B | MISSING | Software gestionale aziendale: quando conviene svilupparne uno su misura? | software gestionale personalizzato / custom management software |
| 10 (11-19) | -  | EXISTS | Automazione con AI per PMI: 5 processi da cui partire | automazione aziendale / business process automation |
| 11 (11-20) | 2026-12-11 A | PARTIAL | Intelligenza artificiale per aziende: applicazioni pratiche | intelligenza artificiale per aziende / artificial intelligence for businesses |
| 12 (11-21) | 2026-12-04 B | MISSING | Quanto costa realizzare un e-commerce nel 2026? | costo e-commerce / e-commerce cost |
| 13 (11-22) | 2026-12-05 B | MISSING | Come vendere online: cosa serve per aprire un negozio digitale | come vendere online / how to sell online |
| 14 (11-23) | 2026-12-06 B | MISSING | SEO locale: come trovare clienti nella propria città su Google | SEO locale / local SEO |
| 15 (11-24) | 2026-12-07 B | MISSING | Come migliorare il posizionamento di un sito web su Google | migliorare posizionamento Google / improve google ranking |
| 16 (11-25) | 2026-12-08 B | MISSING | Perché il tuo sito web non riceve visite? 8 errori da evitare | sito web non riceve visite / website not getting visits |
| 17 (11-26) | 2026-12-09 B | MISSING | Quanto tempo serve per posizionarsi su Google? | tempo posizionamento Google / how long to rank on google |
| 18 (11-27) | 2026-11-27 A | MISSING | Sito web per ristoranti: funzionalità che aiutano ad acquisire clienti | sito web per ristoranti / website for restaurants |
| 19 (11-28) | 2026-11-28 A | PARTIAL | Sito web per professionisti: cosa non dovrebbe mai mancare | sito web per professionisti / website for professionals |
| 20 (11-29) | 2026-11-29 A | MISSING | Applicazioni web personalizzate: quando servono davvero? | applicazioni web personalizzate / custom web applications |
| 21 (11-30) | 2026-11-30 A | MISSING | App mobile aziendale: quando conviene svilupparne una? | sviluppo app mobile / mobile app development |
| 22 (12-01) | 2026-12-01 A | MISSING | CRM aziendale: cos'è e come aiuta a gestire i clienti | software CRM aziendale / business CRM software |
| 23 (12-02) | 2026-12-02 A | MISSING | Come digitalizzare una piccola impresa: guida pratica | digitalizzazione piccole imprese / digitalisation small business |
| 24 (12-03) | 2026-12-03 A | MISSING | Chatbot AI per aziende: come automatizzare il servizio clienti | chatbot AI per aziende / AI chatbot for business |
| 25 (12-04) | 2026-12-04 A | MISSING | Come scegliere un hosting per il proprio sito web | hosting per siti web / website hosting |
| 26 (12-05) | 2026-12-05 A | MISSING | Quando è il momento di rifare il sito web aziendale? | rifare sito web / redesign website |
| 27 (12-06) | 2026-12-06 A | MISSING | Sito web lento: come migliorare velocità e prestazioni | velocizzare sito web / speed up website |
| 28 (12-07) | 2026-12-07 A | PARTIAL | Quanto costa la manutenzione di un sito web? | costo manutenzione sito web / website maintenance cost |
| 29 (12-08) | 2026-12-08 A | MISSING | Software su misura o software standard: quale scegliere? | software su misura / custom software |
| 30 (12-09) | 2026-12-09 A | PARTIAL | Come creare un sito web per un'attività locale a Novara | realizzazione siti web Novara / website design Novara |
| 31 (12-10) | 2026-12-10 A | MISSING | Come scegliere un'agenzia SEO per la propria azienda | agenzia SEO / SEO agency |

## Come funziona la pubblicazione

- Gli articoli si scrivono in `tools/calendar_content.py` (italiano e inglese insieme) e si costruiscono con `python tools/build_calendar_articles.py`.
- Restano in `_scheduled/` (mai pubblicata: `.vercelignore` salta le cartelle con underscore) con la data in `_scheduled/manifest.json`.
- Ogni mattina una GitHub Action (`.github/workflows/publish-scheduled.yml`) esegue `tools/publish_scheduled.py`: sposta gli articoli scaduti in `blog/` ed `en/blog/`, li aggiunge agli indici del blog e alla sitemap, controlla il sito e fa push su `main`. Vercel pubblica.
- Stato `EXISTS`: la pagina c'è già, si ottimizza e basta. `PARTIAL`: l'argomento è toccato da un'altra pagina, angolo nuovo. `MISSING`: da scrivere. `EN-MISSING`: manca solo il gemello inglese.
- Slot A = il giorno originale del calendario; slot B = recupero dei giorni passati senza articolo.
