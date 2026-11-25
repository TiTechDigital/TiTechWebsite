/* Inner-page motion layer.
   The engine is fetched only when it can be enjoyed: no JavaScript, a blocked CDN or
   prefers-reduced-motion all leave the page complete and static. Nothing is hidden
   before its animation runs, so a failed load can never blank the content. */
(() => {
  'use strict';

  const CDN = {
    engine: 'https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/gsap.min.js',
    scroll: 'https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/ScrollTrigger.min.js',
    lenis: 'https://cdn.jsdelivr.net/npm/lenis@1.3.4/dist/lenis.min.js'
  };

  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  const fetchScript = src => new Promise((resolve, reject) => {
    const script = document.createElement('script');
    script.src = src;
    script.async = true;
    script.onload = () => resolve();
    script.onerror = () => reject(new Error(src));
    document.head.append(script);
  });

  /* The rule above a row draws itself: a class and two CSS rules, no engine
     involved. It runs before the CDN is even contacted, so a slow or blocked
     library can never leave the first screenful of rows undrawn. Rows already on
     screen are revealed at once; the rest wait for the scroll, each one a beat
     after the previous. */
  const revealRows = () => {
    const pending = [];
    ['.tiles', '.steps', '.cases'].forEach(selector => {
      document.querySelectorAll(selector).forEach(list => {
        Array.prototype.slice.call(list.children).forEach((row, index) => {
          row.style.setProperty('--d', (index * 0.1).toFixed(2) + 's');
          pending.push(row);
        });
      });
    });

    let frame = 0;
    const draw = () => {
      frame = 0;
      const limit = window.innerHeight * 0.92;
      for (let index = pending.length - 1; index >= 0; index -= 1) {
        if (pending[index].getBoundingClientRect().top < limit) {
          pending[index].classList.add('is-in');
          pending.splice(index, 1);
        }
      }
      if (!pending.length) {
        window.removeEventListener('scroll', queue);
        window.removeEventListener('resize', queue);
      }
    };
    const queue = () => {
      if (frame) return;
      frame = requestAnimationFrame(draw);
    };

    draw();
    if (pending.length) {
      window.addEventListener('scroll', queue, { passive: true });
      window.addEventListener('resize', queue, { passive: true });
    }
  };

  const start = (gsap, ScrollTrigger) => {
    gsap.registerPlugin(ScrollTrigger);
    document.documentElement.classList.add('motion');

    /* smooth scrolling with the same inertia as the home page. Kept apart from the
       rest: if smooth scrolling is unavailable, native scrolling and every reveal
       below still work. */
    try {
      if (window.Lenis) {
        const lenis = window.lenis = new window.Lenis({ lerp: 0.09, anchors: { offset: -80 } });
        lenis.on('scroll', ScrollTrigger.update);
        gsap.ticker.add(time => lenis.raf(time * 1000));
        gsap.ticker.lagSmoothing(500, 33);
      }
    } catch (error) {
      window.lenis = null;
    }

    /* The hero's own arrival is pure CSS in pages.css, so the headline is never
       waiting on this file. All that is left here is the drift as it is passed. */
    const head = document.querySelector('.head');
    if (head) {
      gsap.to(head, {
        opacity: 0.7,
        y: -28,
        ease: 'none',
        scrollTrigger: { trigger: head, start: 'top 12%', end: 'bottom top', scrub: 0.5 }
      });
    }

    /* Three gestures, and nothing else. A heading is uncovered by a mask instead
       of fading in; the rule above a row draws itself across; a project photo
       arrives from behind a curtain. Paragraphs, tables, notes and the form
       never move: reading is not a performance. Every tween is created on entry,
       so a trigger that never fires leaves the element exactly as authored. */
    const uncover = element => gsap.fromTo(element,
      { clipPath: 'inset(0% -10% 100% -10%)', yPercent: 9 },
      { clipPath: 'inset(-25% -10% -25% -10%)', yPercent: 0, duration: 1, ease: 'expo.out', clearProps: 'clipPath,transform' });

    gsap.utils.toArray('.sect__top h2, .cta__title, .lost h1').forEach(heading => {
      ScrollTrigger.create({ trigger: heading, start: 'top 93%', once: true, onEnter: () => uncover(heading) });
    });

    /* a project photo is uncovered from the bottom, once */
    gsap.utils.toArray('.card__media img').forEach(image => {
      const frame = image.closest('.card__media') || image;
      ScrollTrigger.create({
        trigger: frame,
        start: 'top 93%',
        once: true,
        onEnter: () => gsap.fromTo(image,
          { clipPath: 'inset(100% 0% 0% 0%)', scale: 1.08 },
          { clipPath: 'inset(0% 0% 0% 0%)', scale: 1, duration: 1.15, ease: 'expo.out', clearProps: 'clipPath,scale' })
      });
    });

    /* an open FAQ changes the page height: keep the triggers honest */
    let refreshTimer = 0;
    document.querySelectorAll('.faq details').forEach(details => {
      details.addEventListener('toggle', () => {
        clearTimeout(refreshTimer);
        refreshTimer = setTimeout(() => ScrollTrigger.refresh(), 260);
      });
    });

    if (document.fonts && document.fonts.ready) document.fonts.ready.then(() => ScrollTrigger.refresh());
    window.addEventListener('load', () => ScrollTrigger.refresh(), { once: true });
  };

  const boot = () => {
    revealRows();

    fetchScript(CDN.engine)
      .then(() => Promise.all([fetchScript(CDN.scroll), fetchScript(CDN.lenis)]))
      .then(() => {
        if (!window.gsap || !window.ScrollTrigger) return;
        try {
          start(window.gsap, window.ScrollTrigger);
        } catch (error) {
          /* the page stays usable whatever happens on the way here */
        }
      })
      .catch(() => {
        /* offline or blocked: the static page is already complete */
      });
  };

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot, { once: true });
  else boot();
})();
