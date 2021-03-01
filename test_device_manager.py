from RobotRaconteur.Client import *

c = RRN.ConnectService('rr+tcp://localhost:59902?service=device_manager')

devs = c.getf_detected_devices()

print(devs)