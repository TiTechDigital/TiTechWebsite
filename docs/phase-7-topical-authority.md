# Phase 7 — Advanced topical authority: topic clusters

A topic cluster is a pillar page plus a set of supporting articles, each
answering a distinct question, all linked together so that search engines and
visitors can move from the general to the specific and back.

The site already has the five pillars (`/servizi/...`) and four articles. Phase 7
adds the supporting articles and the internal links that make each pillar a
cluster instead of a single page.

Rules that keep a cluster honest:

- **One intent per article.** Two articles that answer the same question
  cannibalise each other. If two slugs feel interchangeable, merge them.
- **No keyword-variation pages.** "Sito web per ristoranti" and "Sito web per
  ristorazione" are the same page.
- **Every article links to its pillar** with a descriptive anchor, and the pillar
  lists every article in its cluster.
- **Every article links to at least one sibling** in the same cluster, so the
  graph is connected, not a star.
- **Articles link to services, not the other way around.** The service page is
  the commercial destination; the article is the entry point.
- **Bilingual parity.** Every Italian article has an English twin with the same
  structure and the same number of sections. The English version is a native
  rewrite, not a translation, but the outline is identical.
- **No fabricated data.** Case studies, metrics and client names appear only
  when they are real. Articles explain methods and decisions, not imaginary
  results.

---

## 1. The five clusters

### Cluster A — Realizzazione siti web (pillar: `/servizi/siti-web/`)

| Slug (IT / EN) | Intent | Distinct question |
|---|---|---|
| `quanto-costa-sito-web-italia-2026` / `website-cost-italy-2026` | Informational | How much does a website cost, and why no price list? (exists) |
| `wordpress-o-sito-su-misura` / `wordpress-vs-custom-website` | Decision | WordPress or custom: how to choose |
| `come-scegliere-hosting` / `how-to-choose-web-hosting` | How-to | How to choose hosting without overspending |
| `manutenzione-sito-web` / `website-maintenance` | Informational | What maintenance includes and what it costs |
| `seo-tecnica-siti-web` / `technical-seo-websites` | How-to | Technical SEO checklist for a website |
| `sito-web-responsive-guida` / `responsive-website-guide` | How-to | What responsive really means and how to test it |

### Cluster B — E-commerce (pillar: `/servizi/e-commerce/`)

| Slug (IT / EN) | Intent | Distinct question |
|---|---|---|
| `e-commerce-b2b-quando-conviene` / `b2b-ecommerce-when-it-pays-off` | Decision | When B2B e-commerce pays off (exists) |
| `piattaforma-e-commerce-come-scegliere` / `how-to-choose-ecommerce-platform` | Decision | How to choose an e-commerce platform |
| `catalogo-prodotti-e-commerce` / `ecommerce-product-catalog` | How-to | How to structure a product catalog |
| `pagamenti-e-commerce` / `ecommerce-payments` | How-to | Payment methods and checkout friction |
| `spedizioni-e-commerce` / `ecommerce-shipping` | How-to | Shipping, returns and logistics |

### Cluster C — Software su misura (pillar: `/servizi/software-su-misura/`)

| Slug (IT / EN) | Intent | Distinct question |
|---|---|---|
| `quando-serve-software-su-misura` / `when-you-need-custom-software` | Decision | When custom software beats off-the-shelf |
| `specifiche-software-su-misura` / `custom-software-specifications` | How-to | How to write a software brief that works |
| `integrazioni-erp-crm` / `erp-crm-integrations` | How-to | ERP/CRM integration without double entry |
| `api-per-aziende` / `apis-for-business` | Informational | What an API is and why it matters |
| `mvp-software-su-misura` / `mvp-custom-software` | How-to | How to scope an MVP |

### Cluster D — Automazione e AI (pillar: `/servizi/automazioni-ai/`)

| Slug (IT / EN) | Intent | Distinct question |
|---|---|---|
| `automazione-ai-pmi-5-processi` / `ai-automation-smes-5-processes` | How-to | Five automatable processes (exists) |
| `automazione-ai-costi-benefici` / `ai-automation-costs-benefits` | Decision | Costs and benefits of AI automation |
| `automazione-processi-senza-ai` / `automation-without-ai` | Informational | When rule-based automation is enough |
| `chatbot-aziendale-quando-ha-senso` / `when-a-business-chatbot-makes-sense` | Decision | When a business chatbot makes sense |
| `automazione-ai-dati-privacy` / `ai-automation-data-privacy` | Informational | Data and privacy in automation |

### Cluster E — SEO (pillar: `/servizi/seo/`)

