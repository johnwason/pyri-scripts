from RobotRaconteur.Client import *
from RobotRaconteurCompanion.Util.IdentifierUtil import IdentifierUtil
import sys

device_name = sys.argv[1]
local_name = sys.argv[2]

c = RRN.ConnectService('rr+tcp://localhost:59902?service=device_manager')

detected_devices=c.getf_detected_devices()

ident_util = IdentifierUtil(RRN, c)

c.add_device(ident_util.CreateIdentifierFromName(device_name), local_name, None)
