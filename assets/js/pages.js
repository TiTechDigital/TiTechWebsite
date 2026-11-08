/* Inner page behaviour: phone menu dialog, current year, mailto form. Deliberately tiny. */
(() => {
  'use strict';
  /* the full-screen menu, same dialog as the home page */
  const menu = document.getElementById('menu');
  const opener = document.querySelector('.nav__menu');
  const closer = document.querySelector('.menu__close');
  if (menu && opener) {
    const setOpen = open => {
      menu.hidden = !open;
      opener.setAttribute('aria-expanded', String(open));
      document.documentElement.classList.toggle('nav-open', open);
      if (window.lenis) { if (open) window.lenis.stop(); else window.lenis.start(); }
      if (open) { if (closer) closer.focus(); }
      else if (opener.offsetParent !== null) opener.focus();
    };
    opener.addEventListener('click', () => setOpen(menu.hidden));
    if (closer) closer.addEventListener('click', () => setOpen(false));
    menu.addEventListener('keydown', event => { if (event.key === 'Escape') setOpen(false); });
    menu.querySelectorAll('.menu__list a').forEach(link => link.addEventListener('click', () => setOpen(false)));
    matchMedia('(min-width: 960px)').addEventListener('change', event => { if (event.matches) setOpen(false); });
  }
  /* Tables turn into cards below 860px, each cell labelled by its column. Tables
     written without data-label get it from the header row, so the labels cannot
     drift from the headings. */
  document.querySelectorAll('.table').forEach(table => {
    const heads = Array.prototype.map.call(table.querySelectorAll('thead th'), th => th.textContent.trim());
    if (!heads.length) return;
    table.querySelectorAll('tbody tr').forEach(row => {
      Array.prototype.forEach.call(row.children, (cell, index) => {
        if (cell.tagName === 'TD' && !cell.hasAttribute('data-label') && heads[index]) {
          cell.setAttribute('data-label', heads[index]);
        }
      });
    });
  });
  const year = document.querySelector('[data-year]');
  if (year) year.textContent = String(new Date().getFullYear());

  /* Contact form: no backend, so compose the message and hand it to the mail client.
     Every sentence a visitor can read lives in the markup rather than here: the form
     says which label each field carries in the email and which message to show when
     something is missing. That keeps this file free of language, so the same script
     serves the Italian and the English form without a branch. */
  const form = document.querySelector('[data-mailto-form]');
  if (form) {
    const to = form.dataset.mailtoForm;
    const status = form.querySelector('.form__status');
    const say = (message, state) => {
      if (!status) return;
      status.textContent = message;
      status.dataset.state = state;
    };
    const answered = field => field.type === 'checkbox'
      ? field.checked
      : String(field.value).trim() !== '';
    form.addEventListener('submit', event => {
      event.preventDefault();
      const fields = Array.prototype.slice.call(form.querySelectorAll('[data-mail-label]'));
      if (fields.some(field => field.hasAttribute('required') && !answered(field))) {
        say(form.dataset.msgIncomplete, 'error');
        return;
      }
      if (!form.checkValidity()) {
        say(form.dataset.msgInvalid, 'error');
        return;
      }
      const lines = [];
      fields.forEach(field => {
        if (field.type === 'checkbox') return;
        const value = String(field.value).trim();
        if (!value) return;
        /* a field without a label is the message: it goes last, after a blank line */
        if (field.dataset.mailLabel) lines.push(field.dataset.mailLabel + ': ' + value);
        else lines.push('', value);
      });
      // Append attribution for lead source tracking.
      const attr = window.titechAttribution || {};
      const attrLines = [];
      if (attr.source) attrLines.push('Fonte: ' + attr.source);
      if (attr.medium) attrLines.push('Mezzo: ' + attr.medium);
      if (attr.campaign) attrLines.push('Campagna: ' + attr.campaign);
      if (attr.landing) attrLines.push('Landing: ' + attr.landing);
      if (attr.referrer) attrLines.push('Referrer: ' + attr.referrer);
      if (attrLines.length) {
        lines.push('', '--- Attribuzione ---');
        attrLines.forEach(l => lines.push(l));
      }
      const href = 'mailto:' + to + '?subject=' +
        encodeURIComponent(form.dataset.msgSubject + ' · ' + String(fields[0].value).trim()) +
        '&body=' + encodeURIComponent(lines.join('\n'));
      say(form.dataset.msgSent.replace('{email}', to), 'ok');
      // Track conversion for any active A/B test.
      if (window.titechExperimentConvert) {
        Object.keys((window.titechExperiments || {}).assignments || {}).forEach(name => {
          window.titechExperimentConvert(name);
        });
      }
      document.dispatchEvent(new CustomEvent('titech:contact-submit', { detail: { form: 'contact_page' } }));
      window.location.href = href;
    });
  }
  /* Below 960px the navbar hides both its links and its CTA, so a phone visitor
     has exactly one path to a human: opening the hamburger. This bar appears
     after the first screen of scrolling and never on the contact page, where the
     form already is the whole point. The number is read from the footer rather
     than written here, so the NAP stays a single fact in the markup. */
  const napLink = document.querySelector('.footer__nap a[href^="tel:"]');
  const number = napLink ? napLink.getAttribute('href').replace(/\D/g, '') : '';
  /* the footer link already carries the prefilled first message, in the right
     language, so the bar copies its href instead of inventing a second one */
  const waLink = document.querySelector('.footer__nap a[href^="https://wa.me/"]');
  if (number && !/\/contatti\/|\/contact\//.test(location.pathname)) {
    const english = (document.documentElement.lang || 'it').slice(0, 2) === 'en';
    const bar = document.createElement('nav');
    bar.className = 'mbar';
    bar.setAttribute('aria-label', english ? 'Quick contact' : 'Contatto rapido');
    bar.innerHTML =
      '<a class="mbar__wa" href="#">' +
      (english ? 'WhatsApp' : 'Scrivi su WhatsApp') + '</a>' +
      '<a class="mbar__tel" href="tel:+' + number + '">' +
      (english ? 'Call' : 'Chiama') + '</a>';
    /* setAttribute, not a string inside innerHTML: a message typed later into the
       footer could contain a quote, and markup should not be built out of text */
    bar.querySelector('.mbar__wa').setAttribute('href',
      waLink ? waLink.getAttribute('href') : 'https://wa.me/' + number);
    document.body.appendChild(bar);
    const toggle = () => {
      const shown = window.scrollY > innerHeight * 0.6;
      document.documentElement.classList.toggle('mbar-on', shown);
    };
    addEventListener('scroll', toggle, { passive: true });
    toggle();
  }
})();
