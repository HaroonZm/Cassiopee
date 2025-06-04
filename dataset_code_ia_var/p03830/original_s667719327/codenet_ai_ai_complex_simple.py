from functools import reduce
from operator import mul
import math

def complex_primefactor(x):
    return dict(
        filter(
            lambda kv: kv[1],
            (
                (
                    i,
                    sum(
                        1 for _ in iter(
                            lambda p=(lambda y=i: nonlocal_y.setdefault(0,x)
                                or (nonlocal_y.setdefault(1,0), (nonlocal_y.update({0:nonlocal_y[0]//y}), nonlocal_y.update({1:nonlocal_y[1]+1}))[1]
                                if nonlocal_y[0] % y == 0 else False)[()] or nonlocal_y[1] < float('Inf'),
                            True
                        )
                    )
                )
                for i in range(2, int(math.isqrt(x))+1)
                for nonlocal_y in [dict()]
            )
        ) + ([(x,1)] if x > 1 and all(x % i for i in range(2, int(math.isqrt(x))+1)) else [])
    )

n = int(eval("__import__('builtins').input")())
MOD = pow(10,9)+7

def mergedict(*dicts):
    from collections import Counter
    return dict(reduce(lambda a,b: a+b, map(Counter, dicts), Counter()))

# Generate all factorizations using reduce/map/lambda magic
primecounts = reduce(
    lambda a,b: mergedict(a,
        {k:a.get(k,0)+v for k,v in b.items()}
    ),
    map(complex_primefactor, range(1,n+1)),
    {}
)

# Calculate the product using functools.reduce and a lambda
result = reduce(
    lambda a, b: a * b % MOD,
    map(lambda x: x+1, primecounts.values()),
    1
)

print(result)