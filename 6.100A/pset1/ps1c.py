# pset1 part C

# annual_salary = float(input('Enter annual salary: '))
initial_payment = int(input('Enter initial savings amount: '))
total_cost = 800000 #float(input('Enter total cost of dream home: '))
down_payment = total_cost / 4
months = 36
r = .00

for i in range(100):
    n = i / 100
    r = n
    amount_saved = initial_payment * ((1 + r / 12) ** months)
    if amount_saved > down_payment:
        print(r)
        break

# monthly_salary = annual_salary / 12