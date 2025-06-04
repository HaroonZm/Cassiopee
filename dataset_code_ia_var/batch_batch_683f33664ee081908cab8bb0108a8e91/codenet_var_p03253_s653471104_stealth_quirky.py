from functools import reduce

N,M = [*map(int, input().split())]

def factors(x):
    p=2
    l=[]
    while p*p<=x:
        if x%p:
            p+=1
        else:
            l.append(p)
            x//=p
    if x>1: l+=[x]
    return l

def C(n,r):
    return reduce(lambda a,b:a*b,range(n-r+1,n+1),1)//reduce(lambda a,b:a*b,range(1,r+1),1) if 0<=r<=n else 0

lst = factors(M)
output = [1]
j=0
while j < len(lst):
    k = 1
    while j+k < len(lst) and lst[j] == lst[j+k]:
        k+=1
    output[0] *= C(N+k-1, k)
    output[0] %= 10**9+7
    j+=k

print(output[0])