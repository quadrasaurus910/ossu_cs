x = int(input("Enter integer: "))
ans = 0
intsLeft = abs(x) # initialize to absolute number

# square a number the hard way
while (intsLeft != 0):
    ans += abs(x)
    intsLeft -= 1

print(f"{x} * {x} = {ans}")