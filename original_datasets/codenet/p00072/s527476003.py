while True:
    n=input()
    if n==0:
        break
    graph=[[1<<30]*n for i in xrange(n)]
    for i in xrange(input()):
        a,b,c=map(int,raw_input().strip().split(","))
        graph[a][b]=graph[b][a]=c
    visited=[False]*n
    visited[0],ans=True,0
    while not all(visited):
        t=min( [(i,j,graph[i][j])for j in xrange(n) if not visited[j] for i in xrange(n) if visited[i]],key= lambda x:x[2])
        ans+=t[2]/100-1
        visited[t[1]]=True
    print ans