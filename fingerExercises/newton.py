#Newton-Raphson for square root
#Find x such that x**2 - 24 is within epsilon of 0 
epsilon = 0.01
k = 24.0
guess = k/2.0
steps = 0
while abs(guess*guess - k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2*guess))
    steps += 1
print(f"Square root of {k} is about {guess}. This took {steps} guesses.")