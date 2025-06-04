from heapq import heappush, heappop, heapify
import sys
readline = sys.stdin.readline
write = sys.stdout.write

N = int(readline())
S = readline().strip()
L = len(S)
S += "+"
if L % 2 == 0 and N < 10:
    write("-1\n")
else:
    pw10 = [1]*11
    for i in range(10):
        pw10[i+1] = pw10[i] * 10
    INF = N + 1
    dist = [[INF]*(L+2) for _ in range(L+1)]
    ques = [[] for _ in range(L+1)]
    ques[0] = [(0, 0)]
    dist[0][0] = 0
    found = False
    for k in range(L+1):
        que = ques[k]
        dist0 = dist[k]
        heapify(que)
        while que:
            cost, i = heappop(que)
            if dist0[i] < cost or i > L:
                continue
            p = S[i]
            if i+1 != L-1:
                if p != "+":
                    v = int(p)
                    if S[i+1] != '+':
                        if cost + v < dist[k+1][i+2]:
                            dist[k+1][i+2] = cost + v
                            ques[k+1].append((cost + v, i+2))
                    else:
                        if cost + v < dist0[i+2]:
                            dist0[i+2] = cost + v
                            heappush(que, (cost + v, i+2))
                if p != "0":
                    nk = k + 1 + (S[i+1] != "+")
                    if cost < dist[nk][i+2]:
                        dist[nk][i+2] = cost
                        ques[nk].append((cost, i+2))
            # inline calc
            for delta_c0, delta_p in [(0, p), (1, "1")]:
                if (delta_p == p and p not in "0+") or (delta_p == "1" and p != "1"):
                    for j in range(i+2, min(i+10, L+1)):
                        if j == L-1:
                            continue
                        p1 = delta_p + S[i+1:j]
                        l = j - i
                        c = delta_c0 + p1.count("+")
                        v = int(p1.replace("+", "0"))
                        if v <= N:
                            nk = k + c + (S[j] != '+')
                            if cost + v < dist[nk][j+1]:
                                dist[nk][j+1] = cost + v
                                ques[nk].append((cost + v, j+1))
                        b = pw10[l-2]
                        cc = c
                        vv = v
                        for e in range(l-2, -1, -1):
                            a = (vv // b) % 10
                            if a:
                                vv2 = vv - a * b
                                cc2 = cc + 1
                                if vv2 <= N:
                                    nk2 = k + cc2 + (S[j] != '+')
                                    if cost + vv2 < dist[nk2][j+1]:
                                        dist[nk2][j+1] = cost + vv2
                                        ques[nk2].append((cost + vv2, j+1))
                                vv = vv2
                                cc = cc2
                            b //= 10
        if dist0[L+1] <= N:
            write("%d\n" % k)
            found = True
            break
    if not found:
        pass