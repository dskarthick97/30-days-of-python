# Day 6

empty_tuple = ()

brothers = ('karthick', 'sabari', 'dhilip', 'sudhakar')
sisters = ('deepika', 'karthika')
siblings = brothers + sisters
print('Siblings:', siblings)

number_of_siblings = len(siblings)
print('Number of siblings:', number_of_siblings)

list_of_siblings = list(siblings)
parents = ['dhilip', 'eeswari']
list_of_siblings.extend(parents)
family_members = tuple(list_of_siblings)
print('My family members:', family_members)

# unpacking siblings and parents from family_members
siblings = family_members[0:6]
print('Unpacked siblings from family_members:', siblings)
parents = family_members[6:]
print('Unpacked parents from family_members:', parents)

fruits = ('apple', 'orange', 'banana')
vegetables = ('onion', 'tomato', 'potato')
animal_products = ('chicken', 'mutton', 'fish', 'prawn')
food_stuff_tp = fruits + vegetables + animal_products
print('Food stuffs:', food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)
print('List of food stuffs:', food_stuff_lt)

middle_item = int(len(food_stuff_lt) / 2)
print(food_stuff_lt[middle_item])

first_three_items = food_stuff_lt[0:3]
print('First three items from food stuff list:', first_three_items)
last_three_items = food_stuff_lt[-3:]
print('Last three items from food stuff list:', last_three_items)

food_stuff_tp = tuple(food_stuff_lt)
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
