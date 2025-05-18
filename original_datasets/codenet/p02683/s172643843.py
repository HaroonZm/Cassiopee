*o, = open(0)

import numpy as np

(n, m, x), *ca = map(lambda x: np.array(list(map(int, x.split()))), o)

INF = 1 << 31

ans = INF

for i in range(2**n):
    tmp = np.zeros(m+1, int)
    sel = []
    for j, dig in enumerate(bin(i)[2:][::-1]):
        if int(dig):
            tmp += ca[j]
            sel.append(j)
    if min(tmp[1:]) >= x:
        ans = min(ans, tmp[0])
        

if ans == INF:
    print(-1)
else:
    print(ans)