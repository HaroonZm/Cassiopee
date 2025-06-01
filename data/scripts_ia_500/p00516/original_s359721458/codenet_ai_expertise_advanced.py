n, k = map(int, input().split())
a = [int(input()) for _ in range(n + k)]
from collections import Counter

cnt = Counter(next(j for j in range(n) if a[i] >= a[j]) for i in range(n, n + k))
print(max(cnt.items(), key=lambda x: x[1])[0] + 1)