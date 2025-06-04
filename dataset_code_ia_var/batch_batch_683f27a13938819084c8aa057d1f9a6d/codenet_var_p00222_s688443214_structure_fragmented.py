from math import sqrt, ceil

def creer_temp(N):
    temp = [True] * (N + 1)
    initialiser_temp(temp)
    appliquer_crible(temp, N)
    return temp

def initialiser_temp(temp):
    temp[0] = False
    temp[1] = False

def appliquer_crible(temp, N):
    borne = calculer_borne_crible(N)
    for i in range(2, borne):
        traiter_crible(temp, i)

def calculer_borne_crible(N):
    return ceil(sqrt(N + 1))

def traiter_crible(temp, i):
    if est_premier(temp, i):
        eliminer_multiples(temp, i)

def est_premier(temp, i):
    return temp[i]

def eliminer_multiples(temp, i):
    start, step = i + i, i
    l = len(temp[start::step])
    marquer_non_premiers(temp, start, step, l)

def marquer_non_premiers(temp, start, step, l):
    temp[start::step] = [False] * l

def lire_entree():
    try:
        return int(input())
    except:
        return None

def boucle_principale(temp, quadruplet):
    while True:
        n = lire_entree()
        if n is None:
            break
        traiter_n(temp, quadruplet, n)

def traiter_n(temp, quadruplet, n):
    borne = calculer_borne_recherche(n)
    for i in range(n, borne, -1):
        if verifier_candidat(temp, quadruplet, i):
            afficher_resultat(i)
            break

def calculer_borne_recherche(n):
    return 9

def verifier_candidat(temp, quadruplet, i):
    return temp[i] and comparer_sequence(temp, quadruplet, i)

def comparer_sequence(temp, quadruplet, i):
    return temp[i-8:i+1] == quadruplet

def afficher_resultat(i):
    print(i)

def main():
    N = definir_constante_N()
    temp = creer_temp(N)
    quadruplet = definir_quadruplet()
    boucle_principale(temp, quadruplet)

def definir_constante_N():
    return 10100000

def definir_quadruplet():
    return [True, False, True, False, False, False, True, False, True]

main()