def lire_entier():
    return int(input())

def lire_liste():
    return list(map(int, input().split()))

def produit_deux_elements(x, y):
    return x * y

def somme_produits_de_deux_listes_parties(liste, i):
    return somme_individuelle(liste, i, i+1)

def somme_individuelle(liste, i, debut_j):
    s = 0
    for j in range(debut_j, len(liste)):
        s += produit_deux_elements(liste[i], liste[j])
    return s

def somme_totale(liste):
    total = 0
    for i in range(len(liste)):
        total += somme_produits_de_deux_listes_parties(liste, i)
    return total

def afficher_resultat(resultat):
    print(resultat)

def main():
    N = lire_entier()
    d = lire_liste()
    a = somme_totale(d)
    afficher_resultat(a)

main()