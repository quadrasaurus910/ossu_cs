def all_true(n, Lf):
    """ n is an int
        Lf is a list of functions that take in an int and return a Boolean
    Returns True if each and every function in Lf returns True when called 
    with n as a parameter. Otherwise returns False. 
    """
    # Using list comprehension to iterate over list executing function

    if False in [f(n) for f in Lf]:
        return False
    else:
        return True

# Examples:
squared = lambda x : x**2 % 2 == 0 
cubed = lambda x : x**3 % 2 == 0    
print(all_true(6, [squared, cubed])) # prints 6