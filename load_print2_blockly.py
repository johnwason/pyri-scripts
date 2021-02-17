from RobotRaconteur.Client import *

script_src = """
<xml xmlns="https://developers.google.com/blockly/xml">
  <block type="procedures_defnoreturn" id="ig-@O/ylKy_@*tL~m@X|" x="138" y="88">
    <field name="NAME">print2_blockly</field>
    <comment pinned="false" h="80" w="160">Describe this function...</comment>
    <statement name="STACK">
      <block type="text_print2" id="leNnyydaklEu0$|E4fU~">
        <value name="TEXT">
          <shadow type="text" id="wWggJq|t$BAzKbOf`dtu">
            <field name="TEXT">Hello World from Blockly text_print2 plugin block!</field>
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

try:
  var_storage.delete_variable("procedure", "print2_blockly")
except:
  pass

var_storage.add_variable2("procedure","print2_blockly","string", \
            RR.VarValue(script_src,"string"), ["blockly"], {}, variable_persistence["const"], None, variable_protection_level["read_write"], \
                [], "text_print2 example diagram", False)

