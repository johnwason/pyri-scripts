@echo off

setlocal

..\venv\Scripts\python add_device.py pyri_variable_storage variable_storage
..\venv\Scripts\python add_device.py pyri_devices_states devices_states
..\venv\Scripts\python add_device.py pyri_sandbox sandbox
..\venv\Scripts\python add_device.py pyri_robotics_jog_service robotics_jog
