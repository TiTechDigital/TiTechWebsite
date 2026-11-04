# Phase 9 — Case-study engine

Numbering note: this file is Phase 9 of the repository's own sequence (the README
runs Phase 5 to Phase 9). It is the **Phase 4** of the roadmap shared in
conversation — "build a case-study engine". Same work, two labels; the
repository keeps its own.

Every finished client project should produce seven things: a portfolio page, a
detailed case study, before-and-after screenshots, technical implementation
details, measurable results where available, a testimonial with permission, and
links to the service pages that were actually sold.

An instruction that lives only in a document is a promise. Here each of the
seven is also a line in `tools/check_site.py`, so a project page that is missing
one of them fails the build instead of shipping quietly.

---

## 1. What ships in the repository

- `assets/snippets/case-study-it.txt` — the Italian stamp: a complete,
  copy-paste inner page (head, nav, menu dialog, breadcrumbs, head block,
  byline, seven sections, footer, five scripts).
- `assets/snippets/case-study-en.txt` — the English stamp, structurally equal to
  the Italian one block by block.
- `audit_case()` in `tools/check_site.py` — the five refusals listed below.
- `case_rule()` in `tools/selftest.py` — proves the rule fires on an incomplete
  page and stays quiet on a complete one. Run `python tools/selftest.py`: the
  last line must read `12 of 12 defects caught`.
- `.quotes[data-single]` in `assets/css/pages.css` — a one-voice testimonial
  block, because a project has one client, not three.

Neither stamp is published. Files in `assets/snippets/` end in `.txt` on purpose:
`check_site.py` scans every `.html` on disk, so a `.html` stamp would be
audited as a page and would never pass.

---

## 2. The seven outputs and the line that enforces each

| Output | Block in the stamp | What the checker refuses |
|---|---|---|
| 1. Portfolio page | `lavori/<slug>/index.html` | a case page with no English twin fails the hreflang and twin-parity rules |
| 2. Case study | the seven `<section>` blocks | `<section>`, `<h2>` and `<tr>` counts differ between the two languages |
| 3. Before and after | two `figure.figure` in `#before-after` | `no image alt mentions "prima"` / `"dopo"` (`"before"` / `"after"` in English) |
| 4. Technical details | `table.table` in `#cosa-abbiamo-costruito` | `no .table with the technical specifics of the build` |
| 5. Measurable results | `data-results` on `#risultati` + `ul.facts` | `no data-results marker`, or `results claimed as verified without a .facts block` |
| 6. Testimonial | `blockquote.quote[data-permission]` | `a quote with no data-permission and no demo disclaimer` |
| 7. Links to services | `@@URL_SERVIZIO@@` in head actions and in the closing `.cta` | `no link to /servizi/` (`/en/services/` in English) |

`data-results` accepts exactly two values. `verified` means the numbers were
measured by someone and the `.facts` block names the source; `not-measured`
means they were not, and the section must say so. Any other value — including
the unfilled token — stops the page.

---

## 3. Tokens

Search the copy for `@@` and every hit has to become real text. `check_site.py`
reports `unfilled template token: [...]` and lists them, so a half-written page
cannot be published by accident.

| Token | Value |
|---|---|
| `@@CLIENTE@@` | the client's name, as they write it themselves |
| `@@SLUG@@` | the URL segment, lowercase, hyphens, no stopwords: `verde-casa` |
| `@@TITOLO@@` | the h1: the problem solved, not the software used |
| `@@PROGETTO_BREVE@@` | three or four words for `<title>`, og:title and `Article.headline` |
| `@@META_DESCRIZIONE@@` | 150–160 characters, factual |
| `@@SETTORE@@` / `@@ANNO@@` | the eyebrow line, e.g. `Arredo` · `2026` |
| `@@SERVIZIO@@` / `@@SERVIZIO_EN@@` | label of the service page that was sold |
| `@@URL_SERVIZIO@@` / `@@URL_SERVIZIO_EN@@` | absolute URL of that service page, used in the JSON-LD `about` reference |
| `@@DATA_PUBBLICAZIONE@@` / `@@DATA_AGGIORNAMENTO@@` | `YYYY-MM-DD`, both in the head and in the JSON-LD |
| `@@DATA_AGGIORNAMENTO_UOMO@@` | the same date in prose: `4 novembre 2026` / `4 November 2026` |
| `@@MISURATO@@` | `verified` or `not-measured` — nothing else |
| `@@NUM_1..3@@` | project commitments (duration, weeks, revisions), not results |
| `@@NUM_RIS_1..3@@` / `@@NUM_RESULT_1..3@@` | measured results, each with its source |
| `@@FONTE@@` / `@@SOURCE@@` | who measured, over which period, with which tool |
| `@@PERMESSO@@` | the written proof that the client approved name and quote |

