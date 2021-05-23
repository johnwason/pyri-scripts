@echo off

setlocal

set ROBOTRACONTEUR_LOG_LEVEL=INFO
set ROBOTRACONTEUR_PYTHON_TRACEBACK_PRINT_EXC=1

title robotics motion

cd %~dp0\..

call venv\Scripts\activate.bat

python -m pyri.robotics.robotics_motion_service

