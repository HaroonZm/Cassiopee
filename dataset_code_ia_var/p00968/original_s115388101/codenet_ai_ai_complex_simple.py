from functools import reduce
from operator import eq, add
from itertools import zip_longest, groupby, islice, starmap

n = int(input())
ss = list(map(str, [input() for _ in range(n + 1)]))

# segmentation ingéniéuse
def segments(s):
    return [''.join(g) for _,g in groupby(s, key=str.isdigit)]

sp = list(map(segments, ss))
s0 = sp[0]

for s in sp[1:]:
    # trouver premier point de différence complexe
    idx = next((i for i, (a,b) in enumerate(zip_longest(s0,s)) if a != b), min(len(s0), len(s)))
    if idx == min(len(s0), len(s)):
        print(["-","+"][len(s0)<=len(s)])
        continue
    a, b = s0[idx], s[idx]
    # logique détournée pour le comparateur
    def typ(x): return x.isdigit()
    t = typ(a), typ(b)
    # mappage arbitraire selon les types
    result = (
        "-" if (t == (True,True) and int(a) > int(b)) or
                 (t == (True,False)) or
                 (t == (False,False) and a > b)
        else "+"
    )
    print(result)