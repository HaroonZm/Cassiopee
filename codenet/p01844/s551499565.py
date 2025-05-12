import sys
readline = sys.stdin.readline
write = sys.stdout.write
def rotate(H, W, R0):
    R1 = [[0]*H for i in range(W)]
    for i in range(H):
        for j in range(W):
            R1[W-1-j][i] = R0[i][j]
    return R1
def make(H, W, R0):
    R1 = [[0]*(W+1) for i in range(H+1)]
    for i in range(H):
        c = 0
        for j in range(W):
            c += R0[i][j]
            R1[i+1][j+1] = c + R1[i][j+1]
    return R1

def solve():
    H, W, N = map(int, readline().split())
    S = [list(map(int, readline().split())) for i in range(H)]
    su = sum(map(sum, S))
    ans = 0
    if N == 2:
        T = make(H, W, S)
        for i in range(H+1):
            e = T[i][W]
            ans = max(ans, min(e, su-e))
        for i in range(W+1):
            e = T[H][i]
            ans = max(ans, min(e, su-e))
    elif N == 3:
        for t in range(4):
            T = make(H, W, S)
            for i in range(H+1):
                e0 = T[i][W]
                for j in range(W+1):
                    e1 = T[H][j] - T[i][j]
                    ans = max(ans, min(e0, e1, su - e0 - e1))
            if t < 2:
                for i in range(W+1):
                    e0 = T[H][i]
                    for j in range(i, W+1):
                        e1 = T[H][j]
                        ans = max(ans, min(e0, e1-e0, su-e1))
            S = rotate(H, W, S)
            H, W = W, H
    else:
        for t in range(4):
            T = make(H, W, S)
            for i in range(H+1):
                for j in range(W+1):
                    e0 = T[i][j]
                    if e0 < ans:
                        continue
                    k1 = 0
                    while k1 < H and T[k1][W] - T[k1][j] < e0:
                        k1 += 1
                    k2 = 0
                    while k2 < W and T[H][k2] - T[i][k2] < e0:
                        k2 += 1
                    if i < k1 and j < k2:
                        continue
                    if k1 <= i and k2 <= j:
                        v1 = su - T[H][k2] - T[i][W] + T[i][k2]
                        v2 = su - T[k1][W] - T[H][j] + T[k1][j]
                        if max(v1, v2) >= e0:
                            ans = max(e0, ans)
                    else:
                        v1 = su - T[H][k2] - T[k1][W] + T[k1][k2]
                        if v1 >= e0:
                            ans = max(e0, ans)
            for i in range(W, -1, -1):
                e0 = T[H][i]
                if e0 <= ans:
                    break
                for j in range(i, W+1):
                    e = T[H][j]
                    e1 = e - e0; e2 = su - e
                    if e1 <= ans or e2 <= ans:
                        continue
                    for k in range(j, W+1):
                        f = T[H][k]
                        if su-f <= ans:
                            break
                        ans = max(ans, min(e0, e1, f-e, su-f))
                    for k in range(H+1):
                        f = T[k][j] - T[k][i]
                        if e1-f <= ans:
                            break
                        ans = max(ans, min(e0, f, e1-f, e2))
                    for k in range(H+1):
                        f = T[k][W] - T[k][j]
                        if e2-f <= ans:
                            break
                        ans = max(ans, min(e0, e1, f, e2-f))
                for j in range(H+1):
                    e1 = T[j][W] - T[j][i]
                    e2 = su - e1 - e0
                    if e1 <= ans or e2 <= ans:
                        continue
                    for k in range(i, W+1):
                        f = T[j][k] - T[j][i]
                        if e1-f <= ans:
                            break
                        ans = max(ans, min(e0, f, e1-f, e2))
                    for k in range(i, W+1):
                        f = T[H][k] - e0 - T[j][k] + T[j][i]
                        if e2-f <= ans:
                            break
                        ans = max(ans, min(e0, e1, f, e2-f))
                for j in range(H, -1, -1):
                    e1 = T[j][W] - T[j][i]
                    if su - e0 - e1 <= ans:
                        continue
                    if e1 <= ans:
                        break
                    for k in range(j, H+1):
                        e2 = T[k][W] - T[k][i]
                        if su-e2-e0 <= ans:
                            break
                        ans = max(ans, min(e0, e1, e2-e1, su-e2-e0))
            S = rotate(H, W, S)
            H, W = W, H
    write("%d\n" % ans)
solve()