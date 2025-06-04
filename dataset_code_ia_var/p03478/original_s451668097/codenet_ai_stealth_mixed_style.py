n,a,b=map(int,input().split())
res=0
def S(x):
    t=0
    k=x
    while k:
        t+=k%10
        k//=10
    return t
i=0
while i<=n:
    if a<=S(i)<=b: res+=i
    i+=1
print(res)