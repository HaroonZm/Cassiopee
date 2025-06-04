from itertools import product, islice, chain

d, e = [input().split() for _ in range(2)]
e = list(chain(e[:3], map(lambda x: e[x], (4, 3)), e[5:]))

def rollings(seq, n):
    return (tuple(seq[i:i + n]) for i in range(len(seq) - n + 1))

t = any(
    any(a == e[0] and b == tuple(e[1:5]) for a, *b in zip(f, *islice(rollings(f * 2, 4), 4)))
    for f in (
        tuple(chain((d[int(j)] for j in p[:3]), (d[int(p[4])], d[int(p[3])]), (d[int(j)] for j in p[5:])))
        for p in ['012345', '152304', '215043', '310542', '402351', '513240']
    )
)
print(('No', 'Yes')[t])