# Day 3

age = 23

height = 6.00

complex_number = 3 + 3j

base = input('Enter the base value: ')
actual_base = int(base)
height = input('Enter the height: ')
actual_height = int(height)
area_of_triangle = 0.5 * actual_base * actual_height
print('The area of the triangle is:', area_of_triangle)

a = int(input('Enter any value for a: '))
b = int(input('Enter any value for b: '))
c = int(input('Enter any value for c: '))
print('The perimeter of the triangle is:', (a + b + c))

length = int(input('Enter the length: '))
width = int(input('Enter the width: '))
print('Area of the rectangle is:', (length * width))
print('Perimeter of the rectangle is:', (2 * (length + width)))

radius = int(input('Enter the radius: '))
print('Area of the circle is:', (3.14 * radius * radius))
print('Circumference of the circle is:', (2 * 3.14 * radius))

# Calculating the slope
x = int(input('Enter the value of x: '))
y = (2 * x) - 2
print('The slope is:', y)

# Finding the slope between two points
x1, y1 = 2, 2
x2, y2 = 6, 10

m = (y2-y1) / (x2-x1)
print('The slope between the given points is:', m)

python_length = len('python')
print('The length of the word python is', python_length)
jargon_length = len('jargon')
print('The length of the word jargon is', jargon_length)

# and statement usage
print('on' in ('python' and 'jargon'))

print('jargon' in 'I hope this course is not full of jargon')

print('on' not in ('dragon' and 'python'))

python_length = len('python')
float_value = float(python_length)
string_value = str(float_value)
print('The float value is:', float_value)
print('The string value is:', string_value)

print(type('10') is type(10))
print(int(9.8) is 10)

hours = int(input('Enter the hours: '))
rate_per_hour = int(input('Enter the rate per hour: '))
your_weekly_earning = hours * rate_per_hour
print('Your weekly earning is', your_weekly_earning)


year = int(input('Enter the number of years that you wanted to live: '))
seconds = year * 24 * 60 * 60
print('You will live for', seconds, 'seconds')
