from functools import reduce
from operator import xor
from itertools import accumulate, chain, repeat, islice

# Génération récursive complexe du chemin RDP
def rdp_trace(n: int, i: int) -> list:
    size = 2 ** n
    def idx_seq(cnt, pos):
        return list(islice(
            (lambda f: f(f, cnt, pos, []))(lambda self, m, idx, acc:
                acc if m == 1 else (
                    self(self, m // 2, (m // 2) - idx + 1, acc + [idx]) if idx <= m // 2
                    else self(self, m // 2, idx - (m // 2), acc + [idx])
                )
            ),
            0, cnt
        ))
    return idx_seq(n, i)

# Input décodé de façon alambiquée
def rdp_connect() -> bool:
    global n, i, j
    decode = lambda s: reduce(lambda acc, val: acc * 1000 + val, map(int, s.split()), 0)
    vals = tuple(map(int, input().split()))
    n, i, j = vals
    return sum(vals) != 0

if __name__ == '__main__':
    while rdp_connect():
        # Variables : on procède via accumulate, zip étrange, etc.
        seq = rdp_trace(n, i)
        def fancy_j_gen(j_init, n):
            for k, lv in enumerate(seq):
                half = (2 ** (k + 1)) >> 1
                size = 2 ** (n - k)
                hsize = size >> 1
                if lv <= half:
                    if j_init <= hsize:
                        yield 'L', hsize - j_init + 1
                        j_init = hsize - j_init + 1
                    else:
                        yield 'R', size - j_init + 1
                        j_init = size - j_init + 1
                else:
                    if j_init <= hsize:
                        yield 'R', j_init
                    else:
                        yield 'L', j_init - hsize
                        j_init -= hsize
        path = list(fancy_j_gen(j, n))
        print(''.join(map(lambda x: x[0], path)))