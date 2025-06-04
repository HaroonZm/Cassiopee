from sys import stdin

def compress_ranges(seq):
    from itertools import groupby, count
    for _, group in groupby(enumerate(seq), lambda x: x[1] - x[0]):
        group = list(group)
        yield group[0][1], group[-1][1]

for line in stdin:
    n = int(line)
    if n == 0:
        break
    p = list(map(int, stdin.readline().split()))
    result = []
    for start, end in compress_ranges(p):
        result.append(f"{start}" if start == end else f"{start}-{end}")
    print(" ".join(result))