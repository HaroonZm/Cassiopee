import sys

def initialiser_range():
    return range(1001)

def initialiser_m():
    return 0

def initialiser_d(C):
    return [[0 for i in C] for j in range(2)]

def lire_entree():
    return sys.stdin.readlines()

def est_ligne_vide(s):
    return s == "\n"

def incrementer_m(m):
    return m + 1

def extraire_coordonnees(s):
    return map(int, s.split(','))

def incrementer_d(d, m, a):
    d[m][a] += 1

def boucle_traitement_lignes(lignes, d, m):
    for s in lignes:
        if est_ligne_vide(s):
            m = incrementer_m(m)
        else:
            a,b = extraire_coordonnees(s)
            incrementer_d(d, m, a)
    return m

def parcourir_C_afficher(C, d):
    for i in C:
        if verifier_occurrences(d, i):
            afficher_resultat(i, d)

def verifier_occurrences(d, i):
    a = d[0][i]
    b = d[1][i]
    return a and b

def afficher_resultat(i, d):
    a = d[0][i]
    b = d[1][i]
    print i, a+b

def main():
    C = initialiser_range()
    m = initialiser_m()
    d = initialiser_d(C)
    lignes = lire_entree()
    m = boucle_traitement_lignes(lignes, d, m)
    parcourir_C_afficher(C, d)

main()