# Calc to determine taxes on 2024 taxes.
# Tell us your salary
monthly_salary = float(input("Enter your monthly salary: "))

# Employment type selector
employment_type = input("Are you self-employed or company-employed? (Enter 'self' or 'company'): ").strip().lower()

# Tax rates input for Virginia 2024
statetax = float(input(".0472 is the tax rate for VA.\nEnter your state tax rate (e.g., 5% as .05): "))

# Standard tax rates for company employees
sstax_employee = .062  # Social Security tax for employee (6.2%)
medicaretax_employee = .0145  # Medicare tax for employee (1.45%)

# Self-employed individuals pay both employee and employer portions
sstax_self = .124  # Social Security tax for self-employed (12.4%)
medicaretax_self = .029  # Medicare tax for self-employed (2.9%)

additional_medicare_tax = .009  # Additional 0.9% Medicare tax for income over $200,000 annually

# Wage base limits for 2024
social_security_wage_base = 168600  # Annual wage base limit for ss
medicare_wage_base = 200000  # Annual threshold for additional Medicare tax

# Convert monthly salary to annual salary
annual_salary = monthly_salary * 12

# Calc the state tax
annual_stax = annual_salary * statetax

# Function to calc fed tax based on annual salary using 2024 tax brackets
def calculate_fed_tax(annual_salary):
    if annual_salary <= 11000:
        return 0.10 * annual_salary
    elif 11000 < annual_salary <= 44725:
        return 1100 + 0.12 * (annual_salary - 11000)
    elif 44725 < annual_salary <= 95375:
        return 5147 + 0.22 * (annual_salary - 44725)
    elif 95375 < annual_salary <= 182100:
        return 16290 + 0.24 * (annual_salary - 95375)
    elif 182100 < annual_salary <= 231250:
        return 37104 + 0.32 * (annual_salary - 182100)
    elif 231250 < annual_salary <= 578125:
        return 52832 + 0.35 * (annual_salary - 231250)
    else:
        return 174238 + 0.37 * (annual_salary - 578125)

# Calc fed tax
annual_ftax = calculate_fed_tax(annual_salary)

# Calc sstax and Medicare tax based on employment type
if employment_type == "self":
    # Self-employed pays both employee and employer portions
    if annual_salary <= social_security_wage_base:
        soctax = annual_salary * sstax_self  # Apply sstax on full salary if under the limit
    else:
        soctax = social_security_wage_base * sstax_self  # Only tax up to the wage base limit

    # Medicare tax for self-employed
    medicare_tax = annual_salary * medicaretax_self

    # Apply additional Medicare tax if income is over the threshold
    if annual_salary > medicare_wage_base:
        medicare_tax += (annual_salary - medicare_wage_base) * additional_medicare_tax

elif employment_type == "company":
    # Company-employed pays only employee portion
    if annual_salary <= social_security_wage_base:
        soctax = annual_salary * sstax_employee  # Apply sstax on full salary if under the limit
    else:
        soctax = social_security_wage_base * sstax_employee  # Only tax up to the wage base limit

    # Medicare tax for employees
    medicare_tax = annual_salary * medicaretax_employee

    # Apply additional Medicare tax if income is over the threshold
    if annual_salary > medicare_wage_base:
        medicare_tax += (annual_salary - medicare_wage_base) * additional_medicare_tax

else:
    print("Invalid employment type entered. Please enter 'self' or 'company'.")
    exit()

# Find total annual taxes
total_taxes = annual_stax + annual_ftax + soctax + medicare_tax

# Calculate the take-home on an annual and monthly basis
annual_takehome = annual_salary - total_taxes
monthly_takehome = annual_takehome / 12

# Display the results
print(f"Your monthly take-home pay will be: ${monthly_takehome:.2f}")
print(f"Your annual take-home pay will be: ${annual_takehome:.2f}")
print()
print(f"You will pay: ${total_taxes:.2f} in total taxes this year.")
