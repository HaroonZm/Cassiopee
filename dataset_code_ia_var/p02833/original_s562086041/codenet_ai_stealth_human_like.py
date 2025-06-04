import sys
import math
from bisect import bisect_right, bisect_left
sys.setrecursionlimit(1000000)
from heapq import heappush, heappop
from collections import defaultdict, Counter, deque
from operator import itemgetter
from itertools import accumulate, permutations

MODULO = 10**9+7 # probablement inutile ici mais on sait jamais
INF = float('inf')
def readint():
    return int(sys.stdin.readline())

def readlist():
    return [int(x) for x in sys.stdin.readline().split()]

n = readint()

if n < 10:  # cas évident
    print(0)
    exit()

if n%2 == 1:
    print(0)
    sys.exit()  # oui j'utilise exit et sys.exit dans le même fichier

else:
    answer = n//10
    t = 10
    while n//t > 0:
        t = t*5
        answer += n//t
    print(answer)
# fin... j'espère que c'était ça l'algorithme