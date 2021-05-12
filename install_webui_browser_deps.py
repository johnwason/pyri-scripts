# Utility script to install WebUI Python wheels
# These wheels are automatically downloaded by the browser and installed in the Pyodide virtual filesystem

# Run on command line to install required packages:

# pip install requests packaging wheel

# Package names to build from the PyRI development tree
wheels_names = ['pyri-webui-browser', 'pyri-common', 'pyri-vision-browser']
# Package names to install from PyPi
pip_wheels_names = ['importlib_resources','RobotRaconteurCompanion', "general_robotics_toolbox"]

import subprocess
import re
import glob
import shutil
import appdirs
from pathlib import Path
import requests
from packaging.version import parse
import sys
import tarfile
import io

pyodide_url = "https://github.com/robotraconteur/robotraconteur_pyodide/archive/refs/heads/gh-pages.tar.gz"

webui_resource_dir = Path(appdirs.user_data_dir(appname="pyri-webui-server", appauthor="pyri-project", roaming=False))
deps_dir = webui_resource_dir.joinpath("deps")
pyodide_dir = webui_resource_dir.joinpath("robotraconteur_pyodide")

webui_deps_package_json = Path(__file__).parent.joinpath("webui_deps_package.json")

def dir_remove_all(path1):
    # Delete contents of deps_dir
    for path in Path(path1).glob("**/*"):
        if path.is_file():
            path.unlink()
        elif path.is_dir():
            shutil.rmtree(path)

def main():
    dir_remove_all(deps_dir)
    dir_remove_all(pyodide_dir)

    deps_dir.mkdir(exist_ok=True, parents=True)
    pyodide_dir.mkdir(exist_ok=True, parents=True)

    shutil.copy(webui_deps_package_json, deps_dir.joinpath("package.json"))

    subprocess.check_call("npm install",shell=True, cwd=deps_dir)
    
    r = requests.get(pyodide_url, allow_redirects=True)
    f = io.BytesIO(r.content)

    with tarfile.open(fileobj=f,mode="r:gz") as tar:
        subdir_and_files = [
            tarinfo for tarinfo in tar.getmembers()
            if tarinfo.name.startswith("robotraconteur_pyodide-gh-pages/")
        ]
        tar.extractall(path=pyodide_dir, members=subdir_and_files)
if __name__ == "__main__":
    main()

