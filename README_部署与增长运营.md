# Worklane Tools — 美国英文工具矩阵：部署、SEO、广告变现

> 交付状态（2026-10-18）：**可运行静态站点工程，未购买/绑定域名，未连接托管账号，未部署公网，未申请AdSense，未提交Search Console。** Worklane Tools是可改的临时品牌名称，域名尚未确定。

## 0. 本地预览

```bash
python3 scripts/build.py
python3 scripts/qa.py      # 本地需要 pip install beautifulsoup4
cd dist && python3 -m http.server 8000
```

在浏览器打开 `http://localhost:8000/`。全部5个工具在 `dist/tools/<slug>/`。预览构建会添加 `noindex`，robots.txt拦截搜索爬虫，并且不加载广告。

## 1. 部署到 Cloudflare Pages（建议）

1. 在GitHub建立一个 **私有或公开仓库**（自行决定），将整个工程（除了 `dist`）上传。确保 `.github/workflows/site-quality.yml` 同步上传。
2. 申请/购买属于自己的`.com`域名；先在Cloudflare建立域名DNS托管或按文档把域名添加到 Pages。
3. Cloudflare → Workers & Pages → Create → Pages → Connect to Git → 选择刚才的仓库。
4. Build command: `python3 scripts/build.py --production`。
5. Build output directory: `dist`；Root directory: 仓库根目录；Production branch: `main`。
6. Environment variable: `SITE_URL=https://你的真实域名`，不要使用`example.com`占位。部署前必须核对自己拥有该域名。Python标准库即可完成构建，无外部服务API。
7. GitHub推送更新触发Cloudflare构建，构建后的公共地址会出现在Cloudflare控制台；要发布失败必须看具体构建日志，不能假设已上线。
8. 同时在Cloudflare设置根域名/`www`的首选版本，避免两者分别收录。

本仓库的GitHub Actions将在每次提交时运行静态SEO检查与原型JS语法检查。**CI通过不是上线成功**；以Cloudflare显示成功且公开HTTPS页面实际访问成功为准。

### Vercel备选

已经提供 `vercel.json`。在Vercel导入GitHub仓库；设 `SITE_URL` 为正式域名；构建会生成`dist/`。不同账户/套餐的构建环境可能存在差异，如果Python不可用，建议先在CI构建`dist/`，再由CLI发布静态目录。

## 2. 已有5个工具与索引权限

| 工具 | URL路径 | 默认正式索引开关 | 说明 |
| --- | --- | --- | --- |
| PunchLite | `/tools/punchlite/` | true | 已具有真实主要功能和独立说明，仍需人工审核准确性 |
| MoveOutPDF | `/tools/moveoutpdf/` | true | 已具有真实主要功能和独立说明，仍需法律/隐私审核 |
| ShotGrid | `/tools/shotgrid/` | false | 候选待验证 |
| GentleNudge | `/tools/gentlenudge/` | false | 候选待验证 |
| NotaryMiles | `/tools/notarymiles/` | false | 未实现GPS自动记录，仅手动记录 |

项目的 `content/catalog.json` 控制每个工具的 `approved_for_index`：只有 `--production` 且开关为 `true` 的工具才会进入Sitemap且有Canonical；其余页面为`noindex,follow`，可以访问测试，但不会被主动提交索引。正式上线前需要自己复核使用体验、版权、政策、隐私/数据保留和文字真实性，必要时将两个默认开放的开关也改为 false。

> 把所有页面设为true不等于Google会收录。Google会自行判断页面质量和搜索价值。批量AI生成几乎相同页面有垃圾内容政策风险，切忌为冲关键词而机械扩增。

## 3. 每天5个：从调研到发布的流水线

