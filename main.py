from RTRQ.kernel import *

def main():
    while 1:
        data = input("user : ")
        if("example1" in data):
            kernel.active_Node(macro.Region_Example1,macro.Node_Example1_handleExample,None)
        if("example2" in data):
            kernel.active_Node(macro.Region_Example2,macro.Node_Example2_handleExample,123)

if __name__ == "__main__":
    main()