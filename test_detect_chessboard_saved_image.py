from pyri.device_manager_client import DeviceManagerClient
from RobotRaconteur.Client import *
import time
import cv2
import numpy as np

# image_name="image_seq1"
image_name="intrinsic_calib_dataset0"

d = DeviceManagerClient('rr+tcp://localhost:59902?service=device_manager', autoconnect=False)

d.refresh_devices(1)

d.connect_device("variable_storage")

var_storage = d.get_device_client("variable_storage",1)

var = var_storage.getf_variable_value("globals",image_name)

def draw(img, corners, imgpts):
    corner = tuple(corners[0].ravel())
    img = cv2.line(img, corner, tuple(imgpts[0].ravel()), (255,0,0), 5)
    img = cv2.line(img, corner, tuple(imgpts[1].ravel()), (0,255,0), 5)
    img = cv2.line(img, corner, tuple(imgpts[2].ravel()), (0,0,255), 5)
    return img

def show_image(image):
    cv_image=image.data.reshape([image.image_info.height, image.image_info.width, int(len(image.data)/(image.image_info.height*image.image_info.width))], order='C')

    width = 7
    height = 6
    square_size=0.03

    gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)

    ret, corners = cv2.findChessboardCorners(gray, (width, height), None)
    print(ret)
    print(corners)

    cv2.imshow("chessboard",cv_image)
    cv2.waitKey(500)

    objp = np.zeros((height*width, 3), np.float32)
    objp[:, :2] = np.mgrid[0:width, 0:height].T.reshape(-1, 2)

    objp = objp * square_size

    mtx = np.array([[616.23,0,641.29],[0,617.23,359.53],[0.0,0.0,1.0]])
    dist = np.array([8.58e-2, -5.4e-2, -3.21e-3, 3.82e-4, 1.35e-2])
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    axis = np.float32([[3,0,0], [0,3,0], [0,0,-3]]).reshape(-1,3)*0.03

    corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
    # Find the rotation and translation vectors.
    ret,rvecs, tvecs = cv2.solvePnP(objp, corners2, mtx, dist)
    # project 3D points to image plane
    imgpts, jac = cv2.projectPoints(axis, rvecs, tvecs, mtx, dist)
    cv_image2 = draw(cv_image,corners2,imgpts)

    cv2.imshow("chessboard_pose",cv_image2)
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
