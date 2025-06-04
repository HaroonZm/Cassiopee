from functools import reduce
import itertools as it

d,g=[int(x) for x in input().split()]
arr=[]
i=0
while i<d:
    arr+=[list(map(int,input().split()))]
    i+=1

ans=1e10
for bits in it.product([0,1],repeat=d):
    score,num=0,0
    idx=None
    def add(x,y):
        return x+y
    for n in range(d):
        if bits[n]:
            tmp=(n+1)*100*arr[n][0]
            b=arr[n][1]
            score=add(score,tmp+b)
            num+=arr[n][0]
        else:
            idx=n if idx is None or n>idx else idx
    # POO
    class X:pass
    x=X();x.value=ans
    if score>=g:
        x.value=min(x.value,num)
    elif idx is not None:
        m=arr[idx][0]-1
        mx=(idx+1)*100*m
        left=g-score
        if left<=mx:
            k=-(-(left)//(100*(idx+1)))
            num+=k
            x.value=min(x.value,num)
    ans=x.value
print(int(ans))