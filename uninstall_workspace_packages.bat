@echo off

setlocal

cd %~dp0\..

venv\Scripts\python -m pip uninstall pyri-common pyri-variable-storage ^
    pyri-device-manager pyri-devices-states pyri-sandbox pyri-webui-server ^
    pyri-core pyri-robotics pyri-example-plugin -y