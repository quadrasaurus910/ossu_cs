n = int(input('Give a positive number: '))

# check if n if positive, print 'hello world' n times
if n > 0:
    for i in range(n):
        print('hello world')
else:
    print(f'{n} is not a positive number.')