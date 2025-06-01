n,m=map(int,input().split())
point=list()
for i in range(m):
    a,h=map(int,input().split())
    point+=[[a,h]]
point.sort(reverse=True)
ans=0
def compute():
    global ans
    for p in point[:-1]:
        a,_=p
        if a>=n:
            pass
        else:
            ans+=n - a
compute()
print(ans)