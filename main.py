from RTRQ.kernel import *
kernel_generate()

import sys

def main():
    arguments = sys.argv
    if(len(arguments)>1):
        if(arguments[1]=="init"):
            None
        elif(arguments[1]=="boot"):
            kernel.active_Node(Region_CLI,Node_CLI_handleMain)
        elif(arguments[1]=="build"):
            kernel.active_Node(Region_Build,Node_Build_handleBuild)
    else:
        print("Vui lòng thêm thông số (init;boot;build) sau pdm")

if __name__ == "__main__":
    main()