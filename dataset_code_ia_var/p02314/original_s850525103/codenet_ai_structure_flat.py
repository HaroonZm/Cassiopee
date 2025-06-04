mod = 10 ** 9 + 7
mod2 = 2 ** 61 + 1
from collections import deque
import heapq
import time
from bisect import bisect_left, insort_left, bisect_right
import sys
import random
import itertools

input = sys.stdin.readline
_NUMINT_ALL = list(range(10))
_START_TIME = time.time()
INDEX_KETA = 10**12

if 1:
    # bloc main linéaire sans fonction
    N_W = input().rstrip("\n").split()
    try:
        N = int(N_W[0])
        W = int(N_W[1])
    except:
        N = N_W[0]
        W = N_W[1]
    dp = [100000] * 100000
    dp[0] = 0
    coins_ = input().rstrip("\n").split()
    try:
        coins = [int(i) for i in coins_]
    except:
        coins = []
        for i in coins_:
            if i in _NUMINT_ALL:
                coins.append(int(i))
            else:
                coins.append(i)
    for i in coins:
        for j in range(100000):
            if j - i < 0:
                continue
            dp[j] = min(dp[j - i] + 1, dp[j])
    print(dp[N])

# Les librairies auxiliaires suivent mais non utilisées ici.
# Tout est linéaire, aucune définition de fonction n'est gardée.
# Les "tools" sont écrits en commentaire car inutilisés dans le main plat.
"""
def kiriage_warizan(a, b):
    return -(-a//b)
def iip(listed=False):
    ...
def iipt(l, listed=True, num_only=True):
    ...
def saidai_kouyakusuu(A):
    ...
def flatten(l):
    ...
def index_sorted(sorted_list, target):
    ...
def time_debug_10percent():
    ...
def time_debug(t):
    ...
def make_graph_edge_flat(N):
    ...
def sort_tuples(l, index):
    ...
def count_elements(l):
    ...
def safeget(l, index, default="exception"):
    ...
def sortstr(s):
    ...
def iip_ord(startcode="a"):
    ...
def YesNo(s):
    ...
def fprint(s):
    ...
def bitall(N):
    ...
def split_print_space(s):
    ...
def split_print_enter(s):
    ...
def soinsuu_bunkai(n):
    ...
def conbination(n, r, mod, test=False):
    ...
def inv(n, mod):
    ...
def power(n, p, mod_=mod):
    ...
def nibutan_func(func, target, left, right, side="left", seido = 1):
    ...
def nibutan_list(list_, target, side="left"):
    ...
class UfTree():
    def __init__(self, maxnum): ...
"""