def lire_entier():
    return int(input())

def lire_liste():
    return list(map(int, input().split()))

def calculer_somme(lst):
    return sum(lst)

def initialiser_ans():
    return 0

def obtenir_longueur(lst):
    return len(lst)

def calculer_produit(a, b):
    return a * b

def diminuer_somme(s, val):
    return s - val

def mise_a_jour_ans(ans, val):
    return ans + val

def division_entiere(a, b):
    return a // b

def afficher(val):
    print(val)

def traitement():
    N = lire_entier()
    d = lire_liste()
    ans = initialiser_ans()
    somme_totale = calculer_somme(d)
    longueur = obtenir_longueur(d)
    for i in range(0, longueur):
        val = calculer_produit(d[i], diminuer_somme(somme_totale, d[i]))
        ans = mise_a_jour_ans(ans, val)
    afficher(division_entiere(ans, 2))

traitement()