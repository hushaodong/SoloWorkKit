# Worklane Tools 美国英语市场日报｜2026-10-20

## 执行摘要

今天基于2026-10-18和2026-10-19的10条历史需求记录，筛选出5个新JTBD并完成5个可交互的移动端英文H5原型。历史去重脚本检查通过；工具矩阵累计15个。5个新增页面均默认 `noindex,follow`；未授权域名、仓库、托管、Search Console和AdSense，因此**没有公网部署、没有已证实收录、没有流量与广告收入**。SEO关键词均为候选词，搜索量/CPC/难度没有外部工具数据，不做数值假设。

## 一、需求研究与证据（评分为人工研究假设，不是成功概率）

### 1. RetainerPulse｜77/100｜P1
- **原始用户证据**：2019-09-06，r/freelance 用户描述客户不断增加临时任务、retainer条款尚未签署、工作量与边界难以控制。https://www.reddit.com/r/freelance/comments/d0n9qn 。补充证据：2024-08-04，r/agency 讨论按月retainer应约定多少小时/天。https://www.reddit.com/r/agency/comments/1ejtvxq 。原始证据并未确认发帖者在美国。
- **用户与JTBD**：独立顾问/小型代理公司；在每月客户任务不断追加时，记录已用时长、识别超额风险并提供客户可读的用量报告。
- **现有替代**：电子表格、通用时间跟踪工具。Clockify Free免费；Basic官方标价 **$3.99/席/月（年付）或$4.99/席/月（月付）**：https://clockify.me/help/administration/billing/subscription-plans 。它提供更丰富的通用时间管理，竞争强。
- **未满足假设**：部分独立顾问只想按客户/月管理retainer使用额度，不想引入团队工作流。尚无付费意愿证据；通用工具可能已满足大多数用户。
- **SEO核心词**：`freelance retainer hours tracker`；长尾 `monthly retainer usage report`, `client retainer hours remaining calculator`, `retainer task hours csv export`。
- **搜索/广告假设**：常青B2B工作流，可能通过“retainer hours tracker”类任务词获客；可展示项目管理/财务软件相关广告。未验证流量、CPC或RPM。
- **MVP**：客户+月份+包含小时+月费，任务级日志、用量预警、CSV、本地存储；无服务器/多端同步。**技术复杂度低，广告适配中高，免费竞争强。**
- **验证动作**：访谈5位采用按小时retainer的美国自由职业者，询问实际使用的替代工具与每月超额频次；用真实CSV导出验证复用率。

### 2. PrintFit｜74/100｜P1
- **原始用户证据**：2025-05-29，r/AskPhotography 用户困惑相机6000×4000像素图片的72 DPI标签是否影响12×18英寸打印、裁切后分辨率如何变化。https://www.reddit.com/r/AskPhotography/comments/1ky4ssp 。美国居住地未确认。
- **用户与JTBD**：摄影师/摄影爱好者；下单打印前确认裁切后实际像素、PPI并得到正确比例的图片。
- **现有替代**：免费开源 Pixel to Print（https://xcreativedesign.github.io/pixel-to-print/）；Photoshop官方美国个人方案页面显示 **US$22.99/月**（具体方案和结算方式需按购买页确认）https://www.adobe.com/products/photoshop/plans.html 。Photoshop为完整编辑软件，不能把其价格当成此功能的直接付费意愿。
- **未满足假设**：免费PPI计算器很多，但“本地上传→中心裁切→PPI验证→下载”的单次闭环可能更省步骤；尚未验证是否足以构成竞争优势。
- **SEO核心词**：`photo print crop calculator`；长尾 `pixels per inch after cropping photo`, `12x8 photo print resolution checker`, `print size aspect ratio crop checker`。
- **搜索/广告假设**：摄影冲印常青搜索需求，打印服务/相纸/摄影器材广告相关。流量和CPC未验证。
- **MVP**：本地文件上传、计算像素保留比例和PPI、中心裁切并导出JPEG；无图片上传，未提供颜色管理或自动增像素。**技术复杂度中等，广告适配中，竞争强。**
- **验证动作**：邀请摄影师用实际打印订单比较原流程与本工具，重点观察裁切错误和任务完成率。

