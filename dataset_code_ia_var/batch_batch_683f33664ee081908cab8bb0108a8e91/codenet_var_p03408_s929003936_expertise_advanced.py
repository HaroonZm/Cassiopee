from collections import Counter
from sys import stdin

n = int(stdin.readline())
s = [stdin.readline().rstrip() for _ in range(n)]
m = int(stdin.readline())
t = [stdin.readline().rstrip() for _ in range(m)]

cs, ct = Counter(s), Counter(t)
ans = max((cs[key] - ct[key] for key in cs.keys() | ct.keys()), default=0)
print(ans)