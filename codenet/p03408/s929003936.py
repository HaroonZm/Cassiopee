from collections import Counter

n = int(input())
s = [input() for i in range(n)]
m = int(input())
t = [input() for i in range(m)]

cs = Counter(s)
ct = Counter(t)

ans = -10000
for key, value in cs.items():
    if ct[key] > 0:
        ans = max(ans, value - ct[key])
    else:
        ans = max(ans, value)
for key, value in ct.items():
    if cs[key] > 0:
        ans = max(ans, -value + ct[key])
    else:
        ans = max(ans, -value)

print(ans)