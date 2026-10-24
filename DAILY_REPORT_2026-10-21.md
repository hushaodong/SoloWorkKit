# Worklane Tools 美国英语市场需求研究与开发日报

**日期：2026-10-21（北京时间）**  
**交付：5条经过初步证据核验的新增需求、5个独立可交互英文H5原型、累计20个工具的统一工程。**  
**经营状态：仅本地构建；未公开部署、未提交Google Search Console、未启用AdSense、未获得广告收入。**

## 1. 去重与质量门槛

- 已从2026-10-20完整ZIP恢复历史15个工具的源代码、`content/catalog.json`、`content/history.json`、`scripts/build.py`、`scripts/qa.py`。
- 本期5个需求与历史15个工具在用户任务、主关键词意图及实现功能上分别区分：DrywallWise（墙面石膏板用量，而非瓷砖材料计价）；VendorBoard（维修供应商调度，而非退租照片或押金）；ScopeLock（自由职业项目范围与变更，而非建筑变更报价或包月工时）；ProofSheet（图像联系表导出，而非拍摄清单或照片打印裁切）；LeaseTick（租约截止提醒，而非按天分摊租金）。
- `scripts/intake.py`的5项必填、语义去重和历史写入通过，历史记录由15增长至20。**自动化去重只做初筛，人工语义对比仍必要。**
- 所有新增工具 `approved_for_index=false`、`evidence_reviewed=false`、`qa_verified=true`。已通过功能测试不代表用户研究充分，暂不公开索引。

## 2. 今日五个机会与完整证据

> 机会评分（0–100）为人工研究阶段判断，不是成功率；美国身份尚未对每个发帖者独立核实。搜索量、CPC、关键词难度和RPM **均未取得可靠实测数据，不予填写虚构数字**。付费证据是相邻产品的市场价格，不是新工具的付费承诺。以下竞争价格是2026-10-21检索到的官方公开页面，价格可能随套餐、地域、计费周期变动。

### A. DrywallWise｜石膏板用量估算（79/100，P1）

- **真实原始用户讨论：** 2025-04-07，r/drywall，用户表示承包商估算约310张4×12板，而多个计算器估算仅约180–210张，担心人工与材料报价存在重大差异。原始链接：<https://www.reddit.com/r/drywall/comments/1jtuuq1>。
- **用户与JTBD：** 小型装修承包商、DIY业主、工地估算人员；需要按房间、墙面、天花板、门窗扣除核对材料订购量。
- **现有替代：** Excel、多个免费面积计算器、承包商人工丈量、专业工程估算软件。
- **竞品与价格：** Houzz Pro官方2026美国页面：Design $99/月、Pro $199/月（Pro含takeoffs）；这是综合项目管理系统价格，**并非独立石膏板计算器价格**。<https://www.houzz.com/houzz-pro/pricing>。
- **未满足点：** 不同计算器、计费面积和现场布局口径不一致；需要可审查的逐房间明细。**风险：** 真实下料优化、接缝和规范不是简单面积公式可以解决。
- **SEO主词：** `drywall sheet calculator by room`；长尾：`drywall sheets per room calculator`、`drywall 4x12 sheet estimate with doors windows`。
- **自然搜索假设：** 具有长期装修估算搜索意图，但SERP免费计算器密集；先验证Google搜索结果是否偏好可交互工具与可导出明细。
- **广告适配：** 中高，建筑材料、承包商软件和装修服务；尚未核实CPC。
- **技术可行性：** 高。已完成房间列表、墙面/天花板、门窗扣除、余量、4×8/4×12、材料费、CSV。
- **商业化假设：** 免费核心工具+合规展示广告；未来验证批量项目报告或施工材料清单高级功能。

### B. VendorBoard｜房东维修供应商任务板（76/100，P1）

