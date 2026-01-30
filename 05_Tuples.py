#A tuple is an ordered, immutable collection of items in Python.\
#It is Immutable

numbers = (10, 20, 30)
data = ("Dev", 25, True)
print(data)

#2. Why Tuples Are Important
#- **Immutable** → cannot be changed
# **Faster** than lists
#- **Safer** for fixed data
#- **Memory efficient**
#- Good for **constants**, **coordinates**, **database records**,

#Tuple Creation Examples
#Normal tuple
t = (1, 2, 3)

#Tuple with different types

info = ("Dev", 22, "Nepal", True)

#Single-element tuple (important!)
x = (10,)  # comma required

#Tuple without parenthesis (packing)
t = 1, 2, 3

#Packing & Unpacking
#Packing
t = 1, 2, 3

#Unpacking
a, b, c = t
print(a, b, c) # 1 2 3  # 1 2 3

#Extended Unpacking
a, *b = (1, 2, 3, 4, 5)
print(a)  # 1
print(b)  # [2, 3, 4, 5]

#Indexing in Tuples

t = (10, 20, 30, 40)

print(t[0])   # 10
print(t[-1])  # 40
print(t[2])   # 30


#Slicing Tuples

t = (10, 20, 30, 40, 50)

print(t[1:4])     # (20, 30, 40)
print(t[:3])      # (10, 20, 30)
print(t[::2])     # (10, 30, 50)


#Immutability(Cannot Modify tuple)

t = (1, 2, 3)
t[0] = 10   # Error: TypeError


#Allowed Tuple Manipulation (since tuple is immutable)
#Concatenation
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)
# (1, 2, 3, 4)

#Repetition
print((1, 2) * 3)
# (1, 2, 1, 2, 1, 2)

#Check element exists
t = (1, 2, 3)
print(2 in t)  # True

#Count Elelments
print((1,2,2,3).count(2)) #2  # 2

#Find Index
print((10, 20, 30).index(20))  # 1

#When To Use Tuples(Real-World Use Cases)

#1. Fixed Data (constants)
days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
print(days)

#GPS Coordinates (x, y, z)
location = (27.7172, 85.3240)

#Database Records
record = (101, "Dev", "Nepal", 22)

#4. Return multiple values from a function

def calculate(a, b):
    return a + b, a * b   # returns tuple

sum_val, prod_val = calculate(5, 10)

#✔ 5. Dictionary keys (only immutable types allowed)

my_dict = {
    (1, 2): "Point A"
}

#Example Program

# tuple basics
t = (10, 20, 30, 40)

print("First element:", t[0])
print("Slice:", t[1:3])
print("Concatenation:", t + (50, 60))
print("Count of 20:", t.count(20))
print("Index of 30:", t.index(30))

# unpacking
a, b, c, d = t
print("Unpacked:", a, b, c, d)











