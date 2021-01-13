# Exceptions
from time import sleep

var = 0

try:
    sleep(1)
    result2 = 2 / var
    if var == 0:
        result1 = 2 / '0'
except ZeroDivisionError:
    print('Bad Division')
except TypeError:
    print('Bad operand type')
except Exception:
    print('something is wrong')
else:
    print('This will only execute if no exception')
finally:
    print('this will always be executed')


# function to device input number to 2

def div(divider=2):
    pass


def check_if_not_0(nr=0):
    if nr == 0:
        raise ValueError('Number is 0')
    print('Value is not 0')
    if nr == 10:
        raise ValueError('Different message')


check_if_not_0(nr=1)
print('new call')
try:
    check_if_not_0(nr=10)
except ValueError as e:
    print('I will try again')
    if e.args[0] == 'Number is 0':
        print('This is my exception')
    else:
        raise e


# class

class CarFactory:
    model = 'VW'

    def __init__(self, color):
        print('Building car')
        self.color = color

    def __le__(first_car, second_car):
        print('first object is', first_car)
        print('second object is', second_car)
        return id(first_car) <= id(second_car)


print('Class attribute:', CarFactory.model)

car1 = CarFactory('green')
print(car1.color)
print('Instance variable:', car1.model)

car2 = CarFactory('blue')
print(car2.color)
print('Instance variable:', car2.model)


print('CAR1 is:', car1)
print('CAR2 is:', car2)
print(dir(car1))
print()
# print(car1 <= car2)
# print(car2 <= car1)
print(car1.__le__(car2))


# mutable class attributes
class A:
    mutable_obj = []

    def change_attr(self, value):
        self.mutable_obj.append(value)

print()
a = A()
a.mutable_obj.append(3)
print(a.mutable_obj)
a.change_attr(1)
print(a.mutable_obj)

print()
b = A()
print(b.mutable_obj)
b.change_attr(2)
print(b.mutable_obj)

print()
print('Object a now has changes added by object b:', a.mutable_obj)



# track how many cars are constructed
class Factory:
    __counter = [0]

    def __init__(self):
        self.__counter.append(self.__counter.pop(0) + 1)

first_car = Factory()
print(first_car._Factory__counter)
second_car = Factory()
print(Factory._Factory__counter)


# private and protected attributes
print()
class A:
    __attr0 = 'really hide'
    _attr1 = 'hide'
    attr2 = 'do not hide'

a = A()
print(a._A__attr0)
print(a._attr1)
print(a.attr2)