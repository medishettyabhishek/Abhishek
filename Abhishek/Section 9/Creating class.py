class teddy:
    quantity = 200

    def __init__(self, name , colour):
        self.colour = colour
        self.name = name

    def change_name(self , name):
        self.name = name

teddy1 = teddy("abhis", "orange")
print(teddy1.name)
print(teddy1.colour)

teddy1.change_name("abhishek")
print(teddy1.name)

