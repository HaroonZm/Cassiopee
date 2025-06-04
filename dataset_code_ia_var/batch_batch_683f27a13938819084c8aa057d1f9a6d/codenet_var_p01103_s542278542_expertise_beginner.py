import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def calcVolume(L, R, T, B, min_wall):
    # Calcule le volume de l'étang
    total = 0
    for x in range(L, R+1):
        for y in range(B, T+1):
            total += (min_wall - garden[y][x])
    return total

def pondsVolume(L, R, T, B):
    # Retourne le volume de l'étang, ou -1 si impossible
    max_in_pond = 0
    for x in range(L, R+1):
        for y in range(B, T+1):
            if garden[y][x] > max_in_pond:
                max_in_pond = garden[y][x]
    min_wall = float('inf')
    # Chercher le minimum sur les murs horizontaux
    for x in range(L-1, R+2):
        if garden[B-1][x] < min_wall:
            min_wall = garden[B-1][x]
        if garden[T+1][x] < min_wall:
            min_wall = garden[T+1][x]
    # Chercher le minimum sur les murs verticaux
    for y in range(B-1, T+2):
        if garden[y][L-1] < min_wall:
            min_wall = garden[y][L-1]
        if garden[y][R+1] < min_wall:
            min_wall = garden[y][R+1]
    if min_wall <= max_in_pond:
        return -1
    else:
        return calcVolume(L, R, T, B, min_wall)

while True:
    d_w = input()
    if not d_w:
        break
    d_w = d_w.strip()
    if not d_w:
        continue
    d, w = map(int, d_w.split())
    if d == 0:
        break
    garden = []
    for _ in range(d):
        row = list(map(int, input().split()))
        garden.append(row)
    answer = 0
    for L in range(1, w-1):
        for B in range(1, d-1):
            for R in range(L, w-1):
                for T in range(B, d-1):
                    res = pondsVolume(L, R, T, B)
                    if res > answer:
                        answer = res
    print(answer)