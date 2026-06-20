#!/usr/bin/env bash
set -euo pipefail

mkdir -p audits

if ! command -v agent-rules-kit >/dev/null 2>&1; then
  echo "agent-rules-kit is not installed."
  echo "Install with: pip install agent-rules-kit==0.3.0"
  exit 0
fi

echo "Running agent-rules-kit doctor..."
agent-rules-kit doctor . > audits/agent-rules-kit-doctor.txt || true

echo "Running agent-rules-kit check..."
agent-rules-kit check . --format markdown > audits/agent-rules-kit-check.md || true

echo "Running agent-rules-kit budget..."
agent-rules-kit budget . > audits/agent-rules-kit-budget.txt || true

echo "Audit files written to audits/"
