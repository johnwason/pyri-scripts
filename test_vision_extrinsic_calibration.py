from pyri.device_manager_client import DeviceManagerClient
from RobotRaconteur.Client import *
import time

d = DeviceManagerClient('rr+tcp://localhost:59902?service=device_manager', autoconnect=False)

d.refresh_devices(1)

d.connect_device("vision_camera_calibration")

calibration_service = d.get_device_client("vision_camera_calibration",1)

calibration_service.calibrate_camera_extrinsic("camera", "camera_intrinsic_calibration", "extrinsic_image0", "chessboard", "camera_extrinsic_calibration")



