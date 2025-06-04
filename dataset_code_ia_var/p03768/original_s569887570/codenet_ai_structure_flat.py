from collections import deque

N, M = map(int, input().split())
ab = []
i = 0
while i < N:
    ab.append([])
    i += 1

i = 0
while i < M:
    a, b = map(int, input().split())
    ab[a-1].append(b-1)
    ab[b-1].append(a-1)
    i += 1

Q = int(input())
vdc = []
i = 0
while i < Q:
    line = input().split()
    vdc.append([int(line[0]), int(line[1]), int(line[2])])
    i += 1

C = []
D = []
i = 0
while i < N:
    C.append(0)
    D.append(-1)
    i += 1

i = Q - 1
while i >= 0:
    v = vdc[i][0]
    d = vdc[i][1]
    c = vdc[i][2]
    q = deque()
    q.append((v - 1, d, c))
    while q:
        temp = q.popleft()
        cv = temp[0]
        cd = temp[1]
        cc = temp[2]
        if D[cv] >= cd:
            continue
        D[cv] = cd
        if C[cv] == 0:
            C[cv] = cc
        j = 0
        while j < len(ab[cv]):
            nv = ab[cv][j]
            q.append((nv, cd - 1, cc))
            j += 1
    i -= 1

i = 0
while i < N:
    print(C[i])
    i += 1