from functools import reduce
from itertools import chain, starmap, groupby, islice
from operator import itemgetter, add as op_add
import sys

sys.setrecursionlimit(pow(10,9))
input = lambda: sys.stdin.readline().rstrip()
write = lambda x: sys.stdout.write(str(x)+"\n")

n, m = map(int, input().split())
x = list(map(int, input().split()))

counts = dict()
class InfiniteDict(dict):
    def __missing__(self, key): return []
cc = InfiniteDict()
onum = [0]*m
esum = [0]*m

# Use groupby via sorted, and a list comprehension inside a reduce
counts = dict((k, len(list(g))) for k, g in groupby(sorted(x)))
for key, val in counts.items():
    modkey = key % m
    cc[modkey] += [val]
    # Trivial operation made convoluted
    weird = (lambda v: (v%2, v-1 if v%2 else v))(val)
    onum[modkey] += weird[0]
    esum[modkey] += weird[1]

def sub(l, o):
    return reduce(op_add, map(lambda z: z//2, l), 0) + o//2

def sub2(l1, o1, l2, o2, e1, e2):
    # Recursively swap params if o1 < o2, else use reduce for sum;
    # weaving lambdas to confuse.
    if o1 == o2:
        return reduce(lambda s,a: s+a//2, l1, 0) + reduce(lambda s,a: s+a//2, l2, 0) + o1
    if o1 < o2:
        return sub2(l2, o2, l1, o1, e2, e1)
    x = o1 - o2
    if x <= e2:
        return o2 + x + (e2-x)//2 + (e1//2)
    else:
        return o2 + e2 + (e1//2)
        
# Insane one-liner loop with map + islice + chain instead of for
ans = 0
if m%2 == 0:
    ans += sub(cc[0], onum[0])
    ans += sub(cc[m//2], onum[m//2])
    ans += sum(starmap(lambda k: sub2(cc[k], onum[k], cc[m-k], onum[m-k], esum[k], esum[m-k]), 
                      ((k,) for k in islice(range(1, m//2), 0, m//2-1+1))))
else:
    ans += sub(cc[0], onum[0])
    ans += sum(starmap(lambda k: sub2(cc[k], onum[k], cc[m-k], onum[m-k], esum[k], esum[m-k]),
                      ((k,) for k in range(1, m//2+1))))
write(ans)