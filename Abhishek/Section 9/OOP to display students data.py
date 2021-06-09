class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_data(self, name , age):
        self.name = name
        self.age = age


    def put_data(self):
        print(self.name)
        print(self.age)


class Science_students(Student):

    def science(self):
        print("this is a science method")

a = Science_students("","")
a.get_data()