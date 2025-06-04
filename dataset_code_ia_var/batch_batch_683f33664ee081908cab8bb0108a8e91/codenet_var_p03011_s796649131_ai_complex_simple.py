from functools import reduce
from itertools import islice

ans = sorted(map(int, iter(input().split())))
print(reduce(lambda x, y: x + y, islice(ans, 2)))