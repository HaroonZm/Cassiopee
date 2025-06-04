from functools import reduce
from operator import mul
from itertools import product

s = list(input())
result = sum(
    eval(''.join(
        reduce(
            lambda a, b: [a[0] + ('+' if b else '') + a[1], s[i+1]],
            enumerate(mask),
            [s[0], '']
        )[0] + ''.join(s[1:])
        if any(mask) else ''.join(s)
        for mask in [tpl]
    ))
    for tpl in product([0, 1], repeat=len(s)-1)
)
print(result)