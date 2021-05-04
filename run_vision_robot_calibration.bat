@echo off

setlocal

set ROBOTRACONTEUR_LOG_LEVEL=INFO
set ROBOTRACONTEUR_PYTHON_TRACEBACK_PRINT_EXC=1

title robot calibration

cd %~dp0\..

call venv\Scripts\activate.bat

python -m pyri.vision.robot_calibration_service --device-info-file=pyri-vision/config/pyri_vision_robot_calibration_service_default_info.yml --device-manager-url=rr+tcp://localhost:59902?service=device_manager --robotraconteur-tcp-ipv4-discovery=true

