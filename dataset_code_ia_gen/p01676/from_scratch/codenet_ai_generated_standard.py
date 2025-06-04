import sys
input=sys.stdin.readline

while True:
    line=input()
    if not line:
        break
    N,M=map(int,line.split())
    adj=[[] for _ in range(N)]
    radj=[[] for _ in range(N)]
    for _ in range(M):
        s,t=map(int,input().split())
        adj[s-1].append(t-1)
        radj[t-1].append(s-1)

    matchR=[-1]*N
    def bpm(u,vis):
        for v in adj[u]:
            if not vis[v]:
                vis[v]=True
                if matchR[v]==-1 or bpm(matchR[v],vis):
                    matchR[v]=u
                    return True
        return False

    result=0
    for u in range(N):
        vis=[False]*N
        if bpm(u,vis):
            result+=1
    print(M - result)