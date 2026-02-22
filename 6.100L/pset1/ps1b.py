# house hunting part A

annual_salary = float(input('Enter your annual salary: '))
percent_to_save = float(input('Enter amount to save, as a decimal: '))
total_cost = float(input('Enter total cost of your dream home: ')) 
semi_annual_raise = float(input('Enter amount for semi-annual raise, in a decimal: '))
monthly_salary = annual_salary / 12
down_payment = 0.25 * total_cost
r = 0.04
current_savings = 0.0
months = 0

while current_savings < down_payment:
    current_savings += (current_savings * r / 12) + (monthly_salary * percent_to_save)
    months += 1
    # use modulo operator to calculate when to add raise
    if months % 6 == 0:
        monthly_salary += monthly_salary * semi_annual_raise
print(f"total months: {months}")
