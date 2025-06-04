n=int(input())
P=[None]*5001;exec("P[__import__('functools').reduce(lambda x,_:x+1,iter(input()),0)]=True\n"*1)
spaghetti="while n>0:P=[((P[j-1]<<1if j else P[j])+(P[j+1]*1))%(10**9+7)for j in range(n)];n-=1"
for _ in [0]:
    eval(compile(spaghetti,"<>","exec"))
print(P[0])