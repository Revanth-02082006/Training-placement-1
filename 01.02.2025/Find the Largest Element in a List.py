# Function to find the largest element in a list
def find_largest(lst):
    return max(lst)

# Input list
input_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]

# Find largest element
largest_element = find_largest(input_list)

# Print result
print("The largest element is:", largest_element)
