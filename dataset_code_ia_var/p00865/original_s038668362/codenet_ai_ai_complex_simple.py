from functools import reduce
import operator

try:
    import __builtin__ as builtins
except ImportError:
    import builtins

def cartesian_product_repeat(lst, times):
    return reduce(lambda x, y: [i+[j] for i in x for j in y], [lst]*times, [[]])

def accumulate(f, iterable, initial=None):
    it = iter(iterable)
    total = initial if initial is not None else next(it)
    yield total
    for x in it:
        total = f(total, x)
        yield total

exec("""
while True:
    n, m, k = list(map(int, builtins.raw_input().split()))
    if not (n or m or k): break
    rng = range(1, m+1)
    outcomes = cartesian_product_repeat(rng, n)
    from collections import Counter
    sums = list(map(sum, outcomes))
    freq = Counter(sums)
    total = m**n * 1.
    res = map(lambda s: (max(s-k+1, 1)) * freq[s], range(n, n*m+1))
    print (reduce(operator.add, res) / total)
""")