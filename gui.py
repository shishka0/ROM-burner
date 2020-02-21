import tkinter as tk

import console
import controlpanel as cp


class ROMBurnerGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('ROM Burner')
        self.window.geometry('1000x300')
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)

        self.main_frame = tk.Frame(self.window)
        self.main_frame.grid(row=0, column=0)
        self.main_frame.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(0, weight=1)

        self.console = console.Console(self.main_frame, 0, 1)
        self.controlpanel = cp.ControlPanel(self.main_frame, 0, 0,
                                            bOpen=self._b_open,
                                            bRefresh=self._b_refresh)

    def _b_open(self, file):
        self.console.print("Opened file: {}".format(file))

    def _b_refresh(self):
        self.console.print("Refreshed serial ports")

    def begin(self):
        self.window.mainloop()