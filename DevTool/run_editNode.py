import sys
sys.path.append("./")

from RTRQ.Extension.Kernel_Default import *
import tkinter as tk
from tkinter import ttk
from RTRQ.kernel import *

app = tk.Tk()


value = kernel.getlist_Region()
cb_Region = ttk.Combobox(app, values=value)
cb_Node = ttk.Combobox(app, values=[])
en_setNode = tk.Entry(app,justify='center')
bt_setNode = tk.Button(app,text="Set")
en_getNode = tk.Entry(app,justify='center')
bt_getNode = tk.Button(app,text="Get")
en_activeNode = tk.Entry(app,justify='center')
bt_activeNode = tk.Button(app,text="Active")


cb_Region.pack(padx=10,pady=2)
cb_Node.pack(padx=10,pady=2)

en_setNode.pack(padx=10,pady=2)
bt_setNode.pack(padx=10,pady=2)

en_getNode.pack(padx=10,pady=2)
bt_getNode.pack(padx=10,pady=2)

en_activeNode.pack(padx=10,pady=2)
bt_activeNode.pack(padx=10,pady=2)

def on_combobox_select(event):
    list_node = cb_Region.get() 
    cb_Node.configure(values=kernel.getlist_Node(list_node))

def onSet():
    Region  = cb_Region.get()
    Node    = cb_Node.get()
    data    = en_setNode.get()  # Get text from the Entry widget
    kernel.set_Node(Region,Node,data)

def onGet():
    Region  = cb_Region.get()
    Node    = cb_Node.get()
    en_getNode.delete(0,'end')
    en_getNode.insert(0,kernel.get_Node(Region,Node))

def onActive():
    Region  = cb_Region.get()
    Node    = cb_Node.get()
    data    = en_activeNode.get()  # Get text from the Entry widget
    kernel.active_Node(Region,Node,data)

cb_Region.bind("<<ComboboxSelected>>", on_combobox_select)
bt_setNode.configure(command=onSet)
bt_getNode.configure(command=onGet)
bt_activeNode.configure(command=onActive)

app.mainloop()
