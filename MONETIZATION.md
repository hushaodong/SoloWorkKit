# AdSense connection and activation

Site: https://soloworkkit-hushaodong.pages.dev/

## Verification stage (2026-10-26)

The public publisher ID in `content/monetization.json` was obtained from this site's new AdSense account. It is a public identifier, not an API credential. The old closed account is not used.

The existing Cloudflare build command remains:

```sh
python3 scripts/build.py --site-url https://soloworkkit-hushaodong.pages.dev
```

This publishes the `google-adsense-account` meta tag on every page and the exact Google seller record at `/ads.txt`. It permits `Mediapartners-Google` and `Google-Display-Ads-Bot` to crawl for verification. It does **not** load the advertising JavaScript, request ads, add ad cookies, or change preview `noindex` tags. General search crawling remains disallowed in preview. These static records alone cannot earn revenue.

Run `python scripts/test_monetization.py`, then the normal build and `python scripts/qa.py`. The build report distinguishes ownership verification, ads.txt, and actual emitted ad loaders.

To remove the binding, clear `adsense_verification_publisher` in the JSON and redeploy. `--adsense-verification-publisher ''` is a local override.

## Required activation steps

1. Publish and check the real HTTPS meta tag and ads.txt, then verify ownership in AdSense. A successful verification is separate from approval to show ads.
2. The operator personally provides Google's required truthful payee name/address and any requested identity verification. Bank account details can generally wait until the payment-method selection threshold; they are different from the required payee profile. Follow the current account's prompts.
3. Finish the content, tool-function, and privacy review. The current collection is still a preview; editorial/functional flags must reflect actual review. Supply an appropriate public operator contact, accurate hosting/advertising data disclosures and applicable user rights before commercial activation.
4. Request site review when the site's and account's requirements permit. Record the actual Google decision; adding code does not establish approval.
5. Configure a Google-certified CMP for applicable EEA/UK/Swiss traffic. Google's Privacy & messaging can supply the European regulations message. Include a clear reject option and test consent, refusal, withdrawal and applicable US state privacy choices. A saved message is not evidence it rendered correctly on the site.
6. After approval and privacy verification, choose a limited ad configuration and review placements. Avoid ads beside calculator, upload, export and payment controls, and avoid overlays that obstruct the task. Configure Auto ads in Google before relying on an ad loader; the loader alone does not guarantee placements or revenue.
7. Only then build with `--production --adsense-publisher <the same ca-pub-ID> --ads-approved --privacy-ready`. The latter flags are operator attestations, not automated Google or legal checks. Production still serves ads only on pages with all three catalog review flags (`approved_for_index`, `evidence_reviewed`, `qa_verified`). Legal/draft pages receive no ad loader.
8. Verify real ad rendering and consent behavior without clicking live ads. Track valid pageviews, impressions, estimated/finalized earnings and later payment holds in AdSense. Do not fabricate traffic, impressions or clicks. Organic search sessions and net income are separate metrics.

Keep advertising disabled if any required step remains incomplete. Do not assert that the full site is monetizing or approved based on this document.

## Official references (checked 2026-10-26)

- [Account setup and possible identity verification before ads](https://support.google.com/adsense/answer/7402256?hl=en)
- [Payment stages and adding bank details](https://support.google.com/adsense/answer/1709858?hl=en)
- [Site verification options and review](https://support.google.com/adsense/answer/12169212?hl=en)
- [Ad crawler access](https://support.google.com/adsense/answer/10532?hl=en)
- [Certified CMP requirement](https://support.google.com/adsense/answer/13554116?hl=en)
