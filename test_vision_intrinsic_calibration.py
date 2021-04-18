from pyri.device_manager_client import DeviceManagerClient
from RobotRaconteur.Client import *
from RobotRaconteurCompanion.Util.ImageUtil import ImageUtil
import time
import cv2

d = DeviceManagerClient('rr+tcp://localhost:59902?service=device_manager', autoconnect=False)

d.refresh_devices(1)

d.connect_device("vision_camera_calibration")

calibration_service = d.get_device_client("vision_camera_calibration",1)

ret = calibration_service.calibrate_camera_intrinsic("camera", "intrinsic_calib_dataset0", "chessboard", "camera_intrinsic_calibration") #"camera_intrinsic_calibration")

image_util = ImageUtil(client_obj=calibration_service)
i=0
for c_img in ret.display_images:
    img = image_util.compressed_image_to_array(c_img)
    cv2.imshow(f"img {i}",img)
    cv2.waitKey()

    i+=1

cv2.destroyAllWindows()