```text
定时研究（ChatGPT每天8点左右）
      ↓
原始抱怨证据 + 竞品/关键词 + 5个候选想法
      ↓
候选归档：content/history.json（防重复）
      ↓
每个候选独立MVP：apps/<slug>/index.html
      ↓
content/catalog.json 新增工具元数据（approved_for_index: false）
      ↓
GitHub commit/PR → CI代码质量 + SEO检查
      ↓
人工复核 → 修改批准标记 → Merge main
      ↓
Cloudflare Pages/Vercel 自动构建/更新公网网址
      ↓
生成sitemap.xml、robots.txt、canonical → GSC收录监测
      ↓
AdSense批准后、经隐私合规确认 → 开启广告
```

**自动化边界**：当前ChatGPT定时任务可以每日做研究和生成交付材料，但不能凭空获得GitHub仓库写权限、Cloudflare部署权限或广告账号批准。要实现每天无人工参与的真实公网自动部署，必须先建立持久Git仓库、完成托管授权，并确保每日执行环境能够自动提交生成代码；否则每天仍可收到可部署的ZIP/源码，不能称作“已上线”。

### 防重复运行

`content/history.json` 保存已研究需求（首次包含上述5个）。每天生成以下JSON文件：

```json
{
  "date": "2026-10-19",
  "needs": [
    {
      "slug": "new-slug",
      "problem": "precise user problem",
      "audience": "independent contractors",
      "evidence_url": "https://www.reddit.com/r/...",
      "evidence_date": "2026-10-15",
      "jtbd": "When ..., I want ..., so I can ...",
      "competitor": "Existing software and actual price source",
      "seo_primary": "specific US-English search phrase",
      "monetization_hypothesis": "ad-supported free workflow"
    }
    // Four more complete needs in the real file; JSON must not contain comments.
  ]
}
```

执行 `python3 scripts/intake.py intake/2026-10-19.json` 检查5个候选的精确与模糊重复，再运行 `python3 scripts/intake.py intake/2026-10-19.json --commit` 持久化。每次提交同步 `history.json` 才能跨天去重。脚本检查形式和文本相似度，不能替代人工判断语义同质化。

### 新工具需满足的准入线

- 至少1条可追溯的用户原始问题链接及时间；实际调研最好更多来源。
- 核心任务可用，完成率可测试；不是只有按钮的营销页。
- 用不同UI与流程解决不同的任务，而不是换个关键词复制同一功能。
- 页面含独立标题/描述/H1、操作说明、限制、真实截图（可选）、风险说明和内链。
- 用户隐私清楚：输入数据上传到哪里、保留多久、如何删除、是否调用AI API。
- 没有版权侵权、误导的转化入口、虚假评分或法律/税务承诺。
- 未通过检查：可以保留为`noindex`候选，不能加入公开Sitemap，也不要部署广告。

## 4. Google Search Console与SEO收录

1. 正式域名开始对外服务且确认HTTPS正常后，在 https://search.google.com/search-console/ 添加域名属性，按提示做DNS TXT所有权验证。
2. 检查 `/robots.txt` 应指向当前真实域名的 `/sitemap.xml`，确保只有允许被索引的页面进入Sitemap。
3. Search Console → Sitemaps → 提交 `https://你的域名/sitemap.xml`（首次一次；之后更新文件，Google可能重新抓取）。
4. 定期从 Search Console 监控 Page indexing、Search results、Crawl statistics、Core Web Vitals：曝光、点击、CTR、平均排名以及未收录原因。
5. GSC或Search Console API 可自动采集自身站点表现（需授权）。**不要**使用Google Indexing API强行提交普通工具页；该API仅支持特定`JobPosting`和`BroadcastEvent`场景。
6. 对已索引但表现差的页面优化实际任务完成体验和内容；对薄弱内容主动保留noindex或下线，切忌无差别提交大量同质页面。

## 5. AdSense广告变现

### 先申请，再打开代码

1. 先运营并完善原创内容、真实可用的核心功能、导航与政策页面。提交AdSense审核前，检查站点所有权、真实经营者联系渠道、隐私政策和其他必要披露。
2. Google AdSense → Sites → Add site → 完成域名验证/审核；只有站点显示Ready且经过必要合规审查，才进行正式广告配置。
3. 在Cloudflare Pages设置：
   - `ADSENSE_PUBLISHER=ca-pub-你的16位真实数字`
   - `ADS_APPROVED=1`（你已经获得批准才设置）
   - `PRIVACY_READY=1`（你已处理实际隐私政策、适用地区用户同意/选择机制才设置）
