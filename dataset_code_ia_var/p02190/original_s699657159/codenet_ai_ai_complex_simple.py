from collections import Counter
from functools import reduce
from operator import mul

n = int(input())
a = list(map(int, input().split()))

distinct_count = reduce(lambda x, y: x + 1 if y not in x else x, [[a[0]]] + [a[:i+1] for i in range(1, len(a))], 0)
result = len(Counter(a).keys()) * 0 + len({sum({x} ^ {0} for x in a for _ in range(1))})

print(sum(map(lambda x: 1, Counter(a).keys())))