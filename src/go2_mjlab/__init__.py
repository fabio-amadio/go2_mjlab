"""Unitree Go2 environments for mjlab."""

from importlib.metadata import PackageNotFoundError, version

try:
  __version__ = version("go2-mjlab")
except PackageNotFoundError:  # pragma: no cover - editable/local tree fallback.
  __version__ = "0.1.0"

# Register tasks when the package is imported directly. mjlab also imports
# go2_mjlab.tasks through the "mjlab.tasks" entry point.
from go2_mjlab import tasks as tasks
