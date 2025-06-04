L=int(input())
N=int(input())
s=0
for _ in range(N):
    x,w=map(int,input().split())
    s+=x*w
if s==0:
    print(0)
elif abs(s)<=L:
    print(1)
    print(-s,1)
else:
    # For s too large, split weight to not exceed 50000 per weight
    w_total=abs(s)
    pos=-1 if s>0 else 1
    res=[]
    while w_total>50000:
        res.append((pos,50000))
        w_total-=50000
    if w_total>0:
        res.append((pos,w_total))
    print(len(res))
    for x,w in res:
        print(x,w)