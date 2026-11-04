# Phase 6 — Measure and prune

Phase 6 is a loop, not a dashboard: one weekly export, one monthly review, one
decision at a time. This file defines the numbers, the cadence, the twenty
keywords and the rules that decide what gets fixed, merged or left alone.

What already ships in the repository:

- `assets/js/measure.js` on all 45 documents (44 published pages + `404.html`).
  With an empty `<meta name="ga4-id">` it sets no cookie, makes no request and
  renders no banner. It does record events in memory (`window.titechEvents`) so
  the instrumentation can be checked before activation.
- Two events: `contact_click` (a phone or email link was clicked) and
  `contact_submit` (a form handed the message to the mail client).
- `tools/set_ga4.py` to switch the measurement ID on or off across the site.
- `tools/check_keywords.py` to keep `docs/keywords.csv` pointed at live pages.
- `tools/gsc_review.py` to turn Search Console exports into a fix/merge list.

What does **not** ship, because it needs accounts or real data: the GA4
property, Search Console access, GBP insights, a rank tracker and the manual
lead log. Section 8 lists them.

---

## 1. Definitions

Words that mean something specific here, so the monthly report cannot drift.

| Term | Definition |
|---|---|
| Click | A click from a Google result, Search Console. Not a visit, not a session. |
| Impression | The page appeared in a result the user could see. |
| CTR | Clicks / impressions for the same filter. |
| Position | Search Console average position across all queries a page appears for. It is not "the ranking" of a keyword. |
| Indexed page | A URL listed as indexed in Search Console → Indexing → Pages. |
| `contact_submit` | The visitor left the site for their mail program. **Not** a lead: the mail may never be sent. |
| `contact_click` | A phone or email link was clicked. Also intent, not a lead. |
| Lead | A real enquiry received (email, phone call or reply) and logged by hand. |
| Qualified lead | A lead where budget, timing and scope fit after the first reply. |
| Long-tail click | A click from a non-branded query that is not one of the 20 tracked terms. |
| Branded query | Any query containing `titech`. |

The rule that keeps this honest: **`contact_submit` never appears in the leads
column.** Only enquiries that actually arrived count.

---

## 2. Cadence

### Weekly — Monday, 20 minutes

1. Search Console → Performance → last 28 days, compared with the previous 28.
2. Export **Pages** and **Queries** as CSV to `reports/gsc-YYYY-MM-DD/`.
3. Search Console → Indexing → Pages: note indexed count and the reason for every
   newly excluded URL.
4. `python tools/gsc_review.py reports/gsc-YYYY-MM-DD/pages.csv reports/gsc-YYYY-MM-DD/queries.csv`
5. Add one row to `docs/scorecard.csv`.
6. Update the manual lead log and check GBP insights (calls, website clicks).

### Monthly — first Monday, 60–90 minutes

1. CrUX: PageSpeed Insights → field data for the origin. Before traffic exists
   this says "no data"; that is an answer, not a failure.
2. GA4 → Reports → Engagement → Events: `contact_submit`, `contact_click`.
   Compare them with the manual lead count.
3. Rank tracking: the 20 terms in `docs/keywords.csv`, location Novara, desktop
   and mobile separately. One device per run, always the same.
4. Prune review: apply section 5. At most two actions per month.
5. If a keyword is replaced, edit `docs/keywords.csv` and run
   `python tools/check_keywords.py`.

### Quarterly

1. Refresh the two pages with the steepest decline (see section 5).
2. Replace dead keywords with queries Search Console already shows.
3. Re-read the targets only with three months of data. Changing a target after
   two weeks is how a plan becomes decoration.

---

## 3. Targets

| Horizon | Target | Measured by | Leading indicator |
|---|---|---|---|
| 90 days | 12–18 pages indexed | GSC → Indexing → Pages, indexed count (of 44) | Pages discovered, sitemap fetches |
| 90 days | 30–60 organic clicks/month | GSC → Performance, total clicks | Impressions in the 11–20 positions |
| 90 days | First GBP leads | GBP insights + manual lead log | Profile views, calls, direction requests |
| 6 months | 3–5 keywords in the top 10 | Rank tracker, 20 keywords | Average position 11–20 trending up |
| 6 months | 8–12 real leads/month | Manual lead log | `contact_click`, `contact_submit` |
| 12 months | Top 3 for two `web agency <city>` terms and one service term | Rank tracker | Top 10 on the same terms |
| 12 months | 800+ organic clicks/month | GSC → Performance | 400–500 clicks/month at month 9 |

Three caveats, because the targets are ambitious and should stay honest:

- **12–18 indexed out of 44 is the right target.** A new domain does not get 44
  pages indexed in a quarter, and an indexed page that earns nothing is not
  progress. The number is a floor for the pages that can win clicks.
- **Two city terms cannot both be Novara.** The site publishes one city, one
  phone number and no street address; the only city term with a real claim is
  `web agency novara`. A second `web agency <city>` needs either a real local
  presence or a page with a reason to exist (clients, work, a local service).
  Options: replace it with a regional term (`web agency Piemonte`), with a
  service term (`realizzazione siti web`), or add the city only when a real
  project there exists. Do not add a city doorway page.
