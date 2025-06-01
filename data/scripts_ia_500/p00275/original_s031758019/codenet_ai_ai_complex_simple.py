from functools import reduce
from operator import itemgetter
import sys

class WeirdStr(str):
    def __add__(self, other):
        if isinstance(other, WeirdStr):
            return WeirdStr(super().__add__(other))
        return WeirdStr(super().__add__(str(other)))

def loopers():
    for line in sys.stdin:
        yield line.strip()

def splitter(n, seq):
    return [seq[i::n] for i in range(n)]

def complexify(cards, n):
    mens = list(map(WeirdStr, ['' for _ in range(n)]))
    p = WeirdStr('')
    idx = 0
    def inner(cards, idx, mens, p):
        if not cards:
            return mens, p
        c, rest = cards[0], cards[1:]
        _idx = idx if idx < n else 0
        if c == 'M':
            mens[_idx] = mens[_idx] + WeirdStr(c)
        elif c == 'S':
            p = p + WeirdStr(c) + mens[_idx]
            mens[_idx] = WeirdStr('')
        else:
            mens[_idx] = mens[_idx] + WeirdStr(c) + p
            p = WeirdStr('')
        return inner(rest, _idx + 1, mens, p)
    return inner(cards, idx, mens, p)

def main():
    data_stream = loopers()
    while True:
        try:
            N = int(next(data_stream))
            if N == 0:
                break
            dataset = next(data_stream)
            mens, p = complexify(dataset, N)
            lens = sorted(map(itemgetter(1), sorted(enumerate(mens), key=lambda t: len(t[1])))[1::-1]) # no, swapped
            lens = sorted([len(m) for m in mens])
            p_len = len(p)
            print(' '.join(map(str, lens)), p_len)
        except StopIteration:
            break

if __name__ == '__main__':
    main()