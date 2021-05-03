from pyri.device_manager_client import DeviceManagerClient
from RobotRaconteur.Client import *
import time
import cv2
from RobotRaconteurCompanion.Util.ImageUtil import ImageUtil
from pathlib import Path

seq_name = "imported_img_seq0"
source_dir = Path(r"C:\Users\wasonj\Documents\pyri\rpi\TeachPendant-Sawyer\RR-plugins\src\plugin-cameraCalibration\calibration_imgs_backup_kinect_lab3")

img_name_prefix="images"
img_name_ext = ".png"
img_count = 50

imgs = []

for i in range(img_count):
    p = source_dir.joinpath(f"{img_name_prefix}{i}{img_name_ext}")
    imgs.append(cv2.imread(str(p)))

# for img in imgs:
#     cv2.imshow("",img)
#     cv2.waitKey(250)


d = DeviceManagerClient('rr+tcp://localhost:59902?service=device_manager', autoconnect=False)

d.refresh_devices(1)

d.connect_device("variable_storage")

var_storage = d.get_device_client("variable_storage",1)

image_util = ImageUtil(client_obj = var_storage)

var_consts = var_storage.RRGetNode().GetConstants('tech.pyri.variable_storage', var_storage)
variable_persistence = var_consts["VariablePersistence"]
variable_protection_level = var_consts["VariableProtectionLevel"]

def save_image(img, i):
    global_name = f"{seq_name}_{i}"
    

    if len(var_storage.filter_variables("globals",global_name,[])) > 0:
        raise RR.InvalidOperationException(f"Global {global_name} already exists")
        
    img = image_util.array_to_compressed_image_png(img)

    attrs = {}
    
    var_storage.add_variable2("globals",global_name,"com.robotraconteur.image.CompressedImage", \
        RR.VarValue(img,"com.robotraconteur.image.CompressedImage"), ["image"], attrs, variable_persistence["const"], 
        None, variable_protection_level["read_write"], \
        [], "Imported image", False)


for i in range(len(imgs)):
    img = imgs[i]
    save_image(img,i)

seq_text = "\n".join([f"{seq_name}_{i}" for i in range(len(imgs))])

var_storage.add_variable2("globals",seq_name,"string", \
        RR.VarValue(seq_text,"string"), ["image_sequence"], {}, variable_persistence["const"], 
        None, variable_protection_level["read_write"], \
        [], "Imported image sequence", False)
