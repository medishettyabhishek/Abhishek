from tkinter import *


class Buttons:

    def __init__(self, rootone):
        frame = Frame(rootone)
        frame.pack()

        self.printbutton = Button(frame, text="click here", command=self.printmessage)
        self.printbutton.pack()

        self.Quitbutton = Button(frame, text="exit", command=frame.quit)
        self.Quitbutton.pack(side=LEFT)

        def printmessage(self):
            print("buttonhole")


root = Tk()
b = Buttons(root)
root.mainloop()
