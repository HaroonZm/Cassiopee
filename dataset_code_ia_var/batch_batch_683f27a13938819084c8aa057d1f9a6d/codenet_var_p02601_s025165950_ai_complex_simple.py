from functools import reduce
from itertools import product

A,B,C=map(int,input().split());K=int(input())
def f(a,b,c,k):
    return any(
        reduce(lambda acc, tpl: acc or (tpl[1]>tpl[0] and tpl[2]>tpl[1]),
               [(
                   a*pow(2,i),
                   b*pow(2,j),
                   c*pow(2,k-i-j)
               )],False)
        for i,j in ((i,j) for i in range(k+1) for j in range(k+1-i))
    )
print(['No','Yes'][f(A,B,C,K)])