| Slug (IT / EN) | Intent | Distinct question |
|---|---|---|
| `seo-tecnica-checklist` / `technical-seo-checklist` | How-to | Technical SEO checklist |
| `seo-locale-novara` / `local-seo-novara` | How-to | Local SEO for a service-area business |
| `contenuti-seo-come-scrivere` / `how-to-write-seo-content` | How-to | How to write content that ranks |
| `seo-vs-google-ads` / `seo-vs-google-ads` | Decision | SEO vs Google Ads |
| `misurare-seo` / `measuring-seo` | How-to | How to measure SEO results |

Each cluster has 5–6 articles. Across five clusters that is 27 new articles (54 pages
with twins). They are not written in one pass: the plan exists now, the articles
are added one cluster at a time, starting with the pillar that has the most
commercial value.

---

## 2. Status

| Cluster | Articles written | Articles planned | Notes |
|---|---|---|---|
| A - Siti web | 2 of 6 (`quanto-costa-sito-web-italia-2026`, `manutenzione-sito-web`) | 4 to write | First cluster started |
| B — E-commerce | 1 of 5 (`e-commerce-b2b-quando-conviene`) | 4 to write | |
| C — Software | 0 of 5 | 5 to write | |
| D — Automazione | 1 of 5 (`automazione-ai-pmi-5-processi`) | 4 to write | |
| E — SEO | 0 of 5 | 5 to write | |

---

## 3. Internal linking graph

For each cluster the links form a triangle, not a star:

- **Pillar → articles**: the service page lists every article in a `.tiles` block
  titled "Approfondimenti" / "Further reading", placed after the FAQ and before
  the CTA.
- **Article → pillar**: every article links to its pillar in the first section
  ("Questo articolo fa parte della guida su [servizio]") and in the CTA at the
  end.
- **Article → siblings**: each article links to at least two siblings in the
  same cluster, in the body where the topic comes up naturally. Not in a "related
  posts" box at the bottom — that is where links go to die.
- **Article → other clusters**: cross-cluster links only when the topic genuinely
  crosses (e.g. the hosting article links to the SEO article on performance).
  Max one cross-cluster link per article.

The blog hub (`/blog/`) gets a `.cards--posts` section per cluster, so a visitor
can browse by topic, not only by date.

---

## 4. Article template (same as the existing four)

Every new article uses the same structure so that `check_site.py` parity holds
and the reader always knows where to look:

1. Breadcrumb: Home → Blog → article
2. Head: eyebrow (`Blog · <category>`), h1, lead, byline (name, role, reading
   time, date)
3. `.takeaways` — 3–5 bullets, the answer in 30 seconds
4. `.toc` — numbered, one entry per section
5. Sections: 4–7, each with an id, an h2 and prose. Tables and `.checks` where
   they earn their place. No decoration.
6. FAQ: 3–5 `<details>` with real questions
7. CTA: one button to the pillar or contact page
8. Footer

JSON-LD: `Organization`, `BreadcrumbList`, `Person` (`#enea-muja`), `BlogPosting`,
`WebPage`, `isPartOf` the `Blog` node. Same as the existing articles.

Reading time: 6–10 minutes. Shorter is better, but an article under 800 words
rarely earns a cluster position.

---

## 5. What makes an article worth writing

Before writing, answer three questions:

1. **What question does this answer that no other page on the site answers?**
   If the answer is "the same as the service page", do not write it.
2. **What would make someone link to it or share it?** If nothing, it is a
   keyword page, not an article.
3. **Can I write it without inventing data?** If the answer needs a metric I do
   not have, either find a verifiable source or change the angle.

Articles that fail any of these three do not get written. A cluster of four good
articles beats a cluster of six padded ones.

---

## 6. Tools

`tools/check_clusters.py` validates cluster integrity:

- every article in a cluster links to its pillar;
- every pillar lists its cluster articles;
- no two articles in the same cluster share a slug;
- IT/EN parity: same articles in both languages;
- every cluster article is in `sitemap.xml`;
- hreflang reciprocity between article twins.

Run it after adding or moving an article, the same way `check_site.py` runs after
any page change.

---

## 7. Blocked on

| Item | Blocked by |
|---|---|
| Cluster articles beyond the first cluster | Writing time; one cluster per month is realistic |
| Real case studies in articles | Real shipped projects (Phase 5) |
| Metrics and benchmarks | Data from real projects, with client permission |
| Cross-cluster links | The target articles must exist first |

---

## 8. What not to do

- Do not create a page for every keyword variation.
- Do not write articles that are thinner than the service page they support.
- Do not add a cluster before its pillar is stable and indexed.
- Do not duplicate the pricing article's ranges in a new article; link to it.
- Do not publish a cluster in one language only.
