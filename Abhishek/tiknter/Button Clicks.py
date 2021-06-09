from tkinter import *

root = Tk()

def button_click():
    print("you have clicked the button")

button1 = Button(root,text = "Click" , command = button_click)
button1.pack()

root.mainloop()