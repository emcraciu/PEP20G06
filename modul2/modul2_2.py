# Input function
print('Your first name is:', input('Enter first name:'))
my_name = input('Your last name:')
print('Your last name is:', my_name)
print()

# Input function returns strings
number1 = input('first number:')
number2 = input('second number:')
print('Sum of str is:', number1 + number2)
print()

# Casting from str to int
number1 = '2'
number2 = '3'
print('Type of number1: ', type(number1))
number1 = int(number1)
print('Type of number1: ', type(number1))
number2 = int(number2)
print('Sum of ints is:', number1 + number2)
print()

# Casting from int to str
number1 = 2
number2 = 3
print('Type of number1:', type(number1))
number1 = str(number1)
print('Type of number1:', type(number1))
number2 = str(number2)
print('Sum of strings:', number1 + number2)
print()

# Exercises -  calculate area of right angle triangle with sides provided from input
sideAB = input('Enter side AB:')
sideBC = input('Enter side BC:')
area = (int(sideAB) * int(sideBC)) / 2
print('Area is:', area)
print()

# Booleans
print('Memory location for object "True":', id(True))
true = True
print('Memory location pointed by variable "true":', id(true))
false = False
print()

# Binary operations
# And operation
result = True and True
print('Response type:', type(result), 'Value is:', result)
# Or operation
result = False or False
print('Response type:', type(result), 'Value is:', result)
# Xor operation
print('Bool operations:', dir(True))
print('True xor False:', True.__xor__(False))

# Unary operations
# Not operation
result = not True
print('Not True is: ', result)
print('Not result is: ', not result)
print()

# Order of operations (not before or)
print('not before or:', (not True) or True)
print('or before not:', not (True or True))
print('Correct result:', not True or True)
print()

# Order of operations (not before and)
print('not before and:', (not False) and False)
print('and before not:', not (False and False))
print('Correct result:', not False and False)
print()

# Order of operations (and before or) - Homework!
print(True and True or False and False)
print()

# Cast for booleans
print('String bool:', str(True), str(False))
print('Integer bool True:', int(True))
print('Integer bool False:', int(False))
print('String "false" to bool:', bool('false'))
print('String "" to bool:', bool(''))
print('Int "100" to bool:', bool(100))
print('String "0" to bool:', bool(0))
print()

# Math operations on bool objects
print('True + True + True =', True + True + True)
print('True - True - True =', True - True - True)
print()

# Object None
none = None
print('Memory location for object None', id(none), id(None))
print('actions for None:', dir(None))
print()

# Exercise - make text difficult to read
string1 = 'Text to scramble'
print('initial string:', string1)

# Rearrange odd and even letters:
string_2 = string1[0::2] + string1[1::2]
print('Rearranged string (odd and even):', string_2)

# Reverse letters:
string_2 = string1[::-1]
print('Rearranged string (reversed):', string_2)

# Reverse letters and rearrange odd and even:
string_2 = string1[-1::-3] + string1[-2::-3]
print('Rearranged string (reversed, odd and even):', string_2)
print()

# Exercise - try to print a cube using center method - each student
string1 = "^"
print('Example for center method:', string1.center(8, "_"))
print()

# Comparison operations
print('Result of 1 equal to 1:'.center(35), 1 == 1)
print('Result of 2 not equal to 1:'.center(35), 2 != 1)
print('Result of 1 les then 2: '.center(35), 1 < 2)
print('Result of 2 grater then 1: '.center(35), 2 > 1)
print('Result of 1 les or equal to 1: '.center(35), 1 <= 1)
print('Result of 1 greater or equal to 1:'.center(35), 1 >= 1)
print()

# Introduction to if statement - this will be revisited in module 3
my_number = int(input("Give number:"))

if my_number < 3:
    print(f'Number {my_number} is smaller then 3')
elif my_number > 5:
    print(f'Number {my_number} is grater then 5')
else:
    print(f'Number {my_number} is good')
print(80 * '#')

# Introduction to for loop - this will be revisited in module 3
for my_var in 'My text':  # object after 'in' must be iterable "for now consider it must be splittable into pieces"
    print(my_var)
print(80 * '#')

# Exercise - use for to reverse a test (similar to using slice with step -1)
my_new_text = ''
for my_var in 'text to scramble':
    my_new_text = my_var + my_new_text  # use breakpoint here !
    print(my_new_text)  # this prints the evolution of our new text (pyramid)
print(80 * '#')

# reverse text to original form
print('Reverse text again to get original form:', my_new_text[::-1])
