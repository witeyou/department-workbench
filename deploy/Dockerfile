FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /srv/workbench
COPY pyproject.toml ./
RUN python -m pip install --no-cache-dir 'uv>=0.9,<1' \
    && uv pip install --system --no-cache -r pyproject.toml
COPY . .
RUN chmod +x scripts/entrypoint.sh
EXPOSE 8000
CMD ["sh", "scripts/entrypoint.sh"]
