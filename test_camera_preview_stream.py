from pyri.device_manager_client import DeviceManagerClient
from RobotRaconteur.Client import *
import time
import cv2

current_compressed_frame = None

def new_frame(pipe_ep):

    global current_compressed_frame
    
    while (pipe_ep.Available > 0):
        
        compressed_image=pipe_ep.ReceivePacket()

        current_compressed_frame=compressed_image


d = DeviceManagerClient('rr+tcp://localhost:59902?service=device_manager', autoconnect=False)

d.refresh_devices(1)

d.connect_device("vision_camera_viewer")

viewer_service = d.get_device_client("vision_camera_viewer",1)

print(viewer_service.device_info.device.name)

camera_viewer = viewer_service.get_camera_viewer("camera")

p=camera_viewer.preview_stream.Connect(-1)

p.PacketReceivedEvent+=new_frame

while True:

    if (not current_compressed_frame is None):
        img = cv2.imdecode(current_compressed_frame.data,1)

        cv2.imshow("Image",img)
    if cv2.waitKey(20)!=-1:
        break
cv2.destroyAllWindows()
