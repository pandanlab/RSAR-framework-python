import sys
sys.path.append("./")

import subprocess
import time
import os

from RTRQ.Extension.Kernel_Default import *
import RTRQ.Extension.DefineNode as macro

# Thêm đường dẫn hiện tại vào sys.path
sys.path.append("./")

class obj_File:
    def __init__(self, id_obj):
        # Khởi tạo kernel driver
        self.id = id_obj
        None 

    def start(self):
        self.nameDriver = "myDriver.ko"
        self.link_fileDriver = os.path.join(os.path.dirname(__file__),self.nameDriver)
        self.runCMD(f"sudo insmod {self.link_fileDriver}")
        self.runCMD("sudo chmod 666 /dev/dev_kimsonfast")

    def runCMD(self,data):
        result = subprocess.run(data, shell=True, check=True)
        #print(result)

    def setLed(self,data):
        self.runCMD(f"echo {data} > /dev/dev_kimsonfast")

    def getButton(self,data):
        self.runCMD(f"head -n 1 /dev/dev_kimsonfast")

    def close(self):
        self.runCMD(f"sudo rmmod {str(self.nameDriver).split('.')[0]}")
        pass

# Khởi tạo đối tượng
hello = obj_File(1)
kernel.register_Method(macro.Region_file,macro.Node_file_handleStart,hello.id,lambda data: hello.start())
kernel.register_Method(macro.Region_file,macro.Node_file_handleStop,hello.id,lambda data: hello.close())
kernel.register_Method(macro.Region_file,macro.Node_file_handlewriteData,hello.id,hello.setLed)
kernel.register_Method(macro.Region_file,macro.Node_file_handlereadData,hello.id,hello.getButton)
