from pyri.device_manager_client import DeviceManagerClient
from RobotRaconteur.Client import *
import time
from RobotRaconteurCompanion.Util.ImageUtil import ImageUtil
from RobotRaconteurCompanion.Util.GeometryUtil import GeometryUtil
import cv2

roi_name = "pick_roi4"
template_name = "perfume_template4"

d = DeviceManagerClient('rr+tcp://localhost:59902?service=device_manager', autoconnect=False)

d.refresh_devices(1)

d.connect_device("vision_template_matching")
d.connect_device("variable_storage")

c = d.get_device_client("vision_template_matching",1)

bounding_box2d_type = RRN.GetStructureType('com.robotraconteur.geometry.BoundingBox2D',c)
named_pose2d_type = RRN.GetStructureType('com.robotraconteur.geometry.NamedPose2D', c)
pose2d_dtype = RRN.GetNamedArrayDType('com.robotraconteur.geometry.Pose2D', c)

var_storage = d.get_device_client("variable_storage",1)

roi = var_storage.getf_variable_value("globals",roi_name).data

#res = c.match_template_stored_image("extrinsic_image0", "test10", None)
res = c.match_template_world_pose_camera_capture("camera", template_name, "camera_calibration_intrinsic", "camera_calibration_extrinsic", 0, None)

img_util = ImageUtil(client_obj = c)
res_img = img_util.compressed_image_to_array(res.display_image)

geom_util = GeometryUtil(client_obj = c)

xyz, rpy, _, _ = geom_util.named_pose_to_xyz_rpy(res.template_matches[0].pose.pose)

cv2.imshow("",res_img)
cv2.waitKey()
cv2.destroyAllWindows()

print(res)