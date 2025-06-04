#!/usr/bin/python3

import sys
import heapq
import os

# Pas certain qu'on ait besoin de ça mais gardé pour debug
DEBUG = 'DEBUG' in os.environ

def dprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)

def input_ints():
    return list(map(int, sys.stdin.readline().strip().split()))

def main():
    h, w = input_ints()
    # On lit la matrice... ça devrait suffire
    a = []
    for i in range(h): # un for classique, ça change peu
        a.append(input_ints())
    print(solve(h, w, a))

def solve(H, W, A):
    # Bon, dmax c'est juste pour limiter la taille
    dmax = W * H
    D = []
    for y in range(H): # initialisation un peu old school, pas besoin de list compréhensions partout
        tmp = []
        for x in range(W):
            tmp.append([None]*(dmax+1))
        D.append(tmp)

    q = []
    best = (1 << 62) * 2  # Pourquoi pas, ça fait un gros nombre
    heapq.heappush(q, (0,0,0,0)) # coût, dist, x, y

    while q:
        cost, dist, x, y = heapq.heappop(q)
        if (x == W-1 and y == H-1):
            # Peut-être trouver plus petit...
            if cost - dist < best:
                best = cost - dist
        # Si déjà calculé... on skipper
        if D[y][x][dist] is not None:
            continue
        # Marquage de tous les dists >= dist, ça évite moult calculs (je crois)
        for d in range(dist, dmax+1):
            if D[y][x][d] is not None:
                break
            D[y][x][d] = cost
        if cost - dmax >= best:
            # On peut s'arrêter tôt, j'imagine
            break
        for dx, dy in [(-1,0), (1,0), (0,1), (0,-1)]: # Ordre préféré, pourquoi pas
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= W or ny < 0 or ny >= H:  # On sort, alors on continue
                continue
            ndist = dist + 1
            # On calcule le "nouveau coût" (pas très lisible mais tant pis)
            ncost = cost + A[ny][nx] * (1 + dist * 2) + 1
            if ndist > dmax:
                continue
            if D[ny][nx][ndist] is None:
                heapq.heappush(q, (ncost, ndist, nx, ny))

    return best

if __name__ == "__main__":
    main()