### 3. DilutionDeck｜68/100｜P2
- **原始用户证据**：2024-02-19，r/CleaningTips 用户询问如何将标签上的“半杯兑一加仑水”换算到20oz喷瓶。https://www.reddit.com/r/CleaningTips/comments/1av0qpv 。专业用户相关性为**间接证据**；另见2024-05-07车内清洁浓缩液配比讨论 https://www.reddit.com/r/AutoDetailing/comments/1cmi6ws 。无法确认美国身份。
- **用户与JTBD**：保洁/汽车美容从业者；按照**厂家已批准的**产品:水比例，快速计算不同瓶容量的浓缩液用量与成本。
- **现有替代**：人工换算、瓶身刻度、免费喷瓶计算器 https://uscalculators.com/detailing/spray-bottle-dilution-calculator/ 。Zep厂家产品标签提供不同用途的配比说明 https://zep.com/products/zep-formula-50-heavy-duty-industrial-degreaser-cleaner-5-gallon-85935 。未核实直接竞品收费价格，不虚构。
- **未满足假设**：标准配比与喷瓶容量不一致时存在心算负担，但大量免费计算器可替代。
- **SEO核心词**：`cleaning concentrate dilution calculator`；长尾 `1 to 10 dilution 32 oz bottle`, `spray bottle concentrate ounces calculator`, `product to water ratio calculator`。
- **搜索/广告假设**：清洁用品耗材广告相关，但化学品内容需谨慎；未验证搜索量、广告竞价。
- **MVP**：产品:水体积比、oz/mL切换、成本/瓶、复制和打印。**技术复杂度低，广告适配中，安全风险中高。**
- **重要限制**：不提供任何化学配方、杀菌效力或混合建议。必须遵循厂商标签/SDS；不同化学品不可混合。

### 4. ProrateClear｜67/100｜P2
- **原始用户证据**：2024-09-12，r/Landlord 讨论搬出当日是否计租；2020-02-21 讨论实际月天数、30天与365/12算法差异。https://www.reddit.com/r/Landlord/comments/1fep9e6 、https://www.reddit.com/r/Landlord/comments/f7e4zr 。部分发帖带美国州标记，但不据此确认所有用户身份。
- **用户与JTBD**：自主管理房东/租客；在租约签署前解释部分月份租金差异，透明对比算法和日期口径。
- **现有替代**：手算、租赁软件。TurboTenant Free免费；Essentials按单位数官方区间 **$149–349/年** https://support.turbotenant.com/en/articles/4003980-is-there-a-cost-to-sign-up-for-turbotenant 。属于综合平台，不是直接同类付费计算器。
- **未满足假设**：现有免费计算器未必展示两种算法的差异与末日是否计租的约定；市场免费替代品多。
- **SEO核心词**：`prorated rent 30 day vs actual days calculator`；长尾 `move in mid month rent proration`, `partial month rent day count calculator`, `rent proration calendar days vs 30`。
- **搜索/广告假设**：租赁管理软件广告相关，搜索需求可能稳定；未验证搜索量/CPC。
- **MVP**：月租、日期、末日包含与否、30天/实际天数对比、复制和打印。**技术复杂度低，广告适配高，法律误导风险中高。**
- **重要限制**：仅做数学计算；不能判断当地法律、是否必须按比例退款，也不能改变已签署租约。

