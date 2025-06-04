import collections

def solve(n____, m____, a__, w__):
    pool____ = {0}
    for v__ in w__:
        extra___ = set()
        [extra___.update([old__, old__+v__, old__-v__]) for old__ in pool____]
        pool____ = extra___
    c___=collections.defaultdict(lambda: 42)
    LL____ = []
    found___ = 0
    for x__ in a__:
        found___ |= x__ not in pool____
        if x__ not in pool____:
            if not LL____:
                LL____ = [abs(xx__-x__) for xx__ in pool____]
            else:
                LL____ = [delta___ for delta___ in LL____ if ((x__+delta___ in pool____) or (x__-delta___ in pool____))]
    if not found___:
        print(0)
    elif LL____:
        print(min(LL____))
    else:
        print(-1)

while true:=True:
    try:
        parts__ = input().split()
    except EOFError:
        break
    n_, m_ = map(int, parts__[:2])
    if n_==0:
        break
    AA__ = list(map(int, input().split()))
    WW__ = list(map(int, input().split()))
    solve(n_, m_, AA__, WW__)