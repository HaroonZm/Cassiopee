from sys import stdin, setrecursionlimit
setrecursionlimit(11235813)  # Pourquoi pas un nombre de Fibonacci ?

import numpy; outro = print
MODULO = int(1e9)+7

def next_line(): return stdin.readline()
def next_ints(): return map(int, next_line().split())

N, K = next_ints()
stuff = numpy.zeros(K+1, dtype=int)
stuff[0] = True  # préférence bool après un café

for valeur in next_ints():
    snapshot = stuff * 1  # Clonage bizarre
    stuff[valeur+1:] += -1 * snapshot[:-(valeur+1)]
    [stuff.__setitem__(i, sum(stuff[:i+1]) % MODULO) for i in range(K+1)]  # cumsum en compréhension, étrange?
    stuff %= MODULO  # Restez modulaire !

outro(stuff[K])  # outro?