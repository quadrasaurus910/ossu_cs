# Showcases Multiple assignment statements can be bound to functions 
# returning fixed sized sequences 

def findExtremeDivisors(n1, n2):
    """Assumes that n1 and n2 are positive ints
    Returns a tuple containing the smallest common divisor > 1 and 
    the largest common divisor of n1 and n2. If no common divisor, 
    returns (None, None)"""
    minVal, maxVal = None, None
    for i in range(2, min(n1, n2) + 1):
        if n1%i == 0 and n2%i == 0: 
            if minVal == None:
                 minVal = i
            maxVal = i
    return (minVal, maxVal)

minD, maxD = findExtremeDivisors(100,200)
print(minD, maxD)