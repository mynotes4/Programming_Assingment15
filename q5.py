"""
Question 5:
Define a class named Shape and its subclass Square. The Square class has an init function which
takes a length as argument. Both classes have a area function which can print the area of the
shape where Shape's area is 0 by default.
"""

class shape():

    def __init__(self,length = 0):
        pass

    def area(self):
        return 0

class square(shape):

    def __init__(self,length = 0):
        self.length = length

    def area(self):
        return self.length*self.length

a = square(5)
print("Area of square with side 5 =",a.area())
print("Prints default area ",square().area())