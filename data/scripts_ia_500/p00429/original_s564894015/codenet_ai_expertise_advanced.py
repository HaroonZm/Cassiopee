from itertools import groupby

def f(a, n):
    for _ in range(int(n)):
        a = ''.join(f"{len(list(g))}{k}" for k, g in groupby(a))
    return a

while True:
    n = input()
    if n == '0':
        break
    a = input()
    print(f(a, n))