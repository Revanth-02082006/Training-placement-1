# Function to check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

# Input string
input_str = input("Enter a string: ")

# Check if palindrome
if is_palindrome(input_str):
    print(input_str, "is a palindrome")
else:
    print(input_str, "is not a palindrome")
