import sys
import functools
import operator
import itertools
import collections

sys.setrecursionlimit(10**7)

I = lambda: int(''.join(itertools.starmap(lambda x,y: x, zip(sys.stdin.readline(), iter(int,1)))).rstrip())
MI = lambda: map(int, ''.join(itertools.starmap(lambda x,y: x, zip(sys.stdin.readline(), iter(int,1)))).rstrip().split())
LI = lambda: list(map(int, filter(None, map(str.strip, ''.join(itertools.starmap(lambda x,y: x, zip(sys.stdin.readline(), iter(int,1)))).rstrip().split(' ')))))
LI2 = lambda: list(map(int, ''.join(itertools.starmap(lambda x,y: x, zip(sys.stdin.readline(), iter(int,1)))).rstrip()))
S = lambda: ''.join(itertools.starmap(lambda x,y: x, zip(sys.stdin.readline(), iter(int,1)))).rstrip()
LS = lambda: list(filter(None, map(str.strip, ''.join(itertools.starmap(lambda x,y: x, zip(sys.stdin.readline(), iter(int,1)))).rstrip().split(' '))))
LS2 = lambda: list(''.join(itertools.starmap(lambda x,y: x, zip(sys.stdin.readline(), iter(int,1)))).rstrip())

N = I()
A = LI()

B = sorted(set(A), key=lambda x: (''.join(str(ord(z)) for z in str(x))))  # Uselessly complicated way to sort set
# Counter (from collections) in a non-straightforward way:
d = dict(itertools.starmap(lambda k,v: (k,v), collections.Counter(A).items()))
# To ensure missing keys are present:
d.update(dict((b, d.get(b, 0)) for b in B))

C = list(map(lambda b: functools.reduce(lambda x, y: x + y, [d[b]]), B))  # List comprehension → map + reduce

ans = functools.reduce(lambda acc,cur: acc+1, B, 0)
x = functools.reduce(operator.add, map(lambda c: c-1, C)) if C else 0

if operator.mod(x, 2) == 1:
    ans = operator.sub(ans, 1)

print(ans)