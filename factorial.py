# figure 4.5

def factI(n):
    """" Assumes n an int > 0
    Returns n!"""
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

def factR(n):
    """Assumes  n an int > 0
    Returns n!"""
    if n == 1:
        return n
    else:
        return n*factR(n - 1)

print(factR(5))