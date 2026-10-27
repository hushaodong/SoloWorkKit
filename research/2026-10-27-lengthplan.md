# 2026-10-27 手动运行：线性切割清单验证版

这是需求研究及公开预览的记录，不是已验证的市场收入、搜索排名或全面法律认证。检查日期：2026-10-27，Asia/Shanghai。

## 需求与取舍

木工和小型加工人员需要把已有的成品长度/数量分配到供应商现有的整根材料上，知道应买几根、每根切什么，以及锯缝和余料分别占多少。触发点是采购/下料前；替代方式为纸笔、表格及已有优化器。

独立信号（只概括任务，不收集用户资料）：

- [木工用户的明确配料任务](https://www.reddit.com/r/woodworking/comments/12td2t6/linear_cut_optimizer/)：给出多种长度、数量及固定原料长度，希望减少浪费并知道采购根数。老需求，不能证明当前增长。
- [金属加工的实际原料约束](https://www.reddit.com/r/metalworking/comments/1p0kfkr/cut_list_optimizer/)：使用已经买下的固定长度余料，需考虑锯缝，并明确寻找免费方案。愿付费证据弱。
- [近期木工规划提问](https://www.reddit.com/r/BeginnerWoodWorking/comments/1vjuk02/which_softwarewebsiteapp_to_calculate_optimal_cut/)：已有图纸和零件清单，需要按原料组织切割次序。评论中有竞品自荐，未作为独立需求证明。

这些作者所在国家未经核实，不把英语帖子自动归为美国。目标四国只是本项目的验证市场。

与既有 35 个工具按任务去重：FenceBid 是围栏工程数量/报价；DrywallWise 是墙板面积/张数；ConcreteYield 是体积；没有逐根长料排样工具。已有照片接触表和费率计算等重复方向不再新建。历史增加 `lengthplan` 去重记录。

## 竞品实现与变现

| 竞品 | 官方功能/收费观察 | 同任务比较及我们的取舍 |
|---|---|---|
| [optiCutter](https://www.opticutter.com/linear-cut-list-calculator)，[官方价格](https://www.opticutter.com/#pricing) | 免费计算器；Standard 显示 EUR 9/月，Professional EUR 19/月，Enterprise API EUR 99/月含 5,000 请求、额外 EUR 0.02/次。年付开关另有优惠，实际结账未测试。付费触发：更大任务、项目历史、高级材料/成本/团队集成。 | 实际浏览器同输入：96 长原料、0.125 锯缝、30×4 和 24×2，得到 2 根、6 刀、168 成品长度、87.5% 成品率；本工具结果相同。免费界面里的价格和最小余料功能显示锁定；我们的报价合计及保留余料阈值可直接用，但不能混合库存/材料，也不能声称优化质量优于竞品。 |
| [Linear Cutting 官方价格](https://linearcutting.com/pricing/) | 免费工具已非常强，包含 500 件、锯缝/端头、导出；Hobby $5/月、Maker $19/月，主要增加 API、项目/工位和团队流程。币种符号按官网记录，未替其假定税费或实际成交。 | 证明“免费计算 + 高级工作流收费”可作为参照，不证明我们有付费客户。我们不复制其代码、模型、文字或素材；差异仍需用户实验验证。 |

本次使用相同的六件样例核对正确性；没有获得实际用户完成时间或优于竞品的证据。拟验证的改进：粘贴已有清单、真实单位换算和一眼可核对的材料平衡能否降低小任务的操作负担。下次用同一空白起点、至少 5 位真实目标用户比较时间、错误和导出完成率；目标中位时间下降 30%，此数字是实验目标，不是结果。本次不联系用户、发帖或购买服务。

## 分国家 SEO 与本地化

| 市场 | 英语查询种子 | 单位/货币支持 | 月搜索量、本站点击份额、自然 sessions |
|---|---|---|---|
| US | linear cut list calculator; lumber cut planner with kerf | 英寸、分数；USD | 全部未知 |
| GB | timber cutting list calculator; cutting optimiser | 毫米；GBP | 全部未知 |
| CA | lumber cut list calculator; linear cutting calculator | 毫米/英寸；CAD | 全部未知 |
| AU | timber cutting optimiser; cutting list calculator | 毫米；AUD | 全部未知 |

进行了带国家词的公开搜索，见到包括英国 [CutNest](https://cutnest.co.uk/timber-cutting-calculator.html)、[贸易工具](https://dtjinteriors.co.uk/trade/toolkit/cut-list-calculator/) 及大量成熟免费工具。这不是经定位的四国 Google 排名快照；不能声称本次检索提供各国排名或绝对量。

Ahrefs 文档接口本次实际返回 `Unknown tool: ahrefs.doc`，未调用付费查询、未获取额度或关键词数据。无 GSC/已验证 organic sessions 数据。低/中/高预测均保留 null；模型不支持宣称每月 10,000 自然搜索访问。CPC、排名难度、RPM、转化率和收入均未知。竞争强、付费动机未验证，决定仅发布零新增服务成本的预览。

四个英语市场共享一个 `lang=en` URL，转换真实数值并提供四种报价币种；不创建近似国家门页，也不伪造翻译或 hreflang。额外语言未完成审校，不发布。

## 实现与边界

入口 `/tools/lengthplan/`。纯本地 JavaScript、无新增依赖/外部字体/第三方脚本、无登录/存储/上传/遥测。支持最多 500 件、同一材料和原料长度、锯缝、两端预留、保留余料阈值、输入粘贴、英寸/毫米真实换算、CSV及浏览器打印入口。标签经 HTML 转义，CSV 单元格防公式注入；输入变化立即失效旧结果与导出，避免打印过期方案。

算法独立编写：先 best-fit decreasing，再对不超过 24 件的任务限节点搜索。只有达到材料长度下界或完成穷举证明时标注该模型下最少原料根数，其余明确为启发式/有限搜索。每件保守预留一次完整锯缝，含最后一件；端头预留含端头修整的锯缝。恒等式：原料 = 成品 + 预留锯缝 + 端头预留 + 余料。不是角度、结构、强度、工艺或机器安全建议，也不保证最低采购成本。

## 法律和数据流初筛

数据流：浏览器获取 Cloudflare Pages 静态资源 → 清单仅在页面内计算 → 用户主动下载 CSV/浏览器打印。清单、姓名、邮箱、地址不上传、不持久化、不加入 URL；CDN 仍会处理访问请求/IP等。没有新增分析、广告或支付数据流。公开用户帖子仅用于任务摘要，不再分发个人资料。

| 范围与官方依据 | 本次判断、措施与剩余问题 |
|---|---|
| 中国：[个人信息保护法](https://www.cac.gov.cn/2021-08/20/c_1631050028355286.htm) | 境内运营的个人信息处理需适用性判断；本次不接收表单输入，禁止收集敏感/客户资料。原托管访问日志、主体经营登记/税务和商业化义务尚不能由工具测试认证，商业广告/收款维持关闭。 |
| 美国：[FTC 广告真实性](https://www.ftc.gov/business-guidance/resources/advertising-faqs-guide-small-business) | 不承诺最优采购/节省百分比/搜索流量或收入；明确有限搜索与物理假设。不是儿童、金融、医疗或结构设计产品。若以后追踪/广告，州隐私适用性须另查。 |
| 英国：[ICO cookies及类似技术](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guide-to-pecr/cookies-and-similar-technologies/) | 当前官方页面注明细化指导正在更新；未把草案视为现行结论。新工具不写 cookie/localStorage，不引入追踪；日后广告必须完成适用同意及撤回测试，不能以“无cookie”免除全部数据义务。 |
| 加拿大：[PIPEDA 与省法](https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/pipeda_brief/) | 不接收清单或新增商业个人数据处理，CDN日志及跨境角色仍需核实；没有定向新增魁北克营销/交易或声称满足法语义务。 |
| 澳大利亚：[OAIC 小企业适用性](https://www.oaic.gov.au/privacy/privacy-guidance-for-organisations-and-government-agencies/organisations/small-business) | 规模和例外、实际联系需判断，不凭小站断言豁免；采用无上传/无追踪的最小数据设计，商业阶段另审适用责任。 |
| 知识产权、费用与安全 | 原创代码及系统字体，无竞品资产复用；不调用付费API/更改付费计划。人为实测材料/设备安全仍由使用者负责；不能把数学证明当现场安全认证。 |

本次仅同意低风险公开预览，不对商业运营/广告/收款做全面合法保证。原站的商业隐私说明和适用CMP仍未完成；不得据此启用广告。

## 发布和验收

默认保持 noindex、空 sitemap、广告脚本关闭；新页暂不开放 SEO 收录。修正旧的 preview robots 禁抓冲突，使爬虫能读取 noindex，依据 [Google 官方说明](https://developers.google.com/search/docs/crawling-indexing/block-indexing)。robots 允许不是批准收录或隐私访问控制。

Cloudflare 继续使用原 main → Pages、构建 `python3 scripts/build.py --site-url https://soloworkkit-hushaodong.pages.dev`、输出 dist。[免费额度](https://developers.cloudflare.com/pages/platform/limits/)当前列 500 builds/月，本次只追加一次部署；实际剩余额度未读取，不宣称无限免费。回滚基点 `3fae3ad98712521721f1f90bcd82d2d75765faef`。任何回滚也需保留其他随后提交，不强推。

数学测试：150 组独立穷举对照，贪心反例、分数、输入拒绝、锯缝/端头边界、500件材料守恒、CSV公式安全。浏览器：真实单位转换、超长输入、重新计算、真实CSV下载及390px布局；打印按钮未生成实体打印/PDF成品。自动测试不能证明真实现场结果。

实际 Git commit、部署 URL、静态审计及浏览器证据另存本次运行目录。部署、索引、访问与收入分别报告；本次不认定一万访问或盈利目标已达成。
