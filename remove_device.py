from RobotRaconteur.Client import *
from RobotRaconteurCompanion.Util.IdentifierUtil import IdentifierUtil
import sys

local_name = sys.argv[1]

c = RRN.ConnectService('rr+tcp://localhost:59902?service=device_manager')


c.remove_device(local_name)
