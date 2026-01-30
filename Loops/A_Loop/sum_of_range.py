

def sum_of_range(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    print(total)


#1 =sum + num = 0 + 1 = 1 
#2 = 1 + 2 = 3
#3 = 3 + 3 = 6
#4 = 6 + 4 = 10
#5 - 10 + 5 = 15

sum_of_range(5)
# prints: 15


def sum_of_range(n):
    total = n * (n + 1) // 2
    print(total)

# Example usage:
sum_of_range(5)  # prints: 15
