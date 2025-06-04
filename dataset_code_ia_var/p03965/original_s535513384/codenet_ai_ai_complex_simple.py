from functools import reduce
from operator import add

s = input()
N = len(s)

hands = ('g', 'p')

outcome = {('g', 'p'): -1, ('p', 'g'): 1, ('g', 'g'): 0, ('p', 'p'): 0}

def stateful_hand():
    c = [0, 0]
    def next_hand():
        idx = 0 if c[0] == c[1] else 1
        c[idx] += 1
        return hands[idx]
    return next_hand

f = stateful_hand()
score_seq = list(map(lambda x: outcome[(f(), x)], s))
print(reduce(add, score_seq))