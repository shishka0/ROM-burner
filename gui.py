import tkinter as tk

import console
import controlpanel as cp

import files
import serialinterface as si

class ROMBurnerGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('ROM Burner')
        self.window.geometry('1000x300')
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)

        self.main_frame = tk.Frame(self.window)
        self.main_frame.grid(row=0, column=0, sticky='NWSE')
        self.main_frame.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(0, weight=1)

        self.console = console.Console(self.main_frame, 0, 1)
        self.controlpanel = cp.ControlPanel(self.main_frame, 0, 0,
                                            print=self.print,
                                            bBurn=self._b_burn)

        self.console.print("---------------- ROM Burner ----------------")

    def print(self, msg):
        self.console.print(msg)

    def _b_open(self, file):
        self.console.print("Selected file: {}".format(file))

    def _b_refresh(self):
        self.console.print("Refreshed serial ports")

    def _b_burn(self, fname, pname):
        try:
            f = open(fname, 'r')
        except OSError:
            self.print("Could not open file '{}'".format(fname))
            return
        data = files.parse(f)
        status = si.send(data, pname)
        if status is False:
            self.print("Could not send data.")
        self.c



    def begin(self):
        self.window.mainloop()