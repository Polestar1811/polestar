Set-Location -LiteralPath "$PSScriptRoot\frontend"
$portableNode = Join-Path $PSScriptRoot ".tools\node-v22.16.0-win-x64"
if (Test-Path (Join-Path $portableNode "npm.cmd")) {
  $env:PATH = "$portableNode;$env:PATH"
}
$ip = (Get-NetIPAddress -AddressFamily IPv4 |
  Where-Object { $_.IPAddress -notlike "127.*" -and $_.IPAddress -notlike "169.254.*" -and $_.PrefixOrigin -ne "WellKnown" } |
  Select-Object -First 1 -ExpandProperty IPAddress)
if (-not $ip) { $ip = "127.0.0.1" }
$env:NEXT_PUBLIC_API_BASE_URL = "http://${ip}:8000"
npm install
npm run dev
