import sys
input=sys.stdin.readline

while True:
    X,Y,Z=map(int,input().split())
    if X==0 and Y==0 and Z==0:
        break
    V=[int(input()) for _ in range(X)]
    events=[None]*(Y+1)
    for _ in range(Z):
        N,E,A=map(int,input().split())
        events[N]=(E,A)
    prob=1/X
    dp=[None]*(Y+1)
    def f(pos,money):
        if pos>=Y:
            return money
        key=(pos,money)
        if dp[pos] is not None:
            return dp[pos]
        res=0.0
        for v in V:
            npos=pos+v
            nmoney=money
            if npos>=Y:
                res+=nmoney*prob
                continue
            if events[npos]:
                E,A=events[npos]
                if E==1:
                    npos2=npos+A
                    if npos2>=Y:
                        res+=nmoney*prob
                    else:
                        res+=f(npos2,nmoney)*prob
                elif E==2:
                    nmoney+=A
                    res+=f(npos,nmoney)*prob
                else:
                    nmoney-=A
                    if nmoney<0:
                        nmoney=0
                    res+=f(npos,nmoney)*prob
            else:
                res+=f(npos,nmoney)*prob
        dp[pos]=res
        return res
    # DP over (pos,money) is heavy; money can be large(up to 100*number of visits),
    # So let's DP only on position and carry money as parameter then memo by tuple.
    from functools import lru_cache
    @lru_cache(maxsize=None)
    def dfs(pos,money):
        if pos>=Y:
            return money
        res=0.0
        for v in V:
            npos=pos+v
            nmoney=money
            if npos>=Y:
                res+=nmoney/X
                continue
            ev=events[npos]
            if ev:
                E,A=ev
                if E==1:
                    npos2=npos+A
                    if npos2>=Y:
                        res+=nmoney/X
                    else:
                        res+=dfs(npos2,nmoney)/X
                elif E==2:
                    nmoney2=nmoney+A
                    res+=dfs(npos,nmoney2)/X
                else:
                    nmoney2=nmoney-A
                    if nmoney2<0:
                        nmoney2=0
                    res+=dfs(npos,nmoney2)/X
            else:
                res+=dfs(npos,nmoney)/X
        return res
    ans=int(dfs(0,0))
    print(ans)