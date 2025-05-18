import sys

N, R = map(int, input().split())
if 2*R > N:
    R = N - R
P = [0] + list(map(int, input().split()))

L = []
used = [False]*(N+1)
pre = 0
for i in range(1, N+1):
    cnt = 0
    while not used[i]:
        used[i] = True
        cnt += 1
        i = P[i]
    if cnt:
        L.append(cnt)
table = [0]*(N+1)
for l in L:
    table[l] += 1
L = []
for i in range(N//2, 0, -1):
    x = table[i]
    if not x:
        continue
    if x == 1:
        L.append(i)
    else:
        p = 1 
        while p+p <= x:
            L.append(p*i)
            p = p+p
        if x - p + 1:
            L.append(i*(x - p + 1))
L = [l for l in L if l <= R]
L.sort()
H = 1
for l in L:
    H = H|(H<<l)
if H & 1<<R:
    print('Yes')
else:
    print('No')