$ErrorActionPreference = "Stop"

$root = $PSScriptRoot
$nodeDir = Join-Path $root ".tools\node-v22.16.0-win-x64"
if (Test-Path (Join-Path $nodeDir "npm.cmd")) {
  $env:PATH = "$nodeDir;$env:PATH"
}

$ip = (Get-NetIPAddress -AddressFamily IPv4 |
  Where-Object {
    $_.IPAddress -notlike "127.*" -and
    $_.IPAddress -notlike "169.254.*" -and
    $_.PrefixOrigin -ne "WellKnown"
  } |
  Select-Object -First 1 -ExpandProperty IPAddress)

if (-not $ip) {
  $ip = "127.0.0.1"
}

$backendUrl = "http://${ip}:8000"
$frontendUrl = "http://${ip}:3000"

Write-Host ""
Write-Host "TeaAgent 正在启动..." -ForegroundColor Cyan
Write-Host "本机访问: http://127.0.0.1:3000" -ForegroundColor Green
Write-Host "客户局域网访问: $frontendUrl" -ForegroundColor Green
Write-Host "API 文档: $backendUrl/docs" -ForegroundColor Green
Write-Host ""
Write-Host "如果客户电脑打不开，请允许 Windows 防火墙放行 Python 和 Node.js。"
Write-Host ""

$backendCmd = "Set-Location -LiteralPath '$root\backend'; python -m uvicorn app.main:app --host 0.0.0.0 --port 8000"
$frontendCmd = "Set-Location -LiteralPath '$root\frontend'; `$env:PATH='$nodeDir;' + `$env:PATH; `$env:NEXT_PUBLIC_API_BASE_URL='$backendUrl'; npm install; npm run dev"

Start-Process powershell -ArgumentList "-NoExit", "-ExecutionPolicy", "Bypass", "-Command", $backendCmd
Start-Sleep -Seconds 2
Start-Process powershell -ArgumentList "-NoExit", "-ExecutionPolicy", "Bypass", "-Command", $frontendCmd
