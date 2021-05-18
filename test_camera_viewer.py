from pyri.device_manager_client import DeviceManagerClient
from RobotRaconteur.Client import *

import time

d = DeviceManagerClient('rr+tcp://localhost:59902?service=device_manager')

d.refresh_devices(1)


viewer = d.get_device_client("vision_camera_viewer",1)
cam = viewer.get_camera_viewer("camera")

cam.capture_frame_preview()