def find_char_positions(text, char):
    for index, c in enumerate(text):
        if c == char:
            print(index)


find_char_positions("banana", "a")

print("*********")
find_char_positions("banana", "n")