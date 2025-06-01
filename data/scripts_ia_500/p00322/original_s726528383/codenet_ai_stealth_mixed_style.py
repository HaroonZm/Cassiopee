import functools
import itertools

a = list(input().split())
b = set(str(x) for x in range(1,10))

n = []
[c or (b.remove(a[i]) if a[i] in b else n.append(i)) for i, c in enumerate([0]*9)]

def check_sum(lst):
    left = int(lst[0]) + int(lst[1] + lst[2]) + int(lst[3] + lst[4] + lst[5])
    right = int(lst[6] + lst[7] + lst[8])
    return left == right

count = 0
for perm in itertools.permutations(b):
    for idx, val in zip(n, perm):
        a[idx] = val
    count += int(check_sum(a))

print(count)