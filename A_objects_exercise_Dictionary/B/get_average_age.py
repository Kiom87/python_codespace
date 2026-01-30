
def get_average_age(people):
    total_age = 0
    count = 0

    for person in people:
        age = person["age"]

        total_age += age

        count += 1

        average = total_age / count
    return round(average, 2)






peeps = [
    {"name":"Lovelace","age":36,"born":"London, UK" },
    {"name":"Kleene","age":85,"born":"Connecticut, US" },
    {"name":"Turing","age":41,"born":"London, UK" },
    {"name":"Hopper","age":85,"born":"New York, US" },
]

print(get_average_age(peeps))
# 61.75


people = [
    {"name":"Orwell","age":46,"born":"Bihar, India" },
    {"name":"Bradbury","age":91,"born":"California, US" },
    {"name":"Huxley","age":69,"born":"California, US" },
]

print(get_average_age(people))
# 68.67
