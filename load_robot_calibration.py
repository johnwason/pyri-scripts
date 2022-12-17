from RobotRaconteur.Client import *
import numpy as np
import general_robotics_toolbox as rox
from RobotRaconteurCompanion.Util.GeometryUtil import GeometryUtil

var_storage = RRN.ConnectService("rr+tcp://localhost:59901?service=variable_storage")

geom_util = GeometryUtil(client_obj = var_storage)

robot_pose1 = geom_util.rox_transform_to_named_pose(rox.Transform(np.eye(3),[0.5,0.0,0.0],"world","robot"))
robot_pose_cov = np.eye(6) * 1e-5

robot_pose = RRN.NewStructure("com.robotraconteur.geometry.NamedPoseWithCovariance", var_storage)
robot_pose.pose = robot_pose1
robot_pose.covariance = robot_pose_cov


var_consts = RRN.GetConstants('tech.pyri.variable_storage', var_storage)
variable_persistence = var_consts["VariablePersistence"]
variable_protection_level = var_consts["VariableProtectionLevel"]

robot_local_device_name = "robot_mp"
output_global_name = f"{robot_local_device_name}_origin_calibration"

var_storage.add_variable2("globals",output_global_name,"com.robotraconteur.geometry.NamedPoseWithCovariance", \
    RR.VarValue(robot_pose,"com.robotraconteur.geometry.NamedPoseWithCovariance"), ["robot_origin_pose_calibration"], 
    {"device": robot_local_device_name}, variable_persistence["const"], None, variable_protection_level["read_write"], \
    [], f"Robot \"{robot_local_device_name}\" origin pose calibration", False)
