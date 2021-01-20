my_list = [1, 2, 3]

my_list_iter = my_list.__iter__()

print(my_list_iter)
print(next(my_list_iter))
print(next(my_list_iter))


# print(len(my_list_iter))

# generator

def my_generator():
    for i in range(3):
        print('before')
        yield i
        print('after')


gen = my_generator()
print(type(gen))
print(gen.__next__())
print('step1')
print(gen.__next__())
print('step2')
print(gen.__next__())
print('step3')
# print(gen.__next__())


# print(my_generator().__next__())

# list comprehension
my_list_c = [i for i in range(10)]
print(my_list_c)

my_gen = (i for i in range(3))
print(my_gen)
print(my_gen.__next__())
print(my_gen.__next__())
print(my_gen.__next__())
print(my_gen.__next__())