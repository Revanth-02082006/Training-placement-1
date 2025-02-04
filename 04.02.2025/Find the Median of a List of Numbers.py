def find_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

input_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
median = find_median(input_list)
print("The median is:", median)
