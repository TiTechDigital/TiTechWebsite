# Phase 8 — Conversion intelligence

Phase 8 stops optimizing for traffic and starts optimizing for revenue. The
metric that matters is:

    Organic revenue / Organic acquisition cost

Everything below serves that number. Traffic, impressions and keyword positions
are inputs, not outcomes.

---

## 1. What ships in the repository

- `assets/js/attribution.js` on all 47 documents: captures first-touch UTM
  parameters, referrer and landing page on the first visit, keeps them in
  `localStorage` under `titech-attribution`, and attaches them as hidden fields
  to every mailto form. The attribution block is also appended to the composed
  email body, so every enquiry arrives with its source.
- `assets/js/experiments.js`: deterministic A/B testing per visitor. Variant
  assignment is stored in `localStorage`; exposure and conversion events are sent
  through the measurement layer. Three experiments are active:
  `hero_headline`, `cta_primary`, `contact_headline`.
- `assets/js/measure.js` extended: every event now carries `source`, `medium`
  and `campaign` from the attribution module.
- Home and contact forms (IT + EN) include attribution in the mailto body and
  trigger `titechExperimentConvert` on submit.
- `data-exp` attributes on the hero headline, the primary CTA and the contact
  heading in both languages.

Nothing here writes to a backend. The site is still static; attribution and
experiments are client-side only.

---

## 2. A/B testing methodology

Rules that keep tests honest:

- **One variable at a time.** Never test a headline and a CTA color together.
- **Run for at least 4 weeks** or 200 sessions per variant, whichever is
  longer. Stopping early reads noise as signal.
- **Measure on qualified leads, not on clicks.** A variant that gets more
  `contact_submit` events but fewer real replies is worse, not better.
- **Promote the winner only after the test reaches significance.** With 20
  leads per month, that means 3–4 months per test.
- **Log every test** in the table at the end of this file: hypothesis, variant,
  metric, duration, result, decision.

Current experiments:

| Experiment | Control | Variant B | Metric |
|---|---|---|---|
| `hero_headline` | "Parliamone" / "Let's talk" | "Parliamo del progetto" / "Let's talk about the project" | `contact_submit` rate |
| `cta_primary` | "Parliamo del progetto" / "Let's talk" | "Raccontaci il progetto" / "Tell us about the project" | `contact_submit` rate |
| `contact_headline` | "Scrivici" / "Write to us" | "Raccontaci il problema" / "Tell us the problem" | `contact_submit` rate |

---

## 3. Industry-specific landing pages

The site already has three sector pages (`/settori/artigianato/`,
`/settori/ristorazione/`, `/settori/professionisti/`) with their English twins.
Each one carries the same structure but different examples, FAQs and CTAs.

To make them convert better:

- The CTA on a sector page should name the sector ("Scrivi per il tuo ristorante",
  not "Scrivi a TiTech").
- The form on a sector page could pre-fill the topic field with the sector.
- The first proof point should be sector-specific, not generic.

These are content changes, not code changes. They belong to Phase 7's cluster
work and Phase 5's portfolio work.

---

## 4. Streamlined quote forms

The current forms have five fields (name, email, company, message, consent) on
the contact page and five on the home (name, email, company, topic, message).
The consent checkbox is legally required and stays.

Rules for keeping a form short:

- Every field must earn its place by changing the reply. If the answer does not
  change with the field, remove it.
- Company is optional and stays optional. It helps qualification but blocks
  nobody.
- The topic selector on the home form replaces a free-text "what do you need"
  question. Keep it.
- Do not add phone number, budget range or timeline to the form. Those come out
  in the first reply, not in the form.

If a shorter form is needed for a specific campaign, create a dedicated landing
page with three fields (name, email, message) instead of trimming the main form.

---

## 5. WhatsApp and telephone conversion tracking

Already live in `measure.js`:

- `contact_click` fires on every `tel:` and `mailto:` link, with `method`
  (`phone`, `email`, `whatsapp`) and `placement` (footer, home_contact,
  page_intro, page_body, cta).
- `contact_submit` fires when a form hands the message to the mail client.

What is **not** tracked and cannot be: whether the email was actually sent,
whether the WhatsApp message was read, whether the phone was answered. Those are
manual.

