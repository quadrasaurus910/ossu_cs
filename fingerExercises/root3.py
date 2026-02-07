i = int(input("Enter an integer: "))
power = 1
root = 0

while  0 < power < 6:
    for r in range(1, i):
        print(r**power)
    power += 1