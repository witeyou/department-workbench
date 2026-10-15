#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
if [[ ! -f .env ]]; then
  cp .env.example .env
  echo '已创建本机开发 .env（切勿用于生产）'
fi
uv sync --dev
uv run python manage.py migrate
uv run python manage.py check
uv run ruff check .
uv run pytest -q
uv run python manage.py makemigrations --check --dry-run
echo '基础检查完成。执行 uv run python manage.py createsuperuser 后启动 runserver。'
