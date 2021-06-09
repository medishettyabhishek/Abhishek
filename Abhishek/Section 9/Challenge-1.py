class Computer():
    def __init__(self,ram,memory,size):
        self.size = size
        self.memory = memory
        self.ram = ram

    def getspec(self):
        print("enter the details")
        self.size = input("enter the size")
        self.memory = input("enter the memory")
        self.ram = input("enter the ram number")

    def displayspec(self):
        print("here are the specs of teh computer")
        print("ram size is:"+self.ram+"memory size is :")


class Desktop(Computer):
    def __init__(self, casecolor):
        self.casecolor = casecolor

    def get_case_details(self):
        self.casecolor = input('Enter case color')

    def put_case_details(self):
        print('case color is: ' + self.casecolor)


class Laptop(Computer):
    def __init__(self, weight):
        self.weight = weight

    def getweight(self):
        self.weight = input('Enter weight')

    def displayweight(self):
        print('weight is: ' + self.weight)