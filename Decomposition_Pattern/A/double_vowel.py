def double_vowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for ch in string:            # double the vowel
        if ch in vowels:
            result.append(ch * 2)
        else:
            result.append(ch)
    
    return ''.join(result)




print(double_vowel("runner"))
# 'ruunneer'

print(double_vowel("stoplight"))
# 'stoopliight'

print(double_vowel("gardener"))
# 'gaardeeneer'

