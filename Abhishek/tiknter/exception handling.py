try:
    a = 20
    b = 0
    print(a/b)
except ZeroDivisionError:
    print("there is an error")
finally:
    a = 20
    b = 10
    print(a / b)