4. 生产构建将向可索引页面的`<head>`注入官方AdSense Auto ads加载脚本，同时生成根路径`/ads.txt`授权行；**不伪造广告、点击或收入**。使用AdSense后台设置广告密度，优先不遮挡工具表单、上传按钮和导出操作。
5. 请按实际法律辖区核查Cookie同意、CCPA/CPRA等数据披露和隐私选择义务；本项目自带页面只是示例，不是法律合规保证。

不建议刚上线就加入大量广告，也不要为提高广告点击率设计误导界面。AdSense明确限制低价值页面、无发布者内容的页面以及妨碍使用的广告。

### 收入测算（**假设，不是收入预测**）

广告收入 ≈ 页面浏览量 ÷ 1000 × Page RPM。Page RPM随流量国家、关键词商业价值、广告展示率、季节和政策限制变化很大，下表仅为敏感性分析。

| 月页面浏览量 | 假设RPM $2 | 假设RPM $5 | 假设RPM $10 |
|---|---:|---:|---:|
| 10,000 | $20 | $50 | $100 |
| 100,000 | $200 | $500 | $1,000 |
| 1,000,000 | $2,000 | $5,000 | $10,000 |

**优先经营指标**：非品牌自然流量、核心任务完成率、重复使用率、每1000次页面浏览收入、单个工具获客/维护成本。广告变现适合搜索量比较稳定、有持续访问的免费工具；小众低流量高意图工具可能更适合付费升级或导流，不能只靠广告。

## 6. 当前仍需要的真实权限

- **GitHub**：当前检查的连接账户可见仓库列表为空。需创建仓库并让连接账户获得访问/写入权限。
- **海外托管**：需要连接 Vercel 或自行在 Cloudflare Pages 连接仓库；本文件本身不会对公网发布。
- **域名**：需拥有自己的`.com`域名并绑定；构建脚本故意拒绝无真实HTTPS域名的生产配置。
- **搜索**：需要站长本人完成Google Search Console域名所有权验证；GSC指标监测需要相应读取权限。
- **广告**：需要申请合规AdSense账户，站点审核批准，取得真实 Publisher ID，完善隐私与政策。

## 7. 产物目录

- `apps/<slug>/index.html`：5个实际可用的工具源文件。
- `content/catalog.json`：唯一站点目录、每工具关键词、限制、索引标记。
- `content/history.json`：跨天需求研究去重记录。
- `scripts/build.py`：生成整站、首页、详情SEO、Sitemap、robots、广告代码/ads.txt。
- `scripts/qa.py`：防止草稿误入索引、检查Title/Meta/H1/Canonical/结构化内容和广告开关。
- `scripts/intake.py`：每日5个需求的重复校验及持久化。
- `.github/workflows/site-quality.yml`：提交时自动构建与基础QA（需GitHub Actions）。
- `dist/`：实际可在本地浏览、也可部署的静态输出目录（预览构建为noindex）。
- `content/metrics_template.csv`：站点增长与收入监控模板。

## 官方参考

- [Cloudflare Pages静态网站部署](https://developers.cloudflare.com/pages/framework-guides/deploy-anything/)
- [Google Sitemap指南](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)
- [Google垃圾内容政策](https://developers.google.com/search/docs/essentials/spam-policies)
- [Google索引API限制](https://developers.google.com/search/apis/indexing-api/v3/using-api)
- [AdSense申请条件](https://support.google.com/adsense/answer/9724)
- [AdSense ads.txt](https://support.google.com/adsense/answer/12171612)
- [AdSense官方广告代码](https://support.google.com/adsense/answer/9274019)
- [Google广告Cookie隐私要求](https://support.google.com/adsense/answer/7549925)
