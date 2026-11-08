# Google Business Profile: attività con area di servizio

TiTech Digital non ha un ufficio aperto al pubblico a Novara. La formula giusta
è quindi una scheda **con area di servizio**: l'indirizzo reale serve solo per
la verifica e non viene mostrato, la scheda mostra invece le zone servite.

Questa guida adatta la procedura del vecchio progetto (DevPortfolioHub,
`GOOGLE_BUSINESS_SETUP.md`) ai dati veri di TiTech. Non copia da lì il telefono né
il nome del brand; delle città tiene quelle dove si lavora davvero, distinguendo
tra quelle da mettere nella scheda e quelle da tenere solo sul sito.

Dati da usare **identici** ovunque: vedi `docs/phase-5-authority.md`, sezione 1.

---

## 1. Creazione della scheda

1. Vai su `business.google.com` con l'account Google dell'azienda (meglio un
   account dedicato, non personale).
2. **Nome attività:** `TiTech Digital`. Nient'altro: aggiungere "Web Agency
   Novara" al nome viola le regole di Google e può far sospendere la scheda.
3. **Categoria principale:** "Web designer" (se non compare con questo nome,
   scegli la voce più vicina a "progettista di siti web").
   **Categorie aggiuntive:** una o due tra società di sviluppo software e
   consulenza di marketing su Internet. I nomi esatti cambiano: scegli dall'elenco
   che Google propone, non inventarne.
4. **"Vuoi aggiungere una sede visitabile dai clienti?"** Rispondi **No**.
5. **Indirizzo:** inserisci l'indirizzo reale da cui lavori. Serve alla
   verifica e Google lo tiene nascosto con questa impostazione. Non usare
   caselle postali né uffici virtuali: non sono ammessi.
6. **Aree di servizio** (massimo 20). Quelle che lavori davvero, dal più vicino:
   Novara, Galliate, Trecate, Arona, Borgomanero, Oleggio, Milano, Torino,
   Biella, Vercelli, Alessandria, Asti. Sono le città a una distanza
   ragionevole da Novara, dove puoi anche incontrare i clienti.
   Roma, Napoli, Firenze, Bologna, Genova e Venezia sono sul sito come clienti a
   distanza, ma conviene **non metterle nella scheda Google**: Google chiede
   aree dove l'attività presta davvero il servizio e può sospendere una scheda
   con aree troppo lontane. Se vuoi comunque aggiungerne qualcuna, mettile
   dopo la verifica e osserva se la scheda resta attiva.
7. **Telefono:** `+39 350 920 5365`.
8. **Sito web:** `https://www.titechdigital.it/novara/`
   (la pagina locale, non la home).

## 2. Orari

Lunedì–venerdì 09:00–18:00, sabato e domenica chiuso. Sono gli stessi dati nel
`ProfessionalService` di `/novara/` e della home: se li cambi, cambiali in
entrambi.

## 3. Descrizione (massimo 750 caratteri)

Testo pronto, senza ripetizioni forzate di parole chiave:

> TiTech Digital è una web agency con sede a Novara. Realizziamo siti web
> aziendali, e-commerce, software su misura e automazioni per imprese, negozi,
> artigiani e studi professionali di Novara e provincia, e lavoriamo a distanza
> con clienti di tutta Italia. Ci occupiamo anche di SEO locale e della scheda
> Google. Ci si incontra di persona a Novara o in videochiamata; prima di
> iniziare ricevi un preventivo scritto con perimetro, tempi e costi.

## 4. Servizi da inserire nella scheda

Uno per voce, con una riga di descrizione e senza prezzi:

| Servizio | Descrizione breve |
|---|---|
| Realizzazione siti web | Siti aziendali veloci e curati, dal progetto alla pubblicazione |
| E-commerce | Negozi online con catalogo, pagamenti e spedizioni |
| Software su misura | Gestionali, portali clienti e dashboard sui processi dell'azienda |
| Automazioni e AI | Automazione dei passaggi manuali ripetuti |
| Consulenza SEO | SEO tecnica e locale, scheda Google, misurazione |

## 5. Foto

Logo (`assets/img/logo-512x512.png`), una copertina, schermate di lavori reali
(con permesso del cliente) e, se vuoi, una foto del team. Niente foto di
repertorio. Poche immagini vere valgono più di molte generiche.

## 6. Verifica

Google decide il metodo: per le attività con area di servizio è comune il video
(mostri da dove lavori e il materiale con cui lavori) o una chiamata. Non c'è un
modo per saltarla: senza verifica la scheda non compare su Maps.

## 7. Dopo la verifica

1. **Recensioni:** manda ai clienti il link diretto, con i testi in
   `docs/phase-5-authority.md`, sezione 3. Mai recensioni scritte da noi.
2. **Aggiungi l'URL del profilo a `sameAs`** nei dati strutturati di
   `index.html` e `novara/index.html` (lo faccio io, mandami il link).
3. **Un post al mese** sulla scheda (nuovo articolo, nuovo lavoro).
4. **Domande e risposte:** rispondi tu per primo alle domande più comuni
   (costi, tempi, zone servite), con le stesse risposte delle FAQ di `/novara/`.
5. **Se un giorno apri un ufficio visitabile:** cambia la scheda in "sede
   visitabile", aggiorna l'indirizzo sul sito (footer, `PostalAddress`) e su
   tutte le directory nello stesso giorno.

## 8. Cose da non fare

- Nome con parole chiave aggiunte.
- Indirizzo diverso da quello reale, ufficio virtuale, casella postale.
- Elenco di città lontane tra le aree di servizio.
- Recensioni inventate, scambi di recensioni, sconti in cambio di recensioni.
- Telefono diverso da quello del sito. Il vecchio numero (+39 376 102 4080) è
  del vecchio progetto e non va usato.
