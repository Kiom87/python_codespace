def max_object_value(obj):
    max_key = max(obj, key=obj.get)
    return [max_key, obj[max_key]]

print(max_object_value({"a":5,"b":2,"c":6,"d":7,"e":4 }))
# ['d', 7]

print(max_object_value({"lychee":11,"rambutan":13,"papaya":9 }))
# ['rambutan', 13]
