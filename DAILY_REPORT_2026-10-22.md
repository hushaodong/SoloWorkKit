# Worklane Tools · US demand and H5 matrix daily report

**Date:** 2026-10-22 · **Cycle:** 5 · **Market:** US English (source geography may be unverified)

## Executive result

Five new, distinct JTBDs were researched and implemented as functional, mobile-friendly, English-language H5 tools. The existing 20 original application source files were byte-for-byte preserved. The catalog and durable idea history now contain **25 entries**. All new tools are **candidate prototypes (`noindex`)**; the local preview `robots.txt` disallows crawlers and the sitemap has zero URLs. **No public deployment, verified Google indexing, approved AdSense account, publisher ID, or revenue has been observed.**

Opportunity scores are *subjective triage rankings*, not conversion probabilities. Keyword volumes, search difficulty, CPC and ad RPM were not verified. An English-language Reddit discussion is not necessarily a US-resident user; US origin is explicit for the Ohio landlord discussion but unconfirmed for most other evidence.

## Five demand investigations

### 1. MarginWatch — 82/100 · P1 · Freelancers / fixed-fee project owners

- **Original pain (2026-02-17):** A freelance web developer reports a 60-hour quoted project that consumed 94 hours and asks for project profitability *during* execution, not after the invoice. [Original Reddit thread](https://www.reddit.com/r/webdev/comments/1r7cdjy/how_do_you_track_project_profitability_as_a/).
- **JTBD:** Know whether the project is still profitable after actual hours, remaining effort and costs are included.
- **Current substitute:** Toggl time logs + invoices + spreadsheet/manual calculations.
- **Competitor and published price:** [Toggl pricing](https://toggl.com/pricing) — Free; Starter **$9/user/month billed annually**. The paid product covers broader time and capacity management, not an identical stand-alone calculator.
- **Unmet wedge:** A one-page fixed-fee *completion forecast*, not a full time-tracking suite. This is an opportunity hypothesis; competition already includes free spreadsheets.
- **SEO target:** `freelance project profitability tracker`; long tails: `fixed price project profit margin calculator`, `freelancer project hours budget tracker`, `project estimate vs actual cost tracker`.
- **Search and ad hypothesis:** Commercially relevant to invoicing/accounting software; intent is clear, but US search volume and advertiser CPC are unmeasured.
- **MVP:** Client quote, budget hours, internal labor rate, outside costs, work logs, remaining-hours forecast, profit/margin comparison, CSV export, browser-local persistence.
- **Technical and commercial risks:** User-supplied cost assumptions, no integrations, data stored only on this device; low defensibility against established platforms.
- **Validation:** Recruit 5 US freelance developers with recent fixed-price projects; measure whether the forecast reveals overruns they would otherwise miss and whether they return after a week. No paid claim until tested.

### 2. TravelBuffer — 77/100 · P1 · Mobile service businesses

- **Original pain (2021-11-01):** A service-business owner says appointment platforms do not reserve travel time before a client visit, making otherwise viable bookings conflict. [Original Reddit thread](https://www.reddit.com/r/smallbusiness/comments/qk22mc/scheduling_software_for_servicebased_business/).
- **JTBD:** Prevent travel and preparation buffers from overlapping another on-site booking.
- **Current substitute:** Manual calendar blocking or full scheduling SaaS.
- **Competitor and published price:** [Acuity Scheduling](https://www.acuityscheduling.com/pricing/) — Starter **$16/month billed annually** or **$20/month billed monthly**. This is an adjacent appointment platform, not proof it lacks all travel-buffer functionality.
- **Unmet wedge:** Offline conflict check and busy-time `.ics` export without account creation or calendar authorization.
- **SEO target:** `appointment travel time buffer calendar planner`; long tails: `mobile service appointment buffer calculator`, `client appointment travel time block ICS`, `on site service scheduling overlap checker`.
- **Search and ad hypothesis:** Niche but commercially oriented field-service scheduling intent; volumes/CPC unverified.
- **MVP:** Manual appointment entries, pre/post travel buffers, overlap detection, localStorage, CSV, UTC-timestamped iCalendar busy blocks.
- **Limitations:** No travel route estimate, live calendar sync, client booking portal or automated reminders. Verify imported event times and daylight saving handling on actual devices.
- **Validation:** Ask 5 on-site tutors, inspectors or consultants to import ICS and compare conflicts against their calendars.

### 3. PhotoVaultPlan — 75/100 · P1/P2 · Photographers

- **Original pain (2024-12-31):** A photographer describes accumulating many external drives and difficulty keeping them backed up; [original discussion](https://www.reddit.com/r/photography/comments/1hqi9gd). **Fresh corroboration (2026-10-15):** A thread discusses rising hard-drive costs and backup trade-offs; [original discussion](https://www.reddit.com/r/photography/comments/1x6oc1y/how_are_you_backing_up_your_photos_in_this_economy/).
- **JTBD:** Forecast years of RAW/video growth and cost of independent local/offsite copies before purchasing storage.
- **Current substitute:** Spreadsheets, multiple drives, NAS comparisons, backup subscription plans.
- **Competitor and published price:** [Backblaze Personal Backup](https://www.backblaze.com/cloud-backup/personal) — **$9/month or $99/year**; [Backblaze B2](https://www.backblaze.com/cloud-storage/pricing) — **from $6.95/TB/month**. **Different billing models and backup coverage; not directly equivalent.**
- **Unmet wedge:** Local sample-file average, 1–10-year archive growth, redundant drive counts, cost assumptions and CSV export.
- **SEO target:** `photography backup storage calculator`; long tails: `RAW photo storage size planner`, `photo backup hard drive cost calculator`, `photographer NAS vs cloud capacity estimate`.
- **Search and ad hypothesis:** Evergreen photo/storage shopping context; ads for drives/cloud could be relevant, but volumes/CPC/RPM are unknown.
- **MVP:** Browser-local file-size sample (no upload), RAW/photo count, annual video, growth, years, local copy count, drive capacity/price, user-entered cloud rate, yearly capacity table and CSV.
- **Limitations:** Capacity planning is not a backup service. Does not account for egress, retention, disk failures, NAS enclosures or restoring from backup.
- **Validation:** Interview 5 wedding or commercial photographers, compare forecast with real storage purchase decisions.

### 4. ReserveReady — 73/100 · P2 · Small US landlords

- **Original pain (2025-06-28):** An Ohio rental owner with seven single-family homes reports repairs consuming a 10–15% rent maintenance reserve and asks whether to build a larger buffer. [Original Reddit thread](https://www.reddit.com/r/realestateinvesting/comments/1lmdcsf).
- **JTBD:** Stress-test whether maintenance cash reserves survive a large unexpected repair at a specific time.
- **Current substitute:** Rent-percentage rule, separate savings accounts and spreadsheets.
- **Competitor and published price:** [Stessa](https://www.stessa.com/pricing/) — Essentials **free**, Manage **$12/month billed annually**, Pro **$28/month billed annually** (official listing).
- **Unmet wedge:** Fast multi-property contributions, explicit routine repairs and a 12-month shock scenario including *minimum* balance, not just year-end total.
- **SEO target:** `rental property maintenance reserve calculator`; long tails: `landlord emergency repair fund planner`, `rental maintenance budget percentage calculator`, `property repair reserve 12 month forecast`.
- **Search and ad hypothesis:** Evergreen landlord budgeting and property-service intent, but free alternatives are strong; volume/CPC unverified.
- **MVP:** Multiple properties, rent, repairs, target reserve, current balance, monthly contribution percentage, one-time repair month, 12-month projection, CSV, localStorage.
- **Limitations:** No vacancy, financing, insurance, capex schedules, legal or tax modeling. It is a scenario, not a financial recommendation.
- **Validation:** Have US landlords compare scenarios with their current maintenance-reserve spreadsheets and ask whether a monthly planning workflow is useful.

### 5. ConcreteYield — 68/100 · P2 · Contractors / DIY concrete buyers

- **Original pain (2024-06-14):** A user planning an 8 × 10 × 6-inch pad questions a calculator's high number of 30 kg concrete bags. [Original Reddit thread](https://www.reddit.com/r/Concrete/comments/1dg3mm4/how_many_bags/). **US user origin not verified**; the use of kilograms may suggest another market.
- **JTBD:** Combine slab and post-hole quantities and estimate bags with explicit product yields and overage.
- **Current substitute:** Product manufacturer calculator, manual math, paper takeoff.
- **Competitor and published price:** [QUIKRETE free concrete calculator](https://www.quikrete.com/calculator/main.asp); official technical training lists approximate **0.60 ft³ per 80 lb bag and 0.45 ft³ per 60 lb bag** ([manufacturer PDF](https://www.quikrete.com/dealers/training/presentations/3-mixing-placing-concrete-cement-mixes-training.pdf)). No paid-price claim.
- **Unmet wedge:** Combine multiple slab/post-hole pours, configurable yield, overage, estimated bag cost and CSV takeoff. This is a *crowded free calculator* category.
- **SEO target:** `concrete bag calculator for multiple pours`; long tails: `concrete cubic yards and bags calculator`, `post hole concrete bag calculator with waste`, `concrete slab material takeoff CSV`.
- **Search and ad hypothesis:** Evergreen materials intent; suppliers and rental ads plausible, but broad competition is severe and CPC/RPM unverified.
- **MVP:** Rectangular and cylindrical volume, quantity, bag yields/custom yield, overage, material cost, CSV, localStorage.
- **Limitations:** No engineering, local code, product strength, mixing instructions or truck delivery quote. Verify actual product labels and site conditions.
- **Validation:** Compare with contractor orders and manufacturer calculators across 10 real takeoffs; abandon if no measurable time savings.

## Distinctness check

- Read `content/history.json` and all prior intake files; 20 previous tools preserved.
- New intent boundaries: **concrete volume/bags** (not drywall/tile), **photo backup capacity** (not crop/contact sheet), **maintenance reserve scenario** (not deposit deductions/lease reminders), **in-progress project margin** (not hourly rate/retainer/scope), **travel buffers and appointment overlap** (not any previous scheduling feature).
- Automated slug uniqueness and approximate textual similarity checks passed. This is not proof of complete semantic uniqueness; final acceptance requires human review.

## Build and QA

| Check | Result |
|---|---|
| Catalog and history | 25 tools / 25 idea entries |
| Previous 20 app source files | SHA-equivalent, no changes |
| JS syntax | 25/25 pass (`node --check`) |
| Build and SEO safety QA | Pass (`scripts/build.py`, `scripts/qa.py`) |
| New-tool Chromium interaction tests | 5/5 pass using injected HTML; includes 390px mobile layout, key calculations, CSV/ICS downloads and JS error checks |
| Preview SEO | All 25 `noindex,follow`; preview robots disallow all; sitemap empty |
| Ads | Disabled; no AdSense script or `ads.txt` |
| Live HTTPS routes / persistent storage across origin | **Not tested** (public deployment not configured; browser test used `set_content`) |

## Deployment, indexing and monetization

| Stage | Verified status |
|---|---|
| GitHub read/write | **Not available in this run:** connected GitHub action requested interactive authorization, impossible in unattended execution. No remote changes made. |
| Cloudflare Pages / Vercel deploy | **Not available:** no authorized target deployment project or verified production domain. |
| Public HTTPS site | Not verified / not deployed by this run |
| Search Console | No verified access; indexed URLs, impressions, clicks and CTR unavailable |
| Sitemap submission | Not submitted; local preview sitemap deliberately empty |
| AdSense | No approved site/publisher ID verified; no ads loaded |
| Revenue / RPM | No connected actual data; not estimated or invented |

### Priority next actions

1. Establish a persistent private GitHub repository and authorized deploy target with a real owned HTTPS domain. Current daily ZIP artifacts do not create a remotely updated site on their own.
2. Review privacy/contact/legal pages with true operator information, test local-storage behavior on a real origin, then approve *selected* tool pages for production indexing. Do not flip all 25 gates at once.
3. Connect Search Console and measure impressions, index status and task completion; only then optimize keyword pages or add compliant AdSense after approval.
4. Prioritize MarginWatch and TravelBuffer user validation; PhotoVaultPlan has strong hardware purchase intent but weaker repeat use.

**Safety principle:** no mass autoindexing, no fabricated keyword volumes or revenue, no automatic payment buttons and no claim of Google acceptance.
