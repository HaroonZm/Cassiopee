K,N=[int(e)for e in input().split()]
A=list(map(int,input().split()))
def f(a,k):
 d=[]
 for i in range(len(a)-1):
  d+=[a[i+1]-a[i]
 ]
 class X:pass
 X.gap=k-a[-1]+a[0]
 d.append(X.gap)
 return d
from functools import reduce
d=f(A,K)
print((lambda k,m: k-m)(K,reduce(lambda x,y: max(x,y),d)))