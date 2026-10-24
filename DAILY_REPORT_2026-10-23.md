# Worklane Tools · US English Tool Matrix · Daily Research & Build Report

**Research date:** 2026-10-23 (Asia/Shanghai) · **Cycle:** 6 · **Status:** Five new functional local-first H5 prototypes built; **not publicly deployed**.

## Executive decision

- **5 distinct jobs-to-be-done investigated; 5 English H5 tools implemented; catalog and idea history now total 30.** All 25 previous application source files were byte-for-byte preserved.
- **Priority validation:** VisitFloor (handyman minimum service-call economics) and ClientRename (photo filename batch ZIP) have the clearest immediate task completion. Neither has demonstrated US search demand, repeat usage or paid conversion yet.
- **Publishing gate:** All new tools have `approved_for_index=false`, `evidence_reviewed=false`, `qa_verified=false`. Preview build uses `noindex,follow`, a disallow-all robots.txt and an empty sitemap. This is intentional, not a claim of search readiness.
- **Revenue:** No public deployment, verified Search Console property, AdSense publisher ID, ad approval or actual advertising revenue. No estimates of CPC, RPM, keyword volumes or income are presented as facts.

## Research methodology and data quality

Source discovery: English-language user discussions on Reddit, paired with adjacent competitors' official pricing pages (verified on 2026-10-23). A Reddit complaint is evidence that **a problem exists for the author**, not proof of a large underserved US market or purchase intent. For most posts the author's US residency is **unverified**; the warranty case is explicitly tagged US-PA, and the handyman thread contains self-reported US state responses. Search intent is hypothesized; Google Keyword Planner, Search Console, Ahrefs/Semrush and AdSense data were **not accessible**. Scores below are subjective prioritization (not success probabilities).

### 1. VisitFloor — 78/100 · P1 · Independent handymen

