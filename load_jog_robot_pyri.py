from RobotRaconteur.Client import *

script_src = """

def jog_robot():
    robot_jog_freespace("robot", [0.2,-0.2,0.2,-0.2,0.2,1,1])
    sleep(2)
    robot_jog_freespace("robot", [0,0,0,0,0,0,0])
"""

var_storage = RRN.ConnectService("rr+tcp://localhost:59901?service=variable_storage")
var_consts = RRN.GetConstants('tech.pyri.variable_storage', var_storage)
variable_persistence = var_consts["VariablePersistence"]
variable_protection_level = var_consts["VariableProtectionLevel"]

var_storage.delete_variable("procedure", "jog_robot")

var_storage.add_variable2("procedure","jog_robot","string", \
            RR.VarValue(script_src,"string"), ["pyri"], {}, variable_persistence["const"], None, variable_protection_level["read_write"], \
                [], "", True)

