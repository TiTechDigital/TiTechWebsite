# Phase 11 — The monthly SEO intelligence loop

Numbering note: this is Phase 11 of the repository's own sequence (the README
runs Phase 5 to Phase 11). It is **Phase 7** of the roadmap shared in
conversation — "review what Search Console actually says, monthly". Same work,
two labels; the repository keeps its own.

The instruction that gives this phase its shape, from the roadmap:

> Instead of constantly creating new articles, improve pages that already have
> search visibility.

Everything below exists to make that sentence executable rather than inspiring.

---

## 1. The rule the month is spent on

**Pages in positions 5–20 first.** They are already seen by enough people that a
better page changes the number, and they are close enough that the next result
is a realistic target. A page in position 43 does not get rewritten; a page in
position 2 does not need anything. A new article is not published in the same
week as a rewrite, because the two effects cannot be told apart afterwards.

Maximum three changed pages per month. Not because the work is slow, but
because a month of Search Console data can only attribute three changes.

---

## 2. What to export, once a month, on the same day

Search Console → Performance → filter by nothing, date range **last 28 days**.

| Export | Dimension | Save as |
| --- | --- | --- |
| Pages | `Page` | `reports/2026-11/pages.csv` |
| Queries | `Query` | `reports/2026-11/queries.csv` |

Then, in the same screen, switch the date to the **previous 28 days** and export
the Pages report again as `reports/2026-10/pages.csv`. That second file is what
makes the "gaining / losing" sections possible; without it the script can only
read one period at a time.

Notes on the files, all handled by the script:

- The download button gives CSV with the UI's own column names. Both languages
  work: `Top pages`/`Pagine principali`, `Position`/`Posizione media`, `Clicks`/`Clic`.
- An Italian export separates values with `;` and writes `2.500` for two and a
  half thousand. The delimiter is sniffed and the thousands separator is
  recognised, so no re-typing is needed.
- Both reports are capped at 1000 rows. Absence of a page is a hint, never a
  verdict — the script says so in its own output.
- `reports/` is in `.gitignore`. Traffic data stays on this machine; the tooling
  and this document are what get committed.

---

## 3. The command

```bash
# this month, both dimensions
python tools/gsc_review.py reports/2026-11/pages.csv reports/2026-11/queries.csv

# this month against last month: who is rising, who is losing clicks
python tools/gsc_review.py reports/2026-11/pages.csv --previous=reports/2026-10/pages.csv

# ignore small noise
python tools/gsc_review.py reports/2026-11/pages.csv --min-impressions=200
```

What each printed section means, and what to do with it:

| Section | Read as | Action |
| --- | --- | --- |
| Pages with no impressions | the export listed a page at zero | check the indexing report before touching anything; a hub or a legal page stays |
| Published pages missing from the export | diffed against `sitemap.xml` | inspect the URL in Search Console; this is the only section that can find a page the UI never shows you |
| Opportunity band, positions 5–20 | the list this phase is about | pick three, rewrite the snippet, then the answer |
| CTR below the position band | seen and not chosen | title and meta description first, body second |
| Queries in the top 10 with a low CTR | the query is close, the snippet is not | same fix, at query level |
| Queries served by more than one page | cannibalisation | one target page keeps the query, the others link to it |
| Pages with almost no clicks | one or two clicks on real impressions | review, do not delete: it may be the only page for that intent |
| Gaining impressions since the previous period | what worked | do the same thing to a page that is not moving |
| Losing clicks since the previous period | seen less, or chosen less | snippet first, then check whether the query mix changed |

Two honest limits:

- **Cannibalisation needs a Query × Page export.** The two separate UI files
  cannot show it, because neither row carries both columns. It appears only from
  an API or Looker export that has both, and the script labels each file it reads
  (`pages`, `queries`, `query+page`) so you can see which case you are in.
- **The "roughly N more clicks" figure is an order of magnitude**, not a
  forecast: it applies the CTR that the band above the page's current position
  tends to hold (`BANDS` in `tools/gsc_review.py`) to the impressions the page
  already gets. It is there to rank the list, not to be reported as a result.

If you pass two exports of the same dimension as plain arguments, the script
prints a warning and keeps going, because their numbers get added together. One
period belongs in the arguments, the previous one in `--previous`.

---

## 4. What the loop still needs by hand

The script reads what Google gave us. Three things on the roadmap's list have no
export worth trusting, so they are read in the interface and written down:

1. **Backlinks.** Search Console → Links → "Top linked pages", "Top linking
   sites". Copy the two counts into the `notes` column of
   `docs/scorecard.csv`. No tool here invents a domain-rating number.
2. **Competitors.** Open the six queries that actually bring enquiries, in a
   private window with an Italian profile, and note who holds positions 5–20.
   That is the only competitor report this project can produce honestly.
3. **Organic lead conversion.** GA4, not Search Console.
   `docs/phase-6-measurement.md` §"Lead conversion rate, read in GA4" gives the
   five clicks to get the number; it goes into `organic_sessions`,
   `generate_lead` and `lead_rate` of the same scorecard row.

One row per week in `docs/scorecard.csv`, written once — the header is already
there, and a row is what makes the next month's comparison possible.

---

## 5. What is missing before the first loop can run

| Missing | Who unblocks it |
| --- | --- |
| Search Console property verified for `titechdigital.it` | the owner, only, in the property settings |
| `reports/` with at least two 28-day Pages exports | 20 minutes in the interface, once verified |
| At least one week of GA4 data after the consent choice | the owner's own browsing does not count; the site needs visitors first |
| Positions to compare against | nothing — the first month is the baseline, and that is normal |

Until the first export exists, this document describes a method that has never
run. That is worth saying plainly: the loop is not delivering anything yet, and
any number quoted from it would be invented.

---

## 6. What deliberately does not happen here

- No rank-tracker subscription, no API scraping of Google: the export is the
  record, and 28-day comparisons are enough to know if a change worked.
- No page deleted because it earns nothing. A hub, a legal page and a page that
  once produced an enquiry all stay.
- No "content refresh" that rewrites a page which is not in the 5–20 band,
  because the only reliable evidence that a rewrite was needed comes from that
  band.
- No new article in the same week as a rewrite (see §1).
