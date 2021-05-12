while True:
    try:

        income = int(input("Please enter your taxable income: "))
        name = input("Please enter your name: ")
    except ValueError:
        print("Sorry, I didn't understand that please enter taxable income as a number")

        continue
    else:
        break
grossMonthly = round(income/12)

if income <= 20000:
    tax = 0

elif income <= 40000: 
    tax = (income - 20000) * 0.1

elif income <= 80000:
    tax = (income-40000) * 0.2 + 2000 

elif income <= 180000:
    tax = (income - 80000) * 0.3 + 10000

else:
    tax = (income - 180000) * 0.4 + 40000

netMonthly = round(tax/12)

print("\nMonthly Payslip for:",'"',name,'"',
    "\nGross Monthly Income:$",grossMonthly,
    "\nMonthly Income Tax:$",netMonthly,
    "\nNet Monthly Income:$",grossMonthly-netMonthly)

input('\nPress Enter to Exit the App')