from collections import Counter
n = int(input())
v = list(map(int, input().split()))
v1 = []
i = 0
while i < n:
    v1.append(v[i])
    i += 2
v2 = []
i = 1
while i < n:
    v2.append(v[i])
    i += 2
cc1 = Counter()
for x in v1:
    cc1[x] += 1
c1 = sorted(cc1.items(), key=lambda x: -x[1])
cc2 = Counter()
for x in v2:
    cc2[x] += 1
c2 = sorted(cc2.items(), key=lambda x: -x[1])
if c1[0][0] != c2[0][0]:
    print(n - c1[0][1] - c2[0][1])
if c1[0][0] == c2[0][0]:
    if len(c1) == 1 and len(c2) == 1:
        print(n // 2)
    if len(c1) == 1 and len(c2) != 1:
        print(n - c1[0][1] - c2[1][1])
    if len(c2) == 1 and len(c1) != 1:
        print(n - c1[1][1] - c2[0][1])
    if len(c1) > 1 and len(c2) > 1:
        x1 = c1[1][1] + c2[0][1]
        x2 = c1[0][1] + c2[1][1]
        m = max(x1, x2)
        print(n - m)