from itertools import combinations
from collections import Counter
import bisect

N, K, L, R, *A = map(int, open(0).read().split())

def subset_sums(arr, up_to):
    counters = [Counter([0])]
    for _ in range(up_to):
        nxt = Counter()
        for prev in counters[-1]:
            for a in arr:
                nxt[prev + a] += counters[-1][prev]
        counters.append(nxt)
    return counters

def optimized_make(arr, K):
    res = [Counter()]
    res[0][0] = 1
    for _ in range(K):
        new = Counter(res[-1])
        for key in res[-1]:
            for a in arr:
                new[key + a] += res[-1][key]
        res.append(new)
    return res

def all_subset_sums(arr, kmax):
    tables = [Counter({0:1})]
    for _ in range(kmax):
        table = Counter()
        for s, cnt in tables[-1].items():
            for a in arr:
                table[s+a] += cnt
        tables.append(table)
    return tables

# Actually, original code only uses up to combinations, that's enough.
def subset_counter(x, kmax):
    res = [Counter()]
    res[0][0] = 1
    for a in x:
        for t in range(min(len(res)-1, kmax), -1, -1):
            res.append(Counter())
            for s in res[t]:
                res[t+1][s+a] += res[t][s]
    # Trim extras
    return [Counter({s:v for s,v in d.items()}) for d in res[:kmax+1]]

P = [Counter() for _ in range(K+1)]
Q = [Counter() for _ in range(K+1)]
half = N//2
partA = A[:half]
partB = A[half:]

for k in range(K+1):
    P[k].update(map(sum, combinations(partA, k)))
    Q[k].update(map(sum, combinations(partB, k)))

ans = 0
for i in range(K+1):
    p = P[i]
    q = Q[K-i]
    q_items = sorted(q.items())
    sums = [x for x, _ in q_items]
    counts = [v for _, v in q_items]
    prefix = [0]
    for v in counts:
        prefix.append(prefix[-1] + v)
    for pv, pc in p.items():
        low = bisect.bisect_left(sums, L - pv)
        high = bisect.bisect_right(sums, R - pv)
        ans += pc * (prefix[high] - prefix[low])
print(ans)