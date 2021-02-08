# iterators

class ListIterator():
    def __init__(self, my_list: list):
        self.my_list = my_list

    def __next__(self):
        return self.my_list.pop(0)


iterator = ListIterator([1, 2, 3])

print(iterator.my_list)
print(iterator.__next__())
print(iterator.my_list)
print(iterator.__next__())
print(iterator.my_list)
print(iterator.__next__())
print(iterator.my_list)


# print(iterator.__next__())


class IntIterator():
    listed_number = []

    def __init__(self, numar: int):
        self.numar = numar
        for i in range(1, self.numar + 1):
            self.listed_number.append(i)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.listed_number) == 0:
            raise StopIteration
        return self.listed_number.pop(0)


class IntObject(int):
    def __init__(self, nr):
        super().__init__(nr)

    def __iter__(self):
        return IntIterator(self)


int_object = IntObject(3)
for i in int_object:
    print(i)


# lambda functions

def func1(a, b):
    return a + b


func2 = lambda a, b: a + b


# map
def process_chr(char: str):
    return chr(ord(char) + 1)


text = 'my_test to process'
result = map(process_chr, text)
print(result)
print(dir(result))
for new_obj in result:
    print(new_obj)

print('#' * 80)
result = map(lambda char: chr(ord(char) + 1), text)
for new_obj in result:
    print(new_obj)

print('#' * 80)
list_number = [i for i in range(10)]
result = map(lambda k: k if k % 2 == 0 else None, list_number)
for i in result:
    print(i)

# filter
print('#' * 180)
list_number = [i for i in range(10)]
result = filter(lambda a: a > 5, list_number)
for i in result:
    print(i)

# any
print('#' * 180)
my_list = [1, 'a', True, False, False]
my_list_f = [0, '', None, False, False]
print(any(my_list))
print(any(my_list_f))

# all
print('#' * 180)
my_list = [1, 'a', True]
my_list_f = [1, 'a', True, False]
print(all(my_list))
print(all(my_list_f))


# mostenire


class Wolf():
    bark = True

    def hunt(self):
        print('Hunting')

    def method_1(self):
        pass


class Dog(Wolf):

    def hunt(self):
        print('can`t do that')

    def method_2(self):
        pass

dog = Dog()
print('dog barks: ',dog.bark)
dog.method_2()
dog.method_1()
dog.hunt()