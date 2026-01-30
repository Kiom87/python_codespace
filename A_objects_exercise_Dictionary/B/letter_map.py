def letter_map(string, dic):#string: the input text you want to transform.#dic: a dictionary that maps characters to their replacements.



    new_str = ""#Initializes an empty string called new_str.

    for ch in string:#Loops through each character ch in the input string, from left to right.##If string is "colossal", then ch will be: 'c', 'o', 'l', 'o', 's', 's', 'a', 'l' (one at a time).

        if ch in dic:#Checks whether the current character ch has a replacement defined in your dictionary dic.

            new_str += dic[ch]#If there is a mapping, append the replacement character (i.e., dic[ch]) to new_str.
                              #Example: if ch is 'o' and dic["o"] is 'x', this appends 'x'.
        else:#If the character isn’t in the dictionary (i.e., no replacement defined), do the fallback behavior.
            new_str += ch#Append the original character unchanged to new_str.




    return new_str #After the loop finishes (you’ve processed every character), return the fully built result string.








print(letter_map("symbolic", {"y":"i","o":"a","c":"k" }))
# 'simbalik'

print(letter_map("colossal", {"o":"x","s":"p" }))
# 'cxlxppal'

print(letter_map("miniscule", {"u":"t","i":"f","e":"q" }))
# 'mfnfsctlq'

