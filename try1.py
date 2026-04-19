# Implement a try/except block 

def sumDigits(s):
    """Assumes s is a string
    Returns the sum of the decimal digits in s
    For example, if s is 'a2b3c' it returns 5"""
    sum = 0
    for i in s:
        try:
            sum += int(i)
        except:
            continue
    return sum

print(sumDigits("a2b3c"))