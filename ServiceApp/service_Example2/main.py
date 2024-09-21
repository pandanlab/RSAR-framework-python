import sys
sys.path.append('./')
from RTRQ.Extension.Kernel_Default import *


def hello(data):
    print(f"example2 : {data}")

kernel.register_Method(macro.Region_Example2,macro.Node_Example2_handleExample,"default",hello)