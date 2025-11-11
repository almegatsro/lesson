class rectangle():

    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width
    
new_rectangle = rectangle(5, 3)
print("dimensions of rectangle: length =", new_rectangle.length, ", width =", new_rectangle.width)
print("Area of rectangle:", new_rectangle.area())    