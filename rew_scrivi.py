# -*- coding: utf-8 -*-
path = r'C:\Users\eneam\Downloads\TiTechWebsite\contatti\index.html'
s = open(path, encoding='utf-8', newline='').read()

# Truncate at <main
idx = s.index('<main id="main">')
head = s[:idx]

clean_main = r'''<main id="main">
  <div class="shell page">
    <nav aria-label="Percorso">
      <ol class="crumbs">
        <li><a href="/">Home</a></li>
        <li aria-current="page">Contatti</li>
      </ol>
    </nav>
    <div class="head">
      <p class="m-eyebrow">Contatti</p>
      <h1 class="m-text-3 head__title">Cosa deve cambiare, e entro quando<span class="m-dot" aria-hidden="true"></span></h1>
      <p class="m-text-5 head__lead">Non serve un brief. Bastano poche righe scritte come le diresti a un collega: cosa fa l'azienda, cosa non funziona oggi, cosa vorresti ottenere. Da lì capiamo se possiamo essere utili e con che ordine di investimento.</p>
    </div>

    <section class="sect" aria-labelledby="scrivi-title">
      <div class="sect__top">
        <h2 class="m-text-4" id="scrivi-title">Scrivici</h2>
        <p class="m-text">Il modulo compone il messaggio e apre il tuo programma di posta: nessun dato passa da un server intermedio.</p>
      </div>
      <form class="form" data-mailto-form="info@titechdigital.it" novalidate
        data-msg-subject="Richiesta dal sito"
        data-msg-incomplete="Compila nome, email e messaggio: sono i tre campi necessari per risponderti."
        data-msg-invalid="Controlla l'indirizzo email e la casella sul trattamento dei dati."
        data-msg-sent="Apriamo il tuo programma di posta con il messaggio già scritto. Se non si apre, scrivi a {email}.">
        <div class="form__row">
          <label class="field">
            <span>Nome e cognome</span>
            <input class="m-field" type="text" name="nome" data-mail-label="Nome" autocomplete="name" required>
          </label>
          <label class="field">
            <span>Email</span>
            <input class="m-field" type="email" name="email" data-mail-label="Email" autocomplete="email" required>
          </label>
        </div>
        <label class="field">
          <span>Azienda o attività <em>(facoltativo)</em></span>
          <input class="m-field" type="text" name="azienda" data-mail-label="Azienda" autocomplete="organization">
        </label>
        <label class="field">
          <span>Il progetto in poche righe</span>
          <textarea class="m-field" name="messaggio" data-mail-label="" rows="6" required placeholder="Cosa fa l'azienda, cosa deve cambiare, entro quando."></textarea>
        </label>
        <label class="form__check">
          <input type="checkbox" name="consenso" required>
          <span>Ho letto la <a href="/privacy/">privacy policy</a> e acconsento al trattamento dei dati per essere ricontattato su questa richiesta.</span>
        </label>
        <div class="form__actions">
          <button class="m-btn" type="submit"><span>Invia la richiesta</span></button>
          <p class="form__status" role="status" aria-live="polite"></p>
        </div>
      </form>
      <div class="cta">
        <h2 class="m-text-4 cta__title" id="cta-scrivi-title">Preferisci un contatto diretto?<span class="m-dot" aria-hidden="true"></span></h2>
        <p class="m-text">Scrivi a info@titechdigital.it oppure avvia una chat su WhatsApp. Rispondiamo con una prima valutazione del progetto e, se ha senso, fissiamo una call di venti minuti.</p>
        <div class="cta__actions">
          <a class="m-btn-2" href="mailto:info@titechdigital.it"><svg class="m-btn__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 7 10 7 10-7"/></svg><span>Scrivi un'email</span></a>
          <a class="m-btn" href="https://wa.me/393761024080?text=Ciao%2C+vorrei+pi%C3%B9+informazioni+sui+vostri+servizi+digitali." rel="noopener" target="_blank" style="color:inherit"><svg class="m-btn__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-8.5 8.5c-1.5 0-2.9-.3-4.2-1l-3 .9 1-.9a8.38 8.38 0 0 1-1.4-4.8A8.38 8.38 0 1 1 21 11.5z"/></svg><span>Avvia una chat su WhatsApp</span></a>
        </div>
      </div>
      <div class="note">
        <p><strong>Tempi di risposta.</strong> Rispondiamo entro un giorno lavorativo, dal lunedì al venerdì. Se la richiesta arriva il venerdì pomeriggio, la risposta può slittare al lunedì. Ogni richiesta riceve una risposta, anche quando è un no.</p>
      </div>
    </section>

    <section class="sect" aria-labelledby="cosa-title">
      <div class="sect__top">
        <h2 class="m-text-4" id="cosa-title">Cosa ci serve per risponderti</h2>
        <p class="m-text">Quattro informazioni trasformano un preventivo generico in una risposta che puoi usare.</p>
      </div>
      <ul class="checks">
        <li><strong>Il settore</strong><span>Artigianato, ristorazione, servizi, manifattura, studio professionale: cambiano le priorità, non solo i contenuti.</span></li>
        <li><strong>Il problema di oggi</strong><span>Un vecchio sito che nessuno aggiorna, ordini gestiti a mano, richieste che si perdono. Il punto di partenza reale conta più dell'obiettivo dichiarato.</span></li>
        <li><strong>La scadenza</strong><span>Una data reale, anche approssimativa. Se è stretta lo diciamo subito, con quanto costa.</span></li>
        <li><strong>Il budget indicativo</strong><span>Non è una trattativa: serve a capire se ha senso parlare. Se il budget è sotto la soglia minima, è utile saperlo prima.</span></li>
      </ul>
    </section>

    <section class="sect" aria-labelledby="dove-title">
      <div class="sect__top">
        <h2 class="m-text-4" id="dove-title">Dove lavoriamo</h2>
      </div>
      <div class="prose">
        <p>TiTech Digital è in Italia e lavora da remoto con aziende italiane, con aziende in Albania e su mercati internazionali. Riunioni in video, file condivisi e una persona di riferimento: la distanza non è il problema, l'assenza di un riferimento sì.</p>
        <p>Quando un progetto richiede incontri in presenza, un workshop da fotografare, un processo di magazzino da osservare, li organizziamo in sede. Lo mettiamo in proposta come viaggio, non lo nascondiamo dentro una riga generica.</p>
        <p>Per i dati fiscali e la fatturazione: TiTech Digital, partita IVA 02829190038. L'indirizzo completo della sede è fornito su richiesta, in proposta e in fattura.</p>
      </div>
    </section>

    <section class="sect sect--paper" aria-labelledby="faq-title">
      <div class="sect__top">
        <h2 class="m-text-4" id="faq-title">Prima di scrivere</h2>
      </div>
      <div class="faq">
        <details>
          <summary>Quanto costa una prima conversazione?</summary>
          <p>Nulla. Trenta minuti in video o al telefono per capire se il progetto è alla portata di entrambi. Se serve un'analisi più approfondita, con accesso ai sistemi, verifica dei contenuti e stima dei tempi, è un lavoro separato con un costo che concordiamo prima.</p>
        </details>
        <details>
          <summary>Prendete anche budget piccoli?</summary>
          <p>Sì, se il lavoro ha senso. Un sito vetrina di poche pagine può rientrare in una fascia contenuta. Quello che diciamo chiaramente è quando un budget non basta per l'obiettivo: in quel caso è meglio ridurre lo scope che ridurre la qualità.</p>
        </details>
        <details>
          <summary>Rispondete anche se non possiamo collaborare?</summary>
          <p>Sempre. Se il progetto non è il nostro lavoro, lo scriviamo con il motivo: una tecnologia fuori dal nostro perimetro, un budget incompatibile, una scadenza impossibile. Un no motivato è più utile di un silenzio.</p>
        </details>
        <details>
          <summary>Posso scrivere in inglese o in albanese?</summary>
          <p>Sì. Scriviamo e lavoriamo in italiano, inglese e albanese. Il sito è in italiano e in inglese; le comunicazioni di progetto le gestiamo nella lingua che preferisci.</p>
        </details>
      </div>
    </section>

    <section class="sect" aria-labelledby="cta-title">
      <div class="cta">
        <h2 class="m-text-4 cta__title" id="cta-title">Preferisci leggere prima di scrivere?<span class="m-dot" aria-hidden="true"></span></h2>
        <p class="m-text">Tempi, fasi e fasce di investimento sono spiegati senza giri di parole. Se il progetto è alla tua portata, lo capisci in due minuti.</p>
        <div class="cta__actions">
          <a class="m-btn-2" href="/come-lavoriamo/"><span>Tempi e investimento</span></a>
          <a class="m-link" href="mailto:info@titechdigital.it" style="color:inherit"><span class="m-link__label">info@titechdigital.it</span><svg class="m-link__arrow" viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8h11M9 3.5 13.5 8 9 12.5"/></svg></a>
        </div>
      </div>
    </section>
  </div>
</main>
<footer id="footer" class="footer">
  <div class="footer__grid">
    <div class="footer__col">
      <p class="footer__label m-text-6">TiTech Digital</p>
      <a class="m-link-2" href="mailto:info@titechdigital.it">info@titechdigital.it</a>
      <a class="m-link-2" href="tel:+393761024080">+39 376 102 4080</a>
    </div>
    <div class="footer__col">
      <p class="footer__label m-text-6">Navigazione</p>
      <a class="m-link-2" href="/">Home</a>
      <a class="m-link-2" href="/servizi/">Servizi</a>
      <a class="m-link-2" href="/lavori/">Lavori</a>
      <a class="m-link-2" href="/come-lavoriamo/">Come lavoriamo</a>
      <a class="m-link-2" href="/chi-siamo/">Chi siamo</a>
      <a class="m-link-2" href="/blog/">Blog</a>
      <a class="m-link-2" href="/contatti/">Contatti</a>
    </div>
    <div class="footer__col">
      <p class="footer__label m-text-6">Legale</p>
      <a class="m-link-2" href="/privacy/">Privacy</a>
      <a class="m-link-2" href="/cookie/">Cookie</a>
    </div>
    <div class="footer__col">
      <p class="footer__label m-text-6">Lingua</p>
      <a class="m-link-2" href="/en/contact/" hreflang="en" lang="en">English</a>
    </div>
  </div>
  <address class="footer__nap m-text-6">
    <span>TiTech Digital</span>
    <a class="m-link-2" href="tel:+393761024080">+39 376 102 4080</a>
    <span>Novara, Italia</span>
  </address>
  <div class="footer__legal m-text-6"><p>© 2026 TiTech Digital · P. IVA 02829190038 · <a href="/privacy/">Privacy</a> · <a href="/cookie/">Cookie</a></p><p>Design e sito web: titechdigital.it</p></div>
</footer>
<script src="/assets/js/pages.js" defer></script>
<script src="/assets/js/measure.js" defer></script>
</body>
</html>
'''

open(path, 'w', encoding='utf-8', newline='').write(head + clean_main)
print('rebuilt ok')
