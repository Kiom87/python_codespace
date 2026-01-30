

def word_replace(text, replacements):
    words = text.split()
    new_words = []
    
    for w in words:
        # Replace the word only if it's an exact match
        if w in replacements:
            new_words.append(replacements[w])
        else:
            new_words.append(w)
    
    return " ".join(new_words)







print(word_replace(
"I never take naps during the day",
    {"never":"always","day":"weekend" }
))
# 'I always take naps during the weekend'

print(word_replace(
"the park is closed",
    {"closed":"open","the":"a" }
))
# 'a park is open'

print(word_replace(
"I do what I want",
    {"I":"we","cat":"dog" }
))
# 'we do what we want'

