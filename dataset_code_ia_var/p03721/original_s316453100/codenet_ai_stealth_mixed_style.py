N,K=[int(j)for j in input().split()]
L=[]
i=0
while i<N:
    t=[int(x) for x in input().split()]
    L+=[t]
    i+=1
from operator import itemgetter
def fx(a):
    return sorted(a,key=itemgetter(0))
L=fx(L)
for e in L:
    K = K - e[1]
    if K<=0:
        print(e[0])
        break