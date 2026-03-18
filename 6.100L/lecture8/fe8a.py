def same_chars(s1, s2):
    """
    s1 and s2 are strings
    Returns boolean True is a character in s1 is also in s2, and vice 
    versa. If a character only exists in one of s1 or s2, returns False.
    """
    # Your code here
    result1 = True
    result2 = True
    for i in s1:
        #print(i)
        if i not in s2:
            result1 = False
    for i in s2:
        #print(i)
        if i not in s1:
            result2 = False
    if result1 == True and result2 == True:
        return True
    return False

# Examples:
print(same_chars("abc", "cab"))     # prints True
print(same_chars("abccc", "caaab")) # prints True
print(same_chars("abcd", "cabaa"))  # prints False
print(same_chars("abcabc", "cabz")) # prints False