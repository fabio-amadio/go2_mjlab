"""go2_mjlab environment listing CLI wrapper."""

from mjlab.scripts.list_envs import main as mjlab_list_envs_main

import go2_mjlab  # noqa: F401


def main() -> None:
  mjlab_list_envs_main()
