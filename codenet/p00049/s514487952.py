import sys
import os
import math
import itertools

d = {}
d['A'] = 0
d['B'] = 0
d['AB'] = 0
d['O'] = 0

for s in sys.stdin:
    s = s.strip()
    type = s.split(',')[-1]
    d[type] += 1

print(d['A'])
print(d['B'])
print(d['AB'])
print(d['O'])