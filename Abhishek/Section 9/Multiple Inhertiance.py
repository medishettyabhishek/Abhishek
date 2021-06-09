class A:
    def a_method(self):
        print("this a a method")
class B:
    def b_method(self):
        print("this a b method")

class C(A,B):
    def c_method(self):
        print("this a c method")

c_object = C()
c_object.a_method()
c_object.b_method()
c_object.c_method()