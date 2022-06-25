from tkinter import *
from tkinter import ttk


def among() -> str:
    variable: str = "I am among"
    return variable


if __name__ == '__main__':
    print(among())
    print()
    root = Tk()
    frm = ttk.Frame(root, padding=300)
    frm.grid()
    ttk.Label(frm, text="Hello World!").grid(column=100, row=100)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    root.mainloop()
