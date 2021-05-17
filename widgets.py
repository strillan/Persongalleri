import tkinter as tk
from tkinter.constants import END
from storage import Storage

class TextBox:
    def __init__(self, master, **kw):
        self.master = master
        self.textbox = tk.Text(master, kw)
        self.textbox.pack()
        self.textbox.bind('<Control-s>', self.save)

        self.storage = Storage()

    def save(self, event):
        print(self.textbox.get('1.0', END))
        #print(self.textbox.get('1.0', 'end-1c'))

