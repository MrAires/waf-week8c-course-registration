@echo off
cd /d "%~dp0"
where py >nul 2>nul
if not errorlevel 1 (set "PY=py -3") else (set "PY=python")
if not exist ".venv\Scripts\python.exe" (
    echo Creating virtual environment...
    %PY% -m venv .venv || (echo Python not found. Install Python and select Add to PATH.& pause & exit /b 1)
)
".venv\Scripts\python.exe" -m pip install -r requirements.txt || (echo Flask installation failed.& pause & exit /b 1)
".venv\Scripts\python.exe" launch.py
if errorlevel 1 (echo App failed. Check the error above.& pause)
