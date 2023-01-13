import os
from pathlib import Path
import shutil

from maadeps.runner import task
from . import vcpkg
from .common import basedir

@task
def sdk_ready():
    return True

@task
def install_runtime():
    if not sdk_ready.completed:
        sdk_ready()
        raise Exception("sdk not prepared")

    target_dir = os.path.join(basedir, "runtime", vcpkg.triplet)

    if "windows" in vcpkg.triplet:
        from .runtime_windows import install_runtime as impl
    elif "linux" in vcpkg.triplet:
        from .runtime_linux import install_runtime as impl
    elif "osx" in vcpkg.triplet:
        raise NotImplementedError()

    impl(target_dir)

def install_file(src, dst):
    if Path(dst).is_dir():
        dst = Path(dst) / Path(src).name
    print("installing", src, "->", dst)
    Path(dst).parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(src, dst)

def match_patterns(path: Path, patterns):
    for pat in patterns:
        if path.match(pat):
            return True
    return False
