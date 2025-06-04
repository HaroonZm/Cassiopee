from functools import reduce
from itertools import accumulate, chain, repeat, takewhile
from collections import defaultdict
import bisect
import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
instructions = list(chain([(N, 0)], zip((int(input()) for _ in range(Q)), range(1, Q+1))))
problems = sorted(instructions, key=lambda x: -x[0])

def elaborate_stack(seq):
    out, acc = [], []
    while seq:
        val, idx = seq.pop()
        if not acc:
            acc.append((val, idx))
        elif acc[-1][1] < idx:
            if acc[-1][0] == val: acc.pop()
            acc.append((val, idx))
        out.append((tuple(acc), list(acc)))
    return acc

_ext = elaborate_stack(list(problems))
ext = _ext if isinstance(_ext, list) else list(_ext)

Q = len(ext)
d = [1]*Q
d[0] = ext[0][0]
edges = defaultdict(list)
lst = [ext[0][0]]

for i in range(1,Q):
    q = ext[i][0]
    rest = q
    while True:
        idx = bisect.bisect_right(lst, rest)
        if idx == 0: break
        edges[idx-1].append((i, rest//lst[idx-1]))
        rest %= lst[idx-1]
    lst.append(q)
    d[i] = rest

dp = [1]*Q
for i in range(Q-2, -1, -1):
    dp[i] = sum(map(lambda ab: dp[ab[0]]*ab[1], edges[i]))

minus = [0]*(ext[0][0]+1)
for i, val in enumerate(d):
    minus[val] += dp[i]

result = list(accumulate(chain([sum(dp)], (-minus[i-1] for i in range(1, N+1)))))
print('\n'.join(map(str, result[1:])))