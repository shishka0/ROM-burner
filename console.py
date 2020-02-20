import tkinter as tk


class Console:
    COLOR_BG    = 'gray35'
    COLOR_TXT   = 'ghost white'

    MAX_TXT = 80*10

    def __init__(self, master, mrow, mcol):
        self.master = master

        # Initialize wrapper frame
        self.frame = tk.Frame(self.master)
        self.frame.grid(row=mrow, column=mcol, sticky='NWSE')
        self.frame.grid(bg=Console.COLOR_BG)

        # Initialize text
        self.text = ''
        self.panel = tk.Label(self.frame)
        self.panel.config(text='Welcome to ROM Burner!',
                          font=('Consolas', 12),
                          bg=Console.COLOR_BG,
                          fg=Console.COLOR_TXT,
                          relief='sunken')
        self.panel.grid(row=0, column=0, sticky='NWSE')

    def _strip_text(self):
        """Strips message to less than MAX_TXT preserving the lines"""
        if len(self.text) > Console.MAX_TXT:
            lines = self.text.split('\n')

            self.text = lines.pop() + '\n'
            while len(self.text) + len(lines[-1]) < Console.MAX_TXT:
                self.text = lines.pop() + '\n' + self.text

    def print(self, msg):
        """Prints message to the console"""
        self.text += msg
        self._strip_text()
        self.panel.config(text=self.text, anchor='nw', justify='l')