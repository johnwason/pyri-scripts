from RobotRaconteur.Client import *

c=RRN.ConnectService('rr+tcp://localhost:59903?service=sandbox')

gen = c.execute_procedure("hello_world", [])

res = gen.Next()

print(res.result_code)
print(res.printed)