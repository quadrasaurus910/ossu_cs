# showcase floating point representation
# a non-integer number is represented in
# a pair of binary numbers, a set of 
# significant digits and an exponent
# the amount of significant digets determine
# the precision
x = 0.0
for i in range(10):
    x = x + 0.1 
    if x == 1.0:
        print(x, '= 1.0') 
    else:
        print(x, 'is not 1.0')