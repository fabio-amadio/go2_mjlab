"""go2_mjlab play CLI wrapper."""

from mjlab.scripts.play import main as mjlab_play_main

import go2_mjlab  # noqa: F401


def main() -> None:
  mjlab_play_main()
