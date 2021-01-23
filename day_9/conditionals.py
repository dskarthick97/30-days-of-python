# Day 9

# Q1
age = int(input('Enter your age: '))
remaining_age = 18 - age

if age > 0:
    if age >= 18:
        print('You are old enough to drive')
    else:
        print(f'You need {remaining_age} more years to learn to drive') 
else:
    print('Invalid age')

# Q2
your_age = age
someones_age = int(input('Enter someone\'s age: '))

if your_age and someones_age > 0:
    age_difference = abs(your_age - someones_age)
    
    if your_age is someones_age:
        print('You both are at the same age!')
    elif age_difference is 1:
        if your_age > someones_age:
            print('You are one year older than him/her')
        else:
            print('You are one year younger than him/her')
    else:
        if your_age > someones_age:
            print(f'You are {age_difference} years older than him/her')
        else:
            print(f'You are {age_difference} years younger than him/her')
else:
    print('Invalid age')

# Q3
a = int(input('Enter a number: '))
b = int(input('Enter another number: '))

if a and b > 0:
    if  a > b:
        print('a is greater than b')
    elif a < b:
        print('a is less than b')
    else:
        print('a is equal to b')
else:
    print('Enter number greater than 0')

# Q4
score = int(input('Enter your score: '))

if score > 80:
    print('Your grade is A')
elif score > 70:
    print('Your grade is B')
elif score > 60:
    print('Your grade is C')
elif score > 50:
    print('Your grade is D')
else:
    print('Your grade is F')

# Q5
month = input('Enter the month: ')

autumn = ['September', 'October', 'November']
winter = ['December', 'January', 'February']
spring = ['March', 'April', 'May']
summer = ['June', 'July', 'August']

if month in autumn:
    print('Its autumn season')
elif month in winter:
    print('Its winter season')
elif month in spring:
    print('Its spring season')
elif month in summer:
    print('Its summer season')
else:
    print('Invalid month')

# Q6
fruit = input('Enter a fruit name: ')

fruits = ['banana', 'orange', 'mango', 'lemon']

if fruit in fruits:
    print('Fruit already exit in the list')
else:
    fruits.append(fruit)
    print('New fruit list:', fruits)

# Q7
person = {
    'first_name': 'Bruce',
    'last_name': 'Wayne',
    'age': 30,
    'is_married': True,
    'skills': ['Detective', 'Combotant', 'Weapon Specialist'],
    'country': 'Oasis',
    'city': 'Gotham',
    'address': {
        'street': 'Elm street',
        'zipcode': '7892'
    }
}

skills = person.get('skills')
if person.get('skills'):
    middle_index = int(len(skills) / 2)
    print(f'Middle skill in the skills list:', skills[middle_index])

is_married = person.get('is_married')
country = person.get('country')
full_name = person.get('first_name') + ' ' + person.get('last_name')

if is_married and country:
    print(f'{full_name} lives in {country}. He is married')
