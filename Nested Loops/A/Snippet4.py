locations = ["flatbush", "williamsburg", "bushwick", "greenpoint"]

for i in range(len(locations)):
    for j in range(i + 1, len(locations)):
        print(locations[i], locations[j])

