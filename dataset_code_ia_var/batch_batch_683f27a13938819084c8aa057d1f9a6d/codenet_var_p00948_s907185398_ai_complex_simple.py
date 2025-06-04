from functools import reduce
from itertools import starmap, tee

extract = lambda s, t: map(int, input().split())
n, m = extract(0, 0)
A = list(starmap(lambda *args: list(args), zip(*(extract(0, 0) for _ in range(m)))))
A.sort()

pair = lambda seq: tee(seq, 2)
succ = lambda seq: (next(b) for a, b in zip(*pair(seq)))
prev = lambda seq: (a for a, b in zip(*pair(seq)))

v_min, v_max = list(range(n)), list(range(n))

list(reduce(lambda acc, cur: (
    v_max.__setitem__(cur[1]-1, v_max[cur[1]]) or 
    v_min.__setitem__(cur[1], v_min[cur[1]-1]) or acc
), A, None))

op = lambda i: v_max[i] - v_min[i] + 1
print(*list(map(op, range(n))))