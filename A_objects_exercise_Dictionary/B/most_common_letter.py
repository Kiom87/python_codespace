

def most_common_letter(string):
    count = {}
    for ch in string:
        count[ch] = count.get(ch, 0) + 1
            
    max_count = max(count.values())
    for ch in string:
        if count[ch] == max_count:
            return ch







print(most_common_letter("building"))
# 'i'

print(most_common_letter("shoestring"))
# 's'

print(most_common_letter("preparedness"))
# 'e'

