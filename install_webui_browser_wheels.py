# Utility script to install WebUI Python wheels
# These wheels are automatically downloaded by the browser and installed in the Pyodide virtual filesystem

# Run on command line to install required packages:

# pip install requests packaging wheel

# Package names to build from the PyRI development tree
wheels_names = ['pyri-webui-browser', 'pyri-common', 'pyri-robotics-browser', 'pyri-vision-browser', 'pyri-robotics-motion-program-browser']
# Package names to install from PyPi
pip_wheels_names = [] #['importlib_resources','RobotRaconteurCompanion', "general_robotics_toolbox", "zipp"]

import subprocess
import re
import glob
import shutil
import appdirs
from pathlib import Path
import requests
from packaging.version import parse
import sys
import argparse

def install_wheel(wheel_name,wheels_dir):
    print(f"Installing {wheel_name}")
    base_path = Path("..").absolute()
    with open(base_path.joinpath(wheel_name).joinpath("setup.py"),"r") as f:
        setup_py_text = f.read()
        #Make sure in the correct directory
        assert f"name='{wheel_name}'" in setup_py_text

        version_match = re.search(r"version\s*=\s*'(\d+\.\d+\.\d+)'",setup_py_text)
        assert version_match is not None
        version = version_match.group(1)
    print(version)

    subprocess.check_call(f"{sys.executable} setup.py bdist_wheel",shell=True,cwd=base_path.joinpath(wheel_name))

    wheel_name2 = wheel_name.replace("-","_")

    wheel_fname = Path(glob.glob(f"../{wheel_name}/dist/{wheel_name2}-{version}*.whl")[0], )
    wheel_target_fname = wheels_dir.joinpath(wheel_fname.name)
    shutil.copyfile(wheel_fname,wheel_target_fname)
    print(f"Copied wheel version {version} to {str(wheels_dir)}")

def install_pip_wheel(wheel_name,wheels_dir):
    package_json = requests.get(f'https://pypi.python.org/pypi/{wheel_name}/json').json()
    releases = package_json["releases"]
    version = parse('0')
    for r in releases:
        ver = parse(r)
        if ver > version:
            version = ver

    release = package_json["releases"][r][0]
    fname = release["filename"]
    assert fname.endswith(".whl")
    url = release["url"]

    wheel_target_fname = wheels_dir.joinpath(fname)
    
    existing_wheels = list(wheels_dir.glob(f"{wheel_name}*.whl"))
    assert len(existing_wheels) <=1, "Multiple wheels of same package detected!"
    if len(existing_wheels) > 0:
        w = existing_wheels[0]
        w_ver_res = re.match(f"{wheel_name}\\-([^\\-]+)-",w.name)
        w_ver = parse(w_ver_res.group(1))
        print(f"Existing package {wheel_name} is version {w_ver}")
        if (w_ver >= version):
            print(f"Existing package {wheel_name} is version {w_ver} is greater or equal to pypi, not replacing")
            return
        else:
            print(f"Existing package {wheel_name} is version {w_ver} is older than pypi, replacing with version {version} from url {url}")
            w.unlink()

    print(f"Downloading and installing {wheel_name} package {version} from url {url}")

    r = requests.get(url, allow_redirects=True)
    open(wheel_target_fname, 'wb').write(r.content)




    

def main():

    parser = argparse.ArgumentParser(description="Install PyRI WebUI Server wheels")
    parser.add_argument("--static-data-dir",type=str,default=None,help="Directory to store WebUI static data (Pyodide, wheels, deps)")

    args, _ = parser.parse_known_args()

    if args.static_data_dir is not None:
        wheels_dir = Path(args.static_data_dir).joinpath("wheels")
    else:
        wheels_dir = Path(appdirs.user_data_dir(appname="pyri-webui-server", appauthor="pyri-project", roaming=False)).joinpath("wheels")

    wheels_dir.mkdir(exist_ok=True, parents=True)

    for w in wheels_names:
        install_wheel(w,wheels_dir)

    # for w in pip_wheels_names:
    #     install_pip_wheel(w,wheels_dir)

if __name__ == "__main__":
    main()