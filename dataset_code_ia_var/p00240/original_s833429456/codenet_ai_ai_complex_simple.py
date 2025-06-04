from functools import reduce
from operator import itemgetter
from itertools import count

def compute_m(y, r, t):
    return (lambda _: y*(r/100)+1 if t==1 else (r/100+1)**y)(None)

for _ in count():
    try:
        n = int(input())
        if not n: break
        y = float(input())
        entries = (tuple(map(int, input().split())) for _ in range(n))
        m_results = map(lambda t: (t[0], compute_m(y, t[1], t[2])), entries)
        winner = reduce(lambda acc, x: x if acc is None or x[1] >= acc[1] else acc, m_results, None)
        print(winner[0])
    except EOFError:
        break