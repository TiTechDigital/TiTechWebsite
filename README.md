# TiTech Digital — Sito web

Sito one-page in italiano e inglese per **TiTech Digital**, partner tecnologico per imprese. Il progetto parte dal template design studio di 8B e ne conserva layout, sistema visivo, tipografia e animazioni: il contenuto è stato riscritto per raccontare posizionamento, servizi e metodo di TiTech Digital.

## Contenuto

La pagina copre:

- **Siti web ed e-commerce** — sviluppo su misura, prestazioni, accessibilità e gestione.
- **Design e identità digitale** — brand identity, UI/UX, design di prodotto e direzione creativa.
- **Software e automazione** — web app, dashboard, API, integrazioni, AI e automazione.
- **SEO e crescita digitale** — SEO tecnica, performance, contenuti e CRO.
- **Supporto continuo** — manutenzione, hosting, assistenza e partnership nel tempo.

Il posizionamento è quello di un partner serio e concreto: competenza tecnica, scelte motivate, attenzione alla qualità e continuità dopo il lancio. La sede è in Italia, con un orizzonte internazionale e un'attenzione particolare al mercato albanese.

## Struttura della pagina

1. Hero con immagine rotonda e parola di apertura.
2. Statement in due righe.
3. Cinque card di servizio su binario orizzontale (siti ed e-commerce, design, software, SEO, supporto).
4. Sei card della ruota dei principi.
5. Metodo in quattro fasi con anello animato.
6. Collage dello studio con competenze integrate.
7. Sei domande frequenti in `<details>`.
8. Contatti con modulo.
9. Footer con saluto, link, email e credito Design: 8B.

Le animazioni GSAP/ScrollTrigger e lo smooth scrolling Lenis sono quelli originali del template. Con `prefers-reduced-motion` attivo la pagina resta completa e statica.

## Lingue

La versione italiana è quella predefinita:

- `/index.html` — italiano
- `/en/index.html` — inglese

Il pulsante `EN` nella barra di navigazione porta alla versione inglese; il pulsante `IT` sulla pagina inglese riporta a quella italiana. Su mobile lo stesso cambio è disponibile come `English` / `Italiano` nel menu.

Le due pagine condividono struttura, animazioni e attributi `data-8b-*`; cambiano testi, metadati e percorsi delle risorse (`../assets/` nella pagina inglese). Non è presente un selettore automatico basato sulla lingua del browser: la scelta resta manuale.

## Anteprima locale

Dalla cartella del progetto:

```bash
python -m http.server 8080 --bind 127.0.0.1
```

Poi aprire `http://127.0.0.1:8080/` (italiano) oppure `http://127.0.0.1:8080/en/` (inglese).

Non serve alcun build step: ogni pagina è un unico `index.html` con CSS e JavaScript inline, più le risorse esterne condivise (font, GSAP, Lenis, immagini).

## Modulo di contatto

Non è configurato un backend. All'invio il modulo:

1. valida nome, email e descrizione;
2. compone una richiesta con nome, email, azienda, area di interesse e messaggio;
3. apre il programma di posta dell'utente tramite `mailto:` verso `info@titechdigital.it`.

L'indirizzo `info@titechdigital.it` è un **segnaposto**: va sostituito con l'indirizzo reale prima della pubblicazione. Per usare un servizio di invio (Formspree, Netlify Forms o un endpoint proprio) basta modificare lo script `section-script:contact` e il markup del form.

## Personalizzazione

- **Testi** — in `index.html` (italiano) e `en/index.html` (inglese). Quando si modifica una versione, aggiornare anche l'altra per mantenere allineati contenuti e metadati.
- **Email** — cercare `info@titechdigital.it` e sostituirla in contatti, footer e script.
- **Immagini** — i WebP ottimizzati sono in `assets/img` e referenziati da entrambe le pagine; le attribuzioni sono in [CREDITS.md](CREDITS.md). Le foto sono illustrative e non rappresentano clienti o progetti reali.
- **Meta e anteprima social** — aggiornare `description`, `og:title`, `og:description` e `og:image` quando saranno disponibili contenuti definitivi.
- **Dati strutturati** — il blocco JSON-LD `Organization` è presente nell'head; aggiungere solo dati verificati (indirizzo, telefono, profili social).

Non rimuovere gli attributi `data-8b-*`, gli ID delle sezioni, i punti decorativi nelle intestazioni, il commento del template, il `<meta name="generator">` e il credito “Design: 8B” nel footer: servono al funzionamento delle animazioni e alla corretta attribuzione del template.

## Font e tecnologie

- **Gabarito** e **Onest** da Google Fonts.
- **GSAP 3.13.0** e **ScrollTrigger** da jsDelivr.
- **Lenis 1.3.4** per lo smooth scrolling.
- CSS con cascade layers, `color-mix()` e unità viewport moderne.

Browser supportati: Chrome/Edge 111+, Safari 16.2+, Firefox 113+.

## Licenza

Il codice del template è distribuito con licenza MIT: vedere [LICENSE](LICENSE). Foto, font e librerie mantengono le proprie licenze: vedere [CREDITS.md](CREDITS.md).

Template originale: [8B](https://8b.com/templates/).
