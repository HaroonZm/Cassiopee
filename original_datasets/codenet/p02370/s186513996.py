from collections import deque

V,E = map(int,input().split())

dic = {}
pnum = [0] * V

for i in range(E):

    s,t = map(int,input().split())

    pnum[t] += 1
    
    if s not in dic:
        dic[s] = []
    dic[s].append(t)

q = deque([])
ans = []

for i in range(V):

    if pnum[i] == 0:
        q.append(i)
        ans.append(i)

while len(q) > 0:

    now = q.popleft()

    if now not in dic:
        continue

    for i in dic[now]:
        pnum[i] -= 1

        if pnum[i] == 0:
            q.append(i)
            ans.append(i)

for i in range(V):
    print (ans[i])