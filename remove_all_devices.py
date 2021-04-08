from RobotRaconteur.Client import *

c = RRN.ConnectService('rr+tcp://localhost:59902?service=device_manager')

active_devices = c.getf_active_devices()

for a in active_devices:
    c.remove_device(a.local_device_name)