#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

if [ ! -f .env ]; then
  cp .env.example .env
fi

if [ -n "${CODESPACE_NAME:-}" ]; then
  export NEXT_PUBLIC_API_BASE_URL="https://${CODESPACE_NAME}-8000.app.github.dev"
  FRONTEND_URL="https://${CODESPACE_NAME}-3000.app.github.dev"
  API_URL="https://${CODESPACE_NAME}-8000.app.github.dev"
else
  export NEXT_PUBLIC_API_BASE_URL="http://127.0.0.1:8000"
  FRONTEND_URL="http://127.0.0.1:3000"
  API_URL="http://127.0.0.1:8000"
fi

echo ""
echo "Starting TeaAgent..."
echo "Frontend: ${FRONTEND_URL}"
echo "API docs: ${API_URL}/docs"
echo ""

if command -v gh >/dev/null 2>&1 && [ -n "${CODESPACE_NAME:-}" ]; then
  gh codespace ports visibility 3000:public 8000:public -c "$CODESPACE_NAME" || true
fi

python -m uvicorn app.main:app --app-dir backend --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!

cleanup() {
  kill "$BACKEND_PID" 2>/dev/null || true
}
trap cleanup EXIT

cd frontend
npm run dev -- -H 0.0.0.0
