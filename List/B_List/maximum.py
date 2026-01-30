# Write a function `maximum(numbers)` that accepts a list of numbers.
# The function should return the largest number in the list.
# If the list is empty, return None.

def maximum(numbers):
    
    if not numbers: 
        return None

    largest = numbers[0]
    for n in numbers[1:]:
        if n > largest:
            largest = n
    return largest
        


# Example:
maximum([5, 6, 3, 7]) #-> 7
maximum([17, 15, 19, 11, 2]) #-> 19
maximum([]) #-> None


#PYTHONIC

def maximum(numbers):
    return max(numbers) if numbers else None

# Example:
maximum([5, 6, 3, 7]) #-> 7
maximum([17, 15, 19, 11, 2]) #-> 19
maximum([]) #-> None