- **800 clicks/month is a head-term result, not a content-volume result.** It
  needs two or three commercial terms in the top 3. Publishing more articles
  will not get there on its own.

The 20 tracked keywords are in `docs/keywords.csv`, with the page each one is
supposed to win. Twelve Italian, eight English, one row per intent. The list is
deliberately small: twenty terms can be checked in ten minutes, two hundred
cannot.

---

## 4. Keywords: how the list is built

Selection rules:

- One term per page intent, not one per synonym. Two terms may share a page;
  two pages may not chase the same term.
- Italian first, because the Italian tree is the primary one. English terms are
  limited to the services that can realistically win abroad.
- No city terms except Novara, for the reason above.
- Every row must point at a canonical URL that exists. `check_keywords.py`
  enforces it.

Replacing a term is allowed. Adding a 21st is not: either a term earns its place
by replacing another, or the list stops being a weekly routine.

---

## 5. Pruning rules

Pruning means **merge with a 301**, not delete. A deleted URL loses whatever
history it had and returns a 404 to anyone who linked it.

| Signal | Threshold | Action |
|---|---|---|
| Not indexed after 90 days | Still excluded, no manual action | Read the reason. "Crawled, not indexed" = quality or duplication; "Discovered, not indexed" = crawl and internal links. Fix that, do not delete. |
| Zero impressions | 90 days, page in the sitemap | Rewrite title, H1 and first paragraph around the query it should serve. Re-check at 180 days. |
| CTR below the band | Position 1–3 and CTR < 10%; 4–10 and < 3%; 11–20 and < 1%, with 50+ impressions | Rewrite title and description first. The page is seen and not chosen. |
| Two URLs, one query | Same query, two pages, 10+ impressions each | Pick one target, link the other to it, differentiate or merge it. |
| Decay | Clicks down more than 30% for three consecutive months | Refresh facts and date. If still down after eight weeks, merge. |
| No traction | Fewer than 2 clicks in a quarter and no lead | Consolidate into the parent page. Keep it if it is the only page for that intent. |
| Never prune | Any page that produced a real lead in the last 12 months | Keep. |
| Never prune | Legal pages, hubs, contact, home | Keep. |

Consolidation procedure:

1. Choose the target: the page with more impressions or the better intent match.
2. Move the unique content into the target. Do not 301 to a page that does not
   answer the old query.
3. Add a 301 in `vercel.json` from the old URL to the new one. If the page has
   an English twin, redirect both.
4. Update internal links, `canonical`, `hreflang`, `sitemap.xml` and the entry in
   `docs/keywords.csv`.
5. Keep the redirect for at least 12 months.
6. Log the action in the pruning table at the end of this file.

Limits: two prunes per quarter, eight weeks before judging the result. Pruning
in a panic is how a site loses the pages that were about to work.

---

## 6. Reports and tools

Exports are private: `reports/` is gitignored and stays out of the repository.
Suggested layout:

```
reports/
  gsc-2026-11-04/
    pages.csv
    queries.csv
  gsc-2026-11-11/
    ...
```

`python tools/gsc_review.py pages.csv queries.csv` accepts the Italian and
English column names of the Search Console export and prints:

- pages with zero impressions;
- pages whose CTR is below the band for their average position;
- queries in the top 10 with a CTR under 2%;
- queries served by more than one page (only when the export contains both
  Query and Page columns, which the two separate UI exports do not);
- pages with almost no clicks.

It does not read the indexing export, which has a different shape. Indexing is a
manual check in the weekly routine.

`docs/scorecard.csv` is the weekly row. One line per Monday, no formulas that
hide the raw number. Columns:

`week,clicks,impressions,ctr,position,indexed,organic_sessions,contact_click_phone,contact_click_email,contact_click_whatsapp,contact_submit,generate_lead,leads,lead_rate,notes`

`leads` is typed by hand. It is the only column that decides whether the site
works. `lead_rate` is the same number as a percentage: `leads / organic_sessions × 100`,
written once the two inputs exist, not estimated from the others.

## Lead conversion rate, read in GA4

The ratio the roadmap asks for — leads divided by organic sessions — needs two
GA4 numbers that live in different reports. Build it once as an exploration, then
change only the date range each week:

1. **Explore → Custom (Free form)**.
2. Segmentation: add a segment filtered on `Session source / medium = google /
   organic`. Name it "Organic". This is the denominator, and it is the only
   segment that should ever be in the ratio.
3. Metric: `Sessions` (start with the unfiltered number, then the same inside the
   Organic segment).
4. Second metric: `Key events` with `generate_lead` marked as a key event in
   **Admin → Key events**. One row of the table, one moment: `contact_submit` and
   `generate_lead` fire together when a form hands its message to the mail
   client, so marking both as key events would count every lead twice.
5. Add `Page path and screen class` as dimension when the question is which page
   converts, and drop it when the question is how many leads the week produced.

