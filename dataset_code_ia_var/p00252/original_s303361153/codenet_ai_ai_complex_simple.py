from functools import reduce
from operator import mul

s = input().split()
t = tuple(map(int, s))
d = { (1,1,0), (0,0,1) }
ans = {True: "Open", False: "Close" }[reduce(mul, [t in d], 1)]
print(ans)