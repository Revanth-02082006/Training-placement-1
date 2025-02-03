def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
if is_anagram(str1, str2):
    print(str1, "and", str2, "are anagrams")
else:
    print(str1, "and", str2, "are not anagrams")
