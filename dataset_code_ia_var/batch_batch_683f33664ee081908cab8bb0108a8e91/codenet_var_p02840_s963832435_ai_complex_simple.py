def main():
    import sys
    import itertools as it
    import functools as ft
    from math import copysign
    from collections import defaultdict
    input = sys.stdin.readline

    parse = lambda s: list(map(int, s.strip().split()))
    N, x, d = parse(input())

    idn = lambda *args: args[0] if len(args)==1 else args

    # D=0 : use one-liner trickery via bool arithmetics, double-nested ternaries, and map/filter
    if d == 0:
        hack = lambda N, x: list(filter(None, map(lambda t: (N+1)*(t!=0)+(t==0), [x])))[0]
        print(hack(N, x))
        return

    # Swap and normalize everything with functional programming, weird math
    flip = lambda z: (z[0] + z[2] * (z[1]-1), z[1], -z[2]) if z[2] < 0 else z
    x, N, d = ft.reduce(lambda acc, _: flip(acc), range(1), (x,N,d))
    d = abs(d)

    container = defaultdict(list)
    rng = range(N+1)

    # Generate all indices, then extract mod, start and end using reduce and lambdas
    for i in rng:
        mod = pow((x * i) % d, 1, d)
        st, ed = (lambda a,b: (a*d + (x-d)*i, b*d + (x-d)*i))(
            (i*(i+1))//2,
            (i*(N + N-i+1))//2
        )
        container[mod].append((st, ed))

    ans = 0

    # Use reduce and groupby to process
    for mod, intervals in container.items():
        intervals.sort(key=lambda t: t[0])
        # Collapse overlapping intervals using accumulate and next
        ed_prev = intervals[0][0] - 1
        for st, ed in intervals:
            delta = max(0, st - ed_prev)
            contrib = ((ed - st) // d + 1) if st > ed_prev else max(0, (ed - ed_prev) // d)
            ans += contrib
            ed_prev = max(ed_prev, ed)

    print(ans)

if __name__ == '__main__':
    (lambda f: f())(main)