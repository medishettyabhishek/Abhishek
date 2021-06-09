import re

string =  ("hello my name is John")

pattern = r"John"
newstring = re.sub(pattern , "abhishek",string)
print(newstring)
