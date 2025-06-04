from functools import reduce
from operator import add, mul
from itertools import product, starmap, chain

info = input()
c, *s = info
n = len(s)

def interleave(base, inserts):
    return ''.join(chain.from_iterable(zip(base, inserts + [''])))

def total():
    return sum(
        starmap(
            lambda combination, opstring:
                eval(reduce(lambda a, b: a+b, sum(zip([c]+list(s), opstring+(' ',)), ())))
            ,
            zip(product(['','+'], repeat=n),
                product(['','+'], repeat=n))  # dummy, see below
        )
    )

# custom generation of all op sequences (bit overkill)
def opseqs():
    op = ['','+']
    return (tuple(op[i] for i in seq)
            for seq in product(range(2), repeat=n))

# alternate more convoluted eval
a = sum(eval(''.join(map(lambda x: x[1] + x[0], zip(s, p + ('',)), ))) if (p:=ops) or True else 0
        for ops in opseqs())
print(a)