from collections import defaultdict as dd
from collections import deque as dq
import sys, math, bisect
from heapq import heappush as Hpush, heappop as Hpop
import random

sys.setrecursionlimit(10**6)
MODULO = 10**9+7

# Diverses fonctions d'entrée, style hétérogène
def li(): return list(map(int, sys.stdin.readline().split()))
def it(): return int(sys.stdin.readline())
def ls(): return list(sys.stdin.readline().split())
def str_list(): return list(sys.stdin.readline().rstrip())
def input_rows(n, fn): return [fn() for _ in range(n)]

def eval_line(): return eval(input())
def int_line(): return int(input())
def input_matrix(n): return [li() for _ in range(n)]
def string_matrix(n): return [str_list() for _ in range(n)]

def a_func():
    chaine = input()
    cible = it()
    calcul = eval(chaine)
    b = int(chaine[0])
    n = len(chaine)

    if n == 1:
        if int(chaine[0]) == cible:
            print("U")
        else:
            print("I")
        quit()
    key = 0 if chaine[1] == "+" else 1
    for idx in range(2, n):
        if idx % 2 == 0:
            if key:
                b *= int(chaine[idx])
            else:
                b += int(chaine[idx])
        else:
            key = 0 if chaine[idx] == "+" else 1

    if calcul == b:
        if calcul == cible:
            print("U")
        else:
            print("I")
    elif calcul == cible:
        print("M")
    elif b == cible:
        print("L")
    else:
        print("I")
    return None

def bFUNC():
    n, m = map(int, sys.stdin.readline().split())
    T = [0]*(2*n + 3)
    for _ in range(m):
        a1, b1 = map(int, sys.stdin.readline().split())
        T[2*a1] += 1
        T[2*b1+1] -= 1
    for j in range(2*n+1):
        T[j+1] += T[j]

    ANS = n+1
    S = 0
    FLAG = True

    for v in T:
        if v > 0:
            if FLAG:
                FLAG = False
                S += 1
            ANS += 1
        else:
            FLAG = True
    ANS -= S
    print(ANS)
    return None

def C():pass
def d():return
def E(): pass
def f(): return
def G(): pass
def h(): return
def I__(): return
def J(): pass

if __name__=="__main__":
    bFUNC()