from pyri.device_manager_client import DeviceManagerClient
from RobotRaconteur.Client import *
import time
import cv2

d = DeviceManagerClient('rr+tcp://localhost:59902?service=device_manager', autoconnect=False)

d.refresh_devices(1)

d.connect_device("vision_camera_viewer")

viewer_service = d.get_device_client("vision_camera_viewer",1)

print(viewer_service.device_info.device.name)

camera_viewer = viewer_service.get_camera_viewer("camera")

compressed_img = camera_viewer.capture_frame_preview()

img = cv2.imdecode(compressed_img.data,1)

cv2.imshow("image",img)
cv2.waitKey()




