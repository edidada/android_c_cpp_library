@echo off
setlocal
rem Windows to Android: libssh2. No Git Bash required.
set "PYTHONUTF8=1"
if not defined PYTHON set "PYTHON=python"
"%PYTHON%" "%~dp0..\android-smoke.py" build %* --library libssh2
exit /b %errorlevel%
