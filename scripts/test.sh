#!/bin/bash
# Local test runner script
# This complements the CI pipeline for local development

set -e

echo "🧪 Running ThreatIntelRelay Tests Locally"
echo "========================================"

# Change to project root
cd "$(dirname "$0")/.."

# Check if Python virtual environment exists
if [ ! -d "venv" ]; then
    echo "⚠️  No virtual environment found. Creating one..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r src/api/requirements.txt
pip install -r src/api/test-requirements.txt

# Run tests
echo "🧪 Running unit tests..."
cd src/api
pytest tests/ -v

echo "✅ All tests passed!"
echo ""
echo "💡 Tip: The CI pipeline will also run these tests automatically on push"
echo "💡 Integration tests run on the main/release branches via GitHub Actions"
