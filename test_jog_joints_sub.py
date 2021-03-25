from pyri.device_manager_client import DeviceManagerClient
from RobotRaconteur.Client import *
import time
import traceback
import os

print(os.getpid())
input()

d = DeviceManagerClient('rr+tcp://localhost:59902?service=device_manager',autoconnect=False)

d.refresh_devices(1)

d.connect_device('joint_jog')

jog_sub = d.get_device_subscription("jog_joint")

i = 0
dir = 0

while True:

    i += 1
    if i > 20:
        i = 0
    elif i > 10:
        dir = -1
    else:
        dir = 1

    try:
        jog_host = jog_sub.GetDefaultClient()
        jog = jog_host.get_jog('robot')
        
        jog.jog_joints3(1,dir)        
    except:
        traceback.print_exc()
    time.sleep(0.1)