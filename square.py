x = int(input("Enter integer: "))
ans = 0
intsLeft = x

# square a number the hard way
while (intsLeft != 0):
    ans += x
    intsLeft -= 1

print(f"{x} + {x} = {ans}")