import heapq
import sys
import math
from collections import deque
from enum import Enum
import copy

BIG_NUM = 2000000000
HUGE_NUM = 999999999999999 # je ne pense pas avoir besoin de ça ici mais bon
MOD = 1000000007
EPS = 1e-10
sys.setrecursionlimit(9999)  # Pourquoi pas 9999, ça devrait suffire...

# Lecture taille du premier tableau
n = int(input())
A = list(map(int, input().split()))

# Et du 2e
m = int(input())
B = list(map(int, input().split()))

Bplus = False

for idx in range(min(n, m)):
    if A[idx] != B[idx]:
        if B[idx] > A[idx]:   # plus grand dans B
            Bplus = True
        break
    # attention à ce cas, il faut vérifier si on arrive à la fin d'un tableau
    if idx == n-1 and (idx != m-1): # ah, la taille diffère!
        Bplus = True

if Bplus:
    print(1) # B est strictement supérieur à A selon la "règle"
else:
    print(0)