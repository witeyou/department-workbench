$ErrorActionPreference = "Stop"
Set-Location (Resolve-Path (Join-Path $PSScriptRoot ".."))
if (-not (Test-Path .env)) {
    Copy-Item .env.example .env
    Write-Host "已创建本机开发 .env（切勿用于生产）"
}
function Run-Checked {
    param([string]$Command, [string[]]$Arguments)
    & $Command @Arguments
    if ($LASTEXITCODE -ne 0) { throw "命令执行失败：$Command $($Arguments -join ' ')" }
}
Run-Checked -Command uv -Arguments @("sync", "--dev")
Run-Checked -Command uv -Arguments @("run", "python", "manage.py", "migrate")
Run-Checked -Command uv -Arguments @("run", "python", "manage.py", "check")
Run-Checked -Command uv -Arguments @("run", "ruff", "check", ".")
Run-Checked -Command uv -Arguments @("run", "pytest", "-q")
Run-Checked -Command uv -Arguments @("run", "python", "manage.py", "makemigrations", "--check", "--dry-run")
Write-Host "基础检查完成。请创建管理员后运行 runserver。"
