# Write a function `remove_capitals(text)` that returns a new string with all
# capital letters removed.

def remove_capitals(text: str ) -> str:
    return ''.join(ch for ch in text if not ch.isupper())

# Example:
remove_capitals("fOrEver")     #-> 'frver'
remove_capitals("raiNCoat")    #-> 'raioat'
remove_capitals("cElLAr Door") #-> 'clr oor'

