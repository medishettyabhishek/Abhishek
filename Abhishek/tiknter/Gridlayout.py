from tkinter import *  # we are importing the tkinter and all other modules here

root = Tk()  # We are creating the Tk class and assigning that to the root object

label1 = Label(root, text="enter the first name")
label2 = Label(root, text="enter the last name")

entry1 = Entry(root)
entry2 = Entry(root)

label1.grid(row=0, column=0)
label2.grid(row=1, column=0)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

root.mainloop()
