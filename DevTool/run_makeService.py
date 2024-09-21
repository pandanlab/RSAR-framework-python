import sys
sys.path.append("./")

import tkinter as tk
from tkinter import ttk

import os

app = tk.Tk()
value = os.listdir("ServiceApp")
et1 = tk.Entry(app,justify='center')
btn1 = tk.Button(app,text="Set")

et1.pack(padx=5,pady=10)
btn1.pack(padx=5,pady=10)

def on_button_click():
    name = f"service_{et1.get()}" 

    os.mkdir(f"ServiceApp/{name}")

    with open(f"ServiceApp/{name}/main.py","w") as file:
        file.write("import sys\n")
        file.write("sys.path.append('./')\n")
        file.write("from RTRQ.Extension.Kernel_Default import *\n\n")

    with open(f"ServiceApp/{name}/listNode.txt","w") as file:
        file.write(f"Node_dataExample\n")
        file.write(f"Node_handleExample\n")


btn1.configure(command=on_button_click)

app.mainloop()
