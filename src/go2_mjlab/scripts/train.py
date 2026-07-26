"""go2_mjlab training CLI wrapper."""

from mjlab.scripts.train import main as mjlab_train_main

import go2_mjlab  # noqa: F401


def main() -> None:
  mjlab_train_main()
