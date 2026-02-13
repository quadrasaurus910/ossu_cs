# compare  Newton-Raphson method vs bisection search

import time

epsilon = 0.01
k = int(input("Enter an integer: "))
guess = k/2.0
steps = 0
steps2 = 0
low = 0.00
high = max(1.0, k)
ans = (low + high) / 2
start1 = time.time()

while abs(guess * guess - k) >= epsilon:
    guess = guess - (((guess ** 2) - k) / (2 * guess))
    steps += 1
stop1 = time.time()
elapse1 = stop1 - start1

start2 = time.time()
while abs(ans ** 2 - k) >= epsilon:
    if ans ** 2 < k:
        low = ans
    else:
        high = ans
    ans = (low + high) / 2.0
    steps2 += 1
stop2 = time.time()
elapse2 = stop2 - start2

print(f"Newton-Raphson method took {steps} steps to find: {guess}. Elapsed time: {elapse1}")
print(f"Bisection search took {steps2} steps to find: {ans}. Elapsed time: {elapse2}")