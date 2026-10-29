# Optional usage analytics

The integration targets the Umami Cloud **Hobby** plan: one site and 100,000 monthly events, with six months of analytics retention, as checked on 2026-10-28. Event properties also consume quota. Do not start a paid trial or upgrade. Current pricing: <https://umami.is/pricing>.

The real Hobby account and website were verified on 2026-10-28. The selected storage region is **US (Oregon)** and the website is `soloworkkit-hushaodong.pages.dev`. `content/analytics.json` is configured for consent-based collection on that hostname only. The user confirmed the public privacy contact. A missing or invalid activation prerequisite fails the build; a build without the reviewed origin does not emit tracking. Public website IDs are not account secrets; never commit credentials or API keys.

When enabled, the build attaches a first-party consent controller to the 40 normal HTML routes. It loads the Umami SDK only after a visitor accepts. Rejection and withdrawal stop future events. GPC/DNT signals keep collection off. A timestamped consent choice is the only new localStorage item and expires after 180 days; failure to save the choice does not prevent using any tool.

## Measurement contract

- A pageview is sent after consent, using the fixed built path and static title. The referrer is reduced to its HTTP(S) origin. Query strings and fragments are not sent.
- All tool routes can record `tool_start` after the first consented user input/change or reviewed button action. It is once per page, not a unique-user metric.
- `action_<static-button-id>` records an action request. It does not prove success.
- Linear Cut Planner additionally emits `tool_complete` after a user-requested calculation succeeds, `tool_error` for a failed calculation, and `export_generated` after CSV data is generated. The initial example is not counted as a completed user calculation. Printing is a request, not a verified saved PDF.
- No form values, filenames, customer data, photographs, amounts, error messages, distinct user IDs or replay data are sent. The third-party receiver still processes connection/IP/browser information; consent does not remove that data flow.
- Pre-consent activity is not queued. Collection failures never block the tools. Each loaded page is capped at 60 events; this is not a complete anti-bot defense or an account-wide quota guarantee.

Umami's default automatic tracking is disabled. Payload fields are explicitly constructed, using the official custom payload interface: <https://docs.umami.is/docs/tracker-functions>. No analytics cookies or session-replay feature are configured by this project. Do not claim that cookie-free software automatically meets all privacy laws.

## Acceptance and operating limits

Run `python scripts/test_analytics.py`, `node scripts/test_analytics.cjs`, the normal build/QA and the existing monetization and arithmetic checks. Synthetic fixtures exercise consent gates and payloads; they are not proof of data reaching a real account. After activation, verify a consented visit and named events in the real dashboard; also test reject, withdraw, invalid input and an exporter in the actual browser.

Retain a record of the actual account plan/region, website ID, data flow, dashboard URL and test timestamps. Keep the dashboard private. The free plan does not include API/MCP access; use the dashboard or permitted export. Do not buy an upgrade for scheduled reporting. Retention and event limits must be monitored in the actual account.

These are consented observations only. Pageviews, unique visitors, visits, sessions, referrer traffic and GSC clicks have different definitions. Search-referrer visits do not by themselves verify the portfolio's 10,000 organic sessions target. Staff/test traffic and bot filters must be documented before claiming that target.

For explicit staff verification, open a page with `?analytics_test=1`. Only the fixed `internal-test` tag is emitted; the query string itself is omitted. Exclude that tag when reporting real acquisition and usage. This is a reporting label, not bot detection or an account-wide staff filter. Other staff browsers should reject analytics or use their own documented exclusion setting.
