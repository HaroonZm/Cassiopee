def saisir_valeurs(n):
    valeurs = []
    for _ in range(n):
        valeur = lire_entier()
        valeurs.append(valeur)
    return valeurs

def lire_entier():
    return int(input())

def trier_liste_decroissant(liste):
    liste.sort(reverse=True)

def calculer_somme_top_n(liste, n):
    return sum(liste[:n])

def main():
    W = saisir_valeurs(10)
    K = saisir_valeurs(10)
    trier_liste_decroissant(W)
    trier_liste_decroissant(K)
    point_W = calculer_somme_top_n(W, 3)
    point_K = calculer_somme_top_n(K, 3)
    afficher_points(point_W, point_K)

def afficher_points(point_W, point_K):
    print(point_W, point_K)

main()