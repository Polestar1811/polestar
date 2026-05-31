Set-Location -LiteralPath "$PSScriptRoot\frontend"
$portableNode = Join-Path $PSScriptRoot ".tools\node-v22.16.0-win-x64"
if (Test-Path (Join-Path $portableNode "npm.cmd")) {
  $env:PATH = "$portableNode;$env:PATH"
}
npm install
npm run build
