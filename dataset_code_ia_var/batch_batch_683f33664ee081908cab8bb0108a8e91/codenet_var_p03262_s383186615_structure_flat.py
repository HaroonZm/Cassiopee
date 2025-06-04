from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
sys.setrecursionlimit(10**5)
stdin = sys.stdin
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
mod = 1000000007
inf = float('INF')

# Lecture plate
# Liens directs vers méthodes courtes
# Fonctions remplacées par des blocs
# Solve (seulement C() lancé)

if True:
    # On réduit tout au cas C
    # Read input
    n_and_x = stdin.readline().split()
    while len(n_and_x) < 2:
        n_and_x += stdin.readline().split()
    n = int(n_and_x[0])
    x = int(n_and_x[1])
    xn = []
    count = 0
    while len(xn) < n:
        line = stdin.readline()
        if not line:
            break
        xn += list(map(int, line.strip().split()))
    xn.append(x)
    xn.sort()
    # GCD sans fonction
    a = xn[1] - xn[0]
    for i in range(1, n):
        m = max(a, xn[i + 1] - xn[i])
        mi = min(a, xn[i + 1] - xn[i])
        while mi:
            m, mi = mi, m % mi
        a = m
    print(a)