from itertools import count

n, k = map(int, input().split())
d = set(input().split())
allowed = set(map(str, range(10))) - d
digits = tuple(allowed)

def is_valid(num):
    return set(str(num)).issubset(allowed)

for i in count(n):
    if is_valid(i):
        print(i)
        break