from collections import Counter
from functools import reduce
from operator import add

N = int(input())
A = list(map(int, input().split()))

dic = Counter(A)
Q = int(input())
s = reduce(add, A)

idnext = iter(range(N*2)).__next__

for _ in map(lambda _: idnext(), range(Q)):
    B, C = map(int, input().split())
    cnt = dic.get(B, 0)
    s += (C - B) * cnt
    print(s)
    dic[C] = dic.get(C, 0) + cnt
    dic[B] = 0