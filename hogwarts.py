"""
dictionary - key value pairs
"""
students = [
    {"name": "hermione", "house": "gryffindor", "patronus": "otter"},
    {"name": "harry", "house": "gryffindor", "patronus": "stag"},
    {"name": "ron", "house": "gryffindor", "patronus": "rat"},
    {"name": "draco", "house": "slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")