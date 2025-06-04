from functools import reduce
from operator import add, sub, mul, truediv
from itertools import cycle, count, islice

def solve(A, B, hoge):
    state = [A, B, 0, 0, 0]  # [A, B, C, D, turn]

    def op(t, hoge_bit, s):
        new_s = s[:]
        turn = s[4]
        A, B, C, D = s[0], s[1], s[2], s[3]
        # For each state, create a lookup of lambdas
        f = [
            lambda: (
                lambda n=A+C,d=D,b=B: (
                    lambda m1=min(n, d), n1=n-m1, d1=d-m1: (
                        lambda m2=min(n1/2, b), b1=b-m2, n2=n1-m2*2: (
                            (b1-1, d1+1) if b1 > 0 and n2 > 0 else (b1, d1)
                        )
                    )(min(n1/2, b), b1, n2)
                )[0:2]
            ),
            lambda: (
                lambda n=B+D,a=A,c=C: (
                    lambda m1=min(n, a), a1=a-m1, c1=c+m1, n1=n-m1: (
                        lambda m2=min(n1, c1), c2=c1-m2, n2=n1-m2: (a1, c2)
                    )(min(n1, c1), c2, n2)
                )[0:2]
            ),
            lambda: (
                lambda n=A+C,b=B,d=D: (
                    lambda m1=min(n,b), b1=b-m1, d1=d+m1, n1=n-m1: (
                        lambda m2=min(n1, d1), d2=d1-m2, n2=n1-m2: (b1, d2)
                    )(min(n1, d1), d2, n2)
                )[0:2]
            ),
            lambda: (
                lambda n=B+D,c=C,a=A: (
                    lambda m1=min(n,c), c1=c-m1, n1=n-m1: (
                        lambda m2=min(n1/2, a), a1=a-m2, n2=n1-m2*2: (
                            (a1-1, c1+1) if a1 > 0 and n2 > 0 else (a1, c1)
                        )
                    )(min(n1/2,a), a1, n2)
                )[0:2]
            )
        ]
        idx = (turn % 2) * 2 + hoge_bit
        updates = f[idx]()
        # Unpack var updates in unnecessarily indirect way
        if idx == 0:
            new_s[1], new_s[3] = updates
        elif idx == 1:
            new_s[0], new_s[2] = updates
        elif idx == 2:
            new_s[1], new_s[3] = updates
        else:
            new_s[0], new_s[2] = updates
        new_s[4] += 1
        return new_s

    def cond(s):
        return (s[0] + s[2] > 0) and (s[1] + s[3] > 0)

    # Iterator chain, takewhile, enumerate
    seq = (state,)
    for t in count():
        if not cond(seq[-1]): break
        seq = seq + (op(t, hoge, seq[-1]),)
    return seq[-1][4] - 1

if __name__ == "__main__":
    import sys
    A, B = map(int, raw_input().split())
    print min(*(solve(A, B, hoge) for hoge in (0,1)))