from collections import deque
import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    H, W, R, C = map(int, readline().split()); R -= 1; C -= 1
    if H == W == 0:
        return False
    G0 = [[] for i in range(H*W+1)]
    G1 = [[] for i in range(H*W+1)]
    g = H*W
    for i in range(H):
        *s, = map(int, readline().split())
        k = W*i
        if i:
            for j in range(W):
                if s[j]:
                    G1[k+j].append(k+j-W)
                    G1[k+j-W].append(k+j)
                else:
                    G0[k+j].append(k+j-W)
                    G0[k+j-W].append(k+j)
        else:
            for j in range(W):
                if s[j]:
                    G1[j].append(g)
                    G1[g].append(j)
                else:
                    G0[j].append(g)
                    G0[g].append(j)
        *s, = map(int, readline().split())
        for j in range(W-1):
            if s[j+1]:
                G1[k+j].append(k+j+1)
                G1[k+j+1].append(k+j)
            else:
                G0[k+j].append(k+j+1)
                G0[k+j+1].append(k+j)
        if s[0]:
            G1[k].append(g)
            G1[g].append(k)
        else:
            G0[k].append(g)
            G0[g].append(k)
        if s[W]:
            G1[k+W-1].append(g)
            G1[g].append(k+W-1)
        else:
            G0[k+W-1].append(g)
            G0[g].append(k+W-1)
    *s, = map(int, readline().split())
    k = (H-1)*W
    for j in range(W):
        if s[j]:
            G1[k+j].append(g)
            G1[g].append(k+j)
        else:
            G0[k+j].append(g)
            G0[g].append(k+j)

    u0 = [0]*(H*W+1)
    u1 = [0]*(H*W+1)
    u0[g] = u1[g] = 1
    que = deque([g])
    while que:
        v = que.popleft()
        for w in G0[v]:
            if u0[w]:
                continue
            if u1[w]:
                que.append(w)
            u0[w] = 1
        for w in G1[v]:
            if u1[w]:
                continue
            if u0[w]:
                que.append(w)
            u1[w] = 1
    if u0[R*W + C]:
        write("Yes\n")
    else:
        write("No\n")
    return True
while solve():
    ...