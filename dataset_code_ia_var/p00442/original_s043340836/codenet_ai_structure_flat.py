n = int(input())
to = [[] for _ in range(n)]
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    to[a-1].append(b-1)
cnt = [0]*n
for i in range(n):
    for j in to[i]:
        cnt[j] += 1
Q = []
for i in range(n):
    if cnt[i] == 0:
        Q.append(i)
f = 0
while len(Q) > 0:
    if len(Q) > 1:
        f = 1
    i = Q[0]
    del Q[0]
    print(i+1)
    for k in to[i]:
        cnt[k] -= 1
        if cnt[k] == 0:
            Q.append(k)
print(1 if f else 0)