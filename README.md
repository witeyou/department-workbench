# 部门智能运营工作台（Codex 启动工程）

用于 20–30 人部门内部的市场、研发、管理协同。**本仓库当前是 V0.0 可运行基础骨架**：Django 登录、角色档案、开发占位首页、Admin、SQLite/PostgreSQL 配置、基础测试和 Docker 部署示例。客户/询盘/需求/项目等业务 CRUD **尚未实现**，请按 `tasks/` 顺序交给 Codex 开发。

## 推荐阅读顺序
1. `docs/START_HERE.md`：本机操作清单与首次 Codex 提示词。
2. `AGENTS.md`：Codex 必须遵守的工程规则。
3. `docs/01-产品范围.md`、`02-业务流程.md`、`03-数据模型.md`、`04-权限矩阵.md`：业务契约。
4. `docs/development-plan.md`：开发路线、阶段验收。
5. `tasks/`：逐轮交给 Codex 的任务卡。

## 最快启动（Windows PowerShell 或 Linux/macOS shell）

要求：Python 3.12、uv、Git。Django 等依赖首次下载需要访问 Python 软件包源。

```bash
cp .env.example .env       # Windows PowerShell: Copy-Item .env.example .env
uv sync --dev
uv run python manage.py migrate
uv run python manage.py createsuperuser
uv run python manage.py runserver 127.0.0.1:8000
```

访问 http://127.0.0.1:8000/ ，使用刚创建的管理员账号登录。进入 `/admin/` 可为账号创建 UserProfile 并分配角色。

也可以执行 `bash scripts/bootstrap.sh`（Windows：`./scripts/bootstrap.ps1`）完成依赖、迁移与检查；管理员账号需另外创建。

运行质量检查：

```bash
uv run python manage.py check
uv run ruff check .
uv run pytest -q
uv run python manage.py makemigrations --check --dry-run
```

**注意**：`.env.example` 内是本机开发用密钥，不能用于内网生产部署。初期 SQLite 仅供开发。首次 `uv sync` 会生成 `uv.lock`，确认测试通过后应提交到 Git 以固定依赖。

## Docker Compose 试运行（Ubuntu）

```bash
cp .env.docker.example .env
# 修改 DJANGO_SECRET_KEY、DB_PASSWORD、DJANGO_ALLOWED_HOSTS
cd deploy
docker compose --env-file ../.env up -d --build
# 从 deploy/ 目录运行：
docker compose --env-file ../.env exec web python manage.py createsuperuser
```

访问 `http://<服务器IP>:8080/`。这是 **HTTP 内网试运行配置**，尚未配置 TLS、统一身份认证、备份、文件下载鉴权或安全监控，**不得直接暴露到公网**。上线清单见 `docs/09-运维发布.md`。

## 开发方法
- 不要用一条提示词让 Codex 生成完整系统；请从 `tasks/00-基础工程验收.md` 开始逐轮实现。
- 市场 → 技术评估 → 商机 → 需求 → 项目和任务 → 领导驾驶舱 → Dify，按业务纵向切片开发。
- 每轮必须有数据库迁移、角色权限验证、测试及可演示操作路径。
- Dify 为可选服务，不能成为基础业务系统的单点依赖。

## 仓库当前状态

| 功能 | 当前状态 |
|---|---|
| Django 登录、退出、Admin、角色档案 | 已实现基础骨架 |
| 首页 | 已实现占位页面，不含真实指标 |
| 客户、询盘、商机 | 仅预留 App |
| 技术评估与需求管理 | 仅预留 App |
| 产品、项目、任务管理 | 仅预留 App |
| Dify 接口与自动化 | 仅预留 App |
| 数据表、业务权限、正式流程 | 等待按任务卡开发 |

## 设计原则

真实业务记录是唯一事实来源。流程状态由业务逻辑维护，AI 只能输出可核查建议。跨组协作先行，视图和图表随后，智能化最后接入。
