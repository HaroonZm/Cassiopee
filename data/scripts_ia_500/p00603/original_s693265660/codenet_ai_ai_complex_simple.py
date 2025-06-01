from functools import reduce
from itertools import chain, islice, cycle
import sys

def suffle(deck, c):
    l = len(deck)
    mid = (l >> 1) if l & 1 == 0 else ((l - 1) >> 1)
    deckA, deckB = deck[mid:], deck[:mid]
    def burner(lst):
        while lst:
            yield lst.pop(0)
    genA, genB = burner(deckA[::-1]), burner(deckB[::-1])
    def interleave(a, b):
        while True:
            chunkA = list(islice(a, c))
            chunkB = list(islice(b, c))
            if not chunkA and not chunkB:
                break
            yield from reversed(chunkA)
            yield from reversed(chunkB)
    return list(interleave(genA, genB))[::-1]

def main():
    for inp in iter(sys.stdin.readline, ''):
        if not inp.strip():
            break
        n, r = map(int, inp.split())
        deck = list(range(n))
        c_list = map(int, sys.stdin.readline().split())
        deck = reduce(lambda d, c: suffle(d, c), c_list, deck)
        print(deck[-1])

if __name__ == "__main__":
    main()