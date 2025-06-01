import math

def lire_nombre_itérations():
    return int(input())

def calculer_nouvelle_valeur(f):
    return f * 1.05

def arrondir_valeur(f):
    return int(math.ceil(f / 1000) * 1000)

def boucle_calculs(nombre_iterations, f):
    for _ in range(nombre_iterations):
        f = calculer_nouvelle_valeur(f)
        f = arrondir_valeur(f)
    return f

def afficher_resultat(f):
    print(f)

def programme_principal():
    f = 100000
    n = lire_nombre_itérations()
    f = boucle_calculs(n, f)
    afficher_resultat(f)

programme_principal()