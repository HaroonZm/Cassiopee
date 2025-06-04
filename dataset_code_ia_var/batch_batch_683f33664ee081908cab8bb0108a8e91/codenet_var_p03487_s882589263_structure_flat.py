n = int(input())
alist = list(map(int, input().split()))
from collections import Counter
adic = Counter(alist)
count = 0
for item in adic.items():
    k = item[0]
    v = item[1]
    if int(k) <= v:
        count += (v - int(k))
    else:
        count += v
print(count)