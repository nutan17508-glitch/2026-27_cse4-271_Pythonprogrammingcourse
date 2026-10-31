principal = float(input("Enter principal amount in rupees: "))
rate = float(input("Enter rate of interest in percent: "))
time = float(input("Enter time in years: "))
CI = principal * (1 + rate / 100) ** time - principal 
print(f"Compound interest is {CI} rupees")