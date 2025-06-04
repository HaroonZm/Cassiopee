def main():
    """
    Fonction principale qui lit deux entrées utilisateur, traite une suite de transitions dynamiques,
    puis affiche le résultat d'une opération basée sur une récurrence modulo 10**9+7.

    Entrées:
        - N (int): entier représentant le nombre d'itérations de la récurrence.
        - M (int): entier représentant la longueur d'une chaîne lue en entrée.

    Sortie:
        - Affiche un entier, résultat du calcul récurrent basé sur N et M.
    """
    # Lire la valeur N depuis l'entrée standard
    N = int(input())

    # Lire une chaîne et en calculer sa longueur pour déterminer M
    M = len(input())

    # Définir la constante de module (grand nombre premier)
    O = 10**9 + 7

    # Initialiser la liste D où D[k] à chaque étape représente une quantité calculée
    # La première valeur (indice 0) est calculée avec pow(-~O//2, M, O)
    # -~O//2 réalise en fait (O+1)//2, soit le nombre entier supérieur à O/2
    D = [pow((-~O)//2, M, O)] + [0] * (N + 1)

    # Effectuer N itérations de la récurrence
    for _ in range(N):
        # Pour chaque position, calculer le nouvel état selon la relation de récurrence:
        # D'[i] = (2 * D[i-1] (si i>0) + D[i+1]) % O
        # Le cas i==0 ne multiplie pas D[i-1] par 2 (car i-1 invalide)
        D = [
            ((2 * D[i - 1] if i > 0 else D[0]) + D[i + 1]) % O
            for i in range(N + 1)
        ] + [0]  # Ajouter un élément à la fin pour aligner les index lors de la prochaine itération

    # Afficher le résultat final pour l'indice M
    print(D[M])


if __name__ == "__main__":
    main()