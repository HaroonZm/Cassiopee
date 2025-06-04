def main():
    # Demande à l'utilisateur d'entrer une valeur et transforme la chaîne d'entrée en entier avec int()
    n = int(raw_input())  # n représente le nombre de matrices ou d'ensembles de dimensions à traiter

    # Création d'une matrice carrée de taille n x n remplie de zéros
    # On utilise une compréhension de liste pour générer la liste, ce qui est équivalent à une boucle imbriquée
    # [ [0] * n for _ in xrange(n)] crée une liste contenant n éléments, chacun étant une liste de n zéros
    m = [ [0] * n for _ in xrange(n)]

    # Création d'une liste p contenant n+1 zéros
    # Cela servira à stocker les dimensions des matrices
    p = [ 0 for _ in xrange(n+1)]

    # Boucle for qui s'exécute de 0 à n-1 (total n passages)
    for i in xrange(n):
        # Lit une ligne de l'entrée utilisateur, la découpe en parties séparées par des espaces
        # et convertit chaque élément en entier
        a = map(int, raw_input().split())

        # Si nous sommes à la première itération (i == 0),
        # cela signifie que nous avons affaire à la première matrice ou au premier ensemble de dimensions
        if i == 0:
            # On stocke la première valeur de a dans p[0] et la deuxième valeur dans p[1]
            # Cela initialise les deux premières dimensions
            p[0] = a[0]
            p[1] = a[1]
        else:
            # Pour toutes les autres matrices (i > 0), on ajoute la dimension finale seulement
            # Cela est correct car les matrices sont enchaînées : la colonne de la matrice précédente
            # est la ligne de la suivante
            p[i+1] = a[1]

    # Boucle pour la chaîne de matrices, commençant à la longueur 2 jusqu'à la longueur n
    for l in xrange(2, n+1):  # l est la longueur de la sous-chaîne de matrices qu'on considère

        # Pour chaque position de départ possible i de la sous-chaîne de longueur l
        # l'intervalle est [i, j] avec j = i + l - 1
        for i in xrange(0, n - l + 1):
            j = i + l - 1    # Détermine la fin de la sous-chaîne

            # On initialise la valeur minimale de multiplication pour cette sous-chaîne
            # à l'infini (float('inf')), pour pouvoir rechercher un minimum réel ensuite
            m[i][j] = float('inf')

            # Parcourir tous les emplacements possibles où on peut diviser la sous-chaîne courante
            # k prend les valeurs de i à j-1 (il représente la séparation de la chaîne) 
            for k in xrange(i, j):

                # Calcul du coût total en choisissant de diviser à l'endroit k
                # m[i][k] : coût pour la première sous-chaîne
                # m[k+1][j] : coût pour la seconde sous-chaîne
                # p[i-1]*p[k]*p[j] : coût de la multiplication des deux matrices résultantes
                # On essaye de minimiser ce coût total sur toutes les valeurs de k possibles

                # À NOTER : p[i-1] peut donner une mauvaise valeur quand i == 0 (p[-1]) ! 
                # Mais le code d'origine le laisse ainsi.
                m[i][j] = min(m[i][j], m[i][k] + m[k+1][j] + p[i-1] * p[k] * p[j])

    # Affiche le nombre minimal de multiplications de la chaîne de matrices,
    # qui est stocké dans m[0][n-1]
    print m[0][n-1]

    # retourne 0 pour indiquer la fin normale de la fonction principale
    return 0

# Point d'entrée du programme
main()