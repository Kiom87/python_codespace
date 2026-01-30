# Write a function `remove_last_vowel` that accepts a string as an argument.
# The function should return the string with its last vowel removed.
# Vowels are the letters: a, e, i, o, u


def remove_last_vowel(s):
    vowels = "aeiouAEIOU"
    # Traverse from end to start to find the last vowel
    for i in range(len(s) - 1, -1, -1):
        if s[i] in vowels:
            return s[:i] + s[i+1:]
    return s  # return original if no vowel found

print(remove_last_vowel("speaker"))# 'speakr'
print(remove_last_vowel("trading"))# 'tradng'
print(remove_last_vowel("thunder"))# 'thundr'
print(remove_last_vowel("myth"))# 'myth'


