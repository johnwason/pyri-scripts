from pyri.device_manager_client import DeviceManagerClient
from RobotRaconteur.Client import *
import time

d = DeviceManagerClient('rr+tcp://localhost:59902?service=device_manager', autoconnect=False)

d.refresh_devices(1)

d.connect_device("variable_storage")

var = d.get_device_client("variable_storage",1)

print(var.filter_variables("globals","",[]))