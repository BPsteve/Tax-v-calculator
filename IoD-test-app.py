# Tell us your salary
salary = float(input("Enter your salary: "))
# Tax rates input for Virginia
statetax = float(input(".0472 is the tax rate for VA.\nEnter your state tax rate: {5% as .05} :"))
# Standard tax rates
fedtax = .1168
sstax = .062
medicaretax = .0145
# Calculate the taxes
stax = (salary*statetax)
ftax = (salary*fedtax)
soctax = (salary*sstax)
mtax = (salary*medicaretax)
# Find total taxes
taxes = (stax+ftax+soctax+mtax)
# Calculate the take home on an annual basis
takehome = (salary-taxes)
# Display for the screen
print("Your take home pay will be: $" + str(takehome))
