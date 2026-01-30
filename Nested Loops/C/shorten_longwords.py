# Write a function `shorten_long_words(sentence)` that accepts a string and returns
# the same sentence where words longer than 4 characters have their vowels removed.


def shorten_long_words(sentence: str) -> str:
    vowels = set("aeiouAEIOU")
    result = []
    word = []

    def flush_word():
        # Process the current buffered word (letters only)
        if not word:
            return
        w = "".join(word)
        if len(w) > 4:
            # Remove vowels
            processed = "".join(ch for ch in w if ch not in vowels)
        else:
            processed = w
        result.append(processed)
        word.clear()

    for ch in sentence:
        if ch.isalpha():
            word.append(ch)
        else:
            # Non-letter encountered: flush current word, then add the character
            flush_word()
            result.append(ch)

    # Flush any remaining word at the end
    flush_word()

    return "".join(result)


# Example usage:
print(shorten_long_words("they are very noble people"))  # 'they are very nbl ppl'
print(shorten_long_words("stick with it"))               # 'stck with it'
print(shorten_long_words("ballerina, you must have seen her"))  # 'bllrna, you must have seen her'


# Example usage:
print(shorten_long_words("they are very noble people"))  # 'they are very nbl ppl'
print(shorten_long_words("stick with it"))  # 'stck with it'
print(shorten_long_words("ballerina, you must have seen her"))  # 'bllrna, you must have seen her'
