@echo off

setlocal

set ROBOTRACONTEUR_LOG_LEVEL=INFO
set ROBOTRACONTEUR_PYTHON_TRACEBACK_PRINT_EXC=1

title program_master

cd %~dp0\..

call venv\Scripts\activate.bat

python -m pyri.program_master --device-info-file=pyri-program-master/config/pyri_program_master_default_info.yml --device-manager-url=rr+tcp://localhost:59902?service=device_manager --robotraconteur-tcp-ipv4-discovery=true

