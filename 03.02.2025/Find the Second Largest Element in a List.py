def second_largest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2]

input_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
second_largest_element = second_largest(input_list)
print("The second largest element is:", second_largest_element)
