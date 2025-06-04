from functools import reduce
from itertools import accumulate, islice, repeat, chain

def meta_transform(n, a):
    A = [a]
    S = 2 ** n
    for i in range(n):
        x = A[-1]
        lim = [S // (2**k) for k in range(1, 4)]
        M = (
            (1, lim[0], lambda _: lim[0] * 2 - x + 1),
            (lim[0]+1, lim[1], lambda _: lim[1] - x + 1),
            (lim[1]+1, lim[2]*3//2, lambda _: x - lim[1]),
            (lim[2]*3//2+1, S, lambda _: x - lim[2]*3//2 + lim[0])
        )
        f = next(f for lo, hi, f in M if lo <= x <= hi)
        A.append(f(x))
        S //= 2
    return list(reversed(A))

def labelify(n, ref_lst, b):
    L, S = '', 2**n
    for i, ref in enumerate(islice(ref_lst, 1, None)):
        pick = (
            (b <= S // 2, ref <= 2**(i+1)//2, lambda: S // 2 - b + 1, 'L', 'R'),
            (b > S // 2, ref <= 2**(i+1)//2, lambda: S - b + 1, 'R', 'L'),
            (True, ref > 2**(i+1)//2, lambda: b - S // 2, 'L', 'R')
        )
        for check1, check2, mod, ch1, ch2 in pick[:2]:
            if check1 and check2:
                b = mod()
                L += ch1
                break
            elif check1 and not check2:
                L += ch2
                break
        else:
            b = pick[2][2]()
            L += pick[2][3]
        S //= 2
    return L

def do_all():
    from sys import stdin
    for z in iter(lambda: tuple(map(int, input().split())), (0,0,0)):
        n, a, b = z
        ref_seq = meta_transform(n, a)
        print(labelify(n, ref_seq, b))
do_all()