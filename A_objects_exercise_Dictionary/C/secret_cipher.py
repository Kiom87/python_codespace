def secret_cipher(string, cipher_map):
    result = ""

    for char in string:
        if char in cipher_map:
            result += cipher_map[char]
        else:
            result += "?"
    return result

print(secret_cipher("jello", {"j":"r","l":"s","e":"i" }))
# 'riss?'

print(secret_cipher("lantern", {"e":"o","l":"p","n":"m","r":"j" }))
# 'p?m?ojm'
