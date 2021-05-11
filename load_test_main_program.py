from RobotRaconteur.Client import *
from RobotRaconteurCompanion.Util.UuidUtil import UuidUtil
import uuid

var_storage = RRN.ConnectService("rr+tcp://localhost:59901?service=variable_storage")
var_consts = RRN.GetConstants('tech.pyri.variable_storage', var_storage)
variable_persistence = var_consts["VariablePersistence"]
variable_protection_level = var_consts["VariableProtectionLevel"]

program_type = RRN.GetStructureType("tech.pyri.program_master.PyriProgram",var_storage)
program_step_type = RRN.GetStructureType("tech.pyri.program_master.PyriProgramStep",var_storage)
program_step_next_type = RRN.GetStructureType("tech.pyri.program_master.PyriProgramStepNext",var_storage)
program_const = RRN.GetConstants("tech.pyri.program_master",var_storage)

uuid_util = UuidUtil(client_obj = var_storage)

def fill_next():
    default = program_step_next_type()
    default.result = "DEFAULT"
    default.op_code = program_const["PyriProgramStepNextOpCode"]["next"]
    default.jump_target = uuid_util.UuidFromPyUuid(uuid.UUID(bytes=b'\x00'*16))

    err = program_step_next_type()
    err.result = "ERROR"
    err.op_code = program_const["PyriProgramStepNextOpCode"]["error"]
    err.jump_target = uuid_util.UuidFromPyUuid(uuid.UUID(bytes=b'\x00'*16))

    return [default,err]


program = program_type()
program.name = "main"
program.steps = []

step1 = program_step_type()
step1.step_name = "step1"
step1.step_id = uuid_util.NewRandomUuid()
step1.procedure_name = "print1"
step1.procedure_args = []
step1.next = fill_next()

program.steps.append(step1)

step2 = program_step_type()
step2.step_name = "step2"
step2.step_id = uuid_util.NewRandomUuid()
step2.procedure_name = "print2"
step2.procedure_args = []
step2.next = fill_next()

program.steps.append(step2)

step3 = program_step_type()
step3.step_name = "step3"
step3.step_id = uuid_util.NewRandomUuid()
step3.procedure_name = "print3"
step3.procedure_args = []

jump = program_step_next_type()
jump.result = "DEFAULT"
jump.op_code = program_const["PyriProgramStepNextOpCode"]["jump"]
jump.jump_target = step1.step_id

step3.next = [jump,fill_next()[1]]

program.steps.append(step3)


try:
  var_storage.delete_variable("program", "main")
except:
  pass

var_storage.add_variable2("program","main","tech.pyri.program_master.PyriProgram", \
            RR.VarValue(program,"tech.pyri.program_master.PyriProgram"), ["program"], {}, variable_persistence["const"], None, variable_protection_level["read_write"], \
                [], "test state machine program", False)