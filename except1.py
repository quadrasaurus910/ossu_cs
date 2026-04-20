def findAnEven(L):
    """Assumes L is a list of integers
    Returns the first even number in L
    Raises ValueError if L does not contain an even number"""
    for i in L:
        try:
            if i % 2 == 0:
                return i
        except:
            continue
    raise ValueError("List contains no even number")

print(findAnEven([1, "a","b"]))