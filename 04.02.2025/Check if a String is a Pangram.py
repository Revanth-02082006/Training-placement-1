import string

def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    return set(s.lower()) >= alphabet

input_str = input("Enter a string: ")
if is_pangram(input_str):
    print(input_str, "is a pangram")
else:
    print(input_str, "is not a pangram")