At a few hundred sessions a month the percentage moves on one or two enquiries.
Read it as a direction over three months, never as a weekly score, and never as
proof that a page "works" while `leads` is still zero because nobody replied.

### Events the site does not send

The requested table also names `whatsapp_click`, `phone_click`, `quote_request`
and `booking_complete`. Three of them are deliberately absent:

- **`whatsapp_click` and `phone_click` are already there** under one name:
  `contact_click` with `method=whatsapp` and `method=phone`, plus `placement` for
  where the link sat (mobile bar, footer, CTA, page body). Two events for two
  methods would give the same information with twice the code.
- **`quote_request` is `generate_lead`.** The site has one enquiry path: the form
  on `/contatti/`. A separate `quote_request` would split a single action into
  two names depending on which button the visitor saw.
- **`booking_complete` needs something to book.** There is no calendar, no
  scheduling backend and no server code; a static site cannot confirm a booking.
  When consultations are bookable, the event comes with the integration, not
  before it.

Where to read each number:

- **Search Console** — Performance for clicks, impressions, CTR, position;
  Indexing → Pages for coverage; Queries for the long tail and the twenty terms.
- **CrUX / PageSpeed Insights** — field Core Web Vitals. It needs traffic. Until
  then use the lab section of PSI and Vercel Speed Insights, and write "no field
  data" in the report.
- **GA4** — Realtime for verification, Engagement → Events for
  `contact_submit`, `contact_click` and `generate_lead`. Mark only
  `generate_lead` as a key event (see the section above). There is no
  attribution modelling at this volume; do not pretend otherwise.
- **GBP** — Performance: calls, messages, website clicks, direction requests.
  These never appear in GA4.
- **Rank tracker** — the 20 terms, Novara, desktop and mobile. Treat it as an
  estimate; Search Console average position is the source of truth for queries
  the site actually appears for.

---

## 7. Activating GA4 (and the consent that goes with it)

The site currently promises, in `/cookie/` and `/en/cookies/`, that no analytics
run and that a banner will appear before any non-essential cookie is set. The
code keeps that promise: with an empty ID, `measure.js` does nothing.

Activation is one change, not two:

1. Create the GA4 property and the web data stream for `titechdigital.it`.
2. Turn off Google Signals and ads personalisation. Set data retention to 14
   months.
3. `python tools/set_ga4.py G-XXXXXXXXXX` (all 45 documents, one ID).
4. Update `/cookie/`, `/en/cookies/`, `/privacy/` and `/en/privacy/` in the same
   change. The banner appears automatically only when an ID is present; it
   stores the choice in `localStorage` under `titech-consent` and loads
   `gtag.js` only after acceptance.
5. Verify: reload, reject, confirm zero requests to `googletagmanager.com` in
   the network panel; accept, confirm page_view in Realtime; then mark
   `contact_submit` and `contact_click` as key events.
6. `python tools/set_ga4.py --off` reverts everything except the policy text.

Draft policy text, to review before publishing (not legal advice):

Italian, `/cookie/`:

> **Cookie di statistica** — Google Analytics 4, attivo solo con consenso:
> misura pagine viste e provenienza delle visite in forma aggregata. Cookie
> `_ga` e `_ga_<id>`, durata 13 mesi. — *Attivo con consenso*
>
> **Memoria locale** — salva la sola scelta sul consenso (`titech-consent`) nel
> browser. — *Attiva*
>
> Il banner compare una volta e chiede il consenso per Google Analytics. Se
> rifiuti, non parte nessuna richiesta a Google e nessun cookie di statistica
> viene scritto. Puoi cambiare scelta cancellando i dati del sito dal browser.

English, `/en/cookies/`:

> **Statistics cookies** — Google Analytics 4, only with consent: aggregate
> page views and traffic sources. Cookies `_ga` and `_ga_<id>`, 13 months. —
> *Active with consent*
>
> **Local storage** — stores only the consent choice (`titech-consent`). —
> *Active*

Privacy pages, both languages: add purpose (aggregate measurement), legal basis
(consent), recipient (Google Ireland Ltd, transfers under the standard
contractual clauses), retention (14 months in GA4, 13 months for the cookie) and
the right to withdraw consent by clearing the site data or rejecting the banner.

If the policy text cannot be updated in the same change, keep the ID empty. An
analytics tag without a matching policy is worse than no analytics.

---

## 8. What is blocked, and on what

| Item | Blocked by |
|---|---|
| GA4 measurement ID | The property does not exist yet; needs the Google account |
| Search Console weekly exports | Domain or URL-prefix property must be verified |
| GBP leads | Google Business Profile verification (Phase 5) |
| CrUX monthly | Traffic threshold; field data may be absent for months |
| Rank tracking | A tracker account, or GSC filtered per keyword |
| Real leads/month | Enquiries must arrive and be logged by hand |
| Second city term | A real presence or project in that city |
| Portfolio/case evidence for CTR | Real client work (Phase 5) |

---

## 9. Pruning log

Append one row per action. Empty until there is data.

| Date | URL | Signal | Action | Target | Review date |
|---|---|---|---|---|---|
| — | — | — | — | — | — |
