# Write a function `alternating_caps(sentence)` that accepts a string containing a sentence.
# The function should return the sentence where words alternate between lowercase and uppercase.

def alternating_caps(sentence):
    list_words = sentence.split(" ")
    new_sentence = []

    for i in range(len(list_words)):
        word = list_words[i]
        if i % 2 == 0:
            new_sentence.append(word.lower())
        else:
            new_sentence.append(word.upper())
    print(" ".join(new_sentence))
# Example:
alternating_caps("take them to school") #-> 'take THEM to SCHOOL'
alternating_caps("What did ThEy EAT before?") #-> 'what DID they EAT before?'

