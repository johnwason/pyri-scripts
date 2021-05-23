@echo off

setlocal

set ROBOTRACONTEUR_LOG_LEVEL=INFO
set ROBOTRACONTEUR_PYTHON_TRACEBACK_PRINT_EXC=1

title devices_states

cd %~dp0\..

call venv\Scripts\activate.bat

python -m pyri.devices_states

