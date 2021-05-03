from pyri.device_manager_client import DeviceManagerClient
from RobotRaconteur.Client import *
import time
import numpy as np



calib_name="camera_intrinsic_calibration"


d = DeviceManagerClient('rr+tcp://localhost:59902?service=device_manager', autoconnect=False)

d.refresh_devices(1)

d.connect_device("variable_storage")

var_storage = d.get_device_client("variable_storage",1)

var = var_storage.getf_variable_value("globals",calib_name)

calib = var.data

print(calib.K.tolist())
d = calib.distortion_info.data
dist = np.array([d.k1,d.k2,d.p1,d.p2,d.k3])
print(dist.tolist())