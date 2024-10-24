from legged_gym.envs.base.legged_robot_config import LeggedRobotCfg, LeggedRobotCfgPPO


class X30RoughCfg(LeggedRobotCfg):
    class init_state(LeggedRobotCfg.init_state):
        pos = [0.0, 0.0, 0.6]  # x,y,z [m]
        default_joint_angles = {  # = target angles [rad] when action = 0.0
            'FL_HipX_joint': 0.0,  # [rad]
            'HL_HipX_joint': 0.0,  # [rad]
            'FR_HipX_joint': -0.0,  # [rad]
            'HR_HipX_joint': -0.0,  # [rad]

            'FL_HipY_joint': -1.,  # [rad]
            'HL_HipY_joint': -1.,  # [rad]
            'FR_HipY_joint': -1.,  # [rad]
            'HR_HipY_joint': -1.,  # [rad]

            'FL_Knee_joint': 1.8,  # [rad]
            'HL_Knee_joint': 1.8,  # [rad]
            'FR_Knee_joint': 1.8,  # [rad]
            'HR_Knee_joint': 1.8,  # [rad]
        }

    class control(LeggedRobotCfg.control):
        # PD Drive parameters:
        control_type = 'P'
        stiffness = {'joint': 40.0}  # 27 20 17 # [N*m/rad]
        damping = {'joint': 2.0}  # 1.0 0.7 [N*m*s/rad]
        # action scale: target angle = actionScale * action + defaultAngle
        action_scale = 0.5
        # decimation: Number of control action updates @ sim DT per policy DT
        decimation = 4

    class asset(LeggedRobotCfg.asset):
        file = '{LEGGED_GYM_ROOT_DIR}/resources/deepRobotics/x30/urdf/robot.urdf'
        name = "x30"
        foot_name = "FOOT"
        penalize_contacts_on = ["THIGH", "SHANK"]
        terminate_after_contacts_on = ["TORSO"]
        self_collisions = 1  # 1 to disable, 0 to enable...bitwise filter

    class rewards(LeggedRobotCfg.rewards):
        soft_dof_pos_limit = 0.9
        base_height_target = 0.25

        class scales(LeggedRobotCfg.rewards.scales):
            torques = -0.0002
            dof_pos_limits = -10.0


class X30RoughCfgPPO(LeggedRobotCfgPPO):
    class algorithm(LeggedRobotCfgPPO.algorithm):
        entropy_coef = 0.01

    class runner(LeggedRobotCfgPPO.runner):
        run_name = ''
        experiment_name = 'rough_x30'
