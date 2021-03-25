from pyri.device_manager_client import DeviceManagerClient
from RobotRaconteur.Client import *
import time

d = DeviceManagerClient('rr+tcp://localhost:59902?service=device_manager', autoconnect=False)

d.refresh_devices(1)

d.connect_device('jog_joint')

jog_service = d.get_device_client("jog_joint",1)

print(jog_service.device_info.device.name)

tool = jog_service.get_tool("tool")

while(True):
    tool.open()
    time.sleep(0.5)
    tool.close()
    time.sleep(0.5)

