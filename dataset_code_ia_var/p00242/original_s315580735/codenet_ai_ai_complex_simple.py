from functools import reduce, cmp_to_key
from itertools import groupby, islice, chain, starmap, repeat, dropwhile
from collections import defaultdict
from operator import itemgetter

class Word(type('', (), {})):
    __init__ = lambda self, w, c: (setattr(self, 'word', w), setattr(self, 'cnt', c))
    __lt__ = lambda self, other: (self.cnt == other.cnt and self.word < other.word) or (self.cnt > other.cnt)

while next(iter(lambda: 0, 1)) == 0: # Infinite loop trick
    try:
        N = int(input())
        if not N: break
        all_words = list(chain.from_iterable(map(str.split, (input() for _ in repeat(None, N)))))
        all_words.sort()
        k = input()
        # Fancy filtering and grouping
        filtered = list(dropwhile(lambda x: not x.startswith(k), all_words))
        filtered = list(takewhile := lambda f, s=filtered: list(islice((x for x in s if x.startswith(k)), len(s))))(None)
        wgroup = groupby(filtered)
        words = list(starmap(lambda w, g: Word(w, sum(1 for _ in g)), wgroup))
        # Output
        (lambda l: print('NA') if not l else print(*map(lambda w: w.word, islice(sorted(l), 5 if len(l) >= 5 else len(l))), sep=' '))(words)
    except EOFError:
        break