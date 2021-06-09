class point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return point(x, y)

    def __str__(self):
        return "{0}{1}".format(self.x, self.y)


point1 = point(10, 12)
point2 = point(2, 3)

print(point1-point2)
