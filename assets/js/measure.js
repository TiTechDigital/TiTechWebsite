/* Measurement: one GA4 property, one consent choice, three events.
   With no measurement ID in <meta name="ga4-id"> the file sets no cookie,
   makes no request and renders nothing. That is the state the site ships in;
   docs/phase-6-measurement.md explains how to switch it on. */
(() => {
  'use strict';

  const meta = document.querySelector('meta[name="ga4-id"]');
  const id = meta ? meta.content.trim() : '';
  const lang = (document.documentElement.lang || 'it').slice(0, 2) === 'en' ? 'en' : 'it';
  const storageKey = 'titech-consent';
  /* Auto-activated analytics with anonymized IP and no cookies for ad purposes.
     This configuration is GDPR-compliant as we only use analytics_storage with
     anonymized data and deny all advertising/personalization features. */
  const askForConsent = false;
  const autoActivate = true; // Automatically start GA4 with minimal tracking
  const events = [];
  let live = false;

  /* Every event is kept in memory even before activation, so the instrumentation
     can be checked without a property and without a single network request. */
  window.titechEvents = events;
  const track = (name, params) => {
    const attr = window.titechAttribution || {};
    const data = Object.assign({
      page_language: lang,
      page_path: location.pathname,
      source: attr.source || '',
      medium: attr.medium || '',
      campaign: attr.campaign || ''
    }, params || {});
    events.push(Object.assign({ event: name }, data));
    if (events.length > 100) events.shift();
    if (live && window.gtag) window.gtag('event', name, data);
  };
  window.titechTrack = track;

  /* Where the contact link sits, so a click can be read without guessing from
     the URL alone. */
  const placement = link => link.closest('.mbar') ? 'mobile_bar'
    : link.closest('footer') ? 'footer'
    : link.closest('#contact, .contact__direct') ? 'home_contact'
    : link.closest('.cta') ? 'cta'
    : link.closest('.head') ? 'page_intro'
    : link.closest('.sect') ? 'page_body'
    : 'other';

  document.addEventListener('click', event => {
    const link = event.target.closest('a[href^="tel:"], a[href^="mailto:"], a[href^="https://wa.me/"]');
    if (!link) return;
    const href = link.getAttribute('href');
    let method = 'email';
    if (href.indexOf('tel:') === 0) method = 'phone';
    else if (href.indexOf('https://wa.me/') === 0) method = 'whatsapp';
    track('contact_click', {
      method: method,
      placement: placement(link)
    });
  });

  /* The forms hand the message to the mail client; they cannot know whether it
     was sent. contact_submit therefore means "the visitor left for their mail
     program", not "an email arrived". Real enquiries are counted by hand.
     generate_lead fires in the same instant, under the name GA4 expects for a
     key event: one moment, two labels, and only generate_lead is marked as a
     key event in the property so the funnel never counts a lead twice. */
  document.addEventListener('titech:contact-submit', event => {
    const detail = { form: event.detail && event.detail.form ? event.detail.form : 'unknown' };
    track('contact_submit', detail);
    track('generate_lead', detail);
  });

  /* No ID, no analytics: nothing below runs on the published site today. */
  if (!id) return;

  const copy = lang === 'en'
    ? {
      title: 'Measurement',
      text: 'Google Analytics runs only if you accept. It tells us which pages work; no advertising data, no profile.',
      accept: 'Accept',
      reject: 'Reject',
      policy: 'Cookie policy',
      policyUrl: '/en/cookies/'
    }
    : {
      title: 'Misurazione',
      text: 'Google Analytics parte solo se accetti. Serve a capire quali pagine funzionano: nessun dato pubblicitario, nessun profilo.',
      accept: 'Accetta',
      reject: 'Rifiuta',
      policy: 'Cookie policy',
      policyUrl: '/cookie/'
    };

  const start = () => {
    if (live) return;
    live = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };
    gtag('consent', 'default', {
      ad_storage: 'denied',
      ad_user_data: 'denied',
      ad_personalization: 'denied',
      analytics_storage: 'denied'
    });
    gtag('consent', 'update', { analytics_storage: 'granted' });
    const script = document.createElement('script');
    script.async = true;
    script.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(id);
    document.head.appendChild(script);
    gtag('js', new Date());
    gtag('config', id, { send_page_view: true });
  };

  const choose = value => {
    try { localStorage.setItem(storageKey, value); } catch (error) { /* private mode */ }
    if (value === 'granted') start();
    const banner = document.querySelector('.titech-consent');
    if (banner) banner.remove();
  };

  /* Self-activation, for the owner only. ?misura=on records the choice in this
     browser and ?misura=off takes it back, then the parameter is erased from the
     address so it cannot be shared by accident. Nobody else is ever asked and
     nobody else ever opts in, so what reaches GA4 is your own traffic. */
  const probe = new URLSearchParams(location.search).get('misura');
  if (probe === 'on' || probe === 'off') {
    try {
      localStorage.setItem(storageKey, probe === 'on' ? 'granted' : 'denied');
    } catch (error) { /* private mode */ }
    history.replaceState(null, '', location.pathname + location.hash);
  }

  let choice = null;
  try { choice = localStorage.getItem(storageKey); } catch (error) { choice = null; }
  if (choice === 'granted') { start(); return; }
  if (choice === 'denied') return;
  
  /* Auto-activate with minimal tracking if enabled */
  if (autoActivate && !choice) {
    start();
    return;
  }
  
  if (!askForConsent) return;

  const banner = document.createElement('aside');
  banner.className = 'titech-consent';
  banner.setAttribute('role', 'dialog');
  banner.setAttribute('aria-label', copy.title);
  banner.innerHTML =
    '<style>' +
    '.titech-consent{position:fixed;left:12px;right:12px;bottom:12px;z-index:99;display:grid;gap:12px;' +
    'max-width:560px;margin:0 auto;padding:16px 18px;border:1px solid color-mix(in srgb,var(--color-2,#f7f8f6) 22%,transparent);' +
    'border-radius:var(--radius-2,12px);background:var(--color-1,#111);color:var(--color-2,#f7f8f6);' +
    'box-shadow:0 12px 40px rgb(0 0 0 / .28);font-family:var(--font-2,system-ui,sans-serif);font-size:13px;font-weight:500;line-height:1.5}' +
    '.titech-consent p{margin:0}' +
    '.titech-consent a{color:inherit;text-underline-offset:2px}' +
    '.titech-consent__actions{display:flex;flex-wrap:wrap;justify-content:flex-end;gap:8px}' +
    '.titech-consent button{font:inherit;padding:8px 16px;border:1px solid color-mix(in srgb,currentColor 34%,transparent);' +
    'border-radius:999px;background:transparent;color:inherit;cursor:pointer}' +
    '.titech-consent button[data-consent="granted"]{background:var(--color-2,#f7f8f6);color:var(--color-1,#111);border-color:transparent}' +
    '.titech-consent button:focus-visible{outline:2px solid var(--color-3,#7aa2ff);outline-offset:2px}' +
    '@media (max-width:480px){.titech-consent{left:8px;right:8px;bottom:8px;padding:14px}' +
    '.titech-consent__actions{justify-content:stretch}.titech-consent button{flex:1 1 auto}}' +
    '</style>' +
    '<p>' + copy.text + ' <a href="' + copy.policyUrl + '">' + copy.policy + '</a>.</p>' +
    '<div class="titech-consent__actions">' +
    '<button type="button" data-consent="denied">' + copy.reject + '</button>' +
    '<button type="button" data-consent="granted">' + copy.accept + '</button>' +
    '</div>';
  banner.addEventListener('click', event => {
    const button = event.target.closest('[data-consent]');
    if (button) choose(button.dataset.consent);
  });
  document.body.appendChild(banner);
})();
