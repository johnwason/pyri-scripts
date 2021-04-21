@echo off

setlocal

..\venv\Scripts\python add_device.py pyri_variable_storage variable_storage
..\venv\Scripts\python add_device.py pyri_devices_states devices_states
..\venv\Scripts\python add_device.py pyri_sandbox sandbox
..\venv\Scripts\python add_device.py pyri_robotics_jog_service robotics_jog
..\venv\Scripts\python add_device.py pyri_camera_viewer_service vision_camera_viewer
..\venv\Scripts\python add_device.py pyri_camera_calibration_service vision_camera_calibration
rem ..\venv\Scripts\python add_device.py pyri_vision_robot_calibration_service vision_robot_calibration
