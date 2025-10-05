#!/bin/bash

echo "🚀 Starting AI-Powered Requirement Engineering Tool..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Please run ./setup.sh first"
    exit 1
fi

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "❌ .env file not found. Please add your OpenAI API key to .env"
    exit 1
fi

# Activate virtual environment and run app
source venv/bin/activate
python app.py
