from mjlab.tasks.registry import list_tasks, register_mjlab_task
from mjlab.tasks.velocity.rl import VelocityOnPolicyRunner

from .env_cfgs import (
  unitree_go2_flat_env_cfg,
  unitree_go2_rough_env_cfg,
)
from .rl_cfg import unitree_go2_ppo_runner_cfg


def _register_if_missing(task_id: str, *, rough: bool) -> None:
  if task_id in list_tasks():
    return
  env_cfg_fn = unitree_go2_rough_env_cfg if rough else unitree_go2_flat_env_cfg
  register_mjlab_task(
    task_id=task_id,
    env_cfg=env_cfg_fn(),
    play_env_cfg=env_cfg_fn(play=True),
    rl_cfg=unitree_go2_ppo_runner_cfg(),
    runner_cls=VelocityOnPolicyRunner,
  )


_register_if_missing("Mjlab-Velocity-Rough-Unitree-Go2", rough=True)
_register_if_missing("Mjlab-Velocity-Flat-Unitree-Go2", rough=False)
