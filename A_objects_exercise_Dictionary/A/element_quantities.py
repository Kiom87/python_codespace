quantities1 = {"cat":3,"bird":1,"dog":2 }

def element_quantities(d):
    result = []
    for key, count in d.items():
        result.extend([key] * count)
    return result

print(element_quantities(quantities1))
# ['cat', 'cat', 'cat', 'bird', 'dog', 'dog']

quantities2 = {"blue":3,"brown":1 }
print(element_quantities(quantities2))
# ['blue', 'blue', 'blue', 'brown']



def element_quantities(d):
    return [key for key, count in d.items() for _ in range(count)]

quantities2 = {"blue":3,"brown":1 }
print(element_quantities(quantities2))
# ['blue', 'blue', 'blue', 'brown']