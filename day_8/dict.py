# Day 8

dog = {}

dog['name'] = 'Daisy'
dog['color'] = 'Chocolate brown'
dog['breed'] = 'beagle pup'
dog['age'] = 6
print(dog)

student = {
    'first_name': 'Lex Luther',
    'last_name': 'Sparrow',
    'gender': 'male',
    'age': 30,
    'maritial_status': 'single',
    'skills': ['Hipnotizing', 'Swimming', 'Running'],
    'country': 'Oasis',
    'city': 'Oz',
    'address': {
        'street': 'Elm street',
        'zipcode': '7892'
    }
}

length_of_student = len(student)
print('Length of student dictionary:', length_of_student)

skills = student.get('skills')
print('Data type of skills:', type(skills))

skills.append('Sky diving')
skills.append('Cycling')
print(student)

keys = student.keys()
print('Keys of student dict:', keys)

values = student.values()
print('Values of student dict:', values)

lt_of_tp = student.items()
print('List of tuples:', lt_of_tp)

student.pop('maritial_status')
print(student)

del dog
