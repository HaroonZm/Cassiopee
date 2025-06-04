from functools import reduce
from itertools import product, chain

def deep_rem(lst, val):
    # Remove first matching val from list
    try:
        lst.remove(val)
    except ValueError:
        pass

def minmaxupd(tpl, x, y):
    # In-place update for min/max bounds
    return tuple(f(a, b) for f, a, b in zip((min, max, min, max), tpl, (x, x, y, y)))

def intervals(mp):
    # Multi-char bounding
    h, w = len(mp), len(mp[0]) if mp else 0
    rng, order = {}, []
    for y, row in enumerate(mp):
        for x, c in enumerate(row):
            rng[c] = minmaxupd(rng[c], x, y) if c in rng else (x, x, y, y)
            if c not in order: order.append(c)
    return rng, order

def verify_and_paint(mp, key, tpl):
    x1, x2, y1, y2 = tpl
    box = chain.from_iterable(mp[y][x1:x2+1] for y in range(y1, y2+1))
    unique = set(box)
    if unique <= {key, "#"}:
        for y in range(y1, y2+1): mp[y][x1:x2+1] = ["#"]*(x2-x1+1)
        return True
    return False

def main():
    [eval('_') for _ in [(
        lambda n: [
            (lambda h, w, mp:
                (lambda rng, keys:
                    (lambda SAFE=lambda: print("SAFE"), SUSPICIOUS=lambda: print("SUSPICIOUS"):
                        [
                            (
                                lambda progress=[True]:
                                    (lambda inner=
                                        lambda : [
                                            progress.__setitem__(0,False) if verify_and_paint(mp,k,rng[k]) and deep_rem(keys,k) else None
                                            for k in list(keys)
                                        ]:
                                        [inner(), 
                                         progress[0] or SUSPICIOUS() or exit()]
                                    )
                            )()
                            for _ in iter(int,1) if keys and progress.__setitem__(0,True)
                        ] if not keys else SAFE()
                    )()
                )(intervals(mp), [*set(c for row in mp for c in row if c != "#")])
            )(
                *[int(i) if k==0 else int(i) if k==1 else None for k,i in enumerate(input().split())], 
                [list(input()) for _ in range(int(input().split()[0]))]
            )
            for _ in range(int(n))
        ]
    )]) for n in [input()]]

main()