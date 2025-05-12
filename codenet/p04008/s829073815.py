import sys
input = sys.stdin.readline
# import heapq as hp

N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
graph = [[] for _ in range(N)]
Par = [-1]*N
for i, a in enumerate(A):
    if i == 0:
        if a != 1:
            ans += 1
        continue
    Par[i] = a-1
    graph[a-1].append(i)

qs = []

stack = [0]
Depth = [-1]*N
Depth[0] = 0
while stack:
    p = stack.pop()
    for np in graph[p]:
        Depth[np] = Depth[p] + 1
        stack.append(np)
    qs.append((Depth[p], p))

qs.sort(reverse=True)
checked = [False]*N

for d, s in qs:
    if d <= K: break
    if checked[s]: continue

    for _ in range(K-1):
        s = Par[s]
    
    que = [s]
    checked[s] = True
    while que:
        qq = []
        for p in que:
            for np in graph[p]:
                if not checked[np]:
                    checked[np] = True
                    qq.append(np)
        que = qq
    
    ans += 1

print(ans)