from pyri.device_manager_client import DeviceManagerClient
from RobotRaconteur.Client import *

import numpy as np

d = DeviceManagerClient('rr+tcp://localhost:59902?service=device_manager', autoconnect=False)

d.refresh_devices(1)

d.connect_device("robotics_motion")

c = d.get_device_client("robotics_motion",1)

target_j = np.random.randn(6)

gen = c.movej("robot", target_j, 50)

while True:
    try:
        gen.Next()
    except RR.StopIterationException:
        break