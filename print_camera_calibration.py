from pyri.device_manager_client import DeviceManagerClient
from RobotRaconteur.Client import *
import time
import numpy as np
from RobotRaconteurCompanion.Util.GeometryUtil import GeometryUtil


calib_name="camera_calibration_intrinsic"


d = DeviceManagerClient('rr+tcp://localhost:59902?service=device_manager', autoconnect=False)

d.refresh_devices(1)

d.connect_device("variable_storage")

var_storage = d.get_device_client("variable_storage",1)

extrinsic_var = var_storage.getf_variable_value("globals",calib_name)
intrinsic_var = var_storage.getf_variable_value("globals","camera_calibration_extrinsic")
robot_var = var_storage.getf_variable_value("globals","robot_origin_calibration")

calib = extrinsic_var.data

print("Camera Matrix")
print(calib.K)
d = calib.distortion_info.data
dist = np.array([d.k1,d.k2,d.p1,d.p2,d.k3])
print("Camera distortion")
print(dist)

geom_util = GeometryUtil(client_obj = var_storage)

T_cam = geom_util.named_pose_to_rox_transform(intrinsic_var.data.pose)
T_rob = geom_util.named_pose_to_rox_transform(robot_var.data.pose)

print("T_cam")
print(T_cam.R)
print(T_cam.p)

print("T_rob")
print(T_rob.R)
print(T_rob.p)

print("T")
T = (T_cam.inv() * T_rob).inv()
print(T.R)
print(T.p)