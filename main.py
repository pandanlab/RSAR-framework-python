from RTRQ.kernel import *
kernel_generate()

import sys

def main():
    while 1:
        data = input("user : ")
        if("example1" in data):
            kernel.active_Node(Region_Example1,Node_Example1_handleExample)
        elif("example2" in data):
            kernel.active_Node(Region_Example2,Node_Example2_handleExample,data)

if __name__ == "__main__":
    main()