from RobotRaconteur.Client import *

script_src = """

def hello_world():
    print("Hello world!")
"""

var_storage = RRN.ConnectService("rr+tcp://localhost:59901?service=variable_storage")
var_consts = RRN.GetConstants('tech.pyri.variable_storage', var_storage)
variable_persistence = var_consts["VariablePersistence"]
variable_protection_level = var_consts["VariableProtectionLevel"]

var_storage.add_variable2("procedure","hello_world","string", \
            RR.VarValue(script_src,"string"), ["pyri"], {}, variable_persistence["const"], None, variable_protection_level["read_write"], \
                [], "", False)

