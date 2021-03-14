from pyri.device_manager_client import DeviceManagerClient
from RobotRaconteur.Client import *
import time
import traceback
import os

print(os.getpid())
input()

d = DeviceManagerClient('rr+tcp://localhost:59902?service=device_manager',autoconnect=False)

d.refresh_devices(1)

d.connect_device('devices_states')

dev_states_sub = d.get_device_subscription("devices_states")
dev_states_wire_sub = dev_states_sub.SubscribeWire('devices_states')

while True:
    try:
        
        print(dev_states_wire_sub.InValue.seqno)
    except:
        traceback.print_exc()
    time.sleep(0.1)
