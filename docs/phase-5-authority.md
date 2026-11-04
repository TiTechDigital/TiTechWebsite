# Phase 5 — Authority: execution kit

Phase 5 is almost entirely off-site: it depends on accounts, clients and real
business data that do not live in this repository. What follows is the
operational part that can be prepared here, plus the exact inputs still missing.

What ships from Phase 5: the visible NAP strip in the footer of every published
page (name, Novara, phone) and the matching `telephone` + `PostalAddress` in the
structured data. Everything else in this file is operational, not code.

---

## 1. Canonical NAP record

Every directory, profile and footer must repeat **the same string**. Mismatches
between "TiTech", "TiTech Digital" and "TiTech Digital S.r.l." are the most
common reason a local entity never consolidates.

| Field | Value |
|---|---|
| Brand name (use everywhere) | `TiTech Digital` |
| Legal name | `[DA CONFERMARE]` |
| VAT | `IT02829190038` |
| Email | `info@titechdigital.it` |
| Phone | `+39 376 102 4080` |
| Street address | non pubblicato |
| City | `Novara` |
| Postcode / province | `[DA COMPLETARE]` |
| Country | `IT` |
| Website | `https://titechdigital.it` |
| Areas served | `Italia`, `Albania` |
| Languages | `italiano`, `inglese` |

The site now publishes name, city and phone in the footer of every page and in
the `Organization` structured data. Only the street address and postcode are
still missing; until they exist, use a service-area profile rather than a
street address on Google Business Profile.

Formatting rules:

- Phone in international form on every platform, e.g. `+39 02 1234 5678`.
  On Italian-only directories (PagineGialle) keep the same digits in local
  form (`02 1234 5678`) — never a different number.
- Address in the same order everywhere: street, postcode, city, province,
  country.
- Never add a second office or a co-working address "just for the listing".
  A second inconsistent address is worse than none.

Paste block for directory forms:

```
TiTech Digital
Novara, Italy
+39 376 102 4080
info@titechdigital.it
https://titechdigital.it
VAT IT02829190038
```

**Street address and postcode are still missing.** Google Business Profile can
work as a service-area business, so verification is not blocked, but the
address fields on PagineGialle and Europages will stay incomplete until they
exist.

---

## 2. Directory checklist

| Platform | What it needs | The trap |
|---|---|---|
| Google Business Profile | Verified address or service area, phone, category, hours, photos, services | Category "Website designer" plus a real service area; do not use a virtual office |
| Bing Places | Same record as GBP; supports import | After importing, re-check the phone format — it often rewrites it |
| Apple Business Connect | Apple ID, place card, hours, photos, action link | Needs a verified location; service-area-only businesses are limited |
| LinkedIn company page | Logo (300×300), cover (1128×191), tagline, industry, location | The website field is nofollow but drives branded search — keep it exact |
| Clutch | Client interviews, verified reviews, portfolio | Paid placement; only worth it once 3+ clients will take a call |
| Sortlist | Free listing, portfolio, services, budget range | Lead-gen inbox fills fast; set expectations on response time |
| GoodFirms | Free listing plus verification | Verification email often lands in spam |
| PagineGialle | VAT, address, phone, category | Italian category list is coarse; pick the closest, do not invent one |
| Europages | Company address, B2B categories, product/service list | B2B only — consumer wording reads wrong there |

Order of work: GBP → Bing Places → Apple → LinkedIn → PagineGialle →
Sortlist/GoodFirms → Clutch (last, because it needs client cooperation).

---

## 3. Review engine: 10–15 in 90 days

Reviews cannot be written for you, and they must not be invented. Publishing
fabricated reviews is an unfair commercial practice under the EU Omnibus rules
transposed in Italy in 2023, and Google removes gated or incentivised reviews.

Rules that keep the profile safe:

- Ask every client, not only the happy ones.
- Never offer a discount, gift or free work in exchange for a review.
- Never filter customers before asking ("leave a review if you were satisfied").
- One request per client per project. No follow-up chains.
- Reply to every review within 48 hours, including critical ones.
- Never paste the same review text on the site and on GBP as if independent.

90-day cadence:

| Weeks | Action |
|---|---|
| 1–2 | List every client delivered in the last 24 months. Pick the 20 most reachable. |
| 3–6 | Send 10 requests, five per week. Track who opened, who replied. |
| 7–10 | Send the next 10. Collect the first 5–8 reviews. |
| 11–13 | Reply to all. Add the best 3 (verbatim, with permission) to the site. |