- **真实原始用户讨论：** 2026-04-23，r/Landlord，一位房东表示目前用表格追踪水管工、油漆工等供应商及不同地址的施工任务，远程协调团队难以保持同步。<https://www.reddit.com/r/Landlord/comments/1str9de/landlordus_keeping_track_of_vendors_handy_men/>。
- **用户与JTBD：** 管理少量房源的美国房东；需要一眼看清谁负责哪个地址、工作进度及下次跟进日期。
- **现有替代：** 电子表格、手机联系人、短信、物业管理SaaS。
- **竞品与价格：** Buildium官方Essential起价$62/月，包含基础维护、租赁与会计功能；这不是纯供应商调度工具价格。<https://www.buildium.com/pricing/>。
- **未满足点：** 全套物业SaaS对小房东可能过重，跨物业供应商分配仍靠表格。**风险：** 本地版无法多人共享，暂时不能解决原始帖的全部协同问题。
- **SEO主词：** `rental property vendor tracker`；长尾：`landlord maintenance vendor tracking spreadsheet`、`property repair contractor assignment tracker`。
- **自然搜索假设：** 面向DIY landlord的具体工具搜索，可能更偏模板下载而非SaaS购买；需对比搜索意图。
- **广告适配：** 中高，物业软件、维修服务；未核实CPC。
- **技术可行性：** 高（单机MVP）。已完成物业、供应商、工种、状态、日期、逾期提示及CSV导出。
- **商业化假设：** 免费广告工具，后续以共享协作/自动提醒作为订阅实验，不宣称已实现。

### C. ScopeLock｜自由职业项目范围变更记录（75/100，P1）

- **真实原始用户讨论：** 2026-03-12，r/web_design，发帖者描述与自由职业者合作中反复出现范围膨胀：初始任务简单、需求持续变化、双方最后对原始约定不一致。<https://www.reddit.com/r/web_design/comments/1rrmke2/how_do_you_guys_actually_handle_scope_creep/>。
- **用户与JTBD：** 网站设计师、开发者、创意服务工作室；需要将初始交付、排除项和追加请求区分开，降低免费返工。
- **现有替代：** 合同附件、邮件、Trello、表格、全功能客户管理软件。
- **竞品与价格：** HoneyBook官方Starter为年付折合$29/月或月付$36/月；该平台功能范围更广。<https://help.honeybook.com/en/articles/2418282-what-s-included-in-each-honeybook-membership-plan>。
- **未满足点：** 简单项目不需要复杂CRM，却需要明确范围变更轨迹。**风险：** 自己勾选Approved不等于客户签字同意。
- **SEO主词：** `freelance scope creep tracker`；长尾：`client change request log template`、`freelance project scope change tracker`。
- **自然搜索假设：** 信息类“如何处理scope creep”竞争较多，工具类长尾可能更适合落地；需验证实际SERP。
- **广告适配：** 中，商业工具和合同软件；未核实CPC。
- **技术可行性：** 高。已完成项目基线、排除项、变更请求、小时数、状态、估值、打印和CSV。
- **商业化假设：** 免费广告工具，后续验证客户签署、历史版本、团队协作付费价值。

### D. ProofSheet｜本地照片联系表（73/100，P2）

- **真实原始用户讨论：** 2026-04-07，r/PhotographyAdvice，一位摄影师通过WeTransfer与PDF联系表交付照片，客户经纪人坚持使用其他服务，摄影师不愿再学习一套复杂系统。<https://www.reddit.com/r/PhotographyAdvice/comments/1sehkp5/advice_for_proofing_for_new_photographer/>。另有2022-09-26 r/AskPhotography用户提及数千张照片缺乏快速生成联系表的方法：<https://www.reddit.com/r/AskPhotography/comments/xovuvx>。
- **用户与JTBD：** 人像、活动、商业摄影师；希望快速生成带编号/文件名的概览图给客户挑选。
- **现有替代：** Photoshop、Lightroom、XnView MP、专业图库和免费联系表生成器。
- **竞品与价格：** XnView MP官网：个人/教育等符合条件用途免费，企业商用单许可证€29。<https://www.xnview.com/en/xnview-mp/>。
- **未满足点：** 轻量交付无需新账户和图库；**但原始讨论也暴露一个问题：客户可能需要交互式选择，而静态PNG不一定解决其真实问题。**
- **SEO主词：** `photo contact sheet generator`；长尾：`contact sheet generator with filenames`、`create photo proof sheet online without upload`。
- **自然搜索假设：** 关键词意图清晰但免费竞争强，优先验证“without upload/with filenames”细分需求。
- **广告适配：** 中，打印服务与创作软件；未核实CPC。
- **技术可行性：** 高。已完成多图本地上传、列数、缩略图尺寸、标题、文件名/编号、Canvas PNG导出；单页限制36张。
- **商业化假设：** 免费广告工具；付费批量导出或交互式选片须先验证需求。

### E. LeaseTick｜租约续约日历（69/100，P2）

