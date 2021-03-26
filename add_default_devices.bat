@echo off

setlocal

..\venv\Scripts\python add_device.py pyri_variable_storage variable_storage
..\venv\Scripts\python add_device.py pyri_devices_states devices_states
..\venv\Scripts\python add_device.py pyri_sandbox sandbox
..\venv\Scripts\python add_device.py pyri_jog_joint_service jog_joint
..\venv\Scripts\python add_device.py pyri_jog_cartesian_service jog_cartesian
