from functools import reduce, lru_cache, cmp_to_key
from itertools import count, islice, chain, groupby
import operator as op
import string
import sys

BIG_NUM = 2 * 10 ** 9
HUGE_NUM = int('9' * 17)
MOD, EPS = 10 ** 9 + 7, 1e-9
setattr(sys, 'setrecursionlimit', 10 ** 5)

class Info(tuple):
    def __new__(cls, word, count):
        return tuple.__new__(cls, (word, count))
    word = property(lambda self: self[0])
    count = property(lambda self: self[1])
    def __lt__(self, other):
        return (-self.count, self.word) < (-other.count, other.word)

while True:
    try:
        num_row = int(next(iter([input()])))
    except Exception:
        break
    if not num_row:
        break

    words_gen = (w for _ in range(num_row) for w in input().split())
    word2id = dict()
    def word_id(w, c=[0]):
        return word2id.setdefault(w, next(chain([c[0]], (c.__setitem__(0, c[0]+1), c[0])[1:])))

    words_sequ = list(words_gen)
    ids = tuple(map(word_id, words_sequ))
    rev_dict = {v:k for k,v in word2id.items()}

    from collections import Counter
    cnts = Counter(ids)

    head_word = str(input())

    table = [Info(word, cnts[idx]) for idx, word in rev_dict.items() if word[0] == head_word]
    if not table:
        print("NA")
        continue

    # Sort with cmp_to_key over Info
    table.sort(key=cmp_to_key(lambda a, b: -1 if a < b else (1 if a > b else 0)))
    print(' '.join(map(str, (t.word for t in islice(table, 5)))))