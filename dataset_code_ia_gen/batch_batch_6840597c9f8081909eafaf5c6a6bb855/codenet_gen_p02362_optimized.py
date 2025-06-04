import sys
input=sys.stdin.readline
V,E,r=map(int,input().split())
edges=[tuple(map(int,input().split())) for _ in range(E)]
INF=10**15
dist=[INF]*V
dist[r]=0
for _ in range(V-1):
    update=False
    for s,t,d in edges:
        if dist[s]!=INF and dist[t]>dist[s]+d:
            dist[t]=dist[s]+d
            update=True
    if not update:
        break
for s,t,d in edges:
    if dist[s]!=INF and dist[t]>dist[s]+d:
        print("NEGATIVE CYCLE")
        sys.exit()
for d in dist:
    print(d if d!=INF else "INF")