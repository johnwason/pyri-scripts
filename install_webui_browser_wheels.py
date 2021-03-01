import subprocess
import re
import glob
import shutil
import appdirs
from pathlib import Path

wheels_names = ['pyri-webui-browser', 'pyri-common']

def install_wheel(wheel_name):
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

    subprocess.check_call("python setup.py bdist_wheel",shell=True,cwd=base_path.joinpath(wheel_name))

    wheel_name2 = wheel_name.replace("-","_")

    wheel_fname = Path(glob.glob(f"../{wheel_name}/dist/{wheel_name2}-{version}*.whl")[0], )
    wheels_dir = Path(appdirs.user_data_dir(appname="pyri-webui-server", appauthor="pyri-project", roaming=False)).joinpath("wheels").joinpath(wheel_fname.name)
    shutil.copyfile(wheel_fname,wheels_dir)
    print(f"Copied wheel version {version} to {str(wheels_dir)}")

def main():
    for w in wheels_names:
        install_wheel(w)

if __name__ == "__main__":
    main()