$ErrorActionPreference = "Stop"

$root = $PSScriptRoot
$envPath = Join-Path $root ".env"
$examplePath = Join-Path $root ".env.example"

if (-not (Test-Path $envPath)) {
  Copy-Item -LiteralPath $examplePath -Destination $envPath
}

$key = Read-Host "请输入 DeepSeek API Key"
if ([string]::IsNullOrWhiteSpace($key)) {
  throw "DeepSeek API Key 不能为空"
}

$content = Get-Content -LiteralPath $envPath -Raw
$updates = @{
  "DEEPSEEK_API_KEY" = $key
  "DEEPSEEK_BASE_URL" = "https://api.deepseek.com"
  "DEFAULT_LLM_PROVIDER" = "deepseek"
  "DEFAULT_FAST_MODEL" = "deepseek-chat"
  "DEFAULT_REASONING_MODEL" = "deepseek-reasoner"
}

foreach ($name in $updates.Keys) {
  $value = $updates[$name]
  if ($content -match "(?m)^$name=") {
    $content = [regex]::Replace($content, "(?m)^$name=.*$", "$name=$value")
  } else {
    $content += "`r`n$name=$value"
  }
}

Set-Content -LiteralPath $envPath -Value $content -Encoding UTF8
Write-Host "DeepSeek 配置已写入 .env，请重新启动后端服务。" -ForegroundColor Green
