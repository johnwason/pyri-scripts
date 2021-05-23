@echo off

setlocal

set ROBOTRACONTEUR_LOG_LEVEL=INFO
set ROBOTRACONTEUR_PYTHON_TRACEBACK_PRINT_EXC=1

title vision calibration

cd %~dp0\..

call venv\Scripts\activate.bat

python -m pyri.vision.camera_calibration_service

