# Write a function `product_up_to(max_num)` that returns the product of all numbers
# from 1 to max_num inclusive. (1*2*3*...*max_num)

def product_up_to(max_num):
    product = 1
    for i in range(1, max_num + 1):
         product *= i
    return print(product)

# Example:
product_up_to(4) #-> 24
product_up_to(5) #-> 120
product_up_to(7) #-> 5040
product_up_to(10) #-> 3628800
product_up_to(20) #-> 2432902008176640000
