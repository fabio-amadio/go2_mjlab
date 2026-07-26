from mjlab.entity import Entity
from mjlab.envs import ManagerBasedRlEnvCfg
from mjlab.tasks.registry import list_tasks, load_env_cfg, load_rl_cfg
from mjlab.tasks.velocity.rl import VelocityOnPolicyRunner

import go2_mjlab  # noqa: F401
from go2_mjlab.robots import get_go2_robot_cfg


def test_go2_robot_compiles() -> None:
  model = Entity(get_go2_robot_cfg()).compile()
  assert model.nq > 0


def test_go2_tasks_registered() -> None:
  task_ids = list_tasks()
  assert "Mjlab-Velocity-Flat-Unitree-Go2" in task_ids
  assert "Mjlab-Velocity-Rough-Unitree-Go2" in task_ids


def test_go2_task_configs_load() -> None:
  for task_id in [
    "Mjlab-Velocity-Flat-Unitree-Go2",
    "Mjlab-Velocity-Rough-Unitree-Go2",
  ]:
    cfg = load_env_cfg(task_id)
    play_cfg = load_env_cfg(task_id, play=True)
    rl_cfg = load_rl_cfg(task_id)

    assert isinstance(cfg, ManagerBasedRlEnvCfg)
    assert isinstance(play_cfg, ManagerBasedRlEnvCfg)
    assert rl_cfg.experiment_name == "go2_velocity"
    assert play_cfg.episode_length_s >= 1e9


def test_go2_runner_registered() -> None:
  from mjlab.tasks.registry import load_runner_cls

  assert load_runner_cls("Mjlab-Velocity-Flat-Unitree-Go2") is VelocityOnPolicyRunner
