/* Margin calculator: rearranges the numbers a merchant already has. Nothing is
   guessed and nothing is looked up: no market average, no "typical AOV", no
   benchmark copied from a vendor deck. Every rate that decides a verdict lives
   on the form as a data-* attribute, so the Italian and the English copy cannot
   drift apart in arithmetic while they drift in wording.
   The sentences a reader sees all live in the markup: this file only adds and
   removes the `hidden` attribute and writes numbers. */
(() => {
  'use strict';

  document.querySelectorAll('[data-margin]').forEach(form => {
    const locale = form.dataset.marginLocale || 'it-IT';
    const money = new Intl.NumberFormat(locale, {
      style: 'currency', currency: 'EUR', maximumFractionDigits: 2
    });
    const moneyWhole = new Intl.NumberFormat(locale, {
      style: 'currency', currency: 'EUR', maximumFractionDigits: 0
    });
    const percent = new Intl.NumberFormat(locale, {
      style: 'percent', maximumFractionDigits: 1
    });
    const count = new Intl.NumberFormat(locale, { maximumFractionDigits: 0 });
    const ratio = new Intl.NumberFormat(locale, { minimumFractionDigits: 2,
                                                   maximumFractionDigits: 2 });
    const dash = '—';

    const field = name => form.querySelector('[data-margin="' + name + '"]');
    const value = name => {
      const input = field(name);
      /* an empty box is not zero: it means the reader has not typed it yet */
      if (!input || String(input.value).trim() === '') return null;
      const n = Number(input.value);
      return Number.isFinite(n) && n >= 0 ? n : null;
    };
    const out = name => form.querySelector('[data-margin-out="' + name + '"]');
    const write = (name, text) => { const node = out(name); if (node) node.textContent = text; };

    const thin = Number(form.dataset.marginThin || 0.08);
    const recalc = () => {
      const aov = value('aov');
      const cogsPct = value('cogs');
      const shipping = value('shipping');
      const feePct = value('fee');
      const feeFixed = value('feeFixed');
      const returnsPct = value('returns');
      const returnCost = value('returnCost');
      const cac = value('cac');
      const orders = value('orders');
      const fixed = value('fixed');

      const ready = [aov, cogsPct, shipping, feePct, cac, orders, fixed]
        .every(n => n !== null);
      const verdicts = Array.prototype.slice.call(form.querySelectorAll('[data-margin-verdict]'));
      const showVerdict = state => verdicts.forEach(node => {
        node.hidden = node.dataset.marginVerdict !== state;
      });

      if (!ready || aov <= 0) {
        ['unit', 'unitPct', 'profit', 'cacMax', 'beRoas', 'breakEven'].forEach(n => write(n, dash));
        showVerdict('incomplete');
        return;
      }

      /* what one order costs before marketing: goods, the courier, the payment
         fee and the share of returns this order is expected to carry */
      const goods = aov * cogsPct / 100;
      const payment = aov * (feePct || 0) / 100 + (feeFixed || 0);
      const returns = (returnsPct || 0) / 100 * (returnCost || 0);
      const variable = goods + shipping + payment + returns;
      const beforeMarketing = aov - variable;
      /* what one order leaves after the cost of acquiring it */
      const contribution = beforeMarketing - (cac || 0);
      const revenue = aov * orders;
      const profit = contribution * orders - fixed;

      write('unit', money.format(contribution));
      write('unitPct', percent.format(contribution / aov));
      write('profit', moneyWhole.format(profit));
      /* the highest acquisition cost an order can pay without losing money */
      write('cacMax', beforeMarketing > 0 ? money.format(beforeMarketing) : dash);
      write('beRoas', beforeMarketing > 0 ? ratio.format(aov / beforeMarketing) : dash);
      write('breakEven', contribution > 0 ? count.format(Math.ceil(fixed / contribution)) : dash);

      const margin = revenue > 0 ? profit / revenue : 0;
      /* an order can pay for itself and the month still not cover the rent, so
         the two states are not the same sentence */
      showVerdict(contribution <= 0 ? 'loss'
        : profit < 0 ? 'uncovered'
        : margin < thin ? 'thin' : 'ok');

      /* a slider shows its own number in the label, the way the cost
         calculator does; the markup says which output to write into */
      form.querySelectorAll('[data-margin-range]').forEach(input => {
        const node = out(input.dataset.marginRange);
        if (node) node.textContent = input.value;
      });
    };

    form.addEventListener('input', recalc);
    form.addEventListener('change', recalc);
    recalc();
  });
})();
