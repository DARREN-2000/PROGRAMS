
#defining england tax rates and tax bands

personal_allowance = 12_500
personal_allowance_limit = 100_000

basic_pay = 37_500
higher_pay = 150_000

basic_rate = 0.2
higher_rate = 0.4
additional_rate = 0.45

print(" - INCOME TAX CALCULATOR - ")
print(" ENGLAND TAX CALUCULATION ")

salary = float(input(" Input Salary "))

if salary > personal_allowance_limit:
    personal_allowance -= (salary - personal_allowance_limit)/2
    if personal_allowance < 0:
        personal_allowance = 0

taxable_income = salary - personal_allowance

if taxable_income <= 0:
    tax = 0
elif taxable_income > 0 and taxable_income <= basic_pay:
    tax = taxable_income * basic_rate
elif taxable_income > 0 and taxable_income <= higher_pay:
    tax = taxable_income * higher_rate   
else:
    tax = (basic_pay * basic_rate) + ((higher_pay - basic_pay) * higher_rate) + ((taxable_income - higher_pay) * additional_rate)

year_tax = round(tax , 2)

monthly_tax = round(tax/12 , 2)

print(f"your yearly tax is ${year_tax}")
print(f"your monthly tax is ${monthly_tax}")
