m=int(input())
n=int(input())
edges=[[] for _ in range(m+1)]
indeg=[0]*(m+1)
for _ in range(n):
    x,y=map(int,input().split())
    edges[x].append(y)
    indeg[y]+=1
# タマは最後に入っているのでm番目に入った（順位はm）
# タマ以外の順序= トポロジカルソートで制約を満たす順番を求める

from collections import deque

q=deque()
res=[]
for i in range(1,m+1):
    if indeg[i]==0:
        q.append(i)
while q:
    u=q.popleft()
    res.append(u)
    for v in edges[u]:
        indeg[v]-=1
        if indeg[v]==0:
            q.append(v)
# タマは最後（m番目）なのでresの最後はタマ
# タマは必ず最後に入るためresの最後はタマでなければならない
# 出力
for r in res:
    print(r)