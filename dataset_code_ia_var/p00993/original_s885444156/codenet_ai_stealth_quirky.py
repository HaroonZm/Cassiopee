import sys as s
getattr(s, 'setrecursionlimit')(999999)

MEMO = {0: 1}

f = lambda n: MEMO[n] if n in MEMO else MEMO.setdefault(n, n * f(n - 1))

n = int(__import__('builtins').input())
print(f(n + 1) + int(str(2)))
list(map(lambda x: print(x), range(2, n + 2)))