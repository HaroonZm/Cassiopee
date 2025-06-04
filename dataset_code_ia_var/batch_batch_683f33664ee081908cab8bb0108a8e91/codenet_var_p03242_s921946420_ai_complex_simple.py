from functools import reduce
from operator import add

s = input()

trans = {ord('9'): 'q', ord('1'): '9', ord('q'): '1'}

def deep_replace(t, d):
    return reduce(add, [[d.get(ord(c), c)] for c in t])

print(''.join(deep_replace(s, trans)))