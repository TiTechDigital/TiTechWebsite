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
