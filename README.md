# Worklane Tools — US utility-tool matrix (deployment starter)

A responsive English-language directory of 35 browser tools, with a static site generator, indexation controls, sitemap and robots generation, AdSense verification and activation guards, duplicate-intake registry, and GitHub Actions quality checks.

**Status:** Public preview at https://soloworkkit-hushaodong.pages.dev/ with default noindex. AdSense ownership verification is being connected; ad serving remains disabled and Google approval is pending. See [MONETIZATION.md](MONETIZATION.md) for the actual activation gates.

## Run locally

```sh
python3 scripts/build.py
python3 -m http.server --directory dist 8000
```

Open <http://localhost:8000> (tools at `/tools/<slug>/`).

## Configure production deployment

```sh
SITE_URL=https://your-real-owned-domain.com python3 scripts/build.py --production
```

Publish the `dist` folder through Cloudflare Pages (build command `python3 scripts/build.py --production`) or Vercel (see `vercel.json`). Do not use sample domains or activate ads before review. Draft tools stay `noindex` and out of the production sitemap; change `content/catalog.json` only after independent editorial and functional approval.

For detailed deployment, Search Console, AdSense and research workflows, see [`README_部署与增长运营.md`](README_%E9%83%A8%E7%BD%B2%E4%B8%8E%E5%A2%9E%E9%95%BF%E8%BF%90%E8%90%A5.md).
