# FOR loops

# for loop uses  iterable objects
string1 = 'my_str'
print('Strings have __iter__ method:', dir(string1))
print('__iter__ method returns on object of type:', type(string1.__iter__()))
print('Iterators have __next__ method', dir(string1.__iter__()))
print()

# Next for iterable objects
iterator = string1.__iter__()
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
# Iterators are consumed and if we were to call it again it would give us StopIteration error
# print(iterator.__next__())
print()

# We can't iterate objects that do not have the __iter__ method like integers
# my_int = 123
# for i in my_int:
#     print(i)
# print()

# for will iterate through each letter
print('#' * 80)
for letter in 'my_text':
    print(letter)
print('#' * 80)

# compare string objects
nr_of_a = ord('a')
print(f'Number of letter a: {nr_of_a}')
nr_of_b = ord('b')
print(f'Number of letter b: {nr_of_b}')

# The character code (number) is used for comparison
message1 = 'check if a {} b using {} operator:'
message2 = 'check if a {} b using {} method:'

print(message1.format('equal to', '==', ), 'a' == 'b')
print(message2.format('equal to', '__eq__'), 'a'.__eq__('b'))

print(message1.format('less or equal to', '<='), 'a' <= 'b')
print(message2.format('less or equal to', '__le__'), 'a'.__le__('a'))

print(message1.format('less then', '<'), 'a' < 'b')
print(message2.format('less then', '__lt__'), 'a'.__lt__('b'))

print(message1.format('grater or equal to', '>='), 'a' >= 'b')
print(message2.format('grater or equal to', '__ge__'), 'a'.__ge__('b'))

print(message1.format('grater then', '>'), 'a' > 'b')
print(message2.format('greater then', '__gt__'), 'a'.__gt__('a'))

# To compare that two objects are the same object and not that they have the same value we use is keyword
message3 = 'check if a {} b using {} keyword:'
a = 'a'
b = 'b'
print(message3.format('is', 'is'), a is b)
print(message3.format('is not', 'is'), a is not b)
print()

# Using break keyword to exit for loops
print('#' * 80)
for i in 'my_text':
    if '_' == i:
        break
    else:
        print(i)
print('#' * 80)
print()

# Using the else condition in for loops.
# Print message if _ not in text
var1 = ''
for i in 'my text':  # my_text
    if '_' == i:
        var1 = '_'
if var1 != '_':
    print(f'The char {var1} is present in text')
print()

# Print message if _ not in text using else statement in for loops
for i in 'my text':  # my_text
    if '_' == i:
        break
else:
    print(f'The char _ is present in text')
print()

# len function is used to determine the length of iterable objects
print('The length of "my_text" using len function is:', len('my_text'))
print('The length of "my_text" using __len__ method is:', 'my_text'.__len__())
print()

# Exercise using conditions with nested for
print('#' * 80)
text = 'my_text'
if len(text) > 3:
    for letter in text:
        var = letter
    print('The variable used in for loop has has the last letter, why?', letter)
print('#' * 80)
print()

# The continue keyword for the for loop
# Remove space from text
print('#' * 80)
text = 'my text'
new_text = ''
for letter in text:
    if letter == ' ':
        continue
    new_text = new_text + letter
print(new_text)
print('#' * 80)
print()

# WHILE loops
print(' WHILE loops '.center(80, '#'))
number = 6
while number > 2:
    if number > 4:
        number = number - 1
        print('Number on if branch is:', number)
    else:
        number = number - 1
        print('Number on else branch is:', number)
print('#' * 80)
print()

# Exercise: read letters from input while value is smaller then 100
print('#' * 80)
while True:
    nr = int(input('Provide number: '))
    if nr > 100:
        break
print(f'The number is less then 100: {nr}')
print('#' * 80)

# Exercise: create new strings from first 5 letters
my_text = 'my_text'
new_text = ''
index = 0
while len(new_text) < 5:
    new_text = new_text + my_text[index]
    index += 1
else:
    print(f'New string from first 5 letters is: {new_text}')
print()

# The range function
print(' The range function '.center(80, '#'))
range_object = range(3)
print('Range functions returns object of type:', type(range_object))
range_iter = range_object.__iter__()
print('Range iterator can be iterated using next:', dir(range_iter))
print('next object in range:', next(range_iter))
print('next object in range:', next(range_iter))
print('next object in range:', next(range_iter))
# print(next(range_iter))
print('#' * 80)
print()


for i in range(3):
    print('range in for:', i)

for i in range(2, 6):
    print('range in for with step 1:', i)

for i in range(2, 6, 2):
    print('range in for with step 2:', i)

# Assigment operators
print(' Assigment operators '.center(80, '#'))
var1 = 1
print(var1)
var1 += 2  # this is equivalent with (var1 = var1 + 1 )
print(var1)
var1 *= 3
print(var1)
var1 /= 3
print(var1)
var1 **= 3
print(var1)