Request email — Italian:

```
Oggetto: due minuti per una recensione?

Ciao [Nome],
spero che [progetto] stia lavorando bene.

Sto raccogliendo feedback verificabili sui progetti di quest'anno: se ti va,
puoi lasciare una recensione qui — bastano due minuti e puoi scrivere quello
che vuoi, anche i punti da migliorare.

[link diretto alla recensione Google]

Grazie,
[Nome]
TiTech Digital
```

Request message — WhatsApp, shorter:

```
Ciao [Nome], tutto bene con [progetto]?
Se ti va di raccontare com'è andata, questo è il link per la recensione:
[link]
Anche una critica è utile, purché sia vera. Grazie.
```

Follow-up, only once, after 10 days:

```
Ciao [Nome], ti riscrivo solo una volta: se la recensione non ti interessa
nessun problema, chiudo qui.
```

Where the site will show them: `assets/snippets/review-schema.txt` is ready,
but it must stay empty (`reviewCount: 0`) until real reviews exist. Never paste
it with placeholder values.

---

## 4. Portfolio surfaces

Behance, Dribbble and Awwwards mostly return nofollow links. They are worth it
for citations, referral traffic and credibility — not for PageRank.

Before submitting anything:

- Submit only work you actually shipped. The three case studies in the pricing
  article (Osteria Verde, Artigiano Casa, Studio Nova) are fictional and must
  never be presented as client work anywhere.
- One project per submission, with a clear problem → decision → result story.
- Six assets per project: hero, three process/detail shots, before/after, one
  outcome line with a verified metric or none at all.
- Awwwards and Dribbble reward craft, not SEO. A generic agency template will
  not pass review.

Each real project also deserves its own page under `/lavori/`, using
`assets/snippets/case-study-schema.txt` for the `CreativeWork` markup.

---

## 5. LinkedIn

Not a ranking factor. It matters because it creates branded searches, and
branded search is a well-documented signal of entity relevance.

Cadence that is sustainable for a small agency: one post per week, one comment
per day on Italian marketing/tech posts. Post types that work:

1. A build decision explained (why a component was hand-coded, why a stack was
   rejected) — no link in the post, link in the first comment.
2. A cost explanation using the published ranges, always labelled as market
   estimates.
3. A migration teardown with the numbers that changed, or an explicit "we don't
   have data for this yet".

Avoid: engagement bait, "excited to announce", stock-photo team posts.

---

## 6. Digital PR: one pitch per month

The pitch must rest on something verifiable. Right now the only publishable
data is the **market range table** in the pricing article, which is labelled as
estimates. The three case studies are fictional and cannot be pitched as data.

Angles that are honest today:

- "Quanto costa un sito web in Italia nel 2026: le fasce di mercato" — a
  price-orientation piece for business outlets.
- "Perché non pubblichiamo un listino" — an agency-transparency angle.
- "B2B e-commerce: quando conviene davvero" — with the order-volume formula.

Angles that need real data first: sector conversion benchmarks, average
delivery times, maintenance spend. Collect them from actual projects, with
client permission, before pitching them.

Pitch email:

```
Oggetto: fasce di prezzo per siti web in Italia, 2026

Ciao [Nome],
scrivo per [testata] perché state coprendo [tema].

Ho pubblicato un'analisi sulle fasce di prezzo dei siti web in Italia nel
2026, con il metodo di calcolo e i limiti dichiarati: [link].

Se vi serve un commento su un preventivo gonfiato o su un'offerta da
poche centinaia di euro, sono disponibile.

[Nome]
TiTech Digital
```

Send to one outlet per month, personalised, no mass BCC. Track replies; two
follow-ups maximum.

---

## 7. What is blocked, and on what

| Item | Blocked by |
|---|---|
| GBP verification | Nothing on the site — needs the Google account and a service area |
| NAP consistency | Street address and postcode for the Italian directories |
| Review schema on site | Real reviews collected and verified |
| Portfolio submissions | At least one real, shipped, client-approved project |
| Digital PR with proprietary data | Client-side data and permission to publish |
| Footer credit rollout | Access to client sites |

Once the street address and postcode exist, they can be added to the visible NAP
strip and to the `PostalAddress` in all 44 pages in one pass.
