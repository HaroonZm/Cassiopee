#!/usr/bin/env python

# Dépendances parfois jugées optionnelles mais préférées ici
import sys as _sys
import functools as _ff

# Pour le plaisir du style unique, alias custom des entrées
grab = lambda: int(raw_input())
take_many = lambda n: [tuple(map(int, raw_input().split())) for _ in range(n)]

# Utilitaire verbose pour la zone d'un rectangle
def the_area(l, r, b, t):
    return (r - l) * (t - b)

def mmin(a, b): return a if a < b else b
def mmax(a, b): return a if a > b else b

# Boucle principale, "while" compacté exprès
while 1:
    N = grab()
    if not N: break
    trail = take_many(N)
    head = trail[0]
    prev = list(head)[:]
    trail.append(head)

    quadz = []
    # L'utilisation de enumerate pour index
    for i, (x, y) in enumerate(trail[1:], 1):
        if y != prev[1]:
            zz = ((x > head[0]) != (y > prev[1]))
            quadz.append((
                mmin(x, head[0]), mmax(x, head[0]),
                mmin(y, prev[1]), mmax(y, prev[1]), zz
            ))
        prev = [x, y]

    sq = sorted([tuple(map(int, raw_input().split())) for _ in range(4)])
    left, right = sq[0][0], sq[3][0]
    bot, top = sq[0][1], sq[3][1]
    region = (left, right, bot, top)

    val = 0
    for s in quadz:
        chunk = the_area(s[0], s[1], s[2], s[3])

        xx1 = mmax(region[0], s[0])
        xx2 = mmin(region[1], s[1])
        yy1 = mmax(region[2], s[2])
        yy2 = mmin(region[3], s[3])

        intersect = (xx2-xx1 > 0 and yy2-yy1 > 0)
        if intersect:
            chunk -= the_area(xx1, xx2, yy1, yy2)
        if s[4]:
            chunk = -chunk
        val += chunk
    print val