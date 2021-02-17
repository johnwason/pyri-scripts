from RobotRaconteur.Client import *

c=RRN.ConnectService('rr+tcp://localhost:59903?service=sandbox')


gen = c.execute_procedure("print2_blockly", [])

res = gen.Next()
gen.Close()

print(res.result_code)
print(res.printed)