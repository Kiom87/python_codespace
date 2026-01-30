# Write a function `common_elements(arr1, arr2)` that accepts two lists as arguments.
# The function should return a new list containing the elements that are found in both input lists.
# The order of elements in the output list doesn't matter.

def common_elements(arr1, arr2):
    new_list = []

    for el in arr1:
        if el in arr2:
            new_list.append(el)

    print(new_list)

# Example:
common_elements(["a", "c", "d", "b"], ["b", "a", "y"]) # -> ['a', 'b']
common_elements([4, 7], [32, 7, 1, 4]) # -> [4, 7]

