from tkinter import *  # we are importing the tkinter and all other modules here

root = Tk()  # We are creating the Tk class and assigning that to the root object

Frame1 = Frame(root)  # This is adding of the frame to the root object
Frame1.pack()  # this is packing the frame to the Main view

Frame2 = Frame(root)
Frame2.pack(side=BOTTOM)  # the second frame selected should be on the bottom side

Button1 = Button(Frame1, text="Click", fg="red")  # Creating a button for the frame 1 with text and colour
Button1.pack()  # Packing this button for the main view

Button2 = Button(Frame2, text="continue", fg="Green")
Button2.pack()

root.mainloop()  # this is to put the Created frame and views in the loop to view
