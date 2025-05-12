import sys

def func(d, S, D):
    if S[d] == []:
        return 2, [d]
    else:
        tmp = 1
        used=[d]
        for k in S[d]:
            ret = func(k,S,D)
            tmp *= ret[0]
            used += ret[1]
        return tmp+1 , used

sys.setrecursionlimit(100000)
N,M=map(int,raw_input().split())
S=[[] for i in range(N)]
D=[-1 for i in range(N)]
for i in range(M):
    s,d=map(lambda x: int(x)-1 ,raw_input().split())
    D[s] = d
    S[d].append(s)

unevaled=range(N)
bans=[]
while(len(unevaled)>0):
    #find root
    tmp=unevaled[0]
    T=[tmp]
    while (1):
        if D[tmp]==-1:
            root=tmp
            break
        elif D[tmp] in T:
            root=D[tmp]
            D[root]=-1
            rebase=T[ T.index(root) : ]
            Stmp=[]
            for r in rebase:
                for rs in S[r]:
                    if rs not in rebase:
                        D[rs]=root
                        Stmp.append(rs)
                if r!=root:
                    unevaled.remove(r)
            S[root]=Stmp[:]
            break
        else:
            tmp=D[tmp]
            T.append(tmp)
    b = func(root, S, D)
    bans.append(b[0])
    for r in b[1]:
        unevaled.remove(r)
ans = reduce(lambda x,y: x*y, bans)
print ans%1000000007