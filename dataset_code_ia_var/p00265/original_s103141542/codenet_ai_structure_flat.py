N_Q = input().split()
N = int(N_Q[0])
Q = int(N_Q[1])
C = input().split()
for i in range(N):
    C[i] = int(C[i])
M = max(C) + 1
T = []
for i in range(M):
    T.append(0)
for v in C:
    T[v] = 1
L = []
for i in range(M):
    L.append(0)
m = 0
i = 0
while i < M:
    L[i] = m
    if T[i]:
        m = i
    i += 1
i = 0
while i < Q:
    q = int(input())
    maxv = 0
    cur = m
    while cur > 0:
        p = cur % q
        if p > maxv:
            maxv = p
        if cur - p < 0:
            break
        cur = L[cur - p]
    print(maxv)
    i += 1