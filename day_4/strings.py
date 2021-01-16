# Day 4

thirty_days_of_python = 'Thirty ' 'days ' 'of ' 'python' # one way to concatenate strings
print(thirty_days_of_python)

coding_for_all = 'Coding ' 'for ' 'all'
print(coding_for_all)

company = 'Coding For All'
print(company)

print(len(company))

print(company.upper())

print(company.lower())

print(company.capitalize())
print(company.title())
print(company.swapcase())

print(company[0:6])

sub_string = 'Coding'
print(company.index(sub_string))
print(company.find(sub_string))

print(company.replace('Coding', 'Python'))

print(company.split())

tech_companies = 'Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(tech_companies.split(', '))

print(company[0])

print(company[-1])

print(company[10])

# abbrevation for 'Python For Everyone' and 'Coding For All'
python_for_everyone = 'Python For Everyone'
split_python = python_for_everyone.split()
P = split_python[0][0]
F = split_python[1][0]
E = split_python[2][0]
abbrevation1 = f'{P}{F}{E}'
print(abbrevation1)

company_split = company.split()
C = company_split[0][0]
F = company_split[1][0]
A = company_split[2][0]
abbrevation2 = f'{C}{F}{A}'
print(abbrevation2)

print(company.index('C'))
print(company.index('F'))
print(company.rfind('l'))

simple_sentence = 'You cannot end a sentence with because because because is a conjunction'
print(simple_sentence.find('because'))
print(simple_sentence.rindex('because'))

print(simple_sentence[31:54])

print(company.startswith('Coding'))

print(company.endswith('coding'))

another_company = '   Coding For All       '
print(another_company.strip())

first_identifier = '30DaysOfPython'
print(first_identifier.isidentifier())
second_identifier = 'thirty_days_of_python'
print(second_identifier.isidentifier())

python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(python_libraries))

print('I am enjoying this challenge.\nI wonder what is next')

print('Name\tAge\tCountry')
print('Karthick\t23\tIndia')

radius = 10
area = 3.14 * radius ** 2
print(f'The area of the circle with {radius} is {area}')

eight = 8
six = 6
print(f'{eight} + {six} = {eight + six}')
print(f'{eight} - {six} = {eight - six}')
print(f'{eight} * {six} = {eight * six}')
print(f'{eight} / {six} = {eight / six}')
print(f'{eight} % {six} = {eight % six}')
print(f'{eight} // {six} = {eight // six}')
print(f'{eight} ** {six} = {eight ** six}')
