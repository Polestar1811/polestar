Set-Location -LiteralPath "$PSScriptRoot\backend"
python -m compileall app
python -m pytest -q
