from pyri.device_manager_client import DeviceManagerClient
from RobotRaconteur.Client import *

d = DeviceManagerClient('rr+tcp://localhost:59902?service=device_manager', autoconnect=False)

d.refresh_devices(1)

d.connect_device("sandbox")

c = d.get_device_client("sandbox",1)

gen = c.getf_output()

while True:
    try:
        ret = gen.Next()
        print([l.output for l in ret.output_list])
    except RR.StopIterationException:
        break



# gen = c.execute_procedure("test_print_many", [])

# while True:
#      try:
#          print(gen.Next().printed)
#      except RR.StopIterationException:
#          break




    