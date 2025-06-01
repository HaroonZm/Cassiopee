def lire_entree():
    return input().split()

def verifier_fin(m):
    return m == "0"

def initialiser_compteurs():
    return 0, 0

def iterer_indices():
    return range(4)

def comparer_caracteres(m, n, i):
    return m[i] == n[i]

def verifier_presence(m, n, i):
    return m[i] in n

def incrementer_h(h):
    return h + 1

def incrementer_b(b):
    return b + 1

def afficher_resultat(h, b):
    print(h, b)

def traiter_cas(m, n):
    h, b = initialiser_compteurs()
    for i in iterer_indices():
        if comparer_caracteres(m, n, i):
            h = incrementer_h(h)
        elif verifier_presence(m, n, i):
            b = incrementer_b(b)
    afficher_resultat(h, b)

def boucle_principale():
    while True:
        m, n = lire_entree()
        if verifier_fin(m):
            break
        traiter_cas(m, n)

boucle_principale()