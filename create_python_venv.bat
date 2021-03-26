@echo off

@echo off

setlocal

cd %~dp0\..

if exist venv\Scripts\python.exe (
    echo Python virtual environment already created, exiting
    exit /B
)

python -m venv venv