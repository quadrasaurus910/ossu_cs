def all_true(n, Lf):
    """ n is an int
        Lf is a list of functions that take in an int and return a Boolean
    Returns True if each and every function in Lf returns True when called 
    with n as a parameter. Otherwise returns False. 
    """
    # Using list comprehension to iterate over list executing function
    print([f(n) for f in Lf])

# Examples:
cubed = lambda x : x**3 % 2 == 0    
all_true(7, [cubed]) # prints 6