# pset1 part C

# variables
initial_deposit = float(input('Enter initial deposit: '))
total_cost = 800000 #float(input('Enter total cost of dream home: '))
down_payment = total_cost / 4
months = 36
amount_saved = 0
r = .00
low = 0.000
high = 1.000
epsilon = 100
steps = 0

# check if inital payment is greater than required down payment, if so assign r to 0.0
if initial_deposit >= (down_payment - 100):
    r = 0.0
# check if initial payment and compounded interest is enough to reach down payment goal, if not assign r to None.
elif (down_payment - (initial_deposit * ((1 + 1 / 12) ** months)))>= epsilon:
    r = None
# run bisection search to find best interest rate based off initial deposit, tolorence: 100
else:
    while (abs(down_payment - amount_saved)) > epsilon:
        midpoint = (low + high) / 2
        r = midpoint
        amount_saved = initial_deposit * ((1 + r / 12) ** months)
        print(f"r: {r}, amount saved: {amount_saved}, diff: {abs(down_payment - amount_saved)}, low: {low}, high: {high}")
        if  down_payment - amount_saved < epsilon:
            high = midpoint
        elif down_payment - amount_saved > epsilon:
            low = midpoint
        steps += 1



print(f"Best interest rate: {r}")
print(f"Bisection search steps: {steps}")
    