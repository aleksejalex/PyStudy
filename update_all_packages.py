"""
Package Updater
updates all packages in current VENV.

HOW TO RUN: execute in command line this: python update_all_packages.py

Created by @aleksejalex, 210801
Modified by
"""

import pkg_resources
from subprocess import call

packages = [dist.project_name for dist in pkg_resources.working_set]
call("pip install --upgrade " + ' '.join(packages), shell=True)