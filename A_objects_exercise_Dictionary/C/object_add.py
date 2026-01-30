obj1 = {"x":3,"y":10 }
obj2 = {"y":2,"x":1 }

def object_add(o1, o2):
    result = {}

    for key in o1:
        result[key] = o1[key]

    for key in o2:
        if key in result:
            result[key] += o2[key]
        else:
            result[key] = o2[key]
    return result
    
print(object_add(obj1, obj2))
# { "x": 4, "y": 12 }


obj3 = {"a":3,"b":2,"c": -1 }
obj4 = {"b":5,"c":1,"e":4 }

print(object_add(obj3, obj4))
# { "a": 3, "b": 7, "c": 0, "e": 4 }

