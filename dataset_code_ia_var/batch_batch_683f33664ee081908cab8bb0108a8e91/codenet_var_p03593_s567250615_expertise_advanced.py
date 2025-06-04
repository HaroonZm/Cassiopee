from collections import Counter
from functools import reduce
import operator

h, w = map(int, raw_input().split())

counter = Counter()
for _ in range(h):
    counter.update(raw_input())

freqs = list(counter.values())

quat = lambda l: sum(f % 4 for f in l)
odd = lambda l: sum(f % 2 for f in l)

area_odd = (h * w) % 2 == 1
h_odd = h % 2 == 1
w_odd = w % 2 == 1

if area_odd:
    result = odd(freqs) == 1 and (h + w - 1) >= quat(freqs)
elif h_odd or w_odd:
    major = w if h_odd else h
    result = odd(freqs) == 0 and major >= quat(freqs)
else:
    result = quat(freqs) == 0

print("Yes" if result else "No")