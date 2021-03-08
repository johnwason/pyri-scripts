from RobotRaconteur.Client import *

db = RRN.ConnectService('rr+tcp://localhost:59901?service=variable_storage')

res = db.filter_variables("procedure", "", ["blockly","pyri"])

print(res)