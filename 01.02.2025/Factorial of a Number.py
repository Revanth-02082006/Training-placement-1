# Function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Input number
num = int(input("Enter a number: "))

# Calculate factorial
result = factorial(num)

# Print result
print("The factorial of", num, "is", result)
