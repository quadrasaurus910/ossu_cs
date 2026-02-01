
inputs = []
odds = []

# Get 10 ints from the user
for i in range(0, 10):
    n = int(input("Enter an integer: "))
    inputs.append(n)

# Add all odd number ints to odds lost
for i in inputs:
    if i % 2 != 0:
        odds.append(i)

if len(odds) == 0:
    print("None of these numbers are odd.")
else:
    print(sorted(odds)[0] + 'is the greatest odd number.')