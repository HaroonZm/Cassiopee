import sys
from collections import deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,w = map(int,readline().split()) #n:頂点数　w:辺の数
g = [[] for i in range(n)] #g[i]:点iに隣接している点のリスト
for i in range(w):
    x,y = map(int,readline().split())
    x,y = x-1,y-1
    g[x].append(y)
    g[y].append(x)

def dfs():
    ans = 0
    queue = deque([[0]]) #queueの中身をvisitedにするlen(queue)==nの時ans+=1
    while queue:
        lst = queue.popleft()
        if len(lst)==n:
            ans += 1
            continue
        for i in g[lst[-1]]:
            if not i in lst:
                queue.append(lst+[i])
    
    return ans

print(dfs())