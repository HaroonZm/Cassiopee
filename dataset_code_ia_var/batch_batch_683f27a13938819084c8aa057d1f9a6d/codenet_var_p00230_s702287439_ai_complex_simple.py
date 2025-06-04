from itertools import cycle, count, repeat, islice, accumulate, takewhile, dropwhile, chain, product
from collections import deque, defaultdict

def fix(alst, blst, floar, buil, n):
    stacks = [alst, blst]
    fun = stacks[buil].__getitem__
    kind = fun(floar)
    # Logical function dict
    jumpers = {
        0: lambda f: f,
        1: lambda f: next(islice((g for g in count(f) if g + 1 == n or fun(g + 1) != 1), 1), f),
        2: lambda f: next(dropwhile(lambda k: fun(k) == 2, count(f, -1)), f)
    }
    return jumpers.get(kind, lambda f: f)(floar)

def search(alst, blst, n):
    que = deque()
    stackz = (alst, blst)
    # Initial fix for both buildings
    roots = tuple(fix(alst, blst, 0, b, n) for b in range(2))
    if n-1 in roots:
        print(0)
        return
    que.extend(((0, roots[0], 0), (0, roots[1], 1)))
    states = defaultdict(lambda: float('inf'))
    states[(roots[0], 0)] = 0
    states[(roots[1], 1)] = 0
    while que:
        c, f, b = que.popleft()
        invb = 1-b # next building
        for delta in (0,1,2):
            nf = f + delta
            if nf >= n:
                break
            kid = fix(alst, blst, nf, invb, n)
            if kid == n-1:
                print(c+1)
                return
            k = (kid, invb)
            if states[k] > c+1:
                states[k] = c+1
                que.append((c+1, kid, invb))
    print("NA")

for k in count():
    n = int(input())
    if not n:
        break
    dat = list(map(int, input().split()))
    dbt = list(map(int, input().split()))
    search(dat, dbt, n)