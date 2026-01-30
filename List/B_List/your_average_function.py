# Write a function `your_average_function(numbers)` that accepts a list of numbers.
# The function should return the average of all elements in the list.
# If the list is empty, the function should return None.

def your_average_function(numbers):
    sum = 0
    count = 0
    for n in numbers:
        sum += n
        count += 1
        ave = sum / count
    return ave
    

# Example:
your_average_function([5, 2, 7, 24])# -> 9.5
your_average_function([100, 6])# -> 53
your_average_function([31, 32, 40, 12, 33]) #-> 29.6
your_average_function([])# -> None

