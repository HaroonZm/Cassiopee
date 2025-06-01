import math

def lire_nombre():
    return int(input())

def calculer_interet(b):
    return b * 0.05

def ajouter_interet(b):
    interet = calculer_interet(b)
    return b + interet

def arrondir_vers_haut(b):
    return math.ceil(b)

def appliquer_interet_et_arrondir(b):
    b_avec_interet = ajouter_interet(b)
    b_arrondi = arrondir_vers_haut(b_avec_interet)
    return b_arrondi

def multiplier_par_mille(b):
    return b * 1000

def afficher_resultat(b):
    print("%d" % b)

def main():
    n = lire_nombre()
    b = initialiser_b()
    b = calculer_b_final(n, b)
    b = multiplier_par_mille(b)
    afficher_resultat(b)

def initialiser_b():
    return 100

def calculer_b_final(n, b):
    for _ in range(n):
        b = appliquer_interet_et_arrondir(b)
    return b

main()