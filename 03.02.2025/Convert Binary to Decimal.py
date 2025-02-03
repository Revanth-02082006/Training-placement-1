def binary_to_decimal(binary_str):
    return int(binary_str, 2)

binary_str = input("Enter a binary number: ")
decimal_number = binary_to_decimal(binary_str)
print("Decimal representation of", binary_str, "is:", decimal_number)
