# Write a function `reverse_iterate(text)` that prints each character of the string
# in reverse order. The function does not return a value, just prints.


def reverse_iterate(text):
    for i in range(len(text) -1, -1, -1):
        print(text[i]) 
# Example:
reverse_iterate("carrot")
# t
# o
# r
# r
# a
# c

reverse_iterate("box")
# x
# o
# b

#Option 2

def reverse_iterate(text):
    for ch in reversed(text):
        print(ch)

reverse_iterate("socks")
# s
# k
# c
# o
# s

#Option 3


def reverse_iterate(text):
    for ch in text[::-1]:
        print(ch)

reverse_iterate("tie")
# e
# i
# t