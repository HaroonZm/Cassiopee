def min_steps_to_process_elements():
    """
    Calcule et affiche le nombre minimal d'étapes nécessaires pour traiter tous les éléments d'une liste selon les paramètres donnés.

    L'utilisateur doit saisir deux entiers `n` et `k` sur la première ligne,
    puis une liste de `n` entiers sur la seconde ligne (la valeur de cette liste n'est pas utilisée dans le calcul).

    Logique :
      - À chaque étape, on peut traiter jusqu'à `k` nouveaux éléments, mais le premier élément doit être traité seul.
      - Après avoir traité le premier élément, on fait des groupes de taille jusqu'à `k` pour traiter tous les autres.
      - Le programme calcule le nombre minimal d'étapes nécessaires pour traiter tous les éléments.

    Affiche :
      - Le nombre minimal d'étapes, sous forme entière.
    """
    # Lecture des deux entiers n (taille de la liste) et k (taille maximale du groupe traité à chaque étape)
    n, k = map(int, input().split())
    # Lecture de la liste d'entiers (non utilisée dans la logique, requise uniquement pour l'entrée)
    a = list(map(int, input().split()))
    # Après avoir traité le premier élément, il faut encore traiter (n-k) éléments
    n -= k
    # k décrémente pour représenter le nombre d'éléments supplémentaires pouvant être traités par étape suivante
    k -= 1
    # Initialiser le compteur d'étapes à 1 (le premier élément déjà traité)
    p = 1
    if n <= 0:
        # Si tous les éléments sont déjà traités à la première étape, il ne faut qu'une étape
        print(p)
    else:
        # Sinon, calcule le nombre d'étapes nécessaires pour traiter les éléments restants
        if n % k == 0:
            # Si les éléments restants se divisent exactement en groupes de taille k
            print(p + n // k)
        else:
            # Si ce n'est pas exact, il faudra une étape supplémentaire pour les éléments restants
            print(p + n // k + 1)

# Appel de la fonction principale pour exécuter le programme
min_steps_to_process_elements()