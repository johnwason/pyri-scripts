from RobotRaconteur.Client import *
from RobotRaconteurCompanion.Util import IdentifierUtil

c=RRN.ConnectService('rr+tcp://localhost:59902?service=device_manager')

ident_util = IdentifierUtil.IdentifierUtil(RRN, c)

devices = c.getf_detected_devices()
print("Detected devices:")
for d in devices:
    print(d.device.name)

print()

active_devices = c.getf_active_devices()
print("Active devices:")
for d in active_devices:
    print(d.local_device_name)

#robot_device_info = c.getf_detected_device_info(ident_util.CreateIdentifierFromName("sawyer_robot"))

#print(ident_util.IdentifierToString(robot_device_info.device))

#c.add_device(robot_device_info.device,"robot",[])

variable_storage_info = c.getf_detected_device_info(ident_util.CreateIdentifierFromName("pyri_variable_storage"))

c.add_device(variable_storage_info.device,"variable_storage",[])


c.device_detected += lambda d: print(f"Device detected: {d.name}")
c.device_lost += lambda d: print(f"Device lost: {d.name}")

print("Press enter to exit")
input()
