#!/usr/bin/env bash
set -euo pipefail

python -m pip install --upgrade pip
python -m pip install -r backend/requirements.txt

cd frontend
npm install
cd ..

if [ ! -f .env ]; then
  cp .env.example .env
fi

echo ""
echo "TeaAgent Codespaces environment is ready."
echo "Run: bash start-codespaces.sh"
