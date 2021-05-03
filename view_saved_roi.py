from pyri.device_manager_client import DeviceManagerClient
from RobotRaconteur.Client import *
import time
import cv2
from RobotRaconteurCompanion.Util.ImageUtil import ImageUtil
import shapely
import shapely.geometry
import numpy as np

image_name="test14"
roi_name = "pick_roi4"


d = DeviceManagerClient('rr+tcp://localhost:59902?service=device_manager', autoconnect=False)

d.refresh_devices(1)

d.connect_device("variable_storage")

var_storage = d.get_device_client("variable_storage",1)

var = var_storage.getf_variable_value("globals",image_name)


image_util = ImageUtil(client_obj = var_storage)
display_img = image_util.compressed_image_to_array(var.data)

roi = var_storage.getf_variable_value("globals",roi_name).data

roi_x = roi.center.pose[0]["position"]["x"]
roi_y = roi.center.pose[0]["position"]["y"]
roi_theta = roi.center.pose[0]["orientation"]
roi_w = roi.size[0]["width"]
roi_h = roi.size[0]["height"]
geom_roi1 = shapely.geometry.box(-roi_w/2.,-roi_h/2.,roi_w/2.,roi_h/2.,ccw=True)
geom_roi2 = shapely.affinity.translate(geom_roi1, xoff = roi_x, yoff = roi_y)
geom_roi = shapely.affinity.rotate(geom_roi2, roi_theta, origin='centroid', use_radians=True)

roi_outline = np.array([geom_roi.exterior.coords],dtype=np.int32)
display_img = cv2.polylines(display_img, roi_outline, True, color=(255,255,0))

cv2.imshow("image",display_img)
cv2.waitKey()

 

cv2.destroyAllWindows()
