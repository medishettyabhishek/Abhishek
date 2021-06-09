from tkinter import *
import parser

root = Tk()


# get the userinputs for the Calcualtor that can be acheived by the function
i = 0


def get_values(num):
    global i
    display.insert(i, num)
    i += 1
def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        Clear_all()
        display.insert(0,result)
    except Exception:
        Clear_all()
        display.insert(0,"Error")


def Clear_all():
    display.delete(0, END)

def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        Clear_all()
        display.insert(0,new_string)
    else:
        Clear_all()
        display.insert(0, "error")

def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i,operator)
    i+= length


# Adding the Input to the Feild
display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W + E)

# Adding the buttons to the calculator

Button(root, text="1", command=lambda: get_values(1)).grid(row=2, column=0)
Button(root, text="2", command=lambda: get_values(2)).grid(row=2, column=1)
Button(root, text="3", command=lambda: get_values(3)).grid(row=2, column=2)

Button(root, text="4", command=lambda: get_values(4)).grid(row=3, column=0)
Button(root, text="5", command=lambda: get_values(5)).grid(row=3, column=1)
Button(root, text="6", command=lambda: get_values(6)).grid(row=3, column=2)

Button(root, text="7", command=lambda: get_values(7)).grid(row=4, column=0)
Button(root, text="8", command=lambda: get_values(8)).grid(row=4, column=1)
Button(root, text="9", command=lambda: get_values(9)).grid(row=4, column=2)

# Adding other buttons to the calculator

Button(root, text="AC", command=lambda: Clear_all()).grid(row=5, column=0)
Button(root, text="0", command=lambda: get_values(0)).grid(row=5, column=1)
Button(root, text="=",command=lambda: calculate()).grid(row=5, column=2)

# Adding the Operator Symbols

Button(root, text="+", command=lambda: get_operation("+")).grid(row=2, column=3)
Button(root, text="-", command=lambda: get_operation("-")).grid(row=3, column=3)
Button(root, text="*", command=lambda: get_operation("*")).grid(row=4, column=3)
Button(root, text="/", command=lambda: get_operation("/")).grid(row=5, column=3)

# Adding few other operations

Button(root, text="pi", comman= lambda:get_operation("*3.14")).grid(row=2, column=4)
Button(root, text="%", command= lambda:get_operation("%")).grid(row=3, column=4)
Button(root, text="(", command= lambda :get_operation("(")).grid(row=4, column=4)
Button(root, text="exp", command= lambda :get_operation("**")).grid(row=5, column=4)

Button(root, text="<-", command=lambda: undo()).grid(row=2, column=5)
Button(root, text="x!").grid(row=3, column=5)
Button(root, text=")", command= lambda :get_operation(")")).grid(row=4, column=5)
Button(root, text="^2", command= lambda :get_operation("**2")).grid(row=5, column=5)

root.mainloop()
