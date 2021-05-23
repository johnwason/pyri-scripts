@echo off

setlocal

set ROBOTRACONTEUR_LOG_LEVEL=INFO
set ROBOTRACONTEUR_PYTHON_TRACEBACK_PRINT_EXC=1

title webui_server

cd %~dp0\..

call venv\Scripts\activate.bat

python -m pyri.webui_server --device-manager-url="rr+tcp://{{ HOSTNAME }}:59902?service=device_manager"

