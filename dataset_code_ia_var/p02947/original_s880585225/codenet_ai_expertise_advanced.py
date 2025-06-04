from collections import Counter
from sys import stdin

s = [line.rstrip() for line in stdin.readlines()[1:]]
counter = Counter(map(lambda x: ''.join(sorted(x)), s))
print(sum(v * (v - 1) // 2 for v in counter.values()))