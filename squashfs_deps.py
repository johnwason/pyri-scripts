import tempfile
import subprocess
import os
from pathlib import Path
import shutil

cd = Path(os.getcwd())
webui_deps_package_json = Path(__file__).parent.joinpath("webui_deps_package.json")

def squashfs_browser_deps():
    with tempfile.TemporaryDirectory() as d1:
        d = Path(d1)
        sqfs_out = cd / "pyri_webui_deps.sqfs"
        shutil.copy(webui_deps_package_json, d.joinpath("package.json"))
        subprocess.check_call("npm install", shell=True, cwd=d)
        subprocess.check_call(f"mksquashfs * {sqfs_out}", shell=True, cwd=(d / "node_modules"))

squashfs_browser_deps()