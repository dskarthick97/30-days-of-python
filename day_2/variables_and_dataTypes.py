# Day 2 - Level 1

first_name = 'Karthick'
last_name = 'Sabari'
full_name = 'Karthick Sabari'
country = 'India'
city = 'Chennai'
age = 23
year = 2021
is_married = False
is_true = True
is_light_on = True
action_movie, thriller_movie, sci_fi_movie = 'Extraction', 'Don\'t Breathe', 'The Matrix'

# Level 2

# checking the data type of the assigned variables
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

length_of_first_name = len(first_name)
length_of_last_name = len(last_name)

print(length_of_first_name)

print(length_of_first_name == length_of_last_name)

num_one, num_two = 5, 4
_total = 5 + 4
_diff = 5 - 4
_product = 5 * 4
_division = 5 / 4
_remainder = 5 % 4
_exp = 5 ** 4
_floor_division = 5 // 4

radius = 30
area_of_circle = 3.14 * ((radius) ** 2)
circum_of_circle = 2 * 3.14 * radius
print(area_of_circle)
print(circum_of_circle)

user_radius = input('Provide the radius of the circle: ')
actual_radius = int(user_radius)
area_of_circle = 3.14 * ((actual_radius) ** 2)
print('Area of the circle is: ', area_of_circle)

first_name = input('Provide your first name: ')
print(first_name)
last_name = input('Provide your last name: ')
print(last_name)
age = input('Provide your age: ')
print(age)
country = input('Provide your country: ')
print(country)
