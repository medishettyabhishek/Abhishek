from tkinter import *


def function1():
    print("menu item clicked")


root = Tk()

mymenu = Menu(root)
root.config(Menu=mymenu)

Submenu = Menu(mymenu)

mymenu.add_cascade(label="file", Menu=Submenu)

Submenu.add_cascade(Label="Project", command=function1)
Submenu.add_cascade(Label="save", command=function1)

root.mainloop()
