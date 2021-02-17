from RobotRaconteur.Client import *

c=RRN.ConnectService('rr+tcp://localhost:59903?service=sandbox')

while(True):
    gen = c.execute_procedure("hello_world_blockly", [])

    res = gen.Next()
    gen.Close()

    print(res.result_code)
    print(res.printed)