def find_largest(lst):
    return max(lst)

input_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
largest_element = find_largest(input_list)
print("The largest element is:", largest_element)
