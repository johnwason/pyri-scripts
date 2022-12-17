import tempfile
import subprocess
import os
from pathlib import Path
import shutil
import requests

cd = Path(os.getcwd())
pyodide_archive_url = "https://github.com/pyodide/pyodide/releases/download/0.21.0/pyodide-build-0.21.0.tar.bz2"

def squashfs_pyodide():
    with tempfile.TemporaryDirectory() as d1:
        d = Path(d1)
        sqfs_out = cd / "pyri_webui_pyodide.sqfs"
        r = requests.get(pyodide_archive_url)
        with open(d/"pyodide.tar.bz2","wb") as f:
            f.write(r.content)

        subprocess.check_call(f"tar xf pyodide.tar.bz2", shell=True, cwd=d)
        
        subprocess.check_call(f"mksquashfs * {sqfs_out}", shell=True, cwd=d/"pyodide")

squashfs_pyodide()