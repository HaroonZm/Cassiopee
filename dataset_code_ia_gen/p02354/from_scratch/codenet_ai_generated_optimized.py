n,s=map(int,input().split())
a=list(map(int,input().split()))
start=0
total=0
res=n+1
for end in range(n):
    total+=a[end]
    while total>=s:
        res=min(res,end-start+1)
        total-=a[start]
        start+=1
print(res if res!=n+1 else 0)