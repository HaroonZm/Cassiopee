import sys
from collections import Counter
input=sys.stdin.readline

N,V= map(int,input().split())
A=[int(input()) for _ in range(N)]
B=[int(input()) for _ in range(N)]
C=[int(input()) for _ in range(N)]
D=[int(input()) for _ in range(N)]

AB=Counter()
for a in A:
    for b in B:
        AB[a+b]+=1

res=0
for c in C:
    for d in D:
        res+=AB[V-(c+d)]

print(res)