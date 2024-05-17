# Calculation to determine taxes.
# Tell us your salary
salary = float(input("Enter your monthly salary: "))

# Tax rates input for Virginia
statetax = float(input(".0472 is the tax rate for VA.\nEnter your state tax rate (e.g., 5% as .05): "))

# Standard tax rates
sstax = .062
medicaretax = .0145

# Calculate the state tax
stax = salary * statetax

# Function to calculate federal tax based on salary
def calculate_fed_tax(salary):
    if salary <= 317:
        return 0.00 + 0.10 * salary
    elif 317 < salary <= 1125:
        return 31.70 + 0.12 * (salary - 317)
    elif 1125 < salary <= 3606:
        return 116.14 + 0.22 * (salary - 1125)
    elif 3606 < salary <= 7333:
        return 633.50 + 0.24 * (salary - 3606)
    elif 7333 < salary <= 13710:
        return 1508.54 + 0.32 * (salary - 7333)
    elif 13710 < salary <= 17325:
        return 3617.02 + 0.35 * (salary - 13710)
    else:
        return 4863.47 + 0.37 * (salary - 17325)

ftax = calculate_fed_tax(salary)

# Calculate other taxes
soctax = salary * sstax
mtax = salary * medicaretax

# Find total taxes
total_taxes = stax + ftax + soctax + mtax

# Calculate the take-home on an annual basis
monthly_takehome = salary - total_taxes
annual_takehome = monthly_takehome * 12

# Display for the screen
print(f"Your monthly take-home pay will be: ${monthly_takehome:.2f}")
print(f"Your annual take-home pay will be: ${annual_takehome:.2f}")