import tkinter as tk

import console
import controlpanel as cp

import files
import serialinterface as si


class ROMBurnerGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('ROM Burner')
        self.window.geometry('1200x300')
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)

        self.main_frame = tk.Frame(self.window)
        self.main_frame.grid(row=0, column=0, sticky='NWSE')
        self.main_frame.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=0)

        self.console = console.Console(self.main_frame, 0, 1)
        self.controlpanel = cp.ControlPanel(self.main_frame, 0, 0,
                                            print=self.print,
                                            bBurn=self._b_burn,
                                            cbPortSelected=self._cb_port_selected
                                            )

        self.console.print("---------------- ROM Burner ----------------")

    def print(self, msg):
        self.console.print(msg)

    def _cb_port_selected(self, port):
        self.print("Selected port {}".format(port))

    def _b_open(self, file):
        self.console.print("Selected file: {}".format(file))

    def _b_refresh(self):
        self.console.print("Refreshed serial ports")

    def _b_burn(self, fname, pname):
        if not pname:
            self.print('Port not selected')
            return
        try:
            f = open(fname, 'r')
        except OSError:
            self.print("Could not open file '{}'".format(fname))
            return
        except TypeError:
            self.print('File is not valid or was not selected')
            return
        data = files.parse(f)
        status = si.send(data, pname)
        if status is False:
            self.print("Could not send data.")
        f.close()
        self.print("Done!")

    def begin(self):
        self.window.mainloop()
