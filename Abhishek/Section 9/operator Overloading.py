#method Overloading for the additiom operation

#First Class should be created and assigned with values

class point():

    #creating the function for the class and attributes
    def __init__(self,x,y):
        self.x = x
        self.y = y
        # now we want to overload the addition operation
    def __add__(self, other):
        x = self.x +other.x
        y = self.y +other.y
        return point(x,y)
    #in the above the step we are adding other where we want to overload the addition operator

    def __str__(self): # this statement is used to format the stirngs
        return "({0},{1})".format(self.x , self.y) # this string is used for formating purpose

point1 = point(5,6)# this the functional call to print the result
point2 = point (4,8)

print(point1+point2) # printing the result on the output screen


