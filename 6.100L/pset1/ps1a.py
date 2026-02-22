# house hunting part A

annual_salary = float(input('Enter your annual salary: '))
percent_to_save = float(input('Enter amount to save, as a decimal: '))
total_cost = float(input('Enter total cost of your dream home: ')) 
monthly_salary = annual_salary / 12
down_payment = 0.25 * total_cost
r = 0.04
current_savings = 0.0
months = 0
while current_savings < down_payment:
    current_savings += (current_savings * r / 12) + (monthly_salary * percent_to_save)
    months += 1
print(f"total months: {months}")
