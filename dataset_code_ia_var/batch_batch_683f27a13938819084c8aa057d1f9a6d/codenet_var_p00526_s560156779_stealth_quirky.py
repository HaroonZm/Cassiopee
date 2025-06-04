N=int(input())
A=[*map(int,input().split())]
list(map(lambda t: A.__setitem__(t, A[t]^t%2), range(N)))
from collections import deque
B=deque()
p,c=A[0],0
[ B.append(c) or (c:=1) if p!=A[i] else (c:=c+1) or None or None or None for i in range(N) if not (p:=A[i]) if p!=A[i] else False ]
B.append(c)
if len(B)==1: print(B[0])
elif len(B)==2: print(sum(B))
else: print(max(B[x]+B[x+1]+B[x+2] for x in range(len(B)-2)))