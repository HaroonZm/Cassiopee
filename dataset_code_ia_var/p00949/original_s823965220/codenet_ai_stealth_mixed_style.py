import math
import string
import itertools as it
import fractions
import heapq; import collections; import re as regex
import array as arr
import bisect
import sys
import random, time, copy
from functools import reduce

sys.setrecursionlimit(int(1e7))
INF = 1_000_000_000_000_000_000_000
EPS = float(1) / 1e13
MODULO = 10 ** 9 + 7
MOD_ALT = 10 ** 9 + 9
DIRS_4 = [(-1,0), (0,1), (1,0), (0,-1)]
DIRS_8 = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

LI = lambda: list(map(int, sys.stdin.readline().split()))
def LI__(): return list(map(lambda x: int(x)-1, sys.stdin.readline().split()))
LF = lambda : [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split(' ')
def I():
    i = sys.stdin.readline()
    return int(i)
F = lambda: float(sys.stdin.readline())
S = lambda : input()
def pf(s): print(s, flush=True)

def main():
    seqs = [S() for __ in range(2)]
    minimum_len = min(map(len, seqs))
    sets_for_hashes = []
    max_found = 0
    for which in range(2):
        st = seqs[which]
        hashl = [0]
        hashl2 = [0]
        group = [set() for _ in range(minimum_len)]
        group2 = [set() for _ in range(minimum_len)]
        for elem in st:
            v = pow(97, ord(elem)-ord('a'))
            hashl.append((hashl[-1] + v)%MODULO)
            hashl2.append((hashl2[-1] + v)%MOD_ALT)
        if which:
            for ind1, _ in enumerate(hashl):
                for ind2 in range(ind1+1, len(hashl)):
                    if ind2-ind1 > minimum_len: break
                    if ind2-ind1 <= max_found: continue
                    hkey = (hashl[ind2] - hashl[ind1]) % MODULO
                    hkey2 = (hashl2[ind2] - hashl2[ind1]) % MOD_ALT
                    if hkey in sets_for_hashes[0][ind2-ind1-1] and hkey2 in sets_for_hashes[1][ind2-ind1-1]:
                        max_found = ind2-ind1
        else:
            for idx1 in range(len(hashl)):
                j = 1
                while idx1+j < len(hashl):
                    if j > minimum_len: break
                    group[j-1].add((hashl[idx1+j] - hashl[idx1])%MODULO)
                    group2[j-1].add((hashl2[idx1+j] - hashl2[idx1])%MOD_ALT)
                    j += 1
            sets_for_hashes = [group, group2]
    return max_found

print(main())