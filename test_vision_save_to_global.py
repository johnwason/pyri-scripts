from pyri.device_manager_client import DeviceManagerClient
from RobotRaconteur.Client import *
import time

d = DeviceManagerClient('rr+tcp://localhost:59902?service=device_manager', autoconnect=False)

d.refresh_devices(1)

d.connect_device("vision_camera_viewer")

viewer_service = d.get_device_client("vision_camera_viewer",1)

cam = viewer_service.get_camera_viewer("camera")

cam.save_to_globals("image1",True)

