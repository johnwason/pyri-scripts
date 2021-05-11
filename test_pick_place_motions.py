from pyri.device_manager_client import DeviceManagerClient
from RobotRaconteur.Client import *
import time
from RobotRaconteurCompanion.Util.ImageUtil import ImageUtil
from RobotRaconteurCompanion.Util.GeometryUtil import GeometryUtil
import cv2
import numpy as np

d = DeviceManagerClient('rr+tcp://localhost:59902?service=device_manager', autoconnect=False)

d.refresh_devices(1)

d.connect_device("robotics_motion")

c = d.get_device_client("robotics_motion",1)

geom_util = GeometryUtil(client_obj = c)


def _run_grab(gen):
    while True:
        try:
            res = gen.Next()
            print(res)
        except RR.StopIterationException:
            break

for i in range(5):
    pose2d_dtype = RRN.GetNamedArrayDType("com.robotraconteur.geometry.Pose2D", c)
    obj_pose = np.zeros((1,),dtype=pose2d_dtype)
    obj_pose[0]["position"]["x"] = 0.1
    obj_pose[0]["position"]["y"] = 0.1
    obj_pose[0]["orientation"] = np.deg2rad(10)

    _run_grab(c.grab_object_planar("robot","tool","robot_origin_calibration","pick_reference",obj_pose, 0.05, 0.01, 50))
    obj_pose[0]["orientation"] = np.deg2rad(120)
    obj_pose[0]["position"]["x"] = -0.2
    _run_grab(c.grab_object_planar("robot","tool","robot_origin_calibration","pick_reference",obj_pose, 0.05, 0.01, 50))

