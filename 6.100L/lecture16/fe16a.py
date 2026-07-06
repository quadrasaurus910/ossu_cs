def flatten(L):
    """ 
    L: a list 
    Returns a copy of L, which is a flattened version of L 
    """
    # Your code here
    if type(L) != list:
        return L
    else:
        if len(L) == 1:
            return L[0]
        else:
            return [flatten(L[0])] + [flatten(L[1:])]

# Examples:
L = [[1,4,[6],2],[[[3]],2],4,5]
print(flatten(L)) # prints the list [1,4,6,2,3,2,4,5]