
# Write a function `trendy_text` that accepts a sentence string as an argument.
# The function should return the sentence where the last vowel of every word
# is removed.


def trendy_text(sentence):
    vowels = "aeiouAEIOU"
    words = sentence.split()
    result_words = []

    for word in words:
        # find last vowel index
        last_vowel_index = -1
        for i in range(len(word)-1, -1, -1):
            if word[i] in vowels:
                last_vowel_index = i
                break
        
        # remove the last vowel if found
        if last_vowel_index != -1:
            word = word[:last_vowel_index] + word[last_vowel_index+1:]
        
        result_words.append(word)

    return " ".join(result_words)



print(trendy_text("the concert will be epic"))
# 't
# 
# 
# 
# 
# letth concrt wll be epc'

print(trendy_text("breakfast food is wonderful"))
# 'breakfst fod s wonderfl'

print(trendy_text("the weather will improve hopefully"))
# 'th weathr wll improv hopeflly'

