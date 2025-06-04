from functools import reduce
from itertools import islice, count

N = int(input())
a = list(map(int, input().split()))

a = sorted(a, reverse=True)

pairs = (i for i in count(1) if i % 2)
indices = list(islice(pairs, len(a)-N-1))

ans = reduce(lambda acc, idx: acc + a[idx], indices, 0)

print(ans)