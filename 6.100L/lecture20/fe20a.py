class Container(object):
    """
    A container object is a list and can store elements of any type
    """
    def __init__(self):
        """
        Initializes an empty list
        """
        self.myList = []

    def size(self):
        """
        Returns the length of the container list
        """
        # Your code here
        return len(self.myList)

    def add(self, elem):
        """
        Adds the elem to one end of the container list, keeping the end
        you add to consistent. Does not return anything
        """
        # Your code here
        self.myList.append(elem)

class Queue(Container):
    """
    A subclass of Container. Has an additional method to remove elements.
    """
    def remove(self):
        """
        The oldest element in the container list is removed
        Returns the element removed or None if the stack contains no elements
        """
        # Your code here
        if self.size() > 0:
            e = self.myList[0]
            self.myList.remove(e)
            return e

c1 = Container()
c1.add('a')
c1.add('b')
c1.add('c')
print(c1.size())
q1 = Queue()
q1.add('a')
q1.add('b')
q1.add('c')
print(q1.size())
print(q1.remove())
print(q1.size())