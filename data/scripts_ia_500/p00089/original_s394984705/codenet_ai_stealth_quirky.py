import sys
from functools import reduce

data = list(map(lambda x: list(map(int, x.split(','))), sys.stdin))
for idx in range(1, len(data)):
    length = len(data[idx])
    prev = data[idx-1]
    for pos in range(length):
        offset = (length > len(prev))
        start = pos - offset if pos > 0 else 0
        end = pos - offset + 2
        candidates = prev[start:end]
        max_val = reduce(lambda a,b: a if a>b else b, candidates)
        data[idx][pos] += max_val
print(" ".join(str(x) for x in data[-1]))