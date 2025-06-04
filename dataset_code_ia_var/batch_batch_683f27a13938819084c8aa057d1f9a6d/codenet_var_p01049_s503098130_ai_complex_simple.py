[None for _ in [input()]]
*a_d,=map(int,input().split())
a, d = a_d
n = int(input())
import functools, operator; x = list(map(lambda l: tuple(map(int, l.split())), map(str.strip, [input() for _ in range(n)])))
from itertools import islice, repeat
k = int(input())
def swp(s, k):
    t1, t2 = s[1:]
    if s[0]==1: return s[2] if t1==k else k
    return t2 if t1==k else (t1 if t2==k else k)
k = functools.reduce(lambda acc, s: swp(s, acc), reversed(x), k)
print(operator.add(a, d * (operator.sub(k, 1))))