- **Original user signal (2026-07-02):** [What is your minimum? — r/handyman](https://www.reddit.com/r/handyman/comments/1ul50tb/what_is_your_minimum/). Respondents disagree about $25–$225+ minimum visits and point out that drive time, truck costs, insurance and admin change the economics. Some self-report US states. This is a pricing discussion, **not** evidence of demand for another calculator.
- **Audience/JTBD:** Solo handymen quoting 15–60-minute repair calls; set a transparent visit minimum that covers both unbillable travel and direct costs.
- **Current workaround:** A flat minimum, hourly rate, spreadsheets or full field-service quoting SaaS.
- **Adjacent competitor/price:** [Jobber Core](https://www.getjobber.com/pricing/) — normal **$29/month when billed annually** for one user on the official pricing page (temporary promotions are separately displayed). Jobber offers a far wider workflow; price is not a direct feature comparison.
- **Gap hypothesis:** Simple cost-based visit floor (drive time + on-site time + truck + materials + overhead + margin), with CSV and customer-ready quote, without CRM setup.
- **SEO primary:** `handyman minimum service call fee calculator`; **long tails:** `handyman trip charge calculator`, `service call minimum price with travel cost`, `small handyman job pricing worksheet`.
- **Search/ad hypothesis:** Evergreen commercially adjacent queries may attract field-service software and insurance advertisers; US monthly volume, competition and CPC **unverified**.
- **Technical feasibility:** High (browser arithmetic, CSV and print); assumptions are user-supplied and taxes/insurance may be incomplete.
- **Validation:** Interview 5 US handymen and compare the recommended floor against 10 past real small jobs; measure whether they adopt a revised minimum or export a quote. Stop if it is only a one-time curiosity with no measurable decision impact.

### 2. ClientRename — 76/100 · P1 · Client-facing photographers

- **Original user signal (2024-07-02):** [Standard for naming final image files — r/photography](https://www.reddit.com/r/photography/comments/1dtwtoi). Photographer asks whether to keep camera filenames or create client-specific sequential names; comments describe different manual conventions.
- **Audience/JTBD:** Portrait, event and product photographers delivering a small finished JPG set; create consistent, client-readable filenames without editing originals.
- **Current workaround:** Lightroom export presets, Adobe Bridge, desktop bulk renamers and manual rename.
- **Adjacent competitor/price:** [Adobe Lightroom](https://www.adobe.com/products/photoshop-lightroom/plans.html) — **$11.99/month** on an annual plan billed monthly; has many other capabilities.
- **Gap hypothesis:** No account, preview naming collisions and generate one ZIP of renamed JPG/PNG/WebP copies. Existing free alternatives are strong.
- **SEO primary:** `batch rename photos for client delivery online`; **long tails:** `client photo file naming generator`, `rename wedding photos sequentially zip`, `browser local batch rename JPG files`.
- **Search/ad hypothesis:** Evergreen file-workflow query, potentially adjacent to photography software and storage; search volume and CPC **unverified**.
- **Technical feasibility:** Medium; browser-local uncompressed ZIP is implemented, with 100-file/120 MiB cap. No RAW, EXIF editing, gallery or upload.
- **Validation:** Give 5 US photographers 20 sample delivery files and measure total time vs Lightroom/Finder; require at least 3 to prefer the flow before SEO promotion. Test iOS Safari separately.

### 3. WarrantyNest — 75/100 · P1/P2 · Small rental owners

- **Original user signal (2025-01-26):** [Landlord US-PA: What are you using to track things?](https://www.reddit.com/r/Landlord/comments/1ia63vx). Author specifically wants to track which property an appliance belongs to, purchase date and warranty, in addition to other property records. [Supporting US-CT inventory discussion (2025-02-12)](https://www.reddit.com/r/Landlord/comments/1inaq8a).
- **Audience/JTBD:** Owners of 2–20 units; quickly find appliance model/serial/warranty expiry before paying for a repair.
- **Current workaround:** Excel, Quicken project notes, folders of receipts and calendar reminders.
- **Adjacent competitor/price:** [Stessa](https://www.stessa.com/pricing/) — **Essentials free**, **Manage $12/month billed annually**. Not a feature-equivalent warranty tracker; Stessa includes property bookkeeping and maintenance.
- **Gap hypothesis:** Appliance-specific local inventory, expiry dates and downloadable ICS reminder calendar without a full property management platform.
- **SEO primary:** `rental property appliance warranty tracker`; **long tails:** `landlord appliance warranty expiry calendar`, `rental appliance serial number inventory spreadsheet`, `appliance warranty reminder ICS export`.
- **Search/ad hypothesis:** Evergreen warranty and maintenance need, potential warranty/repair advertisers; volumes and CPC **unverified**.
- **Technical feasibility:** High for inventory/CSV/ICS, but warranty eligibility depends on registration and manufacturer rules. No automatic alerts or cloud backup.
- **Validation:** Test 5 US landlords with at least 10 appliances each; require successful calendar import and correct manual verification of warranty terms.

### 4. RushQuote — 72/100 · P2 · Freelancers and writers

- **Original user signal (2026-07-02):** [First time freelance writer wants to include rush fee in retainer agreement — r/freelance](https://www.reddit.com/r/freelance/comments/1ul99p5/need_advice_first_time_freelance_writer_wants_to/). Writer worries about 12–24-hour urgent requests and proposes a 25% premium. [Corroboration (2026-06-13)](https://www.reddit.com/r/Freelancers/comments/1u4ux5n/do_you_charge_more_for_rush_jobs/).
- **Audience/JTBD:** Freelancers quoting a last-minute task; communicate the rush premium and extra labor cost explicitly before agreeing.
- **Current workaround:** Rule-of-thumb surcharge, email negotiation, ad-hoc calculator or proposal software.
- **Adjacent competitor/price:** [Bonsai Essentials](https://www.hellobonsai.com/pricing) — **$25/user/month billed monthly**, or **$19/user/month billed annually**, for broader client and proposal management.
- **Gap hypothesis:** Compare percentage surcharge with incremental overtime cost at a target margin; copy a conditional client quote.
- **SEO primary:** `freelance rush fee calculator`; **long tails:** `urgent project surcharge calculator`, `freelance quick turnaround fee quote`, `rush job price premium calculator`.
- **Search/ad hypothesis:** Narrow commercial query with proposal/invoicing adjacency; search volume, competition and CPC **unverified**.
- **Technical feasibility:** High; calculation is simple but there is no universally valid rush percentage, and contracts vary.
- **Validation:** Show 5 US freelance writers/designers two rush requests; test whether they use the proposed wording and gain explicit client agreement. Risk: too narrow to sustain SEO traffic.

### 5. MeterSplit — 69/100 · P2 · Duplex owners and property managers

- **Original user signal (2024-10-09):** [Landlord: water billing question — r/Landlord](https://www.reddit.com/r/Landlord/comments/1g02spq). Duplex landlord with one meter asks how to divide a bill between 3-person and 2-person units. Replies dispute fairness and whether allocation is appropriate at all.
- **Audience/JTBD:** Small landlords seeking an understandable comparison of potential utility allocation assumptions.
- **Current workaround:** Equal split, occupancy-weighted spreadsheet, landlord pays bill, or installing submeters.
- **Adjacent competitor/price:** [Stessa](https://www.stessa.com/pricing/) — Essentials **free**; Manage **$12/month billed annually** (broad property management, not a shared-water allocation specialist). [Splitwise Pro](https://www.splitwise.com/pro) also supports custom splits, but its public page does **not** show a reliable price, so no price is asserted.
- **Gap hypothesis:** Explain fixed-base versus variable usage allocation, occupant-day assumptions and export CSV for discussion. **Not** a legal billing calculator.
- **SEO primary:** `shared water bill split calculator duplex`; **long tails:** `duplex water bill split by occupants calculator`, `shared utility meter allocation worksheet`, `rental water bill per person day calculator`.
- **Search/ad hypothesis:** Specific evergreen question, but jurisdiction-sensitive intent and competition; search volume/CPC **unverified**.
- **Technical feasibility:** High arithmetic feasibility; **higher legal/reputational risk**. Actual utility allocation law and lease restrictions may prohibit the method. Never suggest charging tenants based on an unverified formula.
- **Validation:** Interview US duplex owners in 2 states, have a local professional check legal disclosures, then test whether comparison CSV clarifies discussion without encouraging improper charges.

## Distinctness and historical continuity

Read and compared `content/history.json`, the catalog, previous 2026-10-19 through 2026-10-22 reports and intake records. 25 prior app source HTML files are byte-for-byte unchanged. Five new tasks are distinct from existing entries: shared-meter allocation vs rent proration; filename renaming vs contact sheets/cropping/backup capacity; minimum service-call economics vs room cleaning quotes; rush premium vs sustainable hourly rates/retainer hours; appliance warranty calendar vs vendor maintenance tasks/reserve budgets. Automated intake uniqueness check passed; it cannot prove all semantic differences.

## Engineering and quality checks

| Gate | Result |
|---|---|
| Catalog and persistent idea history | 30 entries / 30 apps |
| Prior source preservation | 25/25 previous app HTML files unchanged |
| JS syntax | 30/30 pass via Node `--check` |
| Static build and SEO safety QA | Pass: 30 pages, Meta, OG, schema, usage guide, internal links, robots/sitemap gate |
| New 5 mobile interactions | Pass using Chromium `set_content`, 390px viewport; no horizontal overflow or uncaught JS exceptions |
| Export behavior | CSV for 4 tools, valid ZIP with image bytes for ClientRename, ICS for WarrantyNest |
| Real localhost HTTP test | Blocked by execution environment's browser policy; **not** equivalent to a real HTTPS deployment test |
| Browser persistence and iOS Safari | Not validated on a real origin/device |
| New page index eligibility | 0/5 approved; `noindex` in preview |
| Advertising | Disabled; no approved publisher ID or `ads.txt` |

## Operations and revenue status

| Metric | Verified value |
|---|---|
| Source tools available locally | 30 |
| GitHub remote | Connected GitHub action requested interactive authorization; no remote repository inspected or written in unattended mode |
| Cloudflare/Vercel deployment | No authorized deployment target or owned production URL; not deployed |
| Public HTTPS URLs | None verified |
| Search Console | Not connected; indexed pages, impressions, clicks and CTR unavailable |
| Google sitemap submission | Not submitted; preview sitemap empty |
| AdSense site approval and publisher ID | Not verified / not configured |
| Actual ad revenue and RPM | No connected data; cannot report |

## Next steps

1. **Highest priority: unlock distribution.** Create/authorize a persistent GitHub repo and deploy to an owned domain via Cloudflare Pages or Vercel. Without this, 30 prototypes are inventory, not a search business.
2. Verify true owner contact, legal and privacy pages; run real-origin/mobile tests. Approve only a few original, useful pages after editorial review and then submit a legitimate sitemap to Search Console. Google indexing is discretionary, not guaranteed.
3. Validate VisitFloor and ClientRename with actual US users; measure task completion, time saved, repeat use and qualified organic search demand before further feature expansion.
4. Do not load AdSense until the site is approved, an actual publisher ID exists and privacy/consent mechanisms are compliant. No paid subscription buttons or backend billing are active.

**Business interpretation:** Creating five tools per day is technically repeatable, but the value of continuing this cadence falls sharply until there is a public site, real search feedback and a revenue channel. The next unit of effort should go to infrastructure and validation rather than unreviewed mass indexing.
