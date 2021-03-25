@echo off

setlocal

set ROBOTRACONTEUR_LOG_LEVEL=INFO
set ROBOTRACONTEUR_PYTHON_TRACEBACK_PRINT_EXC=1

title jog_cart

cd C:\Users\wasonj\Documents\pyri\software\

call venv\Scripts\activate.bat

python -m pyri.robotics.jog_cartesian_service --device-info-file=pyri-robotics/config/pyri_jog_cartesian_service_default_info.yml --device-manager-url=rr+tcp://localhost:59902?service=device_manager --robotraconteur-tcp-ws-add-origin=http://localhost:8000,http://192.168.1.130:8000 --robotraconteur-tcp-ipv4-discovery=true

