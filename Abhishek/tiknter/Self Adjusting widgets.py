from tkinter import *

root = Tk()
label1 = Label(root, text="First", bg="red", fg="Green")
label1.pack(fill=X)

label2 = Label(root, text="Second", bg="blue", fg="Green")
label2.pack(side=LEFT, fill=Y)

label3 = Label(root, text="third", bg="Pink", fg="Green")
label3.pack(side=RIGHT, fill=Y)
root.mainloop()
