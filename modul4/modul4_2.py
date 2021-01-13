# sleep

import time

print(time)
print(time.time())
print(time.sleep(1))

from time import sleep

print('Sleeping 1 second')
sleep(1)


def sleep(seconds):
    print(f'do nothing for {seconds}')


import datetime

datetime.timedelta
print(sleep(10))

from time import sleep as imported_sleep

print(imported_sleep)

# our module
import communicator

import sys

print(sys.path)

# add to path
sys.path.append('/Users/emanuel.craciun/PycharmProjects/PEP20G04')
print(sys.path)

# use communicator
print(communicator.VAR1)
print('number 19 is prime:', communicator.is_prime(19))


# recursive functions
# 3! = 1*2*3
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(factorial(3))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(3))

my_list = [[1, [2, [3]]], [4, [5, [6]]], [7, [8, [9]]]]
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(isinstance(my_list, list))
print(type(my_list) == list)


def flatten_list_to_tuple(list_to_flatten):
    result = []
    for inner_object in list_to_flatten:
        if isinstance(inner_object, int):
            result.append(inner_object)
        else:
            result += list(flatten_list_to_tuple(inner_object))
    return tuple(result)


# variables (global, non-local, local)
VAR1 = 'my var to print'


def outer(arg1):
    global VAR1
    VAR1 = 'some new message'
    VAR2 = 'inside outer'
    VAR3 = 'var3'
    print(outer.__name__, VAR1)

    def inner(arg2):
        VAR1 = 'ceva'
        nonlocal VAR2
        VAR2 = 'now in inner function'
        print(inner.__name__, VAR1)
        print(inner.__name__, VAR2)
        print(inner.__name__, VAR3)

    inner(10)
    print(outer.__name__, VAR2)
    return inner


x = outer(10)
print(__name__, VAR1)
VAR1 = 'my new var to print'
x(10)


def conversation():
    name_ = ''
    def hello(name='sir'):
        nonlocal name_
        name_ = name
        name_ = input(f'hello {name}:')

    def question(q='question'):
        print(f'{name_}, {q}?')

    hello()
    return question


object = conversation()
object('what is that')
