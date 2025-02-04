def is_perfect_cube(n):
    cube_root = round(n ** (1/3))
    return cube_root ** 3 == n

num = int(input("Enter a number: "))
if is_perfect_cube(num):
    print(num, "is a perfect cube")
else:
    print(num, "is not a perfect cube")
