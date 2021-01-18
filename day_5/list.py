# Day 5

empty_list = [] # empty list can be also declared as list()

space_companies = ['SpaceX', 'ISRO', 'NASA', 'Blue Origin', 'Rocket Lab']

number_of_space_companies = len(space_companies)
print(number_of_space_companies)

first_item = space_companies[0]
print(first_item)

middle_item_index = int(number_of_space_companies / 2)
middle_item = space_companies[middle_item_index]
print(middle_item)

last_item = space_companies[number_of_space_companies - 1]
print(last_item)

mixed_data_types = ['Karthick Sabari', 23, 'single', 'Oasis']

it_companies = ['Google', 'Microsoft', 'Apple', 'IBM', 'Amazon', 'Oracle']
print(it_companies)

number_of_it_companies = len(it_companies)
print(number_of_it_companies)

first_company = it_companies[0]
print(first_company)

middle_company_index = int(number_of_it_companies / 2)
middle_company = it_companies[middle_company_index]
print(middle_company)

last_company = it_companies[number_of_it_companies - 1]
print(last_company)

it_companies[3] = 'OFS'
print(it_companies)

it_companies.append('IBM')

it_companies[middle_company_index] = 'Tesla'

it_companies[0].upper()

companies = '# '.join(it_companies)

print('Google' in it_companies)

print(it_companies.sort())
print(it_companies.sort(reverse=True))

print(it_companies[0:3])

print(it_companies[-3:])

del it_companies[0]

it_companies.pop()

it_companies.clear()

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
end_to_end = front_end.extend(back_end)
print(end_to_end)

full_stack = end_to_end.copy()
