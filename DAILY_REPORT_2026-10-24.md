# Worklane Tools — Daily Research & Build Report

**Date:** 2026-10-24 (Asia/Shanghai)  
**Run:** Day 7; five new candidate H5 apps; 35 tools in cumulative local catalog.  
**Status:** Source code and preview build produced. **Not deployed. Not indexed. No advertising or subscription payments enabled.**

## 1. Decision summary

The next two opportunities to validate are **FenceBid** (a gate-aware, multi-run contractor estimate) and **WeddingFlow** (a photographer's ceremony-anchored timeline and booked-coverage conflict check). They have distinct, documented workflows and more plausible willingness to pay for professional time savings than generic single-form calculators. **MulchCompare** is a low-cost organic-search experiment, not a demonstrated paid SaaS opportunity. Scores are researcher judgments, not empirical conversion probabilities.

| Rank | Product | Opportunity score /100 | Priority | User value | SEO hypothesis (unverified) | Ads fit | Implementation |
|---|---|---:|---|---|---|---|---|
| 1 | FenceBid | 81 | P1 | Faster preliminary bids with gate-specific assumptions | Commercial/transactional, moderate competition | High: contractor estimating, materials | Low–medium |
| 2 | WeddingFlow | 80 | P1 | Less repetitive photo-day timeline editing; coverage check | Evergreen niche intent, moderate competition | Medium: CRM, galleries, wedding services | Medium |
| 3 | TurnoverBudget | 74 | P2 | Show owner repair costs plus lost rent, not deposit deductions | Evergreen landlord budgeting, medium competition | High: property software and services | Low |
| 4 | MulchCompare | 70 | P2 | Compare bag vs bulk delivered cost for multiple beds | High utility but strong free incumbents | Medium: local supply and landscape services | Low |
| 5 | FeeNet | 67 | P2 | Compare merchant fee structures and reverse-calculate gross needed | Broad high-competition utility query | Medium: payment products | Low |

**Scoring rubric:** pain intensity (25), evidence quality (20), differentiation (20), SEO intent/competition (15), commercial/advertiser fit (10), technical feasibility (10). We did not measure keyword search volume, CPC, keyword difficulty, organic traffic or willingness to pay; do not interpret these scores as forecasts.

## 2. Evidence and market notes

### A. FenceBid — fence installation estimate with gates (81/100)

- **Primary complaint:** 2025-04-30, r/FenceBuilding: contractor explains that a fixed per-linear-foot fence price misses gate size/count, grade, rocks and material variations, but clients expect an immediate price. Original: https://www.reddit.com/r/FenceBuilding/comments/1kb3yuv
- **Second contextual example:** 2024-07-08, r/Construction: first fence-job estimate lists 457 feet, 58 sections and two gates, asking peers to identify missing labor tasks. https://www.reddit.com/r/Construction/comments/1dyl6i8
- **Persona / JTBD:** small US fence contractor; *when* quoting a mixed fence run at a site, *help me* make a transparent materials/labor draft fast *so I can* follow up with a defensible written estimate.
- **Alternatives:** manual spreadsheets, per-foot rule of thumb, contractor CAD/estimating suites.
- **Competitor / price:** ArcSite offers fence drawing, takeoff, proposals and a **14-day trial followed by a paid subscription**. Official product: https://www.arcsite.com/ ; official trial policy: https://support.arcsite.com/en/articles/7258302-managing-your-arcsite-trial . **Current ArcSite dollar subscription rate not independently verified here.** This establishes adjacent paid software, not FenceBid willingness to pay.
- **Gap hypothesis:** quick multi-run/gate quantities without learning CAD or configuring a full price book. Actual need for this gap is not yet validated.
- **Core SEO:** `fence installation estimate calculator with gates`; long-tail: `fence post spacing and gate estimate`, `multi run fence cost calculator`, `fence panels posts labor quote worksheet`.
- **MVP:** multiple runs, gate width/count, estimated panel/post quantities, editable prices, contingency, itemized CSV and print. **Not an engineering/permit-ready design.**
- **SEO / monetization hypothesis:** professional search intent; relevant advertisers may be contractors' software and material suppliers. Test 20 user interviews/visits; goal ≥5 meaningful estimate completions and ≥2 requests for export/custom templates before adding paid features.

### B. WeddingFlow — photographer timeline planner (80/100)

- **Primary complaint:** 2025-09-13, r/WeddingPhotography: photographer says reconstructing a detailed wedding photo timeline and family-photo list in Word is tedious and time-consuming, and asks for a more efficient workflow. https://www.reddit.com/r/WeddingPhotography/comments/1ng9eg8
- **Supporting problem:** 2024-03-12, r/WeddingPhotography: photographer struggles to fit bridal/group photos between ceremony and sunset. https://www.reddit.com/r/WeddingPhotography/comments/1bd3z27
- **Persona / JTBD:** wedding photographer serving US couples; *when* receiving a couple's confirmed event details, *help me* assemble a realistic photo timeline with coverage warnings *so I can* coordinate with the planner quickly.
- **Alternatives:** Word/Google Docs templates, spreadsheets, Dubsado, photography CRM tools.
- **Competitor / price:** Dubsado official Starter **$35/month** or **$335/year**, Premier **$55/month** or **$525/year**; includes broader CRM features. Official: https://www.dubsado.com/llm-info . The discussion itself mentions Dubsado as a potential automation alternative.
- **Gap hypothesis:** a standalone ceremony-anchored planner with editable duration and coverage warning, no CRM onboarding.
- **Core SEO:** `wedding photography timeline planner`; long-tail: `photographer wedding coverage schedule calculator`, `wedding family portrait timeline maker`, `wedding photo timeline ICS export`.
- **MVP:** time anchor, editable pre/post blocks, booked-coverage conflict flag, CSV and ICS calendar export. Does **not** account for sunset, routes, timezone or complex event dependencies.
- **SEO / monetization hypothesis:** professional lead-gen intent; possible wedding-service ads or future premium timeline templates. Interview 10 working wedding photographers; target ≥3 who would reuse across clients.

### C. TurnoverBudget — owner-side rental turnover costs (74/100)

- **Primary complaint:** 2023-12-23, r/Landlord [US]: landlords compare widely varying tenant-turnover expenses including cleaning, paint, repair and lost vacant time. https://www.reddit.com/r/Landlord/comments/18p7478
- **More recent context:** 2026-07-29, r/Landlord [US-CA]: a landlord questions a $5–6k repaint estimate for a 2-bedroom rental unit. https://www.reddit.com/r/Landlord/comments/1v9ir3l/landlordusca_paint_turnover_costs/
- **Persona / JTBD:** owner of 1–10 rental units; *when* a unit becomes vacant, *help me* plan and track cleaning/repair spend and rent lost to vacancy *so I can* decide what work is economical.
- **Alternatives:** personal spreadsheets, bookkeeping tools, property management suites.
- **Competitor / price:** Stessa Essentials **free**, Manage **$12/month billed annually** or **$15/month billed monthly**. Official: https://www.stessa.com/pricing/ . This is an adjacent full product, not a direct replacement.
- **Gap hypothesis:** transparent turnover-specific worksheet distinct from security-deposit deductions and general maintenance reserve budgets.
- **Core SEO:** `rental turnover cost calculator`; long-tail: `landlord vacancy loss and repair budget`, `rental unit make ready cost worksheet`, `tenant turnover expenses calculator`.
- **MVP:** editable estimated/actual expense rows, vacant days, rent-loss convention, budget variance, local storage and CSV.
- **Risks:** 30-day month convention is a planning assumption, **not** legally mandated proration; no tenant-charge legality claims.
- **SEO / monetization hypothesis:** high-value landlord software advertisers, but low repeat frequency. Test 15 landlords; target ≥5 exports and user feedback on whether vacancy cost is the missing insight.

### D. MulchCompare — bagged vs bulk delivered mulch (70/100)

- **Primary complaint:** 2024-04-01, r/landscaping: homeowner cannot reconcile 97 bags of mulch with the visual size of a yard; commenters note bulk delivery could be cheaper. https://www.reddit.com/r/landscaping/comments/1bsqa1d/im_a_moron_and_cant_figure_out_how_much_mulch_i/
- **Additional evidence:** 2022-08-21, r/LandscapingTips: user asks whether 408 sq ft at 2 inches is about three cubic yards; reply recommends comparing bags with delivery. https://www.reddit.com/r/LandscapingTips/comments/wtzbjh
- **Persona / JTBD:** homeowner or solo landscaper; *when* covering multiple beds, *help me* convert bed dimensions to real order quantities and compare delivery prices *so I can* avoid overbuying.
- **Alternatives:** free supplier mulch calculators, mental math, landscape business software.
- **Competitor / price:** Yardbook Starter **free**, Business **$34.99/month** and Enterprise **$49.99/month**, official: https://www.yardbook.com/pages/pricing . Yardbook is **adjacent landscape operations software**, not proof of paid demand for this calculator. Many free mulch calculators already exist.
- **Gap hypothesis:** multiple-bed and bag-versus-bulk total delivered cost in one mobile page.
- **Core SEO:** `bulk mulch vs bags cost calculator`; long-tail: `mulch bag vs bulk delivery calculator`, `mulch cubic yards multiple garden beds`, `landscape mulch bag count estimate`.
- **MVP:** multiple beds, individual depths, waste allowance, bag size, bulk increment, delivery cost, comparison CSV.
- **SEO / monetization hypothesis:** seasonal informational search; lower paid SaaS likelihood. Test organic landing-page CTR and completion; no search-volume estimate available.

### E. FeeNet — card processing fee net receipts (67/100)

- **Primary complaint:** 2023-06-21, r/smallbusiness: first-time merchant wants to include payment processing cost in prices without surprising customers and asks how to calculate it automatically. https://www.reddit.com/r/smallbusiness/comments/14ff75g
- **Second complaint:** 2024-06-12, r/smallbusiness: merchant says a simple across-the-board fee is impractical when customers also pay cash. https://www.reddit.com/r/smallbusiness/comments/1deejjf/passing_square_processing_fees_on_to_customers/
- **Persona / JTBD:** small US service merchant/freelancer; *when* evaluating card processing expenses, *help me* calculate actual net receipts and reverse gross requirements *so I can* set sustainable internal prices.
- **Alternatives:** calculator, spreadsheet, merchant dashboard, accounting software.
- **Competitor / price:** Square Free has **$0 monthly plan fee**, and its official US support page lists in-person **2.6% + $0.15** and online/invoices **3.3% + $0.30** on Free (actual rates vary by plan and method). https://squareup.com/help/us/en/article/5068-what-are-square-s-fees . This is a processor fee schedule, not a standalone calculator subscription.
- **Gap hypothesis:** side-by-side percentage+fixed comparison and reverse gross-for-net formula; highly competitive generic query.
- **Core SEO:** `credit card processing fee net revenue calculator`; long-tail: `merchant fee calculator percentage plus fixed`, `gross up calculator for payment processing fees`, `small business payment fee comparison`.
- **MVP:** two editable fee models, transaction volume, net receipts, reverse gross target, CSV.
- **Risks:** must not imply card surcharge legality or actual processor quote; applicable card-network and jurisdiction rules differ.
- **SEO / monetization hypothesis:** potentially commercial but heavily contested search; treat as lower-priority experiment until verified impressions appear.

## 3. Deduplication and implementation

Compared new ideas against **all 30 prior catalog entries** (2026-10-18 through 2026-10-23). The new jobs differ in **task outcome and search intent**:

- FenceBid ≠ DrywallWise, TileAudit, ConcreteYield or VisitFloor: gate-aware multi-run fence material takeoff rather than drywall/tile/concrete quantity or handyman minimum call price.
- MulchCompare ≠ DilutionDeck or CleanBid: delivered landscaping materials comparison rather than chemical dilution or house cleaning quotes.
- WeddingFlow ≠ ShotGrid, ProofSheet, TravelBuffer: ceremony-anchored wedding coverage timeline rather than generic shot list, contact sheet or mobile service travel buffering.
- TurnoverBudget ≠ DepositLedger, ReserveReady or VendorBoard: owner make-ready + vacancy expense tracking, not tenant deposit deductions, reserves or vendor coordination.
- FeeNet ≠ RateFloor, RushQuote or MarginWatch: processor fee net receipts, not hourly rate, rush surcharge or project margin.

Catalog and history now contain **35 unique slugs**; 30 previous `apps/*/index.html` files remain byte-identical to the 2026-10-23 package. Each new app is a single-file, local-first English HTML/CSS/JS implementation, includes functional inputs, actual output/export, mobile styling, unique SEO copy, OG tags, SoftwareApplication JSON-LD and a static how-to guide injected by the shared build system.

## 4. QA and release gates

- `python scripts/build.py` — **PASS**; preview generates 35 tool routes.
- `python scripts/qa.py` — **PASS**; title, description, robots, OG, JSON-LD, sitemap and ads gating for all 35.
- `node --check` on 35 app scripts — **PASS**.
- System Chromium 390px tests for 5 new apps — **PASS** on basic inputs, add-row actions, CSV/ICS downloads, JS errors and horizontal overflow. Testing used `page.set_content()` because direct local file navigation was blocked. **Not** a live URL or iOS Safari test.
- 5 new apps have `approved_for_index=false`, `evidence_reviewed=false`, `qa_verified=false`; all 35 preview pages have `noindex,follow`. `robots.txt` disallows all in preview and `sitemap.xml` contains zero URLs.
- AdSense scripts and `ads.txt` **not present**. No real payment checkout is enabled.

**Additional release QA still required:** domain/HTTPS, real URL navigation and canonical tags, Safari, multi-device storage, legal/privacy/contact content verification, accessibility, user testing and source/SEO quality review. Current UI smoke checks alone do not satisfy production release gates.

## 5. Deployment, indexing and revenue truth table

| Area | Verified result as of 2026-10-24 |
|---|---|
| GitHub write access | **Blocked**: connected GitHub read/list requested interactive authorization; no accessible repository confirmed, no push. |
| Cloudflare Pages / Vercel | **Not authorized / not configured**; no public deployment. |
| Owned `.com` and DNS | **Not verified**. |
| Public HTTPS pages | **None verified**. |
| Production canonical / robots / sitemap | Build mechanism exists; no production domain configured; **nothing submitted**. |
| Google Search Console | **Not connected**, impressions/clicks/index coverage unknown. |
| Indexed URLs | **Unknown / not verifiable** (do not report 0 as a measured index count). |
| AdSense | **No verified approved site or publisher ID**; scripts disabled. |
| Ad impressions, RPM, revenue | **Not connected / unavailable**, not measured as $0. |
| Subscriptions | Not activated; no account or billing webhook. |

**Next actions:** register/verify owned domain; authorize a writable GitHub repo and Cloudflare Pages/Vercel; add a real operator contact, reviewed Privacy Policy and Terms; deploy a small hand-reviewed subset; verify Search Console and crawl coverage; apply for AdSense only after real content and site approval. Search indexing and ad income are not guaranteed.

## 6. Experiment gates

For each P1 product, publish only after human review and at least one non-author test of the actual workflow. After a live 30-day observation window, measure search impressions, search clicks, tool start→completion rate, export rate and user feedback. Avoid arbitrary "traffic" claims without Search Console data. Stop adding near-duplicate calculators when the intent or output overlaps existing products. Revisit fee and pricing sources before any public claim.
