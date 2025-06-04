import itertools
import functools
import operator
import collections

def extravagant_map(permutation):
    def mapper(perm):
        return tuple(perm[i] for i in permutation)
    return mapper

op1 = extravagant_map([0,1,2,3,4,5,21,22,23,11,10,9,17,13,14,15,16,12,18,19,20,6,7,8,24,25,26,27,28,29])
op2 = extravagant_map([27,28,29,3,4,5,6,7,8,9,10,11,12,13,15,14,16,17,20,19,18,21,22,23,24,25,26,0,1,2])
op3 = extravagant_map([23,1,2,26,4,5,29,7,8,20,10,11,12,13,14,17,16,15,18,19,9,21,22,0,24,25,3,27,28,6])
op4 = extravagant_map([0,1,21,3,4,24,6,7,27,9,10,18,14,13,12,15,16,17,11,19,20,2,22,23,5,25,26,8,28,29])

op_dict = {1: op1, 2: op2, 3: op3, 4: op4}

def op(p, i):
    return op_dict[i](p)

def group_check(p, starts_ends):
    return all(all(p[a]==p[b] for b in range(s,e)) for a, (s,e) in enumerate(starts_ends))

def identity(x): return x

Q_INDEX = (0,9,12,15,18,21)
perms = [
    (0, 1, 3, 5, 4, 2), (0, 3, 5, 4, 1, 2), (0, 5, 4, 1, 3, 2), (0, 4, 1, 3, 5, 2),
    (2, 1, 5, 3, 4, 0), (2, 5, 3, 4, 1, 0), (2, 3, 4, 1, 5, 0), (2, 4, 1, 5, 3, 0)
]

def valid(p):
    blocks = [(0,1,9),(21,22,30),(9,10,12),(12,13,15),(15,16,18),(18,19,21)]
    for s,e in blocks:
        if len({p[i] for i in range(s,e)}) > 1:
            return False
    q = tuple(p[i] for i in Q_INDEX)
    if q in perms:
        return True
    return False

minimum = 100

def solve(n, p, i):
    global minimum
    if n > 9 or n >= minimum:
        return
    if valid(p):
        minimum = min(minimum, n)
        return
    ForChoices = tuple(j for j in range(1, 5) if j != i)
    for j in ForChoices:
        solve(n+1, op(p, j), j)

try:
    N = int(next(iter([input()])))
except Exception:
    N = int(input())
for _ in range(N):
    minimum = 100
    try:
        p = tuple(map(lambda x: int(x)-1, next(iter([input()])).split()))
    except Exception:
        p = tuple(map(lambda x: int(x)-1, input().split()))
    if valid(p):
        print(0)
        continue
    list(map(lambda i: solve(1, op(p, i), i), range(1,5)))
    print(minimum)