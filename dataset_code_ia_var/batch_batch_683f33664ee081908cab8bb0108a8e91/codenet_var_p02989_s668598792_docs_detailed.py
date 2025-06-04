def main():
    """
    Point d'entrée du programme. 
    Lit un entier (ignoré), puis une liste d'entiers depuis l'entrée standard,
    calcule la différence entre les deux éléments centraux de la liste triée,
    et affiche le résultat.
    """
    # Lire et ignorer la première valeur d'entrée (habituellement la taille de la liste)
    _ = input()

    # Lire la liste d'entiers, les mapper depuis input(), puis la trier par ordre croissant
    A = sorted(list(map(int, input().split())))

    # Calcul de l'indice médian de la liste triée
    mid_index = len(A) // 2

    # Calcul et affichage de la différence entre les deux éléments centraux
    # Pour une liste à nombre pair d'éléments, mid_index et mid_index-1 seront les deux éléments centraux
    print(A[mid_index] - A[mid_index - 1])

if __name__ == '__main__':
    # Si ce fichier est exécuté en tant que programme principal,
    # lancer la fonction principale main().
    main()