/* Lead attribution: capture source, medium, campaign and referrer on the first
   visit of a session and keep them for every later conversion. No cookie is
   written; the data lives in localStorage and is attached to form submissions
   and to every analytics event. */
(() => {
  'use strict';

  const KEY = 'titech-attribution';
  const now = () => new Date().toISOString();

  const read = () => {
    try { return JSON.parse(localStorage.getItem(KEY)) || null; }
    catch (error) { return null; }
  };

  const write = (value) => {
    try { localStorage.setItem(KEY, JSON.stringify(value)); }
    catch (error) { /* private mode: attribution is lost, not blocking */ }
  };

  const params = new URLSearchParams(location.search);
  const existing = read();

  // First touch: only capture if we do not already have attribution, so a
  // later direct visit does not overwrite the original source.
  if (!existing) {
    const data = {
      source: params.get('utm_source') || (document.referrer ? new URL(document.referrer).hostname : 'direct'),
      medium: params.get('utm_medium') || (document.referrer ? 'referral' : 'none'),
      campaign: params.get('utm_campaign') || '',
      content: params.get('utm_content') || '',
      term: params.get('utm_term') || '',
      referrer: document.referrer || '',
      landing: location.pathname + location.search,
      first_visit: now(),
      sessions: 1
    };
    write(data);
  } else if (params.has('utm_source') || params.has('utm_campaign')) {
    // A new campaign visit: bump the session counter but keep first-touch data.
    existing.sessions = (existing.sessions || 1) + 1;
    existing.last_campaign_visit = now();
    write(existing);
  }

  const current = read() || {};

  // Expose for forms and analytics.
  window.titechAttribution = current;

  // Attach attribution as hidden fields to every mailto form on the page.
  const attach = (form) => {
    if (!form || form.dataset.attributionAttached) return;
    form.dataset.attributionAttached = 'true';
    const fields = [
      ['source', current.source],
      ['medium', current.medium],
      ['campaign', current.campaign],
      ['landing', current.landing],
      ['referrer', current.referrer]
    ];
    fields.forEach(([name, value]) => {
      if (!value) return;
      const input = document.createElement('input');
      input.type = 'hidden';
      input.name = 'attr_' + name;
      input.value = value;
      form.appendChild(input);
    });
  };

  const init = () => {
    document.querySelectorAll('form[data-mailto-form]').forEach(attach);
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
