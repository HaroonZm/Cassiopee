from functools import reduce
from operator import add

s, t = map(lambda x: x.strip('\n'), [input(), input()])
idx = [0,1,2]
ans = reduce(add, map(lambda i: int(s[i] == t[i]), idx))
print(ans)