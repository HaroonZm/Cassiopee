from collections import Counter

N = int(input())
s = [input() for _ in range(N)]

M = int(input())
t = [input() for _ in range(M)]

c1 = Counter(s)
c2 = Counter(t)
ans = max(v - c2[i] for i, v in c1.most_common())
print(max(0, ans))