# Write a function `strings_to_lengths(strings)` that accepts a list of strings.
# The function should return a new list containing the lengths of each string.

def strings_to_lengths(strings):
    new_list = []  #Initializes an empty list called new_list.
                   #This will store the lengths of each string from the input list
    for n in strings:#Starts a loop that iterates over each element in strings.
                     #On each iteration, s is a single string from the list (e.g., "hello" on the first pass).
        
        new_list.append(len(n))#Calculates the length of the current string s using len(s) (e.g., len("hello") is 5).
                               #Appends that length to new_list
    return new_list #Returns the completed list of lengths.
                    #At this point, new_list contains one integer per input string, in the same order as the input.

# Example:
strings_to_lengths(["belly", "echo", "irony", "pickled"]) #-> [5, 4, 5, 7]
strings_to_lengths(["on", "off", "handmade"]) #-> [2, 3, 8]

#PYTHONIC Alternative
def strings_to_lengths(strings):
    return [len(s) for s in strings]

strings_to_lengths(["belly", "echo", "irony", "pickled"]) #-> [5, 4, 5, 7]
strings_to_lengths(["on", "off", "handmade"]) 