import random
__author__ = 'pawel'
class RandomGenerator:
    def __generate__(self,max,array_size):
        return [random.random()*max for _ in range(array_size)]

