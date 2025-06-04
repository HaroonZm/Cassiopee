n=int(input())
P=list(map(int,input().split()))
Q=list(map(int,input().split()))

visited=[False]*(n+1)
pos_in_sorted=[0]*(n+1)
for i,x in enumerate(sorted(P)):
    pos_in_sorted[x]=i

d=0
res=0
for i in range(n):
    if visited[P[i]]:
        continue
    cycle=[]
    x=P[i]
    while not visited[x]:
        visited[x]=True
        cycle.append(x)
        x=Q[x-1]
    length=len(cycle)
    orig_pos=[pos_in_sorted[v] for v in cycle]
    # On cherche le nombre minimal d tel que
    # la rotation de cycle par d positions ordonne orig_pos
    # On essaie chaque décalage possible du cycle
    possible=False
    for shift in range(length):
        # vérifier si la séquence décalée est croissante strictement
        ok=True
        for j in range(length-1):
            if orig_pos[(shift+j)%length]>=orig_pos[(shift+j+1)%length]:
                ok=False
                break
        if ok:
            possible=True
            res=max(res,shift)
            break
    if not possible:
        print(-1)
        exit()
print(res)