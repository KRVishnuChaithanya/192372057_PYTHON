def circulate_left(lst, steps=1):
    n = len(lst)
    steps = steps % n  # Adjust steps if it's larger than the length of the list
    return lst[steps:] + lst[:steps]

# Test case
original_list = [1, 2, 3, 4, 5]
rotated_list = circulate_left(original_list, 2)
print("Original List:", original_list)
print("Circulated List (Left):", rotated_list)
