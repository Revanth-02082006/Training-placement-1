def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("Enter a number: "))
result = factorial_iterative(num)
print("The factorial of", num, "is", result)
