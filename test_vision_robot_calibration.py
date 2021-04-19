from pyri.device_manager_client import DeviceManagerClient
from RobotRaconteur.Client import *
import time
from RobotRaconteurCompanion.Util.ImageUtil import ImageUtil
from RobotRaconteurCompanion.Util.GeometryUtil import GeometryUtil
import numpy as np
import cv2

d = DeviceManagerClient('rr+tcp://localhost:59902?service=device_manager', autoconnect=False)

d.refresh_devices(1)

d.connect_device("vision_robot_calibration")

calibration_service = d.get_device_client("vision_robot_calibration",1)

geom_util = GeometryUtil(client_obj=calibration_service)
marker_pose = geom_util.xyz_rpy_to_pose(np.array([0,0.04,0]),np.array([-np.pi/2.0,0.0,0.0]))

ret = calibration_service.calibrate_robot_origin("robot", "camera_intrinsic_calibration", "camera_extrinsic_calibration0",  "robot_calibration_seq0", "DICT_6X6_250", 120, 0.06, marker_pose, "robot_origin_calibration0") # "robot_origin_calibration0"

image_util = ImageUtil(client_obj = calibration_service)
geom_util = GeometryUtil(client_obj = calibration_service)

T = geom_util.named_pose_to_rox_transform(ret.robot_pose.pose)
print(T)
print(ret)

for img1 in ret.display_images:
    img = image_util.compressed_image_to_array(img1)
    cv2.imshow(f"img",img)
    cv2.waitKey()

cv2.destroyAllWindows()



