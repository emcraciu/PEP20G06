### Integers

# binary numbers
# 0001 = 0b0001
# 0002 = 0b0010
# 0003 = 0b0011
# 0004 = 0b0100
# 0005 = 0b0101

# octal numbers
# 0001 = 0o0001
# 0002 = 0o0002
# ...
# 0008 = 0o0010
# 0009 = 0o0011


# hexadecimal numbers
# 0001 = 0x0001
# 0002 = 0x0002
# ...
# 0009 = 0o0009
# 0010 = 0o000a
# 0011 = 0o000b
# ...
# 0015 = 0o000f
# 0016 = 0o0010

# Print in different bases
print('Base2 number (0b0100) is printed in Base10:', 0b0100)
print('Base8 number (0o17) is printed in Base10:', 0o17)
print('Base16 number (0x1f) is printed in Base10:', 0x1f)
print()

# Exponent uses base 10
print('Number with exponent (5e10) is printed:', 5e10)
print()

# Arithmetic Operations
number1 = 3
number2 = 4
number3 = -3

print('division 3/4:', number1 / number2)
print('floordiv 4//3:', number2 // number1)
print('remainder 4%3:', number2 % number1)
print('negative 3:', -number1)
print('Result of 3 + (-3) is:', number1 + number3)
print('3 to the power of 4:', number1 ** number2)
print('Type of number -3:', type(number3))
print()

# Exercise use learned arithmetic operations
a = 3
b = 4
c = 5
result = (-b + pow((b ** 2) - 4 * a * c, 1 / 2)) / (2 * a)
print('Result of quadratic formula is:', result)
print()

### Floats
number4 = 0.75
print('Type of number 0.75:', type(number4))
print()

### Complex
number5 = 1.0 + 2.3j
print('Type of 1.0+2.3j:', type(number5))
print()

# String quotes:
string1 = 'Hello World'
string2 = "Hello World"
string3 = '''Hello World'''
string4 = """Hello World"""
print(string1, string2, string3, string4)
print()

# String interpretation:
string5 = u'Hello\nWorld'
print('unicode string:', string5)
string5 = r'Hello\nWorld'
print('Row string:', string5)
string5 = f'Hello World: {string5}'
print('Formatted string:', string5)
print()

# String slices
result = string4[4]
print('Forth char is:', result)
result = string4[-3]
print('Third char from right is:', result)
result = string4[4:9]
print('Forth to ninth char is:', result)
result = string4[4:9:2]
print('Forth to ninth char with step 2:', result)
result = string4[9:4:-1]
print('9 to 4 char with negative -1 step is:', result)
result = string4[-2:-6:-1]
print('-2 to -6 char with negative -1 step is:', result)
result = string4[-2:-6:-2]
print('-2 to -6 char with negative -1 step is:', result)
print()

# Dot notation for strings:
string1 = 'Hello World: {}, {}'
print('string actions:', dir(string1))
print('All lower case:', string1.lower())
print('All upper case:', string1.upper())
print('Upper first letter:', string1.capitalize())
print('Formated string:', string1.format('one', 'two'))
print('Index of first found "{":', string1.find('{'))
print()

# Dot notation for ints:
print('int actions:', dir(number1))
print('Numbers are:', number1, number2)
print('Addition:', number1.__add__(number2))
print('Use () to call methods on insta:', (3).__add__(4))
print('Multiplication:', number1.__mul__(number2))
print('Division:', number1.__truediv__(number2))
print('Power, __pow__ is **:', number1.__pow__(number2), '==', number1 ** number2)
print()

# Example
result = ''
a = 0
for i in string1:
    if a % 2:
        result = result + i.upper()
    else:
        result = result + i.lower()
    a = a + 1
print('Lower and upper char sequence:', result)
