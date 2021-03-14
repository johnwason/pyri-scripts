@echo off

setlocal

set ROBOTRACONTEUR_LOG_LEVEL=INFO
set ROBOTRACONTEUR_PYTHON_TRACEBACK_PRINT_EXC=1

title variable_storage

cd C:\Users\wasonj\Documents\pyri\software\

call venv\Scripts\activate.bat

python -m pyri.variable_storage --db-file=test3.db --device-info-file=pyri-variable-storage/config/pyri_variable_storage_default_info.yml --robotraconteur-tcp-ws-add-origin=http://localhost:8000

