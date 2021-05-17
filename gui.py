import tkinter as tk
from tkinter import ttk
from widgets import TextBox

import tkinter

class GUI():
    def __init__(self, master):
        master_frame = tk.Frame(master).pack()
        self.textbox = TextBox(master_frame)

    

if __name__ == '__main__':
    a = tk.Tk()
    GUI(a)
    a.mainloop()