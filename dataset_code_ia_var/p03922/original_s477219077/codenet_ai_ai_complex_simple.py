from functools import reduce
from itertools import chain, groupby, product
from operator import mul

n, m = map(int, raw_input().strip().split())
data = list(map(int, raw_input().strip().split()))

ans = 0

elements = set(data)
domain = range(0, max(data)+1)
freq1 = list(map(lambda v: data.count(v), domain))

freq2 = list(map(lambda k: reduce(lambda acc, val: acc + freq1[val], filter(lambda x: x % m == k, domain), 0), range(m)))
freq3 = list(map(lambda k: sum(2 * (freq1[val] // 2) for val in filter(lambda x: x % m == k, domain)), range(m)))

visit = set()
for i in range(m):
    if i in visit:
        continue
    j = (-i) % m
    if (i + i) % m == 0:
        ans += freq2[i] // 2
    elif i != j:
        val = min(freq2[i], freq2[j])
        ans += val
        ans += min(freq3[i], freq2[i] - val) // 2
        ans += min(freq3[j], freq2[j] - val) // 2
        visit.add(i)
        visit.add(j)
    else:
        # should not happen as (i+i)%m==0 handled
        pass

print ans