# Tell us your salary
salary = float(input("Enter your monthly salary: "))

# Tax rates input for Virginia
statetax = float(input(".0472 is the tax rate for VA.\nEnter your state tax rate: {5% as .05} :"))

# Standard tax rates
# use this if you want an estimated tax rate for less than fedtax = .1168
sstax = .062
medicaretax = .0145

# Calculate the taxes
stax = (salary * statetax)

# Function to calculate federal tax based on salaryp

def calculate_fed_tax(salary):
    if salary <= 317:
        return 0.00 + 0.10 * (salary - 0)
    elif 317 < salary <= 1125:
        return 80.80 + 0.12 * (salary - 1125)
    elif 1125 < salary <= 3606:
        return 378.52 + 0.22 * (salary - 3606)
    elif 3606 < salary <= 7333:
        return 1198.46 + 0.24 * (salary - 7333)
    elif 7333 < salary <= 13710:
        return 2728.94 + 0.32 * (salary - 13710)
    elif 13710 < salary <= 17325:
        return 3885.74 + 0.35 * (salary - 17325)
    else:
        return 12816.69 + 0.37 * (salary - 42842)

ftax = calculate_fed_tax(salary)

# Calculate other taxes
soctax = (salary * sstax)
mtax = (salary * medicaretax)

# Find total taxes
taxes = (stax + ftax + soctax + mtax)

# Calculate the take home on an annual basis
takehome = (salary - taxes)
annualtakehome = (takehome * 12)

# Display for the screen
print("Your take home pay will be: $" + str(takehome))
print("Your annual take home pay will be: $" + str(annualtakehome))
