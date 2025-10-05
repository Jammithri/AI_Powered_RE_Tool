#!/bin/bash

echo "🚀 Setting up AI-Powered Requirement Engineering Tool..."

# Create virtual environment
echo "🔧 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment and install dependencies
echo "📦 Installing Python dependencies..."
source venv/bin/activate
pip install -r requirements.txt

# Copy environment file if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file..."
    cp .env.example .env
    echo "⚠️  Please edit .env and add your OpenAI API key!"
    echo "   Get your API key from: https://platform.openai.com/api-keys"
else
    echo "✅ .env file already exists"
fi

echo "✨ Setup complete!"
echo "📋 Next steps:"
echo "   1. Edit .env and add your OpenAI API key"
echo "   2. Run: source venv/bin/activate"
echo "   3. Run: python app.py"
echo "   4. Open: http://localhost:5000"
