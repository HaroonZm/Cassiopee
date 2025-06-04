from collections import deque

V, E = map(int, input().split())

dic = {}
pnum = [0] * V
i = 0
while i < E:
    s, t = map(int, input().split())
    pnum[t] += 1
    if s not in dic:
        dic[s] = []
    dic[s].append(t)
    i += 1

q = deque([])
ans = []
i = 0
while i < V:
    if pnum[i] == 0:
        q.append(i)
        ans.append(i)
    i += 1

while len(q) > 0:
    now = q.popleft()
    if now not in dic:
        continue
    j = 0
    l = dic[now]
    while j < len(l):
        i = l[j]
        pnum[i] -= 1
        if pnum[i] == 0:
            q.append(i)
            ans.append(i)
        j += 1

i = 0
while i < V:
    print(ans[i])
    i += 1