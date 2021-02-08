from random import randint

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


# print(my_gen.__next__())

def ip_generator(subnet):
    network, mask = subnet.split('/')
    ip_segments = network.split('.')
    for seg in ip_segments:
        assert 0 <= int(seg) <= 255, f'Bad IP segment {seg}'
    if mask == '24':
        numbers = [x for x in range(1, 255)]
        for i in range(254):
            value = numbers.pop(randint(0, len(numbers) - 1))
            yield f'{ip_segments[0]}.{ip_segments[1]}.{ip_segments[2]}.{value}/{mask}'
    else:
        raise AssertionError('Bad Mask')


gen = ip_generator('235.245.34.3/24')
for ip in gen:
    print(ip)
