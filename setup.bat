@echo off
echo ================================
echo 🧠 Mood Analyzer - Setup Script
echo ================================
echo.

REM Check Python version
echo 📋 Checking Python version...
python --version
if %errorlevel% neq 0 (
    echo ❌ Python is not installed or not in PATH
    exit /b 1
)
echo ✅ Python detected
echo.

REM Create virtual environment
echo 🔧 Creating virtual environment...
if exist venv (
    echo ⚠️  Virtual environment already exists. Skipping...
) else (
    python -m venv venv
    echo ✅ Virtual environment created
)
echo.

REM Activate virtual environment
echo 🔌 Activating virtual environment...
call venv\Scripts\activate.bat
echo ✅ Virtual environment activated
echo.

REM Install dependencies
echo 📦 Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt
echo ✅ Dependencies installed
echo.

REM Create .env file if it doesn't exist
echo ⚙️  Setting up environment variables...
if not exist .env (
    copy .env.example .env
    echo ✅ .env file created from template
    echo ⚠️  Please edit .env and add your GEMINI_API_KEY
) else (
    echo ⚠️  .env file already exists. Skipping...
)
echo.

REM Create data directory
echo 📁 Creating data directory...
if not exist data mkdir data
echo ✅ Data directory created
echo.

REM Setup complete
echo ================================
echo ✨ Setup Complete!
echo ================================
echo.
echo Next steps:
echo 1. Edit .env and add your GEMINI_API_KEY
echo 2. Run: venv\Scripts\activate.bat (if not already activated)
echo 3. Run: streamlit run app.py
echo.
echo Get your Gemini API key: https://makersuite.google.com/app/apikey
echo.
pause
