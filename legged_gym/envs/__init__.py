from legged_gym import LEGGED_GYM_ROOT_DIR, LEGGED_GYM_ENVS_DIR

from legged_gym.envs.a1.a1_config import A1RoughCfg, A1RoughCfgPPO
from legged_gym.envs.lite3.lite3_config import Lite3RoughCfg, Lite3RoughCfgPPO
from legged_gym.envs.x30.x30_config import X30RoughCfg, X30RoughCfgPPO

from legged_gym.envs.go2.go2_config import GO2RoughCfg, GO2RoughCfgPPO
from legged_gym.envs.h1.h1_config import H1RoughCfg, H1RoughCfgPPO
from legged_gym.envs.h1_2.h1_2_config import H1_2RoughCfg, H1_2RoughCfgPPO
from legged_gym.envs.g1.g1_config import G1RoughCfg, G1RoughCfgPPO
from .base.legged_robot import LeggedRobot

from legged_gym.utils.task_registry import task_registry

task_registry.register( "go2", LeggedRobot, GO2RoughCfg(), GO2RoughCfgPPO())
task_registry.register( "h1", LeggedRobot, H1RoughCfg(), H1RoughCfgPPO())
task_registry.register( "h1_2", LeggedRobot, H1_2RoughCfg(), H1_2RoughCfgPPO())
task_registry.register( "g1", LeggedRobot, G1RoughCfg(), G1RoughCfgPPO())

task_registry.register( "a1", LeggedRobot, A1RoughCfg(), A1RoughCfgPPO())
task_registry.register( "lite3", LeggedRobot, Lite3RoughCfg(), Lite3RoughCfgPPO())
task_registry.register( "x30", LeggedRobot, X30RoughCfg(), X30RoughCfgPPO())
