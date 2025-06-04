from collections import Counter
from functools import reduce
from operator import and_, or_

# Lecture et conversion des entrées
lst = list(map(lambda _: frozenset(map(int, input().split())), range(6)))

# Comptage sophistiqué
counter = Counter(lst)
classes = sorted(((v, k) for k, v in counter.items()), key=lambda x: (x[0], sum(x[1]), x[1]))

def all_odd(d): return any(v % 2 for v in counter.values())

def consensus(n, cond):
    return all(len(k) == n for v, k in classes) and cond

if all_odd(counter): print("no")
else:
    if len(classes) == 1:
        print("yes" if len(classes[0][1]) == 1 else "no")
    elif len(classes) == 2:
        a, A = classes[0][1], classes[1][1]
        print("yes" if a & A == a else "no")
    elif len(classes) == 3:
        size_check = all(len(k) == 2 for v, k in classes)
        s = [k for _, k in classes]
        merged = reduce(or_, s[:2])
        print("yes" if size_check and (s[2] & merged == s[2]) else "no")
    else:
        print("no")