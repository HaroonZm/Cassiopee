def f(n, x):
    i = 0
    while i < 9:
        if n[i] != -1:
            if n[i] != x[i]:
                return True
        i += 1
    return False

import itertools

u = [1,2,3,4,5,6,7,8,9]
n = input().split()
n = list(map(lambda val: int(val), n))

a = 0
for x in itertools.permutations(u):
    if f(n, x):
        continue

    s = 0
    s += x[0]
    s += x[2]
    s += x[5]
    s -= x[8]
    s += (x[1] + x[4] - x[7]) * 10
    s += (x[3] - x[6]) * 100
    if s == 0:
        a += 1
print(a)