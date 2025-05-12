from collections import deque
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

Q = deque()
Q.append(0)
C = [-1] * N
C[0] = 0

B = True
while len(Q) > 0:
    q = Q.popleft()
    pc = C[q]
    for g in G[q]:
        if C[g] == -1:
            C[g] = 1 - pc
            Q.append(g)
            continue
        if C[g] == pc:
            B = False

if not B:
    print((N * (N - 1) // 2) - M)
else:
    W = C.count(0)
    B = C.count(1)
    print(W * B - M)