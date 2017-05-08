from tkinter import *
from tkinter import ttk


class MyGUI:
    def __init__(self):
        self._root = Tk()  # set up the main window
        self._root.title("Calculator - Feet to Meters")

        self._mainframe = ttk.Frame(self._root, padding="3 3 12 12")
        self._mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self._mainframe.columnconfigure(0, weight=1)
        self._mainframe.rowconfigure(0, weight=1)

        # To create a Tkinter variable, call the corresponding constructor: StringVar(), and it's a global variable
        self._MaxValue = StringVar()
        self._minValue = StringVar()

        # set a Label in UI
        ttk.Label(self._mainframe, text="Max Value = ").grid(column=2, row=1, sticky=W)
        self._MaxValue_entry = ttk.Label(self._mainframe, textvariable=self._MaxValue)
        self._MaxValue_entry.grid(column=3, row=1, sticky=(W, E))

        # set a Label in UI
        ttk.Label(self._mainframe, text="min Value = ").grid(column=2, row=2, sticky=E)
        self._minValue_entry = ttk.Label(self._mainframe, textvariable=self._minValue)
        self._minValue_entry.grid(column=3, row=2, sticky=(W, E))

        # padding a little space so that all entries won't be scrunched
        for child in self._mainframe.winfo_children():
            child.grid_configure(padx=7, pady=7)


    def startGui(self):
        # This final line tells Tk to enter its event loop, which is needed to make everything run.
        self._root.mainloop()


    def updateGUI(self, Max, min):
        self._MaxValue.set(Max)
        self._minValue.set(min)

