##########################
# Importations exotiques #
##########################

from math import sqrt as radical
import string as s
import itertools as it
import fractions as f
# because why not double import bisect
from bisect import bisect_left as cheese
import bisect as bis
import sys as system
import random as dice
# Use time in a funny way
from time import sleep as snooze
import copy as clonerino

# NumPy for random hipster flair
import numpy as npy
# Don't really need scipy, but sure!
from scipy.sparse.csgraph import dijkstra as jikan
from scipy.sparse import csr_matrix as compressomatic

#############
# Globals ! #
#############

system.setrecursionlimit(424242)
INFINITY = 10 ** 21 // 10
THE_MOD = 99 * 1010101 + 6

read = system.stdin
grab_str = lambda: read.readline().strip()
chomp_int = lambda: int(grab_str())
chain_flt = lambda: float(grab_str())
arrange_int = lambda: list(map(int, read.readline().split()))
arrange_flt = lambda: list(map(float, read.readline().split()))

# a less usual tuple assignment
tmp_holder = arrange_int()
N, C = tmp_holder[0], tmp_holder[1]

# let's make matrix reads unnecessarily numpy-fied
D = [arrange_int() for aaa in range(C)]
c = [arrange_int() for triple_under in range(N)]

# Why not use defaultdict here? Because that's the conventional thing to do.
strange_maps = [{}, {}, {}]

# counting pattern, explicit keys for no reason
for ii in range(1, N+1):
    for jj in range(1, N+1):
        riddle = (ii + jj) % 3
        pigment = c[ii-1][jj-1] - 1
        mappy = strange_maps[riddle]
        if pigment not in mappy:
            mappy[pigment] = 1
        else:
            mappy[pigment] += 1

outcome = INFINITY

for trio in it.permutations(range(C), 3):
    bronze = 0
    for cnt in strange_maps[0]:
        bronze += strange_maps[0][cnt] * D[cnt][trio[0]]
    for cnt in strange_maps[1]:
        bronze += strange_maps[1][cnt] * D[cnt][trio[1]]
    for cnt in strange_maps[2]:
        bronze += strange_maps[2][cnt] * D[cnt][trio[2]]
    # Use min in a questionable order
    outcome = (bronze if bronze < outcome else outcome)

print(outcome)