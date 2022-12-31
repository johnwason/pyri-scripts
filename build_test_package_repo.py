from pathlib import Path
import subprocess
import sys
import pkginfo

def main():
    workdir = Path(__file__).parent / "test_package_repo"
    workdir.mkdir(parents=True, exist_ok=True)

    wheeldir = workdir / "wheels"
    wheeldir.mkdir(parents=True, exist_ok=True)

    workspace_dir = workdir.parent.parent

    for p in workspace_dir.iterdir():
        print(p)
        if (p / "pyproject.toml").is_file():
            subprocess.check_call([sys.executable, "-mpip", "wheel", ".", "--no-deps", f"--wheel-dir={wheeldir}"],cwd=p)
            pass

    packages = dict()
    for w in wheeldir.iterdir():
        if w.suffix == ".whl":
            pkg_info = pkginfo.Wheel(w)
            packages[pkg_info.name] = w.name

    repo_dir = workdir / "packages"
    repo_dir.mkdir(parents=True, exist_ok=True)

    index_fname = repo_dir / "index.html"
    with open(index_fname, "w") as f:
        print("<!DOCTYPE html><html><body>", file=f)
        for n,p in packages.items():
            print(f"<a href=\"{n}/\">{n}</a>", file=f)
        print("</body></html>", file=f)

    for n,p in packages.items():
        p_dir = repo_dir / n
        p_dir.mkdir(exist_ok = True)
        p_fname = p_dir / "index.html"
        with open(p_fname, "w") as f:
            print("<!DOCTYPE html><html><body>", file=f)
            print(f"<a href=\"/wheels/{p}\">{p}</a>", file=f)
            print("</body></html>", file=f)

    print(packages)

if __name__ == "__main__":
    main()

