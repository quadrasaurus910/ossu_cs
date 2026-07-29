class Circle():
    def __init__(self, radius):
        """ Initializes self with radius """
        self.rad = radius

    def get_radius(self):
        """ Returns the radius of self """
        return self.rad

    def set_radius(self, radius):
        """ radius is a number
        Changes the radius of self to radius """
        self.rad = radius

    def get_area(self):
        """ Returns the area of self using pi = 3.14 """
        return (self.rad**2)* 3.14

    def equal(self, c):
        """ c is a Circle object
        Returns True if self and c have the same radius value """
        return self.rad == c.rad

    def bigger(self, c):
        """ c is a Circle object
        Returns self or c, the Circle object with the bigger radius """
        if self.rad > c.rad:
            return self
        elif self.rad < c.rad:
            return c
        # else:
          #  return f'{self} radius is equal to {c} radius'

c1 = Circle(5)
c2 = Circle(10)
c2.set_radius(7)
print(Circle.get_radius(c2.bigger(c1)))
print(f"Circle c1 has an area of {c1.get_area()}")
