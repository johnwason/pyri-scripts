from pyri.device_manager_client import DeviceManagerClient
from RobotRaconteur.Client import *
import time
import cv2

# image_name="image_seq1"
image_name="intrinsic_calib_dataset0"

d = DeviceManagerClient('rr+tcp://localhost:59902?service=device_manager', autoconnect=False)

d.refresh_devices(1)

d.connect_device("variable_storage")

var_storage = d.get_device_client("variable_storage",1)

var = var_storage.getf_variable_value("globals",image_name)

def show_image(image):
    cv_image=image.data.reshape([image.image_info.height, image.image_info.width, int(len(image.data)/(image.image_info.height*image.image_info.width))], order='C')

    cv2.imshow("image",cv_image)
    cv2.waitKey()

if var.datatype == "com.robotraconteur.image.Image":
    show_image(var.data)
elif var.datatype == "string":
    image_names=var.data.splitlines()
    print(image_names)
    for image_name2 in image_names:
        var2 = var_storage.getf_variable_value("globals",image_name2)
        show_image(var2.data)
        var2_attr = var_storage.getf_variable_attributes("globals",image_name2)
        print(var2_attr)
else:
    assert False, "Invalid variable type"    

cv2.destroyAllWindows()
