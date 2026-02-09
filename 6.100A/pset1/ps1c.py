# pset1 part C

# annual_salary = float(input('Enter annual salary: '))
initial_payment = int(input('Enter initial savings amount: '))
total_cost = 800000 #float(input('Enter total cost of dream home: '))
down_payment = total_cost / 4
months = 36
r = .00
low = 0.00
high = 1.00
epsilon = 100


for i in range(0, 20, 1):
    midpoint = (low + high) / 2
    r = round(midpoint, 2)
    # print(r)
    amount_saved = initial_payment * ((1 + r / 12) ** months)
    print(f"r: {r}, amount saved: {amount_saved}, diff: {down_payment - amount_saved}, low: {low}, high: {high}")
    if  down_payment - amount_saved < epsilon:
        high = midpoint
    elif down_payment - amount_saved > epsilon:
        low = midpoint
        #print(r)
    #print(amount_saved)
    # if amount_saved >= down_payment:
        # print(r)
        # break

# monthly_salary = annual_salary / 12