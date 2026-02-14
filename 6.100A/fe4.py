
N = int(input('Enter a positive integer: '))

decrementor = N

while decrementor > 0:
    if decrementor ** 3 == N:
        print(f'{decrementor} is the cube root of {N}')
        break
    decrementor -= 1
if decrementor == 0:
    print('error')