# compare  Newton-Raphson method vs bisection search

epsilon = 0.01
k = int(input("Enter an integer: "))
guess = k/2.0
steps = 0
steps2 = 0
low = 0.00
high = max(1.0, k)
ans = (low + high) / 2

while abs(guess * guess - k) >= epsilon:
    guess = guess - (((guess ** 2) - k) / (2 * guess))
    steps += 1

while abs(ans ** 2 - k) >= epsilon:
    if ans ** 2 < k:
        low = ans
    else:
        high = ans
    ans = (low + high) / 2.0
    steps2 += 1
    print(ans)

print(f"Newton-Raphson method took {steps} steps to find: {guess}.")
print(f"Bisection search took {steps2} steps to find: {ans}.")