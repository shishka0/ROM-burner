import tkinter as tk
import tkinter.filedialog as filedialog
import tkinter.ttk as ttk
import serialinterface as si


class ControlPanel:
    def __init__(self, master, mrow, mcol, **callbacks):
        self.master = master
        self.callbacks = callbacks

        # Initialize Wrapper frame
        self.frame = tk.Frame(self.master)
        self.frame.grid(row=mrow, column=mcol, sticky='NWSE')
        for i in range(4):
            self.frame.rowconfigure(i, weight=1)
            self.frame.columnconfigure(i, weight=1)

        # Initialize Labels
        self.labels = {}

        plabel = tk.Label(self.frame)
        plabel.config(text='Port:', font=('Consolas', 12))
        plabel.grid(row=0, column=0, sticky='NES')
        self.labels['port'] = plabel

        flabel = tk.Label(self.frame)
        flabel.config(text='File:', font=('Consolas', 12))
        flabel.grid(row=1, column=0, sticky='NES')
        self.labels['file'] = flabel

        fnlabel = tk.Label(self.frame)
        fnlabel.config(text='choose file', font=('Consolas', 10))
        fnlabel.grid(row=1, column=1, sticky='NES')
        self.labels['filename'] = fnlabel

        # Initialize combobox
        self.comboboxes = {}
        fcb = ttk.Combobox(self.frame)
        fcb.config(state='readonly')
        fcb.grid(row=0, column=1, sticky='WE')
        # fcb.bind('<<ComboboxSelected>>', self.port_selected)
        self.comboboxes['port'] = fcb
        self.refresh()

        # Initialize buttons
        self.buttons = {}

        brefresh = tk.Button(self.frame)
        brefresh.grid(row=0, column=2, sticky='WE')
        brefresh.config(text='Refresh', command=self._b_refresh)
        self.buttons['refresh'] = brefresh

        bopen = tk.Button(self.frame)
        bopen.grid(row=1, column=2, sticky='WE')
        bopen.config(text='Open', command=self._b_open)
        self.buttons['open'] = bopen

        bburn = tk.Button(self.frame)
        bburn.grid(row=2, column=1, sticky='WE')
        bburn.config(text='Burn', command=self._b_burn)
        self.buttons['burn'] = bopen

    def _b_burn(self):
        pass

    def _b_open(self):
        fname = filedialog.askopenfilename(initialdir='~',
                                          title='Select file',
                                          filetypes=(('ROM Files', '*.rom'),
                                                     ('All files', '*.*'))
                                          )
        if 'bOpen' in self.callbacks:
            self.callbacks['bOpen'](fname)

    def _b_refresh(self):
        self.refresh()
        if 'bRefresh' in self.callbacks:
            self.callbacks['bRefresh']()

    def refresh(self):
        self.comboboxes['port']['values'] = si.list()