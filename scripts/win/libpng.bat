@echo off
setlocal
rem Windows to Android: libpng. No Git Bash required.
set "PYTHONUTF8=1"
if not defined PYTHON set "PYTHON=python"
"%PYTHON%" "%~dp0..\android-smoke.py" build %* --library libpng
exit /b %errorlevel%
