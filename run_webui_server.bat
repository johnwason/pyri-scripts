@echo off

setlocal

set ROBOTRACONTEUR_LOG_LEVEL=INFO
set ROBOTRACONTEUR_PYTHON_TRACEBACK_PRINT_EXC=1

title webui_server

cd %~dp0\..

call venv\Scripts\activate.bat

python -m pyri.webui_server --device-manager-url=rr+tcp://192.168.1.130:59902?service=device_manager --robotraconteur-tcp-ipv4-discovery=true

