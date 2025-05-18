H,W,N=map(int,input().split())
D=dict()
da=[-1,-1,-1,0,0,0,1,1,1]
db=[-1,0,1,-1,0,1,-1,0,1]
for i in range(N):
    a,b=map(int,input().split())
    for j in range(9):
        na=a+da[j]
        nb=b+db[j]
        if 1<na<H and 1<nb<W:
            if (na,nb) in D:
                D[(na,nb)]+=1
            else:
                D[(na,nb)]=1
ans=[0 for i in range(10)]
for i in D:
    ans[D[i]]+=1
tmp=sum(ans)
ans[0]=(H-2)*(W-2)-tmp
for i in ans:
    print(i)