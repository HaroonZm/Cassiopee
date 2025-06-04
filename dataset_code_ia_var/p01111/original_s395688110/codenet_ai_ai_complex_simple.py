from itertools import count, takewhile
from functools import reduce
from operator import mul

def main(n):
    roots = (lambda d: ((1 + d) / 2 if (1 + d) % 2 == 0 else (1 + d) / 2) )((1 + (8*n)**0.5))
    upper = int(roots // 1) + 1
    next(filter(lambda j: (
        lambda s, l: print(s, l) or True
    )(*divmod((n * 2 + j - j*j)//(2*j) if not (n*2 + j - j*j)% (2*j) and (n*2 + j - j*j)// (2*j)> 0 else (None, None), None))
    , (j for j in range(upper, 0, -1))))

while True:
    try:
        n = reduce(mul, map(int, [input()]))
        if not n:
            break
        main(n)
    except:
        break