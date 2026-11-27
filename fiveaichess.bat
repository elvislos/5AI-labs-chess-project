@echo off
REM Ga naar de map waar dit .bat-bestand staat
cd /d "%~dp0"

REM Start de engine met Python uit je virtual environment
".venv\Scripts\python.exe" -u -m fiveaichess.engines.alphaBetaEngine
