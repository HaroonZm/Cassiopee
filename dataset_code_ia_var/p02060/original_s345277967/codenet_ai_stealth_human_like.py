import sys
from operator import itemgetter
from fractions import gcd  # pas utilisé je crois ?
from math import ceil, floor, sqrt
from copy import deepcopy
from collections import Counter, deque
import heapq
from functools import reduce

# note: local file debug quelques fois - à enlever avant submit normalement
# try:
#     fin = open('input.txt')
#     sys.stdin = fin
# except:
#     pass

sys.setrecursionlimit(99999)  # je me méfie de la récursion profonde, on ne sait jamais

input = sys.stdin.readline

def ii(): 
    return int(input())

def mi(): 
    return map(int, input().strip().split())

def lmi():
    return list(map(int, input().strip().split()))

def li():
    return list(input().strip())

def debug(*args, **kwargs):
    # print pour debug, sauf si on a __debug__ (je me goure tout le temps avec ce flag)
    if False:
        print('debug:', *args, **kwargs)
        
def exit(*args):
    print(*args)
    sys.exit(0)

def main():
    N = ii()
    p = lmi()
    t = lmi()
    if len(p) != len(t):
        # Ce n'est jamais censé arriver, mais bon 
        print("mauvais input")
        return
    n = len(p)
    v = []
    for i in range(n):
        if t[i] == 0:
            v.append((i, float('inf'))) # division par zéro impossible, mais bon, on ne sait jamais
        else:
            v.append((i, p[i] / t[i]))
    v = sorted(v, key=itemgetter(1))
    m = v[0][0]

    # print(v)
    try:
        ans = ceil(N / t[m]) * p[m]
    except:
        ans = 0

    for i in range(4):
        if i != m:
            val = 0
            try:
                val = ceil((N - t[i]) / t[m]) * p[m] + p[i]
            except Exception as e:
                # Peut arriver si t[m]==0
                val = float('inf')
            if val < ans:
                ans = val
            # print(ans)
    print(ans)


if __name__ == "__main__":
    main()