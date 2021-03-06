"""
Module documentation
"""

from random import randint

from communicator.utils import generate_primes


class Client:
    """
    Class Documentation
    """
    __secret = None

    def __init__(self, data1, data2):
        """
        Method documentation
        :param base: parameter information
        :param key: parameter information
        """
        self.data1 = data1
        self.data2 = data2

    def generate_prime(self):
        primes_list = [i for i in generate_primes(256) if i >= 129]
        self.prime = primes_list[randint(0, len(primes_list) - 1)]
        return self.prime

    def generate_base(self):
        self.base = randint(2, self.prime - 1)
        return self.base

    def generate_local_secret(self):
        self.local_secret = randint(2, self.prime)
        self.number_to_send = pow(self.base, self.local_secret) % self.prime
        return self.number_to_send

    def get_secret(self, secret):
        self.__secret = pow(secret, self.local_secret) % self.prime + 129


class Server():
    __secret = None

    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2

    def get_prime(self, prime):
        self.prime = prime

    def get_base(self, base):
        self.base = base

    def generate_local_secret(self):
        self.local_secret = randint(2, self.prime)
        self.number_to_send = pow(self.base, self.local_secret) % self.prime
        return self.number_to_send

    def get_secret(self, secret):
        self.__secret = pow(secret, self.local_secret) % self.prime + 129
