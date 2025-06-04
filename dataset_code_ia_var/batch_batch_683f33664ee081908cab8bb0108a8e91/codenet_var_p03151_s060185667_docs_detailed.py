def main():
    """
    Programme principal permettant de lire deux ensembles de nombres entiers,
    puis de calculer combien d'opérations minimum sont nécessaires pour équilibrer
    la somme du premier ensemble avec le second en 'empruntant' des quantités d'un élément
    de l'ensemble qui est surplus pour combler le déficit de l'autre.
    Affiche -1 si ce n'est pas possible, ou 0 si aucune opération n'est nécessaire.
    """

    # Lecture de la taille des tableaux
    n = int(input("Entrez la taille des tableaux : "))

    import numpy as np

    # Initialisation des tableaux a et b de longueur n, contenant des zéros de type int
    a = np.zeros(n, dtype=int)
    b = np.zeros(n, dtype=int)

    # Lecture des valeurs pour a et b via des chaînes d'entrées séparées
    buf1 = input("Entrez les valeurs du tableau a séparées par des espaces : ").split()
    buf2 = input("Entrez les valeurs du tableau b séparées par des espaces : ").split()

    # Remplissage des tableaux a et b avec les valeurs saisies converties en entiers
    for i in range(n):
        a[i] = int(buf1[i])
        b[i] = int(buf2[i])

    # Variable résultat, initialisée à 0 (aucune opération par défaut)
    r = 0

    # Si la somme de a est strictement inférieure à celle de b, retour impossible
    if np.sum(a) < np.sum(b):
        r = -1
    else:
        # Calcul du tableau des différences entre a et b
        c = a - b
        # Tri du tableau c en ordre croissant pour d'abord identifier les déficits
        c = np.sort(c)
        # Si tous les éléments sont positifs ou nuls, pas besoin d'opération
        if c[0] >= 0:
            r = 0
        else:
            # Recherche du premier indice où le déficit est comblé (élément positif ou nul)
            ii = -1
            for i in range(n):
                if c[i] >= 0:
                    ii = i
                    break
            # Somme initiale des déficits (tous les éléments négatifs)
            debt = np.sum(c[:i])
            # Boucle sur les excédents les plus importants pour combler le déficit
            for j in range(n):
                debt += c[n - 1 - j]
                if debt >= 0:
                    # Le nombre minimal d'opérations est le nombre d'index négatifs + le nombre d'index excédentaires utilisés
                    r = ii + (j + 1)
                    break
    # Affichage du résultat final
    print(r)

if __name__ == "__main__":
    main()