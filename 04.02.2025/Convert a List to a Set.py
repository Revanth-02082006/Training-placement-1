def list_to_set(lst):
    return set(lst)

input_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
result_set = list_to_set(input_list)
print("The set is:", result_set)
