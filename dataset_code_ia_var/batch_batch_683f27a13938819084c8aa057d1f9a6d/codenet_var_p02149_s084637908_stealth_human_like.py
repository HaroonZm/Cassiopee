#!/usr/bin/env python3
import sys
import math
from heapq import heappush, heappop
from collections import defaultdict
import bisect
import random

# Bon, voilà des fonctions utilitaires... pas toutes forcément utiles ici mais je stocke tout ça au cas où.
def LI():
    # retourne une liste d'entiers (entrée standard)
    return list(map(int, sys.stdin.readline().split()))

def I():
    return int(sys.stdin.readline())

def LS():
    return list(map(list, sys.stdin.readline().split()))

def S():
    return list(sys.stdin.readline())[:-1]

def IR(n):
    l = [None]*n
    for j in range(n):
        l[j] = I()
    return l

def LIR(n):
    l = [None]*n
    for i in range(n): l[i] = LI()
    return l

def SR(n):
    res = []
    for i in range(n): res.append(S())
    return res

def LSR(n):
    l = [None for _ in range(n)]
    for i in range(n):
        l[i] = SR()
    return l

mod = 10**9+7

# Partie A - c'est simple, on récupère les scores et on sort une lettre...
liste = LI()
ss = "ABC"
# On cherche l'index du max: c'est un peu sale mais bon, ça marche.
idx = liste.index(max(liste))
print(ss[idx])

#Ouais, tout ça pour ça...
# Pas touché aux autres sections, elles sont toutes vides de toute façon.