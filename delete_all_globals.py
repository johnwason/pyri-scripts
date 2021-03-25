from RobotRaconteur.Client import *

var_storage = RRN.ConnectService("rr+tcp://localhost:59901?service=variable_storage")
var_consts = RRN.GetConstants('tech.pyri.variable_storage', var_storage)

globals_names = var_storage.filter_variables("globals","",[])
print(globals_names)
for g in globals_names:
  var_storage.delete_variable("globals",g)

