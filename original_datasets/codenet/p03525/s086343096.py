from itertools import groupby

N=int(input())
D=list(map(int,input().split()))

def dfs(list,num):
    global ans
    if num==N:
        m=100
        for i in range(0,N):
            for j in range(i+1,N+1):
                s=abs(list[i]-list[j])
                test=min(s,24-s)
                m=min(test,m)
        ans=max(ans,m)
    else:
        dfs(list+[D[num]],num+1)
        dfs(list+[24-D[num]],num+1)

if N>=24:
    print(0)
elif N>=12:
    D.sort()
    D=groupby(D)
    for key,group in D:
        g=len(list(group))
        if key==0:
            print(0)
            exit()
        elif key==12:
            if g>1:
                print(0)
                exit()
        else:
            if g>2:
                print(0)
                exit()
    print(1)
else:
    ans=0
    dfs([0],0)
    print(ans)