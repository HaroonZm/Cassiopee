from functools import reduce
from operator import add
N,*rest=map(int,open(0).read().split())
T=rest[:N]
M=rest[N]
ops=rest[N+1:]
S=lambda:reduce(add,T)
for q in (ops[i:i+2] for i in range(0,len(ops),2)):
    print(S()-T[q[0]-1]+q[1]-T[q[1]%1])