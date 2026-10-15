# START HERE — 启动与工作清单

本清单是**推荐执行顺序**。目录当前提供 V0.0 骨架，不是已完成的部门管理平台。

## A. 第一天：准备开发环境

- [X] 将压缩包解压为 `department-workbench/`，不要移动内部目录。
- [X] 安装 Git、Python 3.12、uv、Codex CLI/IDE 扩展；确认 `git --version`、`uv --version`。
- [X] 在项目根目录执行 `git init`，建立私有 GitLab 仓库，并设置远端；不要提交 `.env`。
- [X] 复制 `.env.example` 到 `.env`；本机默认 SQLite。
- [X] 运行 `uv sync --dev`，首次生成 `uv.lock` 并纳入 Git。
- [X] 运行 `uv run python manage.py migrate`，运行 `uv run python manage.py createsuperuser`。
- [X] 运行 `uv run python manage.py runserver`，浏览器访问 `http://127.0.0.1:8000/`。
- [X] 运行 `uv run pytest -q`、`uv run ruff check .`、`uv run python manage.py check`。
- [X] 用浏览器确认：未登录跳转登录页、管理员登录后有首页和管理后台、退出登录有效。
- [X] 完成一次初始 Git 提交：`git add . && git commit -m "chore: initialize department workbench scaffold"`。

Windows PowerShell 的文件复制命令为 `Copy-Item .env.example .env`。`uv run` 命令在 PowerShell、CMD 和 Bash 下均可使用。

可选快速初始化脚本：Linux/macOS 执行 `bash scripts/bootstrap.sh`；Windows PowerShell 执行 `./scripts/bootstrap.ps1`（按公司的脚本执行策略运行）。脚本不创建管理员账号。

## B. 第一次启动 Codex

1. 用 Codex 打开项目根目录，确保它可读取根目录的 `AGENTS.md`。
2. 把以下整段作为第一次任务指令（也保存在 `tasks/00-基础工程验收.md`）：

> 请先阅读 AGENTS.md、docs/START_HERE.md、docs/01-产品范围.md、docs/02-业务流程.md、docs/03-数据模型.md、docs/04-权限矩阵.md 以及 tasks/00-基础工程验收.md。请执行任务 00：验证启动工程的安装、迁移、登录、基本安全配置与自动化测试；必要时只修复启动工程缺陷，不要提前开发市场/需求/研发模块。完成后说明所有变更、验证命令和结果，并在 docs/development-plan.md 更新任务 00 状态。

3. 审核 Codex 修改内容，确认通过后再提交。
4. 依次提交 `tasks/01-客户与询盘.md`、`02-售前技术评估.md`、`02B-商机与商务跟进.md` 等；**一次只交一张任务卡**。

## C. 建议先与市场负责人、研发负责人确认的业务规则

- [ ] 询盘由谁录入？询盘关闭有哪些原因？商机与询盘是否一对多？
- [ ] 什么条件下触发售前技术评估？谁有权指派技术负责人？
- [ ] 技术评估完成是否就等于研发承诺？（建议否）
- [ ] 需求接受、拒绝、暂缓由谁决策？
- [ ] 定制项目应在商务确认哪个节点创建？
- [ ] 产品研发与定制项目是否共用任务状态？（建议共用，里程碑可分型）
- [ ] 项目进度以哪些客观数据计算？何时由负责人确认？
- [ ] 领导最希望首页看到的 6 个指标是什么？
- [ ] 谁可以查看客户联系方式、预计金额和研发内部工时？
- [ ] 定义超期阈值、通知频率、数据留存与备份周期。

上述问题不必全部解决才能开发登录、客户、询盘模块；**遇到特定流程分歧时，在对应任务进入开发前决定。**

## D. 代码开发完成后的演示顺序

- [ ] 市场人员录入客户和询盘。
- [ ] 市场发起技术评估申请，研发负责人指派评估人。
- [ ] 研发提交结论并退回市场，形成完整可追溯历史。
- [ ] 业务负责人确认需求接受、暂缓或拒绝。
- [ ] 需求挂接产品、版本或客户定制项目，并创建任务。
- [ ] 项目经理查看里程碑、超期任务和阻塞问题。
- [ ] 领导查看业务统计卡片并下钻原始记录。
- [ ] Dify 生成询盘分析草稿，用户修改并确认后保存。

## E. 试点上线前不可省略

- [ ] 真实用户权限/数据隔离测试；检查非法 ID 越权访问。
- [ ] PostgreSQL 环境验收，确认数据库迁移一致。
- [ ] 内网 TLS 及生产环境密钥、安全 Cookie。
- [ ] 文件上传类型与大小限制、访问授权、病毒扫描策略（如涉及客户附件）。
- [ ] PostgreSQL 和附件备份；独立环境恢复演练。
- [ ] 至少 1 名业务负责人确认流程，1 名技术负责人承担维护。
- [ ] 选一个市场小组、一个研发小组试点，不直接全员替换旧流程。
