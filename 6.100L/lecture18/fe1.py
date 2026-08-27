

class Circle():
    def __init__(self, radius):
        """ Initializes self with radius """
        self.radius = radius

    def get_radius(self):
        """ Returns the radius of self """
        return self.radius

    def __add__(self, c):
        """ c is a Circle object 
        Returns a new Circle object whose radius is 
        the sum of self and c's radius """
        return Circle(self.get_radius() + c.get_radius())

    def __str__(self):
        """ A Circle's string representation is the radius """
        return str(f"Circle has radius {self.get_radius()}, "
                   f"diameter {self.get_radius() * 2}, "
                   f"circumference {round((self.get_radius()*2) * 3.14, 3)}")


c1 = Circle(5)
c2 = Circle(10)
print((c1 + c2).get_radius())
print(c1)