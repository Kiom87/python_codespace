# Write a function `lengthiest_word(sentence)` that accepts a string containing a sentence.
# The function should return the longest word in the sentence.
# If there is a tie, return the word that appears later in the sentence.
def lengthiest_word(sentence):
    list_words = sentence.split(" ")
     
    long_word = ""

    for word in list_words:
        if len(word) >= len(long_word):
           long_word = word
    print(long_word)
    

# Example:
lengthiest_word("I am pretty hungry")# -> 'hungry'
lengthiest_word("we should think outside of the box")# -> 'outside'
lengthiest_word("down the rabbit hole")# -> 'rabbit'
lengthiest_word("simmer down")# -> 'simmer'

