import random


def crypt_decrypt(string, key):
    result = []
    for letter in string:
        result.append(chr(ord(letter).__xor__(key)))
    return ''.join(result)


def is_prime(number):
    for i in range(2, number // 2 + 2):
        if not number % i:
            return False
    return True


def generate_primes(limit):
    result = []
    for i in range(limit):
        if is_prime(i):
            result.append(i)
    return result


def select_primes(number_of_values, limit):
    result = []
    primes_list = generate_primes(limit)
    for _ in range(number_of_values):
        count = len(primes_list)
        selector = random.randint(0, count - 1)
        result.append(primes_list.pop(selector))
    result.sort()
    return result


print(select_primes(2, 542))
print('name of module is:', __name__)
print('name of package is:', __package__)
