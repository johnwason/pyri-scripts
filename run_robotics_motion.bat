@echo off

setlocal

set ROBOTRACONTEUR_LOG_LEVEL=INFO
set ROBOTRACONTEUR_PYTHON_TRACEBACK_PRINT_EXC=1

title robotics motion

cd %~dp0\..

call venv\Scripts\activate.bat

python -m pyri.robotics.robotics_motion_service --device-info-file=pyri-robotics/config/pyri_robotics_motion_service_default_info.yml --device-manager-url=rr+tcp://localhost:59902?service=device_manager --robotraconteur-tcp-ipv4-discovery=true

