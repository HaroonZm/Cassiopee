from sys import stdin
from collections import Counter

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
prefix_counters = [Counter()]
for num in a:
    prefix_counters.append(prefix_counters[-1] + Counter([num]))

q = int(stdin.readline())
for _ in range(q):
    b, e, k = map(int, stdin.readline().split())
    print(prefix_counters[e][k] - prefix_counters[b][k])