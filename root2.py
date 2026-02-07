#Figure 3.1
#Find the cube root of a perfect cube 
# highlight decrementing function
x = int(input('Enter an integer: ')) 
for ans in range(0, abs(x)+1):
    print(f'Value of the decrementing function abs({x}) - {ans}**3 is {abs(x) - ans**3}')
    if ans**3 >= abs(x): 
        break
if ans**3 != abs(x):
    print(x, 'is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of', x,'is', ans)