# Day 5
# Level 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages)

# finding mininum and maximum age
minimum_age = min(ages)
ages.append(minimum_age)
maximum_age = max(ages)
ages.append(maximum_age)
print('List after adding the minimum and maximum age:', ages)

# finding the median age
length = len(ages)
median = length / 2
print('Median age:', median)

# finding the average age
total = sum(ages)
average = total / length
print('Average of ages:', average)

# finding the range of ages
range = maximum_age - minimum_age
print('The range of ages:', range)
