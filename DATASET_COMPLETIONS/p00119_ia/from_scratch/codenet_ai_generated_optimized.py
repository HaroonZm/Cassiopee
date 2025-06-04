m=int(input())
n=int(input())
edges=[[] for _ in range(m+1)]
indeg=[0]*(m+1)
for _ in range(n):
    x,y=map(int,input().split())
    edges[x].append(y)
    indeg[y]+=1
from collections import deque
q=deque()
for i in range(1,m+1):
    if indeg[i]==0:
        q.append(i)
res=[]
while q:
    u=q.popleft()
    res.append(u)
    for v in edges[u]:
        indeg[v]-=1
        if indeg[v]==0:
            q.append(v)
# タマは必ず最後に入ったのでリストの最後に来る（入室順の最後）
# 証言は「私はyより先に入った」、つまりx < yの制約で、したがってyはxの後、よってyの入室順はxの後
# トポロジカルソートで解決できる
for r in res:
    print(r)