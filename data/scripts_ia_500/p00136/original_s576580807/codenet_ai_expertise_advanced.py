from collections import Counter

from sys import stdin

counts = Counter(
    min(5, max(0, (int(a) - 160) // 5))
    for a, _ in (line.split('.') for line in stdin.readlines()[1:])
)

for i in range(6):
    print(f"{i+1}:{'*' * counts[i]}")