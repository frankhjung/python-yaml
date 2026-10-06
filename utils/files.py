"""Helper functions to read YAML files from a path or directory."""

import glob
import os.path


def list_yamls(target: str) -> list[str]:
    """Return YAML files matching a file path or directory."""
    if os.path.isfile(target):
        return [target]
    if os.path.isdir(target):
        return sorted(glob.glob(os.path.join(target, "*.yaml")))
    return sorted(glob.glob(target))
