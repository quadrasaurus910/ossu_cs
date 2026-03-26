for i in map(lambda x,y : x*y, [1,2,3,4], [2,3,4,5]):
    ...
    #print(i)

string = 'word'
cubed = lambda x : x**3
print([x**3 for x in range(1,11)])
print([cubed(x) for x in range(1,11)] )