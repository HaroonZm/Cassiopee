from functools import reduce
from operator import itemgetter
from bisect import bisect_left
n = int(input())
a = list(map(int, input().split()))
q = int(input())
k = [(*map(int, [input(), [i][0]]),) for i in range(q)]

a = sorted(reduce(lambda x, y: x+[y], a, []))
k = sorted(k, key=itemgetter(0))

ans = list(map(lambda _: n, range(q)))
_ = list(map(lambda z: ans.__setitem__(z[1], bisect_left(a, z[0])), k))
print(*ans, sep='\n')