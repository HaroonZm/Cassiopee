from functools import reduce
from operator import xor

s = input()

mirror = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'}
magic = lambda x: ''.join(mirror.get(c, c) for c in reversed(x))
res = reduce(lambda a, b: a and b, (xor(ord(a), ord(b)) == 0 for a, b in zip(s, magic(s))), True) and len(s) == len(magic(s))

print(["No", "Yes"][res])