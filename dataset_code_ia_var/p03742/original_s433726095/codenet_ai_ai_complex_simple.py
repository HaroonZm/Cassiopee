from functools import reduce
from operator import xor

def sophisticated_input():
    return list(map(int, ''.join(chr(ord(c)) for c in input()).split(' ')))

x, y = sophisticated_input()
threshold = lambda a, b: reduce(lambda acc, val: acc + (1 if val else 0), [abs(a - b) >= 2], 0)
result = (lambda t: ['Brown', 'Alice'][t])(threshold(x, y))
print(result)