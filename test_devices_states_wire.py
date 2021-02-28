from RobotRaconteur.Client import *

c = RRN.ConnectService('rr+tcp://localhost:59905?service=devices_states')

devices_states,_ = c.devices_states.PeekInValue()

print(devices_states)