GBP calls are tracked in Google Business Profile Insights, not in GA4. Log them
in the same lead spreadsheet.

---

## 6. Lead source attribution

First-touch attribution is captured by `attribution.js`:

- UTM parameters (`source`, `medium`, `campaign`, `content`, `term`) if present.
- Otherwise the referrer hostname, classified as `referral`.
- Otherwise `direct`.
- Landing page and timestamp.

The data is stored in `localStorage` under `titech-attribution` and attached to
every form submission (hidden fields + a text block in the email body). It is
also sent with every GA4 event.

Limitations:

- localStorage is per-browser. A visitor who switches device loses attribution.
- First-touch only. Last-touch and multi-touch require a backend.
- Private browsing loses attribution on close.

For a site at this volume, first-touch is enough. Multi-touch attribution at
50 leads per month is a vanity exercise.

---

## 7. CRM integration

The site has no backend and no CRM. The path forward:

1. **Now (no code):** a shared spreadsheet (`docs/scorecard.csv` plus a lead
   log) with columns: date, name, email, source, medium, campaign, landing,
   qualified (yes/no), value (estimated), status (open/won/lost), notes.
2. **When leads exceed 10/month:** connect a form backend (Formspree, a Vercel
   function, or a simple endpoint) that writes to a CRM via webhook. HubSpot
   free tier and Pipedrive are the two sensible options for a small agency.
3. **What to integrate first:** lead creation with source attribution. Not
   deal stages, not pipeline automation, not email sequences. Those come after
   the data is clean.

The form currently uses `mailto:`. Replacing it with a real endpoint is a
one-file change in `pages.js` and the home inline scripts: swap
`window.location.href = 'mailto:...'` for a `fetch()` to the endpoint. The
validation logic stays.

---

## 8. Follow-up automation

Do not automate follow-up until the manual process works and is documented.
When it does:

- **Day 0:** auto-reply confirming receipt, with a link to the relevant case
  study or article.
- **Day 3:** if no reply, a short check-in ("did the message arrive?").
- **Day 10:** if still no reply, close the thread politely.
- **After a won deal:** a thank-you with a review request (Phase 5 rules apply).

Automation runs from the CRM, not from the site. The site's only job is to
capture the lead with correct attribution.

---

## 9. Tracking qualified leads and closed deals

Definitions:

- **Lead:** an enquiry that arrived (email, phone, form, WhatsApp).
- **Qualified lead:** a lead where budget, timing and scope fit after the first
  reply.
- **Closed deal:** a signed proposal.

Tracking:

| Stage | Where it lives | Updated by |
|---|---|---|
| Lead | Lead log spreadsheet | Manual, on arrival |
| Qualified | Lead log spreadsheet | Manual, after first reply |
| Closed | Lead log spreadsheet + invoice | Manual, on signature |

Revenue attribution: each closed deal is tagged with the original source from
the lead log. Monthly: sum revenue by source, divide by cost per source.

Cost per source:

- Organic: hosting + domain + tooling, divided by months. No ad spend.
- GBP: zero direct cost, but time spent on the profile counts.
- Referral: time spent on the relationship.
- Paid (if ever): actual ad spend.

The ratio `Organic revenue / Organic acquisition cost` is the number that
decides whether SEO is worth continuing. If it is below 3 after 12 months, the
site is not working as a sales channel and the strategy needs rethinking, not
more content.

---

## 10. What not to optimize for

- Keyword rankings without revenue attached.
- Traffic from queries that never convert.
- Form submissions that never become replies.
- A/B test winners chosen on click rate instead of closed deals.
- Dashboard metrics that nobody acts on.

---

## 11. Experiment log

| Date | Experiment | Variant | Metric | Duration | Result | Decision |
|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — |

---

## 12. Blocked on

| Item | Blocked by |
|---|---|
| CRM integration | No backend; needs a form endpoint and a CRM account |
| Follow-up automation | CRM integration first |
| Revenue tracking | Real closed deals with attributed sources |
| A/B test results | Traffic and lead volume (months, not weeks) |
| Industry-specific CTAs | Content work (Phase 7) |
