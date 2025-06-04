from functools import reduce
from itertools import starmap

X, Y = map(lambda s: int.__new__(int, s), input().split())
verdict = dict(enumerate(['Alice', 'Brown']))[reduce(lambda a, b: int(a >= 2), starmap(abs, [(X, Y)]))]
print(verdict)