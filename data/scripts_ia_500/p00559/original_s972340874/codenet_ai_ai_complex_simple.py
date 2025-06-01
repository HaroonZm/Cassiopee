from functools import reduce
from operator import add as op_add
N,Q,S,T = map(int, __import__('sys').stdin.readline().split())
A = list(map(int, __import__('sys').stdin.read().split()))
A, B, C = A[:N+1], list(map(lambda i: A[i+1]-A[i], range(N))), 0
C = reduce(lambda acc,i: acc+(S if A[i]>=A[i+1] else T)*(A[i]-A[i+1]), range(N), 0)
def add(k,x):
    return reduce(lambda a,b: a+b, [
        (-T*x) if (x>=0 and B[k]<=0 and B[k]+x<=0) else 0,
        (T*B[k] - S*(B[k]+x)) if (x>=0 and B[k]<=0 and B[k]+x>0) else 0,
        (-S*x) if (x>=0 and B[k]>0) else 0,
        (-S*x) if (x<0 and B[k]>=0 and B[k]+x>=0) else 0,
        (S*B[k]-T*(B[k]+x)) if (x<0 and B[k]>=0 and B[k]+x<0) else 0,
        (-T*x) if (x<0 and B[k]<0) else 0
    ])
ans, idx = [], 0
for _ in range(Q):
    l,r,x = A[N+1+idx], A[N+2+idx], A[N+3+idx]
    idx += 3
    C += add(l-1,x)
    B[l-1] += x
    if r < N:
        C += add(r,-x)
        B[r] -= x
    ans.append(C)
print('\n'.join(map(str, ans)))