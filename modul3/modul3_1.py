# FOR loop

# Iterable object

string1 = 'My str'
print(dir(string1))

# Next for iterable objects
print(type(string1.__iter__()))
print(dir(string1.__iter__()))
print()

iterator = string1.__iter__()
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())

# print(iterator.__next__())
my_int = 123

# for i in my_int:
#     print(i)
print()
for i in 'my_text':
    print(i)
print('done')

# compare string
nr = ord('a')
print(f'Number of a: {nr}')
nr = ord('b')
print(f'Number of b: {nr}')

print('check if a == b:', 'a' == 'b')
print('check if a.__eq__(b):', 'a'.__eq__('b'))

print('check if a<=b', 'a' <= 'b')
print('check if a<=b', 'a'.__le__('a'))

print('Check if a > b:', 'a' > 'b')
print('Check if a > b:', 'a'.__gt__('a'))

print('Check if a >= b:', 'a' >= 'b')
print('Check if a >= b:', 'a'.__ge__('b'))

print('check if a<b', 'a' < 'b')
print('check if a<b', 'a'.__lt__('b'))

print(dir(1))
print('1 + 2 = ', (1).__add__(2))

print()
# exercise exit for on _
for i in 'my_text':
    if '_' == i:
        break
    else:
        print(i)
print()

# exercise print 'yey' if _ not in text
var1 = ''
for i in 'mytext':
    if '_' == i:
        var1 = '_'
print('var1=', var1)
if var1 != '_':
    print('yey')
print()

# exercise print 'yey' if _ not in text
var1 = ''
for i in 'my_text':
    if '_' == i:
        break
else:
    print('For else statement:', 'yey')

print()
# len function
print(len('my_text'))
print('my_text'.__len__())

print()

text = 'my_text'
if len(text) > 3:
    for letter in text:
        var = letter
    print(letter)

# continue

# new text without spaces
text = 'my text'
new_text = ''
for letter in text:
    if letter == ' ':
        continue
    new_text = new_text + letter
print(new_text)

print()

# while loop
a = 4
while a > 2:
    if a > 2:
        a = a - 1
    else:
        a = a + 1
    print('True')

# Read while value is smaller then 100
# len(text)<5 letters then add new characters
my_text = 'my_text'
new_text = ''
var1=0
while len(new_text) < 5:
    new_text=new_text+my_text[var1]
    var1+=1
    print(new_text)


# function range

range_object = range(3)
print(type(range_object))
range_iter = range_object.__iter__()
print(next(range_iter))
print(next(range_iter))
print(next(range_iter))
# print(next(range_iter))

for i in range(3):
    print('in for:', i)

for i in range(2, 6):
    print('in for with step 1:', i)

for i in range(2, 6, 2):
    print('in for with step:', i)

# Assigment operator
var1 = 1
print(var1)
var1 += 2  # (var1 = var1 + 1 )
print(var1)
var1 *= 3
print(var1)
var1 /= 3
print(var1)
var1 **= 3
print(var1)