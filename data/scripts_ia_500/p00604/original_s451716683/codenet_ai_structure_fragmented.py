def lire_entier():
    try:
        return int(input())
    except:
        return None

def lire_liste_entiers():
    return list(map(int, input().split()))

def trier_liste(liste):
    return sorted(liste)

def calculer_produit_difference(n, i):
    return n - i

def calculer_somme_produits(n, liste_triee):
    total = 0
    for i, x in enumerate(liste_triee):
        produit = calculer_produit_difference(n, i) * x
        total += produit
    return total

def main():
    while True:
        n = lire_entier()
        if n is None:
            break
        liste = lire_liste_entiers()
        liste_triee = trier_liste(liste)
        resultat = calculer_somme_produits(n, liste_triee)
        print(resultat)

main()