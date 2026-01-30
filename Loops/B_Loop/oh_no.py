# Write a function `no_ohs(text)` that prints each character of the string except 'o'.
# The function does not return a value, just prints.

def no_ohs(text):
    for char in text:
        if char != 'o': #If the character is not 'o', we print it.

           print(char)

 

# Example:
no_ohs("code")
# c
# d
# e


def no_as(text):
    for char in text:
        if char != 'a':
            print(char)

no_as("abracadabra")

#b
#r
#c
#d
#b
#r

def no_space(text):
    for char in text:
        if char != ' ':
            print(char)


no_space("I Love Python")