cat1 = {"name":"jinkee","breed":"calico" }
cat2 = {"name":"garfield","breed":"red tabby" }

def key_pair(c1, c2, key):
    

    
    return [c1[key], c2[key]]


print(key_pair(cat1, cat2,"breed"))
# ['calico', 'red tabby']

print(key_pair(cat1, cat2,"name"))
# ['jinkee', 'garfield']

