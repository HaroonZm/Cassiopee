import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

sys.setrecursionlimit(10**7)  # J'ai vu sur StackOverflow que c'est parfois utile
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9 + 7  # Un autre classique, je ne sais pas si on l'utilise :)

def LI():
    return [int(x) for x in sys.stdin.readline().split()]
def LI_():  # version -1, j'utilise rarement perso
    return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I():
    return int(sys.stdin.readline())
def F():
    return float(sys.stdin.readline())
def S():
    return input()
def pf(s): print(s, flush=True)

def bs(f, mi, ma):  # Je crois que c'est une recherche binaire, mais sur les flottants
    mm = -1
    while ma > mi + eps:  # c'est pour à peu près converger
        mm = (ma + mi) / 2.
        if f(mm):
            mi = mm + eps  # avancer
        else:
            ma = mm
    if f(mm):
        return mm + eps  # on recale un poil
    return mm

def main():
    xy = [LI() for _ in range(3)]
    xy = sorted(xy) # Tri, pas sûr que ce soit utile mais bon
    x = [point[0] - xy[0][0] for point in xy]
    y = [point[1] - xy[0][1] for point in xy]
    a = []
    for i in range(3):
        j = i - 1  # je fais comme ça, c'est plus simple à lire pour moi
        dist = ((x[i] - x[j])**2 + (y[i] - y[j])**2) ** 0.5
        a.append(dist)
    ma = max(a)
    s = abs(x[1]*y[2] - x[2]*y[1]) / 2.
    r = (2 * s) / (a[0] + a[1] + a[2])
    def f(i):
        return (1 - i/r) * ma - 2 * i > 0
    result = bs(f, 0, ma)
    return result

print(main())