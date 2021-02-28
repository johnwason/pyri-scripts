from RobotRaconteur.Client import *
from RobotRaconteurCompanion.Util.IdentifierUtil import IdentifierUtil

c = RRN.ConnectService('rr+tcp://localhost:59902?service=device_manager')

detected_devices=c.getf_detected_devices()

ident_util = IdentifierUtil(RRN, c)

c.add_device(ident_util.CreateIdentifierFromName("sawyer_robot"), "robot",None)