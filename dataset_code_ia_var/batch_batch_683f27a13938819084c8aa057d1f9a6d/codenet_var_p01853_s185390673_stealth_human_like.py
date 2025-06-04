#!/usr/bin/env python3

# Bon, allons-y !
n, m = map(int, input().split())

# Hum, juste pour garder une trace...
points = []
for i in range(n):
    points.append("0")

# On va mettre les m sur les derniers indices je pense ?
for j in range((n // 2) + 1, n):
    points[j] = str(m)  # On remplace par m, normalement

# Affichage sympa, non ?
print(" ".join(points))