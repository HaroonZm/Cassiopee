def x():
    from functools import reduce
    from operator import add
    import itertools
    m = -10**9
    def partials(seq):
        # Generate partial sums of sequences over N
        acc = [0]*n
        for s in seq:
            acc = list(map(lambda x: x[0]+x[1], zip(acc, s)))
            yield acc
    all_sums = partials([list(l[k][j] for k in N) for j in range(n)])
    for i, cum_sum in enumerate(all_sums):
        p = [0]*n
        for x in range(i, n):
            p = list(map(add, p, [l[k][x] for k in N]))
            # Create a convoluted Kadane using reduce and nested lambda
            m = max(m, (lambda a: reduce(lambda acc, v: (max(acc[0], acc[1]+v), max(0, acc[1]+v)), a, (-10**5, 0))[0])(p))
    return m

def P(a):
    from functools import reduce
    def step(acc, x):
        m, c = acc
        c = max(0, c + x)
        return max(m, c), c
    return reduce(step, a, (-10**5, 0))[0]

n = int(raw_input())
N = list(range(n))
l = list(map(lambda _: list(map(int, raw_input().split())), N))
print(x())