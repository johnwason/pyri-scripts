from atexit import register
import RobotRaconteur as RR
RRN = RR.RobotRaconteurNode.s

from pyri.util.robotraconteur import register_default_ws_origins

with RR.ServerNodeSetup("test.register_default_ws_origins",63847) as node_setup:
    register_default_ws_origins(node_setup.tcp_transport, 8000)

    print(node_setup.tcp_transport.GetWebSocketAllowedOrigins())
