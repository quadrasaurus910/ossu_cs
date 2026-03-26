for i in map(lambda x,y : x*y, [1,2,3,4], [2,3,4,5]):
    ...
    #print(i)

string = 'word'
cubed = lambda x : x**3
# list comprehension
print([x.upper() for x in string])
# list comprehension with an if statement
print([x**3 for x in range(1,11) if x%2==0])
# list comprehension with function
print([cubed(x) for x in range(1,11)] )
# list filtered with lambda, higher-order programming
print(list(filter(lambda x : x**3 % 2 == 0, range(1,11))))