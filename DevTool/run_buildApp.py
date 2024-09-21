import sys
sys.path.append("./")

import subprocess
import shutil
import os

shutil.copy("DevTool/store/main.spec","main.spec")
subprocess.run("pyinstaller main.spec")
shutil.rmtree("build")
shutil.copy("dist/main.exe","DevTool/output/main.exe")
shutil.rmtree("dist")
os.remove("main.spec")