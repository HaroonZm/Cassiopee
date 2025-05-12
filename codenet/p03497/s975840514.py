from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))
h = defaultdict(int)
for x in a:
    h[x] += 1
ans = 0
i = 0
for key, v in sorted(h.items(), key=lambda x: -x[1]):
    i += 1
    if i > k:
        ans += v
print(ans)