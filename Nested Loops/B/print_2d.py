# Write a function `print2d(matrix)` that accepts a 2D list and prints all inner elements.


array1 = [
    ["a", "b", "c", "d"],
    ["e", "f"],
    ["g", "h", "i"]
]

def print2d(matrix):
    for row in matrix:
        for el in row:
        
           print(el)




print2d(array1)
# prints:
# a
# b
# c
# d
# e
# f
# g
# h
# i

array2 = [[9, 3, 4], [11], [42, 100]]
print2d(array2)
# prints:
# 9
# 3
# 4
# 11
# 42
# 100


