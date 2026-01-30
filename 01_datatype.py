print("hello world")

x = 10

y = 15

print(x + y)

# data type

x = 20

print(id(x))

x = 30

print(id(x))


nums = [5,6,8,9]

print(type(nums))

print(id(nums))

nums.append(100)

print(id(nums))

## **Immutable Data Types**

#(You cannot change the value after creation. A new object is created.)

#Integer
a = 10
print(id(a))
a = 20
print(id(a))  # different id -> new object created

#String

name = "Dev"
print(id(name))

name = "Dev Tech"
print(id(name))  # string changed → new object created

#List

nums = [1, 2, 3]
print(id(nums))

nums.append(4)
print(nums)
print(id(nums))  # same id -> changed inside same object


#int 
age = 25

#float

price = 99.99

#bool

is_active = True

#str
message = "Hello Python"

#list(mutable)
names = ["Ram", "Shyam", "Hari"]
names.append("Sita")
print(names)

#tuple (immutable)
point = (10, 20)

#dict (mutable)
student = {"name": "Dev", "age": 22}
student["age"] = 23

#set(mutable, no duplicates)
unique_numbers = {1, 2, 3, 3, 4}

#frozenset(immutable set)
fs = frozenset([1, 2, 3])

#bytes (immutable)
b = b"hello"

#bytearray (mutable)

ba = bytearray(b"hello")
ba[0] = 72   # H