- **真实原始用户讨论：** 2026-09-25，r/PropertyManagement，用户讨论小房东反复在表格和日历之间复制租客、租约、提醒数据；评论提及只有3套房也可能漏掉续约提醒。<https://www.reddit.com/r/PropertyManagement/comments/1wpk0yg/how_do_you_keep_tenant_info_lease_dates_and_rent/>。
- **用户与JTBD：** 少量房源房东；将租约截止日和事先确认的提醒天数转为个人日历事件。
- **现有替代：** Google Sheets + Calendar、物业SaaS、手动日历。
- **竞品与价格：** TurboTenant官方支持文档：免费版；Essentials 1–10单元$149/年，Pro 1–10单元$199/年（均按年计费）。<https://support.turbotenant.com/en/articles/4003980-is-there-a-cost-to-sign-up-for-turbotenant>。
- **未满足点：** 小房东想减少重复录入；**风险：** 不同州、城市、合同对续约通知期限要求不同，不能自动推断法律时限；本地版也不能实时同步提醒。
- **SEO主词：** `lease renewal reminder calendar`；长尾：`lease expiration tracker with reminders`、`lease notice deadline calendar ics export`。
- **自然搜索假设：** 搜索需求可能较小、偏现有物业平台；以ICS导出差异化测试。
- **广告适配：** 中，物业管理服务；未核实CPC。
- **技术可行性：** 高。已完成多租约录入、用户自定义提前天数、日期计算、CSV及ICS日历导出。
- **商业化假设：** 免费广告工具；后续考虑真正提醒服务，但需要后台、用户账户和隐私合规。

## 3. 交付与自动化状态

| 项目 | 本期结果 |
|---|---|
| 历史原型 | 15个完整保留 |
| 新增原型 | DrywallWise、VendorBoard、ScopeLock、ProofSheet、LeaseTick |
| 累计工具 | 20个 |
| 源码路径 | `apps/<slug>/index.html` |
| 可部署构建 | `dist/`，首页+20个工具页 |
| 去重记录 | `content/history.json`共20条 |
| 研究数据 | `intake/2026-10-21.json` |
| SEO | 页面静态内容、Meta、OG、结构化数据、内部链接、robots与Sitemap生成逻辑齐备 |
| 新增页面索引 | 全部`noindex`；预览Sitemap不包含页面 |
| AdSense | 无发布商ID、无审核状态；广告脚本与ads.txt均未生成 |
| 代码检查 | 20个工具的JavaScript代码块全部通过Node语法检查；20个页面通过SEO QA |
| 交互检查 | 5个新增工具通过Chromium 390px宽度的核心交互流程；ProofSheet PNG与LeaseTick ICS下载通过 |
| 测试边界 | Chromium使用`set_content`验证交互，未验证真实HTTPS路由、刷新后的localStorage持久性及跨设备体验 |
| GitHub | 已授权账户列出0个可用仓库，未远端提交 |
| Cloudflare/Vercel | 无可用部署授权及已验证域名，未公网发布 |
| Google Search Console | 未接入；无法报告真实收录、曝光或点击 |
| 广告与收入 | 未接入，不能报告实际RPM/收入 |

**质量注意：** 源码和构建结果可运行，并不代表已经通过用户价值审核、法律审核、AdSense站点审核或Google收录。SEO页不可因生成数量而默认发布。

## 4. 今日经营判断与下一步

1. **优先人工验证DrywallWise、VendorBoard、ScopeLock**：与现有15个工具不重复，且可测量完成任务的时间与结果。DrywallWise可先在美国承包商群体验证计算口径，VendorBoard验证是否真正需要跨设备协作，ScopeLock验证用户是否愿意记录每次变更。
2. **ProofSheet保持P2**：功能有明确使用价值，但免费竞争强，且部分客户真正需要交互选片而非PNG。
3. **LeaseTick保持P2**：法律差异与提醒服务边界必须明确，避免宣传为法律合规提醒。
4. **部署是持续阻塞项**：需要拥有的域名、可写GitHub仓库、Cloudflare Pages或Vercel授权、真实运营者联系信息；发布后才可验证HTTP 200、canonical、Sitemap和Search Console。
5. **广告暂不启用**：需要通过AdSense审核、真实发布商ID、适用的隐私/同意机制，并观察真实自然搜索流量后再优化广告位置。不能把“技术预留”写成“已变现”。

## 5. SEO与变现数据模板（目前均未接入）

| 指标 | 本期实测 |
|---|---|
| Google已索引页 | 无法核实；网站未公开部署 |
| 自然搜索曝光 | 未接入 |
| 自然搜索点击 | 未接入 |
| 搜索CTR | 未接入 |
| 广告请求与展示 | 未启用 |
| AdSense收入 | 未接入 |
| 关键词搜索量、CPC、RPM | 未经核实，不提供估计值 |
