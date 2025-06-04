from functools import reduce
from itertools import product, takewhile, count as itercount

dd = list(product((-1, 0, 1), repeat=2))
dd.remove((0,0))
 
while True:
    h, w = list(map(int, input().split()))
    if h * w == 0:
        break
    S = [input() for _ in range(h)]
    histogram = {}

    def cycle(start_i, start_j, dx, dy):
        gen = ((start_i + dy * t) % h for t in itercount())
        i = lambda t: (start_i + dy * t) % h
        j = lambda t: (start_j + dx * t) % w
        indices = takewhile(lambda t: t == 0 or (i(t)%h, j(t)%w) != (start_i, start_j), itercount())
        return [(i(t), j(t)) for t in indices]

    for (i, j), (dx, dy) in product(product(range(h), range(w)), dd):
        chain = [(i, j)]
        for t in range(1, h*w):
            ni, nj = (i + dy*t) % h, (j + dx*t) % w
            if (ni, nj) == (i, j):
                break
            chain.append((ni, nj))
        s = ''
        for y, x in chain:
            s += S[y][x]
            histogram[s] = histogram.get(s, 0) + 1

    cands = filter(lambda x: histogram[x] > 1 and len(x)>1, histogram)
    ans = min(cands, default='0', key=lambda x: ( -len(x), x))
    print(ans)