from collections import Counter
from heapq import nlargest

n, k = map(int, input().split())
b = list(map(int, input().split()))
counter = Counter(b)
balls = sum(nlargest(k, counter.values()))
print(n - balls)