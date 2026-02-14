
N = int(input('Enter a positive integer: '))

incrementor = 0

while incrementor <= N:
    if incrementor ** 3 == N:
        print(f'{incrementor} is the cube root of {N}')
        break
    incrementor += 1
if incrementor == N + 1:
    print('error')