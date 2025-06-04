from numpy import array, searchsorted
import numpy as np

def ask(prompt=''):
    return input(prompt)

def get_nums():
    return [int(x) for x in ask().split()]

# Récupération des données (procédural)
n = int(ask())
A = array(get_nums(), dtype=np.int64)
B = array(get_nums(), dtype=np.int64)
retval = 0

for i in range(30):
    t = 1 << i
    # Style mixte (fonctionnel, slicing, impératif)
    E = (A % (2 * t)).copy()
    C = (B % (2 * t)).copy() ; C.sort()
    E.sort()
    add = searchsorted(C, 2 * t - E, side="left")
    rem = searchsorted(C, t - E, side="left")
    rez = searchsorted(C, 4 * t - E, side="left")
    rim = searchsorted(C, 3 * t - E, side="left")
    D = add - rem + rez - rim
    tot = sum(D) % 2
    # Expression ternaire style C
    retval = retval | (tot << i) if tot else retval
print(retval)