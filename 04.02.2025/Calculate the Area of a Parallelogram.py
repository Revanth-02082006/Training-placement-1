def area_of_parallelogram(base, height):
    return base * height

base = float(input("Enter the base of the parallelogram: "))
height = float(input("Enter the height of the parallelogram: "))
area = area_of_parallelogram(base, height)
print("The area of the parallelogram is:", area)
