from pyri.device_manager_client import DeviceManagerClient
from RobotRaconteur.Client import *

import time

d = DeviceManagerClient('rr+tcp://localhost:59902?service=device_manager')

d.refresh_devices(1)


jog_service = d.get_device_client("cartesian_jog",1)

print(jog_service.device_info.device.name)

jog = jog_service.get_jog("robot")

#jog.setf_jog_mode()

#for x in range(100):
    #jog.jog_joints3(1,1)
#jog.setf_halt_mode()

jog.prepare_jog()

while True:
    for i in range(20):
        jog.jog_cartesian3([0,0,1],[0,0,0])
        time.sleep(0.005)

    jog.stop_joints()

    for i in range(20):
        jog.jog_cartesian3([0,0,-1],[0,0,0])
        time.sleep(0.005)

    jog.stop_joints()
