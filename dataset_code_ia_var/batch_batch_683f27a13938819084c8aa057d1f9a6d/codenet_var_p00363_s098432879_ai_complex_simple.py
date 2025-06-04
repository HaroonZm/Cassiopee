from functools import reduce
from operator import add
w, h, a = map(lambda x: int(x) if x.isdigit() else x, input().split())
matrix = [[
    (lambda y: 
        (lambda s: reduce(add, s))
        (["+"] + ["-" for _ in range(w - 2)] + ["+"])
    )(i)
    if i in {0, h-1}
    else 
    (
        (lambda middle:
            reduce(add, ["|"] + 
                   ["." for _ in range((w-2)//2)] + 
                   [a] + 
                   ["." for _ in range((w-2)//2)] + 
                   ["|"])
        )(i)
        if i == h//2 else 
        reduce(add, ["|"] + ["." for _ in range(w-2)] + ["|"])
    )
    for i in range(h)
][i] for i in range(h)]
print('\n'.join(matrix))