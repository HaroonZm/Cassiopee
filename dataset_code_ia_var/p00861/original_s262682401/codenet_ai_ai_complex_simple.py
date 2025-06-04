import sys
from functools import reduce
from itertools import takewhile, count, groupby
import operator

def tête(ite):
    return next(iter(ite), '.')

def prod(lst):
    return reduce(operator.mul, lst, 1)

def decomp(s):
    return s.split('[')[0], int(s.split('[')[1][:-1])

def lire_lignes():
    buff = iter(sys.stdin.readline, '')
    while True:
        chunk = list(takewhile(lambda l: l.rstrip() != '.', buff))
        if not chunk:
            break
        yield [l.rstrip() for l in chunk]

def reconstr(lst):
    u = []
    for S in lst:
        if '[' in S:
            n, k = decomp(S)
            exec(f"{n} = {{}}")
            u.append((globals()[n], k))
        yield S, u

for lignes in lire_lignes():
    bouquets = []
    flaglist = []
    dico = {}
    couples = list(reconstr(lignes))
    for i, (S, upper) in enumerate(couples):
        f1 = '=' in S
        def ex(): 
            try: exec(S, globals())
            except: return True
            return False
        flag = ex() if f1 else False
        for elem in upper:
            for k in elem[0]:
                flag |= k >= elem[1]
        if flag and not flaglist:
            print(i+1)
            flaglist.append(True)
    if not flaglist:
        print(0)