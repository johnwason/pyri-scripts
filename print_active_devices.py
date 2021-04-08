from RobotRaconteur.Client import *

c = RRN.ConnectService('rr+tcp://localhost:59902?service=device_manager')

active_devices = c.getf_active_devices()

for a in active_devices:
    print(f"local name: {a.local_device_name}")
    if a.device is not None:
        print(f"device name: {a.device.name}")
    print(f"urls:")
    for u in a.urls:
        print(f"    {u}")
    print()