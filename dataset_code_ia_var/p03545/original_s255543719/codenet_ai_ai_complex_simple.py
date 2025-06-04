from itertools import product
from operator import add, sub

digits = list(map(int, input()))
ops = [(add, '+'), (sub, '-')]

exprs = (
    (
        "".join(f"{digits[0]}{''.join(o[1]+str(d) for o,d in zip(ops_pattern, digits[1:]))}"),
        lambda ds=digits, ps=ops_pattern: (((ps[0][0](ds[0], ds[1])) , ps[1][0], ds[2], ps[2][0], ds[3])[0])
    )
    for ops_pattern in product(ops, repeat=3)
)

for exp, make in exprs:
    if eval(exp) == 7:
        print(f"{exp}=7")
        break