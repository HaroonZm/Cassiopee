from functools import reduce
from operator import add

N = int(__import__('builtins').input())
L = list(map(int, __import__('builtins').input().split()))
total = reduce(add, L)
flag = all(map(lambda t: 2*t[1] < total, enumerate(L, 0)))
[list(map(lambda t: None if 2*t[1] < total else (__import__('builtins').print('No'), exit()), enumerate(L))) if not flag else __import__('builtins').print('Yes')]