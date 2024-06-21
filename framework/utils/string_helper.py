import random
import string


class StringHelper:

    @staticmethod
    def get_random_string(length):
        return ''.join(random.sample(set(string.ascii_letters), length))