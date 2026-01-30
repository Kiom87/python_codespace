#Dictionary Example

student = {
    "name": "Dev",
    "age": 22,
    "country": "Nepal"
}
print(student)

#Accessing Dictionary
print(student["name"]) #Dev
print(student["age"])

#Dictionary is Mutable
student["age"] = 23
print(student)


#Dictionary Manipulation
#Add new key
student["course"] = "Python"
print(student)

#Remove Key
student.pop('age', None)#Returns none  
print(student)
# or student.pop('age', 'N/A')

#Remove last inserted item
student.popitem() #('course', 'Python')
print(student)
#Delete key
del student["country"]
print(student)

#Clear Dictionary

student.clear()
print(student)


#Dictionary Methods

print(student.keys())
print(student.values())
print(student.items())

#Update multiple values

student.update({"name": "Ram", "age": 30})
print(student)

#Dictionary Comprehension
squares = {x: x*x for x in range(5)}
print(squares)
# {0:0, 1:1, 2:4, 3:9, 4:16}


cube = {x: x*x*x for x in range(5)}
print(cube)
## 7. **Dictionary Use Cases**

#- JSON / API data
#- Database records
# Configuration settings
#- Key-value mappings
#- User profiles / metadata


