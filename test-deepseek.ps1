$ErrorActionPreference = "Stop"

$body = @{
  email = "owner@example.com"
  password = "demo"
} | ConvertTo-Json

$login = Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8000/api/auth/login" -ContentType "application/json" -Body $body
$headers = @{ Authorization = "Bearer $($login.access_token)" }
$result = Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8000/api/admin/model-test" -Headers $headers
$result | ConvertTo-Json -Depth 8
