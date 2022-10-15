people = [
    {"name":"Marcus", "house":"hufflepuff"},
    {"name": "Hermione", "house":"Griffindor"},
    {"name": "Harry", "house":"Grinffondor"},
    {"name": "Grinny", "house":"Slytherin"},
]

people.sort(key = lambda person : person["name"])

print(people)