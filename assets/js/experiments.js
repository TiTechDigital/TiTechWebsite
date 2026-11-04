/* A/B testing: deterministic variant assignment per visitor, applied to any
   element carrying data-exp="name" and data-variant="text". Exposure and
   conversion events are sent through the measurement layer when it is active.
   With no measurement ID the assignments still happen and are visible in
   window.titechExperiments, so the setup can be checked without analytics. */
(() => {
  'use strict';

  const STORAGE_KEY = 'titech-experiments';

  const read = () => {
    try { return JSON.parse(localStorage.getItem(STORAGE_KEY)) || {}; }
    catch (error) { return {}; }
  };
  const write = (value) => {
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(value)); }
    catch (error) { /* private mode */ }
  };

  // Deterministic hash: same visitor + experiment = same variant every time.
  const hash = (text) => {
    let h = 0;
    for (let i = 0; i < text.length; i++) {
      h = ((h << 5) - h + text.charCodeAt(i)) | 0;
    }
    return Math.abs(h);
  };

  // Visitor id: reuse attribution landing or generate a stable random id.
  const visitorId = (() => {
    const key = 'titech-visitor';
    let id = null;
    try { id = localStorage.getItem(key); } catch (error) { id = null; }
    if (!id) {
      id = 'v_' + Math.random().toString(36).slice(2) + Date.now().toString(36);
      try { localStorage.setItem(key, id); } catch (error) { /* private mode */ }
    }
    return id;
  })();

  const isEn = (document.documentElement.lang || '').slice(0, 2) === 'en';

  // Experiment definitions: name -> array of variant values.
  // Variant 0 is always the control (original text). Language-aware.
  const EXPERIMENTS = isEn ? {
    'hero_headline': [
      "Let's talk",
      'Let\'s talk about the project'
    ],
    'cta_primary': [
      "Let's talk",
      'Tell us about the project'
    ],
    'contact_headline': [
      'Write to us',
      'Tell us the problem'
    ]
  } : {
    'hero_headline': [
      'Parliamone',
      'Parliamo del progetto'
    ],
    'cta_primary': [
      'Parliamo del progetto',
      'Raccontaci il progetto'
    ],
    'contact_headline': [
      'Scrivici',
      'Raccontaci il problema'
    ]
  };

  const assignments = read();
  const applied = {};

  const assign = (name) => {
    if (assignments[name]) return assignments[name];
    const variants = EXPERIMENTS[name];
    if (!variants || variants.length < 2) return null;
    const idx = hash(visitorId + ':' + name) % variants.length;
    assignments[name] = { variant: idx, value: variants[idx], assigned: new Date().toISOString() };
    write(assignments);
    return assignments[name];
  };

  const apply = () => {
    document.querySelectorAll('[data-exp]').forEach((el) => {
      const name = el.dataset.exp;
      const assignment = assign(name);
      if (!assignment || assignment.variant === 0) return; // control: leave as is
      const original = el.textContent;
      if (!el.dataset.expOriginal) el.dataset.expOriginal = original;
      el.textContent = assignment.value;
      applied[name] = assignment.variant;
      // Track exposure
      if (window.titechTrack) {
        window.titechTrack('experiment_exposure', {
          experiment: name,
          variant: String(assignment.variant),
          variant_value: assignment.value
        });
      }
    });
  };

  // Conversion: call window.titechExperimentConvert(name) on a successful lead.
  window.titechExperimentConvert = (name) => {
    const a = assignments[name];
    if (!a) return;
    if (window.titechTrack) {
      window.titechTrack('experiment_conversion', {
        experiment: name,
        variant: String(a.variant),
        variant_value: a.value
      });
    }
  };

  window.titechExperiments = { assignments, applied, EXPERIMENTS, visitorId };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', apply);
  } else {
    apply();
  }
})();
