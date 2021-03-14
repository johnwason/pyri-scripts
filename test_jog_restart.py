import subprocess
import time

while True:

    p = subprocess.Popen([r"C:\Users\wasonj\Documents\pyri\software\venv\Scripts\python.exe", "-m", "pyri.robotics.jog_joint_service", "--device-info-file=pyri-robotics/config/pyri_jog_joint_service_default_info.yml", "--device-manager-url=rr+tcp://localhost:59902?service=device_manager", "--robotraconteur-tcp-ws-add-origin=http://localhost:8000"])
    time.sleep(10)
    p.kill()
    time.sleep(5)
