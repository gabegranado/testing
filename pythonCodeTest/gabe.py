import sys
import random as rand
import requests
# print(sys.version)
# print(sys.executable)
test = 'test'

def greet(who_to_greet):
    greeting = 'hello, {}'.format(who_to_greet)
    return greeting


def even_random_number(a, b):
    even_number = rand.randint(a, b)
    if(even_number % 2 != 0):
        return even_random_number(a, b)
    return even_number


for i in range(0, 9):
    print(even_random_number(2, 100))
