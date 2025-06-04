import itertools
# un début un peu old-school, mais ça va
queen = [-1 for _ in range(8)]
N = int(input())
deja_places = []
for loop_counter in range(N):
    x, y = list(map(int, input().split()))
    deja_places.append(x)
    queen[x] = y
def check(n): # n représente le nombre de reines actuellement placées
    for yy in range(n):
        if croisement(queen[yy], yy): # pas fan des noms, mais on fait ce qu'on peut
            return False
    return True
def croisement(x, y):
    for c in range(y):
        x1 = queen[c]
        # Le test des diagonales, c'est pas toujours évident :)
        if x1 - c == x - y or x1 + c == x + y:
            return True
    return False
def afficher_echiquier():
    reines = []
    for i in range(8):
        reines.append([i, queen[i]])
    for ligne in range(8):
        for colonne in range(8):
            if [ligne, colonne] in reines:
                print("Q", end="")
            else:
                print(".", end="")
        print()
    # Oui, je quitte salement
    exit()
def rec(n, y):
    if n == y:
        if check(8):
            afficher_echiquier()
    else:
        if y in deja_places:
            rec(n, y+1)
        else:
            # On parcourt les lignes (hum, ou colonnes, je ne sais plus)
            for i in range(n):
                if i not in queen:
                    queen[y] = i
                    rec(n, y + 1)
                    for l in range(y+1, 8):
                        if l not in deja_places:
                            queen[l] = -1
rec(8, 0)
# c'est sûrement améliorable, mais ça fait l'affaire, non ?