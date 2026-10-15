"""本机非敏感环境检查（不会输出密钥值）。"""
import importlib.util
import os
import platform
import sys

print(f"Python: {sys.version.split()[0]} / {platform.system()}")
for module in ("django", "pytest", "psycopg"):
    print(f"{module}: {'installed' if importlib.util.find_spec(module) else 'missing'}")
print(f"DATABASE_URL: {'configured' if os.getenv('DATABASE_URL') else 'not in process env (SQLite default)'}")
print("提示：请执行 uv run python manage.py check 和 uv run pytest 进行功能校验")
