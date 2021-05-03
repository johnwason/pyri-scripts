from pyri.device_manager_client import DeviceManagerClient
from RobotRaconteur.Client import *
import time
from RobotRaconteurCompanion.Util.ImageUtil import ImageUtil
from RobotRaconteurCompanion.Util.GeometryUtil import GeometryUtil
import cv2
import numpy as np

d = DeviceManagerClient('rr+tcp://localhost:59902?service=device_manager', autoconnect=False)

d.refresh_devices(1)

d.connect_device("vision_aruco_detection")

c = d.get_device_client("vision_aruco_detection",1)

geom_util = GeometryUtil(client_obj = c)

b = RRN.NewStructure("com.robotraconteur.geometry.BoundingBox2D", c)
center = RRN.NewStructure("com.robotraconteur.geometry.NamedPose2D", c)
pose2d_dtype = RRN.GetNamedArrayDType("com.robotraconteur.geometry.Pose2D", c)
size2d_dtype = RRN.GetNamedArrayDType("com.robotraconteur.geometry.Size2D", c)
center.pose = np.zeros((1,),dtype=pose2d_dtype)
center.pose[0]["position"]["x"] = 990
center.pose[0]["position"]["y"] = 64
center.pose[0]["orientation"] = np.deg2rad(10)
b.center = center
size = np.zeros((1,),dtype=size2d_dtype)
size[0]["width"] = 100
size[0]["height"] = 100
b.size = size

#res = c.detect_aruco_stored_image("test18", "camera_intrinsic_calibration", "camera_extrinsic_calibration0", "DICT_4X4_1000", 200, 0.0375, None)
res = c.detect_aruco_camera_capture("camera", "camera_calibration_intrinsic", "camera_calibration_extrinsic", "DICT_4X4_1000", 200, 0.0375, None)

m = res.detected_markers[0]
print(m.marker_corners)

print(res.detected_markers)

xyz,rpy = geom_util.pose_to_xyz_rpy(m.marker_pose.pose)
T = geom_util.pose_to_rox_transform(m.marker_pose.pose)

img_util = ImageUtil(client_obj = c)
img = img_util.compressed_image_to_array(res.display_image)
cv2.imshow("",img)
cv2.waitKey()
cv2.destroyAllWindows()

