from RobotRaconteur.Client import *

var_storage = RRN.ConnectService("rr+tcp://localhost:59901?service=variable_storage")
pyri_src = var_storage.getf_variable_value("procedure", "test_pyri")
print(pyri_src)

