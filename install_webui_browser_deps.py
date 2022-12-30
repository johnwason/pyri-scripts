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
import argparse

pyodide_url = "https://github.com/pyodide/pyodide/releases/download/0.21.3/pyodide-build-0.21.3.tar.bz2"

webui_deps_package_json = Path(__file__).parent.joinpath("webui_deps_package.json")

def dir_remove_all(path1):
    # Delete contents of deps_dir
    for path in Path(path1).glob("**/*"):
        if path.is_file():
            path.unlink()
        elif path.is_dir():
            shutil.rmtree(path)

def main():

    parser = argparse.ArgumentParser(description="Install PyRI WebUI Server dependencies")
    parser.add_argument("--static-data-dir",type=str,default=None,help="Directory to store WebUI static data (Pyodide, wheels, deps)")

    args, _ = parser.parse_known_args()

    if args.static_data_dir is not None:
        static_data_dir = Path(args.static_data_dir)
    else:
        static_data_dir = Path(appdirs.user_data_dir(appname="pyri-webui-server", appauthor="pyri-project", roaming=False))
    deps_dir = static_data_dir.joinpath("deps")
    pyodide_dir = static_data_dir.joinpath("robotraconteur_pyodide")

    dir_remove_all(deps_dir)
    dir_remove_all(pyodide_dir)

    deps_dir.mkdir(exist_ok=True, parents=True)
    pyodide_dir.mkdir(exist_ok=True, parents=True)

    shutil.copy(webui_deps_package_json, deps_dir.joinpath("package.json"))

    subprocess.check_call("npm install",shell=True, cwd=deps_dir)

    # Install golden-layout.min.js due to annoying missing file
    gl_umd_dir = deps_dir / "node_modules" / "golden-layout" / "dist" / "bundle" / "umd"
    gl_umd_dir.mkdir(exist_ok=True, parents=True)
    gl_umd_js = Path(__file__).parent.joinpath("golden-layout.js")
    shutil.copyfile(gl_umd_js, gl_umd_dir / gl_umd_js.name)
    
    r = requests.get(pyodide_url, allow_redirects=True)
    f = io.BytesIO(r.content)

    with tarfile.open(fileobj=f,mode="r:bz2") as tar:
        
        tar.extractall(path=pyodide_dir)
if __name__ == "__main__":
    main()

