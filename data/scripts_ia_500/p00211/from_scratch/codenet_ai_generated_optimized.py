import sys
import math

input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    ds = []
    vs = []
    for _ in range(n):
        d, v = map(int, input().split())
        ds.append(d)
        vs.append(v)

    # On calcule le temps T pour que tous reviennent en même temps : c'est le PPCM des temps de tours
    # Temps de chaque élève = d_i / v_i en fraction d'entier

    # Pour ne pas avoir de float, on note temps_i = d_i / v_i
    # On multiplie tous temps_i par une même valeur (le PPCM des v_i) pour avoir des entiers
    # Soit P = ppcm(v_1,...,v_n)
    # temps_i * P = (d_i * P) / v_i = entier

    def lcm(a, b):
        return a * b // math.gcd(a, b)

    P = 1
    for v in vs:
        P = lcm(P, v)

    nums = []
    # Le temps multiplié par P pour chaque élève (en entier)
    for d, v in zip(ds, vs):
        nums.append(d * (P // v))

    # Le retour simultané correspond au PPCM des nums
    L = 1
    for num in nums:
        L = lcm(L, num)

    # Le nombre de tours par élève = (temps commun) / (temps de 1 tour)
    # tours_i = (L / nums_i) * (P / v_i) => en simplifiant,
    # mais en fait le temps réel T = L / P
    # tours_i = T / temps_i = (L/P) / (d_i/v_i) = (L/P) * (v_i/d_i) = L * v_i / (P * d_i)

    for i in range(n):
        tours = L * vs[i] // (P * ds[i])
        print(tours)