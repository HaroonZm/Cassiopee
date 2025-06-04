from collections import deque

N = int(input())
H = W = 4
S = 1 << 16
P = [list(map(int, input().split())) for _ in range(N)]
C = [input() for _ in range(H)]
I = "RGB".index
ps = set()
for i in range(N):
    h, w = P[i]
    for y in range(1 - h, H):
        py = max(0, y)
        sh = min(H, y + h) - py
        for x in range(1 - w, W):
            px = max(0, x)
            sw = min(W, x + w) - px
            ps.add((px, py, sw, sh))

L = len(ps)
M = [0] * L
V = [None] * L
for l, (x, y, w, h) in enumerate(ps):
    s = S - 1
    b = 0
    v = [0] * 3
    for i in range(h):
        for j in range(w):
            k = 1 << ((y + i) * W + (x + j))
            s ^= k
            c = I(C[y + i][x + j])
            v[c] |= k
    M[l] = s
    V[l] = v

U = [-1] * S
que = deque([0])
U[0] = 0
while que:
    state = que.popleft()
    d = U[state]
    for i in range(L):
        n_state = state & M[i]
        for v in V[i]:
            if not v:
                continue
            if U[n_state | v] != -1:
                continue
            U[n_state | v] = d + 1
            que.append(n_state | v)

print(U[S - 1])