from functools import reduce
from operator import add, ge

*nhw_raw, = input(),
nhw = list(map(int, nhw_raw[0].split()))
print(reduce(add,
    map(lambda ab: (
        (lambda conds: int(all(conds)))(
            [ge(x, y) for x, y in zip(ab, nhw[1:])]
        )
    ), 
        (list(map(int, input().split())) for _ in range(nhw[0]))
    )
))