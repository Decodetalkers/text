#!/usr/bin/env python
import sys
import subprocess
def _sync_submodule():
    print(" --- Initializing submodules")
    try:
        subprocess.check_call(["git", "submodule", "init"])
        subprocess.check_call(["git", "submodule", "update", "--recursive", "--remote"])
    except Exception:
        print(" --- Submodule initialization failed")
        print("Please run:\n\tgit submodule update --init --recursive")
        sys.exit(1)
    print(" --- Initialized submodule")

_sync_submodule()
