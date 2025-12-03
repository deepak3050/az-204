#!/bin/bash
# AZ-204 Learning App - Quick Start Script

echo "Starting AZ-204 Learning App..."
echo "================================"
echo ""

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "❌ 'uv' is not installed."
    echo ""
    echo "Install it with:"
    echo "  curl -LsSf https://astral.sh/uv/install.sh | sh"
    echo "  or: pip install uv"
    exit 1
fi

echo "✅ Found uv package manager"
echo ""
echo "📚 Starting Flask development server..."
echo "   The app will be available at:"
echo "   - http://localhost:5000"
echo "   - http://$(ipconfig getifaddr en0 2>/dev/null || hostname -I | awk '{print $1}'):5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

cd learning-app && uv run python app.py
