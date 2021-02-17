from RobotRaconteur.Client import *

script_src = """
<xml xmlns="https://developers.google.com/blockly/xml">
  <block type="procedures_defnoreturn" id="ig-@O/ylKy_@*tL~m@X|" x="138" y="88">
    <field name="NAME">hello_world_blockly</field>
    <comment pinned="false" h="80" w="160">Describe this function...</comment>
    <statement name="STACK">
      <block type="text_print" id="leNnyydaklEu0$|E4fU~">
        <value name="TEXT">
          <shadow type="text" id="wWggJq|t$BAzKbOf`dtu">
            <field name="TEXT">Hello World from Blockly!</field>
          </shadow>
        </value>
      </block>
    </statement>
  </block>
</xml>
"""

var_storage = RRN.ConnectService("rr+tcp://localhost:59901?service=variable_storage")
var_consts = RRN.GetConstants('tech.pyri.variable_storage', var_storage)
variable_persistence = var_consts["VariablePersistence"]
variable_protection_level = var_consts["VariableProtectionLevel"]

var_storage.add_variable2("procedure","hello_world_blockly","string", \
            RR.VarValue(script_src,"string"), ["blockly"], {}, variable_persistence["const"], None, variable_protection_level["read_write"], \
                [], "", False)

