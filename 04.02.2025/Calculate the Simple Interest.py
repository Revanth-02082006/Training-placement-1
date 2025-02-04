def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate: "))
time = float(input("Enter the time in years: "))
interest = simple_interest(principal, rate, time)
print("The simple interest is:", interest)
