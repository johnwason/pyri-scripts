@echo off

setlocal

cd %~dp0\..

where /q npm
IF ERRORLEVEL 1 (
    ECHO NodeJS npm command is not found. Install NodeJS before continuing
    EXIT /B 100
)

venv\Scripts\python -m pip uninstall pyri-common -y
venv\Scripts\python -m pip uninstall pyri-variable-storage -y
venv\Scripts\python -m pip uninstall pyri-device-manager -y
venv\Scripts\python -m pip uninstall pyri-devices-states -y
venv\Scripts\python -m pip uninstall pyri-sandbox -y
venv\Scripts\python -m pip uninstall pyri-webui-server -y
venv\Scripts\python -m pip uninstall pyri-core -y
venv\Scripts\python -m pip uninstall pyri-robotics -y
venv\Scripts\python -m pip uninstall pyri-vision -y
venv\Scripts\python -m pip uninstall pyri-example-plugin -y

venv\Scripts\python -m pip install -e pyri-common
if %errorlevel% neq 0 exit /b %errorlevel%
venv\Scripts\python -m pip install -e pyri-variable-storage
if %errorlevel% neq 0 exit /b %errorlevel%
venv\Scripts\python -m pip install -e pyri-device-manager
if %errorlevel% neq 0 exit /b %errorlevel%
venv\Scripts\python -m pip install -e pyri-devices-states
if %errorlevel% neq 0 exit /b %errorlevel%
venv\Scripts\python -m pip install -e pyri-sandbox
if %errorlevel% neq 0 exit /b %errorlevel%
venv\Scripts\python -m pip install -e pyri-webui-server
if %errorlevel% neq 0 exit /b %errorlevel%
venv\Scripts\python -m pip install -e pyri-core
if %errorlevel% neq 0 exit /b %errorlevel%
venv\Scripts\python -m pip install -e pyri-robotics
if %errorlevel% neq 0 exit /b %errorlevel%
venv\Scripts\python -m pip install -e pyri-vision
if %errorlevel% neq 0 exit /b %errorlevel%
venv\Scripts\python -m pip install -e pyri-example-plugin
if %errorlevel% neq 0 exit /b %errorlevel%

venv\Scripts\python -m pip install requests packaging wheel
if %errorlevel% neq 0 exit /b %errorlevel%

@REM venv\Scripts\pyri-sandbox-service --install-blockly-compiler
@REM if %errorlevel% neq 0 exit /b %errorlevel%

cd scripts
..\venv\Scripts\python install_webui_browser_wheels.py
if %errorlevel% neq 0 exit /b %errorlevel%
..\venv\Scripts\python install_webui_browser_deps.py
if %errorlevel% neq 0 exit /b %errorlevel%
