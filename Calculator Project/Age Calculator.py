import datetime
from tkinter import *

root = Tk()
root.title("Age Calculator".center(350))


def CalculateAge(nameValue=None):
    today = datetime.today()
    birthdate = datetime.date(int("enter the date"), int("enter the year"), int("enter the month"))
    age = today.year - birthdate.year - (int(today.month, today.day))
    Label(text=f"{nameValue.get()} your age is {age}")


# Adding the label Names to the Grid
Label1 = Label(root, text="enter the Name ")
Label2 = Label(root, text="enter the year of birth ")
Label3 = Label(root, text="enter the Month ")
Label4 = Label(root, text="enter the Day ")

Button1 = Button(root, text="calculate", command=CalculateAge(), fg="Green")

# Adding the Entry to the grid
entry1 = Entry(root)
entry2 = Entry(root)
entry3 = Entry(root)
entry4 = Entry(root)

# Assigning the Labels to the Grid by using the column and rows

Label1.grid(row=0, column=0)
Label2.grid(row=1, column=0)
Label3.grid(row=2, column=0)
Label4.grid(row=3, column=0)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2, column=1)
entry4.grid(row=3, column=1)

Button1.grid(row=4, column=1)

root.mainloop()
