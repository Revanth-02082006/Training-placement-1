def is_perfect_number(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

num = int(input("Enter a number: "))
if is_perfect_number(num):
    print(num, "is a perfect number")
else:
    print(num, "is not a perfect number")