Tokens left inside `@@...@@` in the stamps (guidance such as
`@@Paragrafo 1: la situazione precedente...@@`) are instructions: replace them
with real text, do not delete the block around them.

---

## 4. Publishing a case

1. Copy `case-study-it.txt` to `lavori/<slug>/index.html` and
   `case-study-en.txt` to `en/work/<slug>/index.html`. **Both, in the same
   session.** The hreflang pair is what makes the English page findable, and a
   one-language case fails the checker.
2. Delete the leading HTML comment in both files.
3. Fill every token. Check: `grep -c '@@' lavori/<slug>/index.html` must print 0.
4. Screenshots: two landscape captures per language, the same viewport for
   before and after. Save as
   `assets/img/casi/<slug>-prima-700.webp`, `-prima-1400.webp`, `-dopo-700.webp`,
   `-dopo-1400.webp`, and set `width`/`height` to the real pixel size of the
   capture so the layout reserves the space.
5. Write the results section last. If there is nothing measured, say so and
   name the tool that will measure it: `data-results="not-measured"`.
6. Ask for permission before writing the quote into the page (§5). Put the
   evidence string in `data-permission`.
7. Add the project to the hub: in `lavori/index.html` and `en/work/index.html`,
   give the matching `.card` an `href` and the class `card card--link`, and
   mirror the change in both languages.
8. Rebuild the sitemap: `python tools/build_sitemap.py`.
9. `python tools/check_site.py` must print `0 problems`.
10. `python tools/selftest.py` must print `12 of 12 defects caught`.
11. Preview at `http://127.0.0.1:8080/lavori/<slug>/` and on the phone. Two
    things to look at specifically: the table must not scroll sideways
    (`.table td:last-child` does not wrap — the last column holds short values
    only), and the alt text of both screenshots must read as a sentence.
12. Publish.

---

## 5. Asking for the testimonial

The quote is the client's words, received in writing. Send something like this
after delivery, never before:

> **IT** — Ti ho mandato una riga sul progetto, quella che preferisci: se ti
> va, la pubblico sul sito con il tuo nome e il ruolo. Scrivimi anche solo «ok,
> pubblica», così ho il consenso per iscritto. Se preferisci cambiare una
> parola, cambia pure: la riportiamo come la scrivi tu.

> **EN** — I wrote a short line about the project, the part you liked most: if
> you are happy, I would like to publish it on the site with your name and
> role. A one-line "yes, go ahead" is enough for me to keep it in writing. Feel
> free to change any word — we print what you write.

`data-permission` then holds the evidence, not the quote:
`data-permission="email del 3 ottobre 2026"`. A name without that line does not
go online; an anonymous sentence either stays out or carries
`class="tag-demo"` and says what it is.

---

## 6. What may never be written

The whole point of the rule is here. Google's guidance on people-first content
rewards original information and first-hand experience; a case study is the one
page where inventing either would be both the lie and the penalty.

- No invented SEO improvement: not "posizioni triplicate", not "traffico +200%".
  If Search Console was not connected during the project, the results section
  says the project had no measurement attached.
- No invented revenue, orders or leads. A number the client did not send or
  allow you to read does not exist.
- No before-and-after screenshots of something you did not build, and no
  reconstruction of a previous site that no longer exists. Say which half is
  missing.
- No `AggregateRating` or `Review` markup without real, dated, attributable
  reviews. The site publishes none today and the checker would not know; this
  rule is the only guard.
- No testimonial wording improved for rhythm. Typos in a quote stay, unless the
  client asks otherwise.

Demo material already on `/lavori/` is labelled: the six projects are fictional
and the page says so in a visible `.note`. That label goes away the day a real
case replaces them, not before.

---

## 7. Blocked input

Everything above is ready except the raw material: **there are no shipped
client projects yet.** The six cards on `/lavori/` are demos, so there is
nothing to write a case study about and nobody to ask permission from. This is
the same single blocker that gates the review engine in Phase 5 and the case-study
references in Phase 7.

When the first real project closes, the workflow in §4 is a one-afternoon job
per language.
