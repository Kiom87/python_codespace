# Write a function `sum_up_to(max_num)` that returns the sum of all whole numbers
# from 1 to max_num inclusive.

def sum_up_to(max_num):
    
    return sum(range(1, max_num + 1 ))
        
        


# Example:
print(sum_up_to(4))  #-> 10
print(sum_up_to(5))  #-> 15
print(sum_up_to(2))  #-> 3

