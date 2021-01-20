#Day 7

# Given sets and a list
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

length = len(it_companies)
print('Number of IT companies in the set:', length)

it_companies.add('Twitter')
print(it_companies)

another_set_of_it_companies = {'OFS', 'ZOHO','Infosys', 'CTS', 'TCS'}
it_companies.update(another_set_of_it_companies)
print('Set of IT companies after the update:', it_companies)

it_companies.remove('Facebook')
print('IT companies after the removal of Facebook:', it_companies)

# difference between remove() and discard()
"""
remove() method raises and error if the specified element is not in the set
whereas discard() method won't raises an error
"""

print('Before the join operation between the sets:', A)
print('After joining sets:', A.union(B))  # we can also use update() to join sets

print(A.intersection(B))

print(A.issubset(B))

print(A.isdisjoint(B))

# joining A with B
print('Set B after joining A:', B.union(A))

# joining B with A
print('Set A after joining B:', A.union(B))

print(A.symmetric_difference(B))

del A
del B

length_of_list = len(age)
print('Length of List:', length_of_list)

ages = set(age)
length_of_set = len(ages)
print('Length of set:', length_of_set)
print(length_of_list is length_of_set)

sentence = 'I am a teacher and I love to inspire and teach people'
words_in_sentence = sentence.split()
print('Number of words in the sentence', len(words_in_sentence))
unique_words_in_sentence = set(words_in_sentence)
print('Unique words used in the sentence:', unique_words_in_sentence)
print('Number of unique words used in the sentence:', len(unique_words_in_sentence))
