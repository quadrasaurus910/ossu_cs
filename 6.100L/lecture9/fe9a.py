def dot_product(tA, tB):
    """
    tA: a tuple of numbers
    tB: a tuple of numbers of the same length as tA
    Assumes tA and tB are the same length.
    Returns a tuple where the:
    * first element is the length of one of the tuples
    * second element is the sum of the pairwise products of tA and tB
    """
    # Your code here
    total = 0
    l = lambda x,y : x*y
    print(map(l, tA, tB))
    for i in range(len(tA)):
        total += tA[i] * tB[i]
    return (len(tA), total)


# Examples:
tA = (1, 2, 3)
tB = (4, 5, 6)   
print(dot_product(tA, tB)) # prints (3,32)