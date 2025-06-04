def read_inputs():
    try:
        while True:
            try: n, r = map(int, raw_input().split())
            except EOFError: return
            yield n, r, list(map(int, raw_input().split()))
    except: pass


def split_deck(deck, n):
    mid = n // 2
    return deck[mid:], deck[:mid]

from itertools import islice

for params in read_inputs():
    n, r, cset = params
    deck = [i for i in range(n)]
    for index in range(r):
        c = cset[index]
        a, b = split_deck(deck, n)
        merged = []
        var = 0
        while bool(a) or bool(b):
            if c <= len(a):
                merged += [a.pop(0) for _ in range(c)]
            else:
                merged += a[:]
                a[:] = []
            if c <= len(b):
                merged += [b.pop(0) for _ in range(c)]
            else:
                merged += b[:]
                b[:] = []
        deck[:] = merged[:]
    print(deck[-1])