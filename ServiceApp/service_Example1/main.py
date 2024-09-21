import sys
sys.path.append('./')
from RTRQ.Extension.Kernel_Default import *

def hello():
    print("example1")

kernel.register_Method(macro.Region_Example1,macro.Node_Example1_handleExample,"default",lambda data: hello())