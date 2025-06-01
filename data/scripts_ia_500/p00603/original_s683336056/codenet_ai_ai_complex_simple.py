import sys
from functools import reduce
from operator import itemgetter

class DeckManipulator:
    def __init__(self, n):
        self.n = n
        self.cards = list(range(n))

    def split_deck(self):
        half = self.n >> 1
        return (self.cards[half:], self.cards[:half], [])

    def interleave_chunks(self, a, b, c):
        def fold_deck(t, _):
            a_chunk = t[0][:c]
            b_chunk = t[1][:c]
            return (t[0][c:], t[1][c:], t[2] + a_chunk + b_chunk)
        return reduce(fold_deck,
                      range((self.n + c - 1) // c),
                      (a, b, []))[2]

    def shuffle(self, ops):
        for c in ops:
            a, b, empty = self.split_deck()
            self.cards = self.interleave_chunks(a, b, c)

def parse_input():
    return list(map(str.rstrip, sys.stdin))

def pairwise(iterable):
    return zip(*[iter(iterable)]*2)

def main():
    lines = parse_input()
    for line1, line2 in pairwise(lines):
        N, R = map(int, line1.split())
        ops = list(map(int, line2.split()))
        dm = DeckManipulator(N)
        dm.shuffle(ops)
        print(dm.cards[-1])

if __name__ == "__main__":
    main()