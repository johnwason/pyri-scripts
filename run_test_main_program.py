from RobotRaconteur.Client import *
from RobotRaconteurCompanion.Util.UuidUtil import UuidUtil
import uuid

from pyri.device_manager_client import DeviceManagerClient
from RobotRaconteur.Client import *

import numpy as np
import time

d = DeviceManagerClient('rr+tcp://localhost:59902?service=device_manager', autoconnect=False)

d.refresh_devices(1)

d.connect_device("program_master")

c = d.get_device_client("program_master",1)

c.run()

time.sleep(4.1)

c.pause()
time.sleep(1)
c.clear_step_pointer()