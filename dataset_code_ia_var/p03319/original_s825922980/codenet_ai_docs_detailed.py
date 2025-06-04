def main():
    """
    Fonction principale du programme.
    Lit deux entiers N et K depuis l'entrée standard, puis une liste d'entiers (qui ne sert pas au calcul ici).
    Calcule et affiche le nombre minimum d'opérations requises selon une formule donnée.
    """
    from math import ceil  # Importation de la fonction ceil pour arrondir au supérieur

    # Lecture des valeurs N (taille du problème) et K (paramètre de limitation) depuis l'entrée standard
    N, K = map(int, input().split())

    # Lecture d'une liste d'entiers depuis l'entrée standard, stockée dans 'a'.
    # L'étoile permet de dépaqueter les valeurs dans la liste 'a'.
    *a, = map(int, input().split())

    # Calcul du nombre minimal d'opérations nécessaires.
    # (N - K) correspond au nombre d'éléments restants après la première opération.
    # Chaque opération suivante peut traiter jusqu'à (K - 1) nouveaux éléments,
    # car la première opération prend K éléments, et chaque suivante peut en traiter K-1 (supposant un recouvrement d'un élément).
    # On utilise ceil pour arrondir à l'entier supérieur (cas où la division n'est pas exacte).
    # On ajoute 1 pour compter la première opération.
    ans = ceil((N - K) / (K - 1)) + 1

    # Affichage du résultat final
    print(ans)

if __name__ == '__main__':
    main()