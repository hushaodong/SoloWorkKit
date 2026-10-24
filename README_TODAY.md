# Worklane Tools — 2026-10-21

This increment preserves 15 previous tools and adds five browser-first MVPs:

- `drywallwise`: multi-room drywall sheet quantity and CSV
- `vendorboard`: landlord vendor assignment and follow-up tracker
- `scopelock`: freelancer scope baseline and change-request log
- `proofsheet`: browser-local photo contact sheet PNG generator
- `leasetick`: lease expiration and notice calendar ICS export

## Preview build

```bash
python scripts/build.py
python scripts/qa.py
```

Open `dist/index.html` through a static file server (for example `python -m http.server 8000 --directory dist`) and navigate to `/tools/<slug>/`.

**Do not publish the preview as an indexable site.** Preview mode writes `robots.txt` with `Disallow: /`, marks pages `noindex`, and leaves the sitemap empty. The preview does not enable ads or payments.

## Tests

- `node --check` on all five new app scripts.
- `python scripts/qa.py` checks 20 built app pages and SEO safety.
- `python scripts/test_2026_10_21.py` tests the five new interactive flows with Chromium and 390px viewport using HTML `set_content`. This does not prove HTTPS routing or persistence across reloads.

## Production prerequisites

1. Own a real `.com` domain and verify access.
2. Create/authorize a writable GitHub repo and connect it to an overseas static host (Cloudflare Pages or Vercel).
3. Verify the site's actual privacy policy, contact details, terms, and relevant consent controls.
4. Manually review each candidate's originality, user value, accuracy and evidence; only then change its `approved_for_index`, `evidence_reviewed`, `qa_verified` flags.
5. Build for production: `python scripts/build.py --production --site-url https://YOUR-REAL-DOMAIN` and then run QA. Use the actual domain, not the placeholder.
6. Deploy `dist/`, verify public HTTPS routes, canonical, robots and sitemap, and connect Google Search Console.
7. Apply for AdSense only once the site meets content and policy requirements; do not set an AdSense publisher ID until the real site is approved and privacy/consent requirements are satisfied.

## Files

- `DAILY_REPORT_2026-10-21.md`: original discussion links, dated evidence, competitor pricing, keywords, risks and decisions.
- `intake/2026-10-21.json`: structured research and dedup inputs.
- `content/history.json`: 20 persistent historical needs (must be committed to remote repo to persist across sessions).
- `content/catalog.json`: app metadata and indexing approval flags.
- `dist/`: ready-to-host **preview** output, not a deployed website.
