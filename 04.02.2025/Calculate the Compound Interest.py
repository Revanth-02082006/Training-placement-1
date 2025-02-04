def compound_interest(principal, rate, time):
    amount = principal * (1 + rate / 100) ** time
    return amount - principal

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate: "))
time = float(input("Enter the time in years: "))
interest = compound_interest(principal, rate, time)
print("The compound interest is:", interest)
