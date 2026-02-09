# pset1 part C

# annual_salary = float(input('Enter annual salary: '))
initial_payment = int(input('Enter initial savings amount: '))
total_cost = 800000 #float(input('Enter total cost of dream home: '))
down_payment = total_cost / 4
months = 36
r = .00
low = 0.01
high = 1.00
epsilon = 100


for i in range(0, 100, 1):
    ans = (low + high) / 2
    r = ans
    print(ans)
    amount_saved = initial_payment * ((1 + r / 12) ** months)
    if amount_saved - down_payment >= epsilon:
        ...
        #print(r)
    #print(amount_saved)
    # if amount_saved >= down_payment:
        # print(r)
        # break

# monthly_salary = annual_salary / 12