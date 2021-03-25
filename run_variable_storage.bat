@echo off

setlocal

set ROBOTRACONTEUR_LOG_LEVEL=INFO
set ROBOTRACONTEUR_PYTHON_TRACEBACK_PRINT_EXC=1

title variable_storage

cd %~dp0\..

call venv\Scripts\activate.bat

python -m pyri.variable_storage --db-file=test3.db --device-info-file=pyri-variable-storage/config/pyri_variable_storage_default_info.yml --robotraconteur-tcp-ws-add-origin=http://localhost:8000,http://192.168.1.130:8000 --robotraconteur-tcp-ipv4-discovery=true

