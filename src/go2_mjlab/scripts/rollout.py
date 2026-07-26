"""Minimal raw rollout example for the Unitree Go2 environment."""

from __future__ import annotations

import time
from typing import Any

import torch
from mjlab.envs import ManagerBasedRlEnv
from mjlab.tasks.registry import load_env_cfg
from mjlab.utils.torch import configure_torch_backends
from mjlab.viewer import NativeMujocoViewer

import go2_mjlab.tasks  # noqa: F401  # Registers Unitree Go2 tasks.

TASK = "Mjlab-Velocity-Flat-Unitree-Go2"
NUM_ENVS = 1
NUM_STEPS = 1000
SEED = 42
DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"
VISUALIZE = True
REALTIME = True


class ViewerEnv:
  """Tiny adapter so the mjlab viewer can inspect the raw env."""

  def __init__(self, env: ManagerBasedRlEnv):
    self.env = env

  @property
  def num_envs(self) -> int:
    return self.env.num_envs

  @property
  def device(self) -> str:
    return self.env.device

  @property
  def cfg(self) -> Any:
    return self.env.cfg

  @property
  def unwrapped(self) -> ManagerBasedRlEnv:
    return self.env


def main() -> None:
  configure_torch_backends()
  torch.manual_seed(SEED)

  env_cfg = load_env_cfg(TASK, play=True)
  env_cfg.scene.num_envs = NUM_ENVS
  env_cfg.seed = SEED

  env = ManagerBasedRlEnv(cfg=env_cfg, device=DEVICE)
  viewer = (
    NativeMujocoViewer(ViewerEnv(env), policy=lambda obs: obs)
    if VISUALIZE
    else None
  )

  try:
    observation, info = env.reset(seed=SEED)
    del observation, info

    action_dim = env.action_manager.total_action_dim
    returns = torch.zeros(NUM_ENVS, device=DEVICE)

    if viewer is not None:
      viewer.setup()
      viewer.sync_env_to_viewer()

    for step in range(NUM_STEPS):
      if viewer is not None and not viewer.is_running():
        break

      step_start = time.perf_counter()

      if viewer is not None:
        viewer.sync_viewer_to_env()

      # Replace this tensor with actions from your own framework.
      action = 2.0 * torch.rand((NUM_ENVS, action_dim), device=DEVICE) - 1.0

      observation, reward, terminated, truncated, info = env.step(action)
      del observation, info

      returns += reward
      done = terminated | truncated

      if torch.any(done):
        print(f"step={step + 1}: done env ids={done.nonzero().flatten().tolist()}")
        # No manual reset is needed: mjlab auto-resets done envs by default.

      if viewer is not None:
        viewer.sync_env_to_viewer()

      if REALTIME:
        elapsed = time.perf_counter() - step_start
        time.sleep(max(0.0, env.step_dt - elapsed))

    print(f"returns={returns.cpu().tolist()}")
  finally:
    if viewer is not None:
      viewer.close()
    env.close()


if __name__ == "__main__":
  main()
