# ABC_150_C_Count_Order.py

from itertools import permutations

N = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

pp = sorted(p)
qq = sorted(q)
P = list(permutations(pp))
Q = list(permutations(qq))
# print(P, Q)

a=P.index(tuple(p))
b=Q.index(tuple(q))
print(abs(a-b))