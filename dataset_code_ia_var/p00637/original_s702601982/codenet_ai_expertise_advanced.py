from sys import stdin
from itertools import groupby, count

def group_consecutive(nums):
    for _, g in groupby(enumerate(nums), lambda ix: ix[0] - ix[1]):
        seq = list(map(lambda x: x[1], g))
        yield seq[0], seq[-1]

lines = stdin.read().splitlines()
it = iter(lines)

while True:
    n = int(next(it))
    if n == 0:
        break
    line = list(map(int, next(it).split()))
    result = []
    for start, end in group_consecutive(line):
        if start == end:
            result.append(f"{start}")
        else:
            result.append(f"{start}-{end}")
    print(' '.join(result))