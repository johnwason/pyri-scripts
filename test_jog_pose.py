from pyri.device_manager_client import DeviceManagerClient
from RobotRaconteur.Client import *
import general_robotics_toolbox as rox
from RobotRaconteurCompanion.Util.RobotUtil import RobotUtil
from RobotRaconteurCompanion.Util.GeometryUtil import GeometryUtil
import copy
import numpy as np

d = DeviceManagerClient('rr+tcp://localhost:59902?service=device_manager', autoconnect=False)

d.refresh_devices(1)

d.connect_device('robotics_jog')
d.connect_device('robot')

jog_service = d.get_device_client("robotics_jog",1)

print(jog_service.device_info.device.name)

jog = jog_service.get_jog("robot")

jog.setf_jog_mode()

#for x in range(100):
    #jog.jog_joints3(1,1)
#jog.setf_halt_mode()

robot = d.get_device_client("robot",1)

robot_state,_ = robot.robot_state.PeekInValue()
q_current = robot_state.joint_position
robot_util = RobotUtil(client_obj = robot)
rox_robot = robot_util.robot_info_to_rox_robot(robot.robot_info,0)
geom_util = GeometryUtil(client_obj = jog_service)
T = rox.fwdkin(rox_robot, q_current)
print(f"Current xyz = {T.p}, rpy = {np.rad2deg(rox.R2rpy(T.R))}")
T2 = copy.deepcopy(T)
T2.p[1] += 0.1
T3 = copy.deepcopy(T)
T3.p[1] -= 0.1
pose_des = geom_util.rox_transform_to_pose(T2)
pose_des2 = geom_util.rox_transform_to_pose(T3)

for i in range(10):
    jog.jog_joints_to_pose(pose_des, 50)
    jog.jog_joints_to_pose(pose_des2, 50)
