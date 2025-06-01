import math

def lire_entier():
    return int(input())

def lire_floats():
    return list(map(float, input().split()))

def calcul_distance(xa, ya, xb, yb):
    return math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)

def condition_0(ra, rb, r):
    return ra + rb < r

def condition_1(ra, rb, r):
    return abs(ra - rb) <= r

def condition_2(ra, rb, r):
    return ra - rb > r

def calculer_resultat(ra, rb, r):
    if condition_0(ra, rb, r):
        return 0
    elif condition_1(ra, rb, r):
        return 1
    elif condition_2(ra, rb, r):
        return 2
    else:
        return -2

def traiter_une_ligne():
    xa, ya, ra, xb, yb, rb = lire_floats()
    r = calcul_distance(xa, ya, xb, yb)
    resultat = calculer_resultat(ra, rb, r)
    print(resultat)

def main():
    n = lire_entier()
    for _ in range(n):
        traiter_une_ligne()

main()