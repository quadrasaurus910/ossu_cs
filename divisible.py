x = int(input("What is x: "))
y = int(input("What is y: "))

n = 1

while True:
    if (n % x == 0) and (n % y == 0):
        break
    n += 1

print(f"{n} is divisible by {x} and {y}")