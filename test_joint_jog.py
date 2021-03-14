from pyri.device_manager_client import DeviceManagerClient
from RobotRaconteur.Client import *

d = DeviceManagerClient('rr+tcp://localhost:59902?service=device_manager', autoconnect=False)

#d.refresh_devices(1)

d.connect_device('joint_jog')

jog_service = d.get_device_client("joint_jog",1)

print(jog_service.device_info.device.name)

jog = jog_service.get_jog("robot")

jog.setf_jog_mode()

#for x in range(100):
    #jog.jog_joints3(1,1)
#jog.setf_halt_mode()

jog.jog_joints_to_angles([0.1,0.1,-0.1,0.1,-0.1,0.2,0.3])

