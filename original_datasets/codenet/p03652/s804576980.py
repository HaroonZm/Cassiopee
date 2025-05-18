from collections import defaultdict

N, M = map(int, input().split())
INF = float('inf')

A = [tuple(map(int, input().split())) for _ in range(N)]

def search(sports):
    if not sports:
        return INF

    cnt = [0] * (M + 1)
    for a in A:
        for p in a:
            if p in sports:
                cnt[p] += 1
                break

    ret = max(cnt)
    maxSport = cnt.index(ret)
    sports.remove(maxSport)

    return min(ret, search(sports))

ans = search(set(list(range(1, M + 1))))
print(ans)