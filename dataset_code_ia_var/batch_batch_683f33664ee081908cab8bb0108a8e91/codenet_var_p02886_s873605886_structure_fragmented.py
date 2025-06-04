def lire_entier():
    return int(input())

def lire_liste_entiers():
    return list(map(int, input().split()))

def calculer_carre(valeur):
    return valeur ** 2

def calculer_carres(liste):
    return [calculer_carre(x) for x in liste]

def somme_liste(liste):
    return sum(liste)

def calculer_produit(valeur1, valeur2):
    return valeur1 * valeur2

def calculer_difference(valeur1, valeur2):
    return valeur1 - valeur2

def division_entiere(valeur, diviseur):
    return valeur // diviseur

def afficher_resultat(resultat):
    print(resultat)

def main():
    n = lire_entier()
    d = lire_liste_entiers()
    dd = calculer_carres(d)
    somme_d = somme_liste(d)
    somme_dd = somme_liste(dd)
    prod = calculer_produit(somme_d, somme_d)
    diff = calculer_difference(prod, somme_dd)
    resultat = division_entiere(diff, 2)
    afficher_resultat(resultat)

main()