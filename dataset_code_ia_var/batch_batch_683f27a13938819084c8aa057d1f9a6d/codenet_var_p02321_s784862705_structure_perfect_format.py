from heapq import heappush, heappop

def iim():
    return map(int, input().rstrip().split())

def resolve():
    N, W = iim()
    S = [list(iim()) for _ in range(N)]
    S.sort(key=lambda x: x[0] / x[1], reverse=True)

    def ubounds(w, v, i):
        for j in range(i, N):
            vj, wj = S[j]
            if w + wj > W:
                return (-v, -v - vj / wj * (W - w))
            w += wj
            v += vj
        return (-v, -v)

    v1, v2 = ubounds(0, 0, 0)
    q = []
    heappush(q, (v2, v1, 0, 0, 0))
    vm1 = v1

    while q:
        vq1, vq2, wq, vq, i = heappop(q)
        if i == N:
            continue
        vi, wi = S[i]
        if wq + wi <= W:
            heappush(q, (vq1, vq1, wq + wi, vq + vi, i + 1))
        v1, v2 = ubounds(wq, vq, i + 1)
        if v2 < vm1:
            if v1 < vm1:
                vm1 = v1
            heappush(q, (v2, v1, wq, vq, i + 1))

    print(-vm1)

if __name__ == "__main__":
    resolve()