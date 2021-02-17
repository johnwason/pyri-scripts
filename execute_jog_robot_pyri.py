from RobotRaconteur.Client import *

c=RRN.ConnectService('rr+tcp://localhost:59903?service=sandbox')

gen = c.execute_procedure("jog_robot", [])

res = gen.Next()

print(res.result_code)
print(res.printed)