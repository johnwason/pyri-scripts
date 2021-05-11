from pyri.device_manager_client import DeviceManagerClient
from RobotRaconteur.Client import *
from RobotRaconteurCompanion.Util.GeometryUtil import GeometryUtil

import numpy as np

import general_robotics_toolbox as rox

d = DeviceManagerClient('rr+tcp://localhost:59902?service=device_manager', autoconnect=False)

d.refresh_devices(1)

d.connect_device("robotics_motion")
d.connect_device("robot")

c = d.get_device_client("robotics_motion",1)

#p_target = np.array([-np.random.uniform(0.4,0.8),np.random.uniform(-0.1,0.1),np.random.uniform(0.0,0.4)])
p_target = np.array([-np.random.uniform(-0.1,0.1),np.random.uniform(-0.1,0.1),np.random.uniform(0.0,0.4)])
rpy_target = np.random.randn(3)*0.5
rpy_target[0] += np.pi
R_target = rox.rpy2R(rpy_target)
# p_target = np.array([-0.6, 0.0, 0.1])
# R_target = np.array([[0,1,0],[1,0,0],[0,0,-1]])
T_target = rox.Transform(R_target,p_target)

r = d.get_device_client("robot", 1)

geom_util = GeometryUtil(client_obj = r)
p_target = geom_util.rox_transform_to_pose(T_target)

print("Begin movel")
gen = c.movel("robot", p_target, "world", "robot_origin_calibration", 50)

while True:
    try:
        gen.Next()
    except RR.StopIterationException:
        break
print("End movel")