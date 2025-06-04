from functools import reduce
from itertools import accumulate, chain, islice, tee
import operator

def orderN(N, L, ices):
    def peekable(iterable):
        it1, it2 = tee(iterable)
        next(it2, None)
        return zip(it1, chain(islice(it2, N-1), [None]))

    up, down = L - ices[0], L - ices[0]
    peaks = []
    add = peaks.append

    def combine(x, i, flag):
        return x + (L - ices[i+1]) if i + 1 < N else x

    def process():
        state = (up, down)
        indices = range(len(ices))
        ops = []
        for i, nxt in peekable(indices):
            if nxt is not None:
                if ices[i] < ices[nxt]:
                    add(state[1])
                    state = (state[0] + L - ices[nxt], L - ices[nxt])
                else:
                    add(state[0])
                    state = (L - ices[nxt], state[1] + L - ices[nxt])
            else:
                add(state[0])
                add(state[1])
        return peaks

    print(max(process()))

N, L = map(int, raw_input().split())
ices = list(map(int, [raw_input() for _ in range(N)]))

orderN(N, L, ices)