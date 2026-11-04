/* Article data layer: SVG charts and the indicative cost calculator.
   Same rule as pages.js: the file carries no language. Every string a reader
   sees (titles, axis units, tooltips, result labels) arrives through data-*
   attributes written in the page, so one script serves the Italian and the
   English article without a branch. Charts degrade to their fallback sentence,
   which the markup already provides, when this file never runs. */
(() => {
  'use strict';

  const NS = 'http://www.w3.org/2000/svg';
  const svgEl = (name, attrs) => {
    const node = document.createElementNS(NS, name);
    for (const key in attrs) node.setAttribute(key, attrs[key]);
    return node;
  };
  const number = (value, locale) => new Intl.NumberFormat(locale).format(value);

  /* an axis that never lies: always from zero, topped out at the first clean
     step of {1, 1.2, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10} × 10ⁿ above the data */
  const niceMax = raw => {
    if (raw <= 0) return 1;
    const base = Math.pow(10, Math.floor(Math.log10(raw)));
    for (const step of [1, 1.2, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10]) {
      if (step * base >= raw - 1e-9) return step * base;
    }
    return 10 * base;
  };

  const W = 640, H = 340, PAD = { l: 58, r: 16, t: 20, b: 42 };
  const plotW = W - PAD.l - PAD.r;
  const plotH = H - PAD.t - PAD.b;

  const fmtTick = (value, locale) =>
    (value % 1 === 0 ? number(value, locale) : number(+value.toFixed(1), locale));

  /* one floating tooltip per chart, fed by [data-tip] shapes; the same value
     is printed as a label or a dot title, so touch users lose nothing */
  const bindTips = (chart, svg) => {
    const tip = document.createElement('div');
    tip.className = 'chart__tip';
    tip.setAttribute('aria-hidden', 'true');
    chart.appendChild(tip);
    const move = (target, event) => {
      const box = chart.getBoundingClientRect();
      const x = event.clientX - box.left + 12;
      const y = event.clientY - box.top - 34;
      tip.textContent = target.getAttribute('data-tip');
      tip.style.transform = 'translate(' + Math.min(x, box.width - 10) + 'px,' + Math.max(y, 4) + 'px)';
      tip.dataset.show = '1';
    };
    svg.querySelectorAll('[data-tip]').forEach(shape => {
      shape.addEventListener('pointermove', event => move(shape, event));
      shape.addEventListener('pointerleave', () => { tip.dataset.show = '0'; });
    });
  };

  const frame = (data) => {
    const svg = svgEl('svg', { viewBox: '0 0 ' + W + ' ' + H, role: 'presentation' });
    const max = niceMax(Math.max(...data.series.flatMap(s => s.values)) * 1.02);
    const ticks = 4;
    for (let t = 0; t <= ticks; t += 1) {
      const y = PAD.t + plotH - (plotH * t) / ticks;
      svg.append(svgEl('line', { class: 'grid', x1: PAD.l, x2: W - PAD.r, y1: y, y2: y }));
      const label = svgEl('text', { class: 'axis axis-y', x: PAD.l - 10, y: y + 4 });
      label.textContent = fmtTick((max * t) / ticks, data.locale);
      svg.append(label);
    }
    svg.append(svgEl('line', { class: 'grid', x1: PAD.l, x2: PAD.l, y1: PAD.t, y2: PAD.t + plotH }));
    return { svg, max };
  };

  const drawLine = (chart, data) => {
    const { svg, max } = frame(data);
    const stepX = data.labels.length > 1 ? plotW / (data.labels.length - 1) : plotW;
    const yOf = value => PAD.t + plotH - (value / max) * plotH;

    data.labels.forEach((labelText, i) => {
      const x = PAD.l + stepX * i;
      const text = svgEl('text', { class: 'axis axis-x', x, y: H - 14 });
      text.textContent = labelText;
      svg.append(text);
    });

    data.series.forEach((series, sIndex) => {
      const alt = sIndex % 2 === 1;
      const points = series.values.map((value, i) =>
        [PAD.l + stepX * i, yOf(value)]);
      const path = points.map((p, i) => (i ? 'L' : 'M') + p[0].toFixed(1) + ' ' + p[1].toFixed(1)).join(' ');
      if (!alt && data.series.length === 1) {
        const area = svgEl('path', {
          class: 'area',
          d: path + ' M' + points[points.length - 1][0].toFixed(1) + ' ' + (PAD.t + plotH) +
             ' L' + points[0][0].toFixed(1) + ' ' + (PAD.t + plotH) + ' Z'
        });
        svg.append(area);
      }
      const line = svgEl('path', { class: 'line trace' + (alt ? ' line-alt' : ''), d: path });
      if (series.color) line.style.stroke = series.color;
      /* the draw-in animation needs the real length: dasharray here, dashoffset
         from the keyframe reading the same custom property */
      const len = points.reduce((acc, p, i) =>
        acc + (i ? Math.hypot(p[0] - points[i - 1][0], p[1] - points[i - 1][1]) : 0), 0);
      line.style.strokeDasharray = String(Math.ceil(len));
      line.style.setProperty('--len', String(Math.ceil(len)));
      svg.append(line);
      points.forEach((p, i) => {
        const dot = svgEl('circle', { class: 'dot' + (alt ? ' dot-alt' : ''), cx: p[0], cy: p[1], r: 4.5 });
        if (series.color) dot.style.stroke = series.color;
        dot.setAttribute('data-tip',
          data.labels[i] + ' · ' + series.name + ': ' + fmtTick(series.values[i], data.locale) + (data.unitSuffix || ''));
        svg.append(dot);
      });
    });

    if (data.axisUnit) {
      const unit = svgEl('text', { class: 'axis axis-unit', x: PAD.l, y: 12 });
      unit.textContent = data.axisUnit;
      svg.append(unit);
    }
    paint(chart, svg);
    bindTips(chart, svg);
  };

  const drawBars = (chart, data) => {
    const { svg, max } = frame(data);
    const groups = data.labels.length;
    const slot = plotW / groups;
    const barW = Math.min(56, (slot * 0.68) / data.series.length);
    const yOf = value => PAD.t + plotH - (value / max) * plotH;

    data.labels.forEach((labelText, g) => {
      const centerX = PAD.l + slot * g + slot / 2;
      const text = svgEl('text', { class: 'axis axis-x', x: centerX, y: H - 14 });
      text.textContent = labelText;
      svg.append(text);
      data.series.forEach((series, s) => {
        const offset = (s - (data.series.length - 1) / 2) * (barW + 6);
        const value = series.values[g];
        const x = centerX + offset - barW / 2;
        const y = yOf(value);
        const bar = svgEl('rect', {
          class: (data.series.length === 1 ? (g === 0 ? 'c-before rise' : 'c-after rise') : (s === 0 ? 'c-before rise' : 'c-after rise')),
          x, y, width: barW, height: Math.max(2, PAD.t + plotH - y), rx: 3
        });
        bar.setAttribute('data-tip',
          labelText + ' · ' + series.name + ': ' + fmtTick(value, data.locale) + (data.unitSuffix || ''));
        svg.append(bar);
        const valueText = svgEl('text', { class: 'bar-value', x: x + barW / 2, y: y - 7 });
        valueText.textContent = fmtTick(value, data.locale);
        svg.append(valueText);
      });
    });

    if (data.axisUnit) {
      const unit = svgEl('text', { class: 'axis axis-unit', x: PAD.l, y: 12 });
      unit.textContent = data.axisUnit;
      svg.append(unit);
    }
    paint(chart, svg);
    bindTips(chart, svg);
  };

  /* only the fallback sentence makes way for the SVG: the title, the legend
     and the illustrative-data caption are children the page owns */
  const paint = (chart, svg) => {
    const fallback = chart.querySelector('.chart__fallback');
    if (fallback) chart.replaceChild(svg, fallback);
    else chart.append(svg);
  };

  document.querySelectorAll('.chart[data-chart]').forEach(chart => {
    const type = chart.dataset.chart;
    let data;
    try {
      data = {
        labels: JSON.parse(chart.dataset.labels || '[]'),
        series: JSON.parse(chart.dataset.series || '[]'),
        unitSuffix: chart.dataset.chartSuffix || '',
        axisUnit: chart.dataset.chartUnit || '',
        locale: chart.dataset.chartLocale || 'it-IT'
      };
    } catch (error) {
      return; /* malformed attributes: the fallback sentence stays on screen */
    }
    if (!data.labels.length || !data.series.length) return;
    if (type === 'line') drawLine(chart, data);
    else drawBars(chart, data);
  });

  /* ── Calculator ─────────────────────────────────────────────────────────
     Every rate (base cost, per extra page, multiplier, weeks) lives on the
     <option>/<input> itself, so the formula here is arithmetic only. */
  document.querySelectorAll('[data-calc]').forEach(form => {
    const locale = form.dataset.calcLocale || 'it-IT';
    const money = new Intl.NumberFormat(locale, {
      style: 'currency', currency: 'EUR', maximumFractionDigits: 0
    });
    const kind = form.querySelector('[data-calc-kind]');
    const pages = form.querySelector('[data-calc-pages]');
    const design = form.querySelector('[data-calc-design]');
    const ints = form.querySelector('[data-calc-integrations]');
    const checks = Array.prototype.slice.call(form.querySelectorAll('[data-calc-add]'));
    const out = name => form.querySelector('[data-calc-out="' + name + '"]');
    const round50 = n => Math.round(n / 50) * 50;

    const recalc = () => {
      const option = kind.selectedOptions[0];
      const rates = option.dataset;
      const pageList = Math.max(Number(pages.value) || 0, Number(rates.included || 0));
      let subtotal = Number(rates.base) +
        Math.max(0, pageList - Number(rates.included)) * Number(rates.perUnit);
      subtotal *= Number(design.selectedOptions[0].dataset.mult || 1);
      subtotal += Number(ints.value) * Number(form.dataset.calcIntegrationCost);

      let pct = 0;
      checks.forEach(box => {
        if (!box.checked) return;
        const add = box.dataset.calcAdd;
        if (add === 'seo' || add === 'lang') pct += Number(box.dataset.pct);
        if (add === 'copy') subtotal += pageList * Number(box.dataset.perPage);
      });
      subtotal *= 1 + pct;

      const min = round50(subtotal * 0.85);
      const max = round50(subtotal * 1.3);
      if (out('min')) out('min').textContent = money.format(min);
      if (out('max')) out('max').textContent = money.format(max);

      const weeksBase = rates.weeks.split(',');
      const weeks = [
        Math.round(Number(weeksBase[0]) + pageList * Number(rates.weeksPerUnit) + Number(ints.value) * Number(rates.weeksPerIntegration)),
        Math.round(Number(weeksBase[1]) + pageList * Number(rates.weeksPerUnit) + Number(ints.value) * Number(rates.weeksPerIntegration))
      ];
      if (out('weeks')) out('weeks').textContent = weeks[0] + '–' + weeks[1];

      const maint = form.querySelector('[data-calc-maint]');
      const maintOut = out('maint');
      if (maint && maintOut) {
        /* the result line lives in the panel: show it only when maintenance
           was requested, and keep the checkbox itself always reachable */
        const line = maintOut.closest('.calc__maint');
        maintOut.textContent = money.format(Number(maint.dataset.yearlyMin)) + ' – ' +
          money.format(Number(maint.dataset.yearlyMax));
        if (line) line.hidden = !maint.checked;
      }
      if (out('pages')) out('pages').textContent = pages.value;
      if (out('ints')) out('ints').textContent = ints.value;
    };

    form.addEventListener('input', recalc);
    form.addEventListener('change', recalc);
    recalc();
  });
})();
