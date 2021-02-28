from RobotRaconteur.Client import *

c = RRN.ConnectService('rr+tcp://localhost:59905?service=devices_states')

pyri_dev_info = c.getf_device_info('variable_storage')
print(pyri_dev_info)

dev_info = c.getf_standard_device_info('variable_storage')
print(dev_info)

extended_dev_info = c.getf_extended_device_info('variable_storage')
print(extended_dev_info)