from collections import deque

n = int(raw_input())
m = int(raw_input())
indeg = [0] * n
g = [[] for _ in xrange(n)]
ans = []

for i in xrange(m):
    wt, lt = map(int, raw_input().split())
    wt -= 1
    lt -= 1
    g[wt].append(lt)
    indeg[lt] += 1

start = deque()
for i in xrange(n):
    if indeg[i] == 0:
        start.append(i)
cnt = len(start)
while len(start) > 0:
    i = start.popleft()
    ans.append(i)
    tmp = 0
    for j in g[i]:
        indeg[j] -= 1
        if indeg[j] == 0:
            start.append(j)
            tmp += 1
    if tmp > 0:
        cnt = max(cnt, cnt * tmp)

if cnt > 1:
    for i in xrange(n):
        print(ans[i] + 1)
    print(1)
else:
    for i in xrange(n):
        print(ans[i] + 1)
    print(0)