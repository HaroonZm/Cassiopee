def lire_n():
    return int(input())

def lire_a_b():
    ligne = input()
    return extraire_a_b(ligne)

def extraire_a_b(ligne):
    return [int(item) for item in ligne.split()]

def lire_p():
    ligne = input()
    return extraire_p(ligne)

def extraire_p(ligne):
    return [int(item) for item in ligne.split()]

def init_compteurs():
    return 0, 0, 0

def determiner_categorie(item, a, b):
    if item <= a:
        return 1
    elif item <= b:
        return 2
    else:
        return 3

def incrementer_compteur(categorie, p1, p2, p3):
    if categorie == 1:
        return p1 + 1, p2, p3
    elif categorie == 2:
        return p1, p2 + 1, p3
    else:
        return p1, p2, p3 + 1

def compter_par_categorie(p, a, b):
    p1, p2, p3 = init_compteurs()
    for item in p:
        categorie = determiner_categorie(item, a, b)
        p1, p2, p3 = incrementer_compteur(categorie, p1, p2, p3)
    return p1, p2, p3

def trouver_min(*args):
    return min(args)

def afficher(val):
    print(val)

def main():
    n = lire_n()
    a, b = lire_a_b()
    p = lire_p()
    p1, p2, p3 = compter_par_categorie(p, a, b)
    resultat = trouver_min(p1, p2, p3)
    afficher(resultat)

main()