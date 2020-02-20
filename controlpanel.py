import tkinter as tk


class ControlPanel:
    def __init__(self, master, mrow, mcol):
        self.master = master

        # Initialize Wrapper frame
        self.frame = tk.Frame(self.master)
        self.frame.grid(row=mrow, column=mcol, sticky='NWSE')

