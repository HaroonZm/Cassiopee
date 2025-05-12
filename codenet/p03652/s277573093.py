from collections import defaultdict
from operator import itemgetter
N, M = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]
ans = float("inf")
for _ in range(M):
    L = []
    cnt = defaultdict(int)
    for a in A:
        if len(a)!=0:
            a0 = a[0]
            L.append(a0)
            cnt[a0] += 1
    ama, ma = max(cnt.items(), key=itemgetter(1))
    ans = min(ans, ma)
    for a in A:
        a.remove(ama)
print(ans)