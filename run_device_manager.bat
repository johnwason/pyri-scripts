@echo off

setlocal

set ROBOTRACONTEUR_LOG_LEVEL=INFO
set ROBOTRACONTEUR_PYTHON_TRACEBACK_PRINT_EXC=1

title device_manager

cd C:\Users\wasonj\Documents\pyri\software\

call venv\Scripts\activate.bat

python -m pyri.device_manager --device-info-file=pyri-device-manager/config/pyri_device_manager_default_info.yml --variable-storage-url=rr+tcp://localhost:59901?service=variable_storage --robotraconteur-tcp-ws-add-origin=http://localhost:8000

