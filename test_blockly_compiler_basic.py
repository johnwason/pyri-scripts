from pyri.sandbox.blockly_compiler import BlocklyCompiler

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

c = BlocklyCompiler()

py_code = c.compile("hello_world_blockly", script_src)

print(py_code)