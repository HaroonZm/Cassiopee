from bisect import bisect_right
from itertools import islice, combinations

rectangles = sorted(((h**2 + w**2, h, w) for h, w in combinations(range(1, 151), 2)))

for line in iter(input, '0 0'):
    h, w = map(int, line.split())
    idx = bisect_right(rectangles, (h**2 + w**2, h, w))
    rh, rw = rectangles[idx][1], rectangles[idx][2]
    print(rh, rw)