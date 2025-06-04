from functools import reduce
from operator import mul

*A,=map(int,input().split())
K=int(input())

l=[A.copy()]
g=lambda x,y:[x[0]>x[1],x[1]>x[2]]

def f(a):
    i=0
    while i<K:
        h=g(a)
        if not h[0] and not h[1]:
            print('Yes')
            return
        idx=max(range(2),key=lambda j:a[j]>=a[j+1])
        a[idx+1]<<=1
        i+=1
    print('No')

f(A)