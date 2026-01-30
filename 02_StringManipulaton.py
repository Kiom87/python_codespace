#String Indexing
s = "PYTHON"

#Positive Indexing
print(s[0]) #P
print(s[3]) #H
print(s[5]) #N

#Negative Indexing
print(s[-1]) #N

print(s[-3]) #H

print(s[-4]) #T

a = "some long word hello world"

#Positive Indexing

print(a[5]) #l
print(a[7]) #n
print(a[10]) #w
print(a[15]) #h

#Negative Indexing
print(a[-1]) #d
print(a[-5]) #w
print(a[-10]) #e

#String Slicing
#Rules
#start : included
#end : excluded
#step : jump size

b = "PYTHON"

print(b[0:3]) #PYT(0,1,2)
print(b[2:5]) #THO(2,3,4)
print(b[:4]) #PYTH(from start) 
print(b[3:]) #HON(From Current Till End)

#Step Slicing
print(b[0:6:1]) #PYTHON(Increment/Step is 1)
print(b[0:6:2]) #PTO(Increment/Step is 2)
print(b[0:6:3]) #PH(Increment/Step is 3)

m = "some long word hello world"

reverse = m[::-1]

print(reverse)

reverse = m[::-2]

print(reverse)

reverse = m[::-3]

print(reverse)

reverse = m[1::]

print(reverse)



reverse = m[2::]

print(reverse)

list = ['some', 'long']

ans = list[0]

rev = ans[::-1]

print (rev)
print("hello"[::-1])     # olleh
print("devtech"[::-1])   # hcetved




text = "Hello Python!"

print(text.upper())
print(text.lower())
print(text.capitalize())
# Hello python!
print(text.title())
# Hello Python(Caps First letter of each word)!


#Strip(Remove spaces)
msg = "   Python  "
print(msg.strip())
# Python
print(msg.lstrip())
# Python
print(msg.rstrip())
#    Python

t = "Hello Python!"

arr = t.split(" ")
print(arr)

for word in arr:
    print(word)

print(t.find("Python"))
#return length of the string


print(s.find())

ec = "Hello Python"

encode = ec.encode("utf-8")
print(encode)

decode = encode.decode("utf-8")
print(decode)

#replace
s = "I love Java"
print(s.replace("Java", "Python"))
# I love Python

#Split and Join
sentence = "apple,banana,mango"
print(sentence.split(","))
# ['apple', 'banana', 'mango']

#Join
items = ["a", "b", "c"]
print("-".join(items))
# a-b-c

#find and count

print(text.find("Python"))
# 6

print("banana".count("a"))
# 3

#Check Methods (Boolean Methods)
#isalpha()
print("Hello".isalpha())
# True

#isdigit()
print("12345".isdigit())
# True

#isnumeric
print("⑦".isnumeric())
# True (for numeric symbols)


#isalnum(letters + numbers)
print("Hello123".isalnum())
# True


print("HELLO".isupper())  # True
print("hello".islower())  # True

#Decoding and Encoding

#encode
text = "Hello Python"
encoded = text.encode("utf-8")
print(encoded)
# b'Hello Python'

#Decode
decoded = encoded.decode("utf-8")
print(decoded)
# Hello Python

msg = "नमस्ते"   # Nepali/Hindi text
enc = msg.encode("utf-8")
print(enc)        # b'\xe0\xa4\xa8...'

dec = enc.decode("utf-8")
print(dec)        # नमस्ते

#startswith() & endswith()
filename = "photo.png"

print(filename.startswith("photo"))  # True
print(filename.endswith(".png"))     # True

#Format Strings
name = "Dev"
age = 25
print(f"My name is {name} and I am {age} years old.")

print("Hello, {}".format("Python"))



#Reversing a String
s = "Python"
print(s[::-1])
# nohtyP



#Complete Example 
text = "  I Love Python Programming  "
t = "I,Love,Python,Programming"

print(text.upper())
print(text.lower())
print(text.title())
print(text.strip())
print(text.replace("Python", "Java"))
print(text.split())
print("-".join(["A","B","C"]))
print(text.count("o"))
print(text.startswith(" I"))
print(text.endswith("ing"))
print(text.encode("utf-8"))
print(text[::-1])






