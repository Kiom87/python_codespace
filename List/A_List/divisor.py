# Write a function `divisors(num)` that accepts a number.
# The function should return a list containing all positive numbers that divide num exactly.

def divisors(num):
    num_list = []
    for i in range(1, num + 1):
        if num % i == 0:
           num_list.append(i) 
    return num_list

# Example:
divisors(15) #-> [1, 3, 5, 15]
divisors(7) #-> [1, 7]
divisors(24) #-> [1, 2, 3, 4, 6, 8, 12, 24]

#For Larger numbers

def divisors_fast(num):
    """
    Return a sorted list of all positive divisors of num using a sqrt(n) approach.
    """
    n = abs(int(num))
    if n == 0:
        return []
    small, large = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            small.append(i)
            j = n // i
            if i != j:  # avoid duplicates when n is a perfect square
                large.append(j)
        i += 1
    return small + large[::-1]

divisors(15) #-> [1, 3, 5, 15]
divisors(7) #-> [1, 7]
divisors(24) #-> [1, 2, 3, 4, 6, 8, 12, 24]

#Simple Version

def divisors(num):
    """
    Return a list of all positive divisors of num.
    For negative inputs, uses the absolute value.
    For num == 0, returns an empty list (no positive divisors).
    """
    n = abs(int(num))
    if n == 0:
        return []  # or raise ValueError("0 has infinitely many divisors")
    return [i for i in range(1, n + 1) if n % i == 0]

divisors(15) #-> [1, 3, 5, 15]
divisors(7) #-> [1, 7]
divisors(24) #-> [1, 2, 3, 4, 6, 8, 12, 24]