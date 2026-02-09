# pset1 part C

# annual_salary = float(input('Enter annual salary: '))
initial_payment = int(input('Enter initial savings amount: '))
total_cost = 800000 #float(input('Enter total cost of dream home: '))
down_payment = total_cost / 4
months = 36
amount_saved = 0
r = .00
low = 0.000
high = 1.000
epsilon = 100


while (abs(down_payment - amount_saved)) > epsilon:
    midpoint = (low + high) / 2
    r = midpoint
    # print(r)
    amount_saved = initial_payment * ((1 + r / 12) ** months)
    print(f"r: {r}, amount saved: {amount_saved}, diff: {abs(down_payment - amount_saved)}, low: {low}, high: {high}")
    if  down_payment - amount_saved < epsilon:
        high = midpoint
    elif down_payment - amount_saved > epsilon:
        low = midpoint

print(f"rate: {r * 100}%")
    