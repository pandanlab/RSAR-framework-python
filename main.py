import RTRQ.Extension.DefineNode as Macro
from RTRQ.kernel import *

while 1:
    data = input("user : ")
    if("write" in data):
        kernel.active_Node(Macro.Region_file,Macro.Node_file_handlewriteData,data.split()[1])
    elif("read" in data):
        kernel.active_Node(Macro.Region_file,Macro.Node_file_handlereadData,data)
    elif("break" in data):
        break
    else:
        print(data)
