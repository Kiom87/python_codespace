# Write a function `remove_dupes(lst)` that accepts a list and returns a new list
# where each element appears only once.


def remove_dupes(lst):
    new_list = []
    for item in lst:
        if item not in new_list:  # O(n) per check; overall O(n^2) in worst case
            new_list.append(item)
    return new_list


print(remove_dupes(["x", "y", "y", "x", "z"]))  # ['x', 'y', 'z']
print(remove_dupes([False, False, True, False]))  # [False, True]
print(remove_dupes([42, 5, 7, 42, 7, 3, 7, 7]))  # [42, 5, 7, 3]













def remove_dupes(lst):
    seen = set()
    new_list = []

    for item in lst:
        if item not in seen:
            seen.add(item)
            new_list.append(item)
    return new_list        



# Example usage:
print(remove_dupes(["x", "y", "y", "x", "z"]))  # ['x', 'y', 'z']
print(remove_dupes([False, False, True, False]))  # [False, True]
print(remove_dupes([42, 5, 7, 42, 7, 3, 7, 7]))  # [42, 5, 7, 3]

