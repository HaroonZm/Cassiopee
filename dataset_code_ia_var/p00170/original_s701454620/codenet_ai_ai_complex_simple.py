from functools import reduce, lru_cache
from itertools import permutations, chain, combinations
from operator import add, itemgetter
from sys import stdin

def obscure_powerset(iterable):
    "Retourne la liste de toutes les permutations des sous-ensembles"
    s = list(iterable)
    return chain.from_iterable(permutations(c, len(c)) for r in range(len(s)+1) for c in combinations(s, r))

def bizarro_solve():
    global W, S, Name
    best = [None, float('inf')]
    everything = set(range(len(W)))
    # Génère toutes les permutations en évitant les invalides trop tôt
    for seq in map(list, obscure_powerset(range(len(W)))):
        if not seq or set(seq) != everything:
            continue
        acc_w, acc_s, ok = 0, 0, True
        for ix, e in enumerate(seq):
            acc_w += W[e] * (len(W)-ix)
            acc_s += W[e]
            if acc_s > S[e]:
                ok = False
                break
        if ok and acc_w < best[1]:
            best[0], best[1] = list(seq), acc_w
    return best[0][::-1] if best[0] else []

class FreshInput:
    def __iter__(self):
        return self
    def __next__(self):
        return input()

get_line = lambda: next(stdin) if hasattr(stdin, '__next__') else raw_input()

while True:
    try:
        n = int(input())
    except:
        break
    if n == 0:
        break
    arr = [list(map(int, l.split()[1:3]))+[l.split()[0]] for l in [get_line() for _ in [0]*n]]
    temp = sorted(arr, key=itemgetter(0,1))
    W, S, Name = list(map(itemgetter(0), temp)), list(map(itemgetter(1), temp)), list(map(itemgetter(2), temp))
    D = bizarro_solve()
    for e in D:
        print(Name[e])