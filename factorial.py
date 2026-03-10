# figure 4.5

# Implements the factorial
# 1! = 1
# (n + 1)! = (n + 1) * n!

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
    print(f'n = {n}')
    if n == 1:
        return n
    else:
        return n*factR(n - 1)

print(factR(5))