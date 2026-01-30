# Write a function `odd_sum(max_num)` that returns the sum of all odd numbers
# from 1 to max_num inclusive.

def odd_sum(max_num):
    if max_num < 1:
        return 0
    return sum(range(1, max_num + 1, 2))


# Example:
print(odd_sum(10)) #-> 25  # 1 + 3 + 5 + 7 + 9
print(odd_sum(5))  #-> 9   # 1 + 3 + 5


def odd_sum(max_num):
    """Return the sum of all odd numbers from 1 to max_num inclusive, using a formula."""
    if max_num < 1:
        return 0
    k = (max_num + 1) // 2
    return k * k
