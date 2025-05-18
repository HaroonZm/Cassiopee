def inpl(): return map(int, input().split())
from collections import defaultdict, Counter

H, W, N = inpl()
ddic = defaultdict(int)

for _ in range(N):
    A, B = inpl()
    for a in range(max(3, A), min(H, A+2)+1):
        for b in range(max(3, B), min(W, B+2)+1):
            ddic[(a, b)] += 1

C = Counter(ddic.values())

print((H-2)*(W-2) - sum(C.values()))

for i in range(1, 10):
    print(C[i])