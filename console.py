import tkinter as tk


class Console:
    COLOR_BG    = 'gray35'
    COLOR_TXT   = 'ghost white'

    MAX_LINES   = 8

    def __init__(self, master, mrow, mcol):
        self.master = master

        # Initialize wrapper frame
        self.frame = tk.Frame(self.master)
        self.frame.grid(row=mrow, column=mcol, sticky='NWSE')
        self.frame.config(bg=Console.COLOR_BG)

        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)

        # Initialize text
        self.panel = tk.Text(self.frame, state=tk.DISABLED)
        self.panel.config(
                          font=('Consolas', 12),
                          bg=Console.COLOR_BG,
                          fg=Console.COLOR_TXT,
                          relief='sunken'
        )
        self.panel.grid(row=0, column=0, sticky='NWSE')
        self.print("ROM Burner")

    def _strip_text(self):
        """Strips message to less than MAX_LINES"""
        nlines = self.nlines()
        if nlines > Console.MAX_LINES:
            self.panel.delete('1.0', str(float(nlines - Console.MAX_LINES)))

    def nlines(self):
        return int(self.panel.index(tk.END).split('.')[0]) - 1

    def print(self, msg):
        """Prints message to the console"""
        if not msg.endswith('\n'):
            msg += '\n'
        self.panel.config(state=tk.NORMAL)
        self.panel.insert(tk.END, msg)
        self._strip_text()
        self.panel.see(tk.END)
        self.panel.config(state=tk.DISABLED)

    def clear(self):
        self.text = ''
        self.panel.config(text=self.text, anchor='nw', justify='l')