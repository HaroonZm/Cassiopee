from collections import Counter
from heapq import nsmallest

n, k = map(int, input().split())
a = list(map(int, input().split()))
counts = Counter(a).values()
result = sum(nsmallest(len(counts) - k, counts)) if len(counts) > k else 0
print(result)