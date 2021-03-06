# Configuration file for jupyter lab

import os
import subprocess

from traitlets.config import get_config

c = get_config()


def post_save_hook(model, os_path, contents_manager):
    cwd, name = os.path.split(os_path)

    if model["type"] == "notebook" and ".py.ipynb" in os_path:
        output = name.replace(".ipynb", "").lower()

        subprocess.check_call(
            [
                "jupyter",
                "nbconvert",
                "--to",
                "python",
                "--output",
                output,
                name,
            ],
            cwd=cwd,
        )
        subprocess.check_call(["chmod", "u+x", output], cwd=cwd)


c.FileContentsManager.post_save_hook = post_save_hook
