#   Graphics
#   Written by Owen Davidson for personal use
#   This File handles GUI implementation for the
#   Babelic Transliterator encrypted message
#   generator under the MIT license utilizing
#   TKinter
import sys
sys.path.insert(0, './Library-Of-Pybel')

from tkinter import *
from tkinter import filedialog
import time
import os
import re
import library_of_babel

class App:

    #   Explicit class constructor
    #   Handles window elements that appear on every screen of the application,
    #       so they will not have to be redrawn with every change of UI.

    def __init__(self, master):
        master.wm_title("Babelic Transliterator")
        self.frame = Frame(master, borderwidth=10, width=800, height=600)
        self.frame.grid()
        self.searcher = Button(
            self.frame, text="Search", command=self.sayHi
        )
        self.importer = Button(
            self.frame, text="Import", command=self.displayAddr
        )
        self.translator = Button(
            self.frame, text="Translate", command=None
        )
        self.exporter = Button(
            self.frame, text="Export", command=None
        )
        self.tb = Text(self.frame)
        self.tb.grid(rowspan = 4, row=1, column=0)
        self.searcher.grid(row=1, column=1)
        self.importer.grid(row=2, column=1)
        self.translator.grid(row=3, column=1)
        self.exporter.grid(row=4, column=1)

        self.current = None

    #   Handles startup, polling, and cleanup of the whole application

    def run(self, root):
        #root.maxsize(800,600)
        #root.minsize(800,600)
        #root.resizable(width=False, height=False)
        root.mainloop()
        root.destroy()

    def getAddress(self):
        filename = filedialog.askopenfilename(initialdir = ".")
        if os.path.isfile(filename):
            with open(filename, 'r') as f:
                lines = f.readlines()
                return(lines[4][10:])
    def displayAddr(self):
        address = self.getAddress()
        self.tb.insert(INSERT, address)
        self.tb.grid(rowspan = 4, row=1, column=0)

    def sayHi(self):
        print("HI!")

root = Tk()

app = App(root)

app.run(root)
