# Write a function `remove_first_vowel(s)` that accepts a string and returns the string
# with its first vowel removed.


def remove_first_vowel(s):
    vowels = "aeiouAEIOU"
    for i, ch in enumerate(s):
        if ch in vowels:
            return s[:i] + s[i+1:]
    return s  # return unchanged if no vowel found


# Example usage:
print(remove_first_vowel("volcano"))  # 'vlcano'
print(remove_first_vowel("celery"))  # 'clery'
print(remove_first_vowel("juice"))  # 'jice'

