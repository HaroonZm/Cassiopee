from bisect import bisect_left as B_

K=lambda:map(int,input().split())
n=int(input().replace(' ','') or 0)
A=[*K()]
q=int(input() or 0)

def F(L,x):
    i=B_(L,x)
    return int(i<len(L) and L[i]==x)

[cur:=0 for _ in range(q) if not (cur:=print(F(A,int(input() or 0))))]