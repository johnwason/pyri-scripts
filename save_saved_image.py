from pyri.device_manager_client import DeviceManagerClient
from RobotRaconteur.Client import *
import time
import cv2
from RobotRaconteurCompanion.Util.ImageUtil import ImageUtil

# image_name="image_seq1"
# image_name="template_match_test_image"
# image_name = "test5"
image_name = "aruco_cube0"

d = DeviceManagerClient('rr+tcp://localhost:59902?service=device_manager', autoconnect=False)

d.refresh_devices(1)

d.connect_device("variable_storage")

var_storage = d.get_device_client("variable_storage",1)

var = var_storage.getf_variable_value("globals",image_name)

img_util = ImageUtil(client_obj=var_storage)

def save_image(image, image_name):
    img2 = img_util.compressed_image_to_array(image)
    cv2.imwrite(f"{image_name}.png",img2)

if var.datatype == "com.robotraconteur.image.CompressedImage":
    save_image(var.data, image_name)
elif var.datatype == "string":
    image_names=var.data.splitlines()
    print(image_names)
    i = 0
    for image_name2 in image_names:
        var2 = var_storage.getf_variable_value("globals",image_name2)
        save_image(var2.data,f"{image_name}{i}")
        var2_attr = var_storage.getf_variable_attributes("globals",image_name2)
        print(var2_attr)
        i+=1
else:
    assert False, "Invalid variable type"    

cv2.destroyAllWindows()
