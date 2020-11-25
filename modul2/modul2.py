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

# Print in base 2
print(0b0100)
print(5e100)

# Arithmetic Operations

number1 = 3
number2 = 4
number3 = -3

print('division 3/4:', number1 / number2)
print('floordiv 4//3:', number2 // number1)
print('remainder 4%3:', number2 % number1)
print('negative 3:', -number1)
print('zero:', number1 + number3)
print('3 to the power of 4:', number1 ** number2)
print('Type of number -3:', type(number3))

a = 3
b = 4
c = 5

result = (-b + pow((b ** 2) - 4 * a * c, 1 / 2)) / (2 * a)
print(result)

number4 = 0.75
print('Type of number 0.75:', type(number4))

number5 = 1.0 + 2.3j
print('Type of 1.0+2.3j:', type(number5))

# String quotes:
string1 = 'Hello World'
string2 = "Hello World"
string3 = '''Hello World'''
string4 = """Hello World"""
print(string1, string2, string3, string4)

# String interpretation:
string5 = u'Hello\nWorld'
print('unicode string:', string5)
string5 = r'Hello\nWorld'
print('Row string:', string5)
string5 = f'Hello World: {string5}'
print('Formatted string:', string5)

# String slices
result = string5[4]
print('Forth char is:', result)
result = string5[-3]
print('third char from right is:', result)
result = string5[4:9]
print('Forth to seventh char is:', result)
result = string5[9:4:-1]
print('Forth to seventh char is:', result)
result = string5[-2:-6:-1]
print('result:', result)
result = string5[-2:-7:-2]
print('result:', result)

# Dot notation for strings:
print('string actions:', dir(string1))
print(string1.lower())
print(string1.upper())
print(string1.capitalize())
print(string1.format())

# Dot notation for ints:
print(number1.__add__(number2))
print((3).__add__(4))
print('multiplication:', number1.__mul__(number2))
print('division:', number1.__truediv__(number2))
print('power of:', number1.__pow__(number2), '==', number1 ** number2)



# x = []
# a = 0
# for i in string1:
#     if a%2:
#         x.append(i.upper())
#     else:
#         x.append(i.lower())
#     a = a + 1
#
# print(''.join(x))
