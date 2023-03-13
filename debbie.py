Languages=['Javascript','Python', 'dart' ]

print(Languages[2])

Languages[2]='CSS'

print(Languages[2])

#a list can have a number of different data types e.g
#my_list[1, 'Hello', 3.4]

#negative indexing in python
Languages=['Javascript','Python', 'dart' ]
print(Languages[2])
print(Languages[-1])

#slicing of python list
my_list=['p', 'r', 'o', 'g', 'r', 'a', 'm', 'l']

print(my_list[2:5])
print(my_list[5:])
print(my_list[:])

#adding elements to a python list
numbers=[21,34,45,12]
print('Before Append:', numbers)

numbers.append(32)

print('After Append:', numbers)

prime_numbers=[2,3,4]
print('List1:', prime_numbers)

even_numbers=[4,6,8]
print('List2:', even_numbers)

prime_numbers.extend(even_numbers)

print('List after append:', prime_numbers)

#removing an item from a list
Languages=['Javascript','Python', 'dart' ]

del Languages[1]
print(Languages)

Languages.remove('Javascript')
print(Languages)

#iterating through a list
Languages=['Javascript','Python', 'dart' ]
for Language in Languages:
    print(Language)

Languages=['Javascript','Python', 'dart' ]
print('c' in Languages)
print('Python' in Languages)

#python list strength
Languages=['Javascript','Python', 'dart' ]
print('List:', Languages)
print('Total Elements:', len(Languages))

#python list comprehension
numbers=[numbers*numbers for numbers in range(1,6)]
print(numbers)