### 5. TileAudit｜63/100｜P2
- **原始用户证据**：2026-02-19，r/Tile 用户质疑承包商是否应该将10%瓷砖废料也纳入按面积计费的人工费；2023-11-18，r/HomeImprovement 用户对1200 sq ft施工订购1800 sq ft材料表示疑问。https://www.reddit.com/r/Tile/comments/1r91s4c/how_labor_is_calculated/ 、https://www.reddit.com/r/HomeImprovement/comments/17yg9cu 。美国身份未逐一验证。
- **用户与JTBD**：地砖安装承包商及业主；分别解释净铺贴面积、材料损耗、整箱购买数量和人工费计算基数。
- **现有替代**：手工报价和大量免费工具；TilePlan的免费网页布局工具 https://tileplan.app/ ，TilesPOS免费瓷砖数量计算器 https://www.tilespos.com/en/tile-calculator.html 。**直接竞品价格为免费。**
- **未满足假设**：通用材料计算器主要解决“买几箱”，未必对比“人工按净面积还是采购面积计费”的价格差异。
- **SEO核心词**：`tile labor vs material waste calculator`；长尾 `tile installation labor square footage calculator`, `tile quote waste cost comparison`, `tile material vs installed area`。
- **搜索/广告假设**：建材/施工报价相关广告可能匹配；核心关键词搜索量未核实，竞争免费工具众多。
- **MVP**：材料面积、废料、箱数、材料成本、两种人工计费基数差额、打印/复制。**技术复杂度低，广告适配中高，市场拥挤。**

## 二、去重与质量结果

- 历史库2026-10-18的5个种子工具：PunchLite、MoveOutPDF、ShotGrid、GentleNudge、NotaryMiles。
- 2026-10-19新增5个：ChangeOrderPad、DepositLedger、LicenseScope、RateFloor、CleanBid。
- 今天5个：TileAudit、DilutionDeck、PrintFit、ProrateClear、RetainerPulse。
- `python scripts/intake.py intake/2026-10-20.json --commit`：**通过，累计15条去重记录**。这仅是字符串/词集去重加人工任务边界复核，不是全网需求唯一性证明。
- `python scripts/build.py`：**通过，15个H5站点路径**。
- `python scripts/qa.py`：**通过，SEO标签/结构化数据/noindex/广告安全门禁/目录存在检查**。
- Node `--check`：**新增5个均通过**。
- Chromium浏览器以 `set_content` 渲染并交互：**新增5个均通过390px横向溢出检查、核心计算/交互、无页面JS异常**；PrintFit的本地文件上传及裁切JPEG下载通过；RetainerPulse新增日志与CSV下载通过。浏览器安全策略阻止本地HTTP/file URL导航，因此**未验证真实域名下的刷新后localStorage持久性**。
- 发现并修复一个浮点精度问题：TileAudit当 100×1.12/16 时直接`ceil`会误多算一箱；已加入微小浮点容差并回归测试。
- SEO：所有预览页面均`noindex,follow`；预览robots `Disallow: /`；Sitemap为空。新增工具的`qa_verified=true`只表示本地技术测试，`evidence_reviewed=false`与`approved_for_index=false`，**不开放生产索引**。

## 三、发布、索引与广告状态

| 项目 | 2026-10-20实际状态 |
|---|---|
| 工具总数 | 15，新增5 |
| GitHub | 已连接账户返回0个可访问仓库；无远端提交 |
| 域名 | 未提供/未验证 |
| Cloudflare/Vercel | 无已确认可执行的托管授权 |
| HTTPS公网部署 | 未完成 |
| Google Search Console | 未连接，无法核实收录与查询数据 |
| Google收录 | **未知/无公网站点**，不是已收录0篇的测量结果 |
| SEO关键词搜索量、CPC | 未验证 |
| 自然搜索曝光、点击 | 未接入 |
| AdSense | 无批准站点及Publisher ID；广告代码关闭，ads.txt未生成 |
| 广告收入 | 未接入，不能声称为0美元实测 |
| 订阅收款 | 未配置，不显示可用购买按钮 |

## 四、下一步与经营建议

**优先验证RetainerPulse和PrintFit的真实使用完成率**，再决定是否开放索引。另三个工具免费竞品充足或存在合规风险，不建议因“每日5个”就全部发布。应先由运营者提供一个已注册的`.com`域名、可写GitHub仓库、海外托管授权、有效联系渠道与已审阅的隐私政策；之后验证真实HTTPS、robots/canonical/sitemap并接入Search Console。AdSense需通过账户与站点审核、填写真实Publisher ID并按访问者所在地落实同意管理后再开启。**Sitemap提交不等于Google收录。**
