from pyri.device_manager_client import DeviceManagerClient
from RobotRaconteur.Client import *
import time
from RobotRaconteurCompanion.Util.ImageUtil import ImageUtil
from RobotRaconteurCompanion.Util.GeometryUtil import GeometryUtil
import cv2

d = DeviceManagerClient('rr+tcp://localhost:59902?service=device_manager', autoconnect=False)

d.refresh_devices(1)

d.connect_device("vision_camera_calibration")

calibration_service = d.get_device_client("vision_camera_calibration",1)

ret = calibration_service.calibrate_camera_extrinsic("camera", "camera_intrinsic_calibration", "extrinsic_image0", "chessboard", "camera_extrinsic_calibration0") # "camera_extrinsic_calibration1")

image_util = ImageUtil(client_obj = calibration_service)
geom_util = GeometryUtil(client_obj = calibration_service)

T = geom_util.named_pose_to_rox_transform(ret.camera_pose.pose)
print(T)
print(ret)

img = image_util.compressed_image_to_array(ret.display_image)
cv2.imshow(f"img",img)
cv2.waitKey()

cv2.destroyAllWindows()



