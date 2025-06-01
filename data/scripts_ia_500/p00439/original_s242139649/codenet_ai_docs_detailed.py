a, s = [0]*100003, [0]*100003

def max_subarray_sum_with_length_k():
    """
    Lit des paires (n, k) depuis l'entrée standard et pour chaque paire,
    calcule la somme maximale d'un sous-tableau de longueur k dans une séquence
    de n entiers. Le programme s'arrête quand n vaut 0.

    Processus:
    - Lecture de n et k.
    - Lecture d'une séquence de n entiers.
    - Calcul des sommes cumulatives ajustées pour obtenir les sommes
      de sous-tableaux de taille k.
    - Recherche et affichage de la somme maximale parmi ces sous-tableaux.
    """
    while True:
        n, k = map(int, input().split())  # Lecture de n et k
        if n == 0:
            break  # Condition d'arrêt du programme

        # Lecture du premier élément de la séquence
        a[0] = int(input())
        s[0] = a[0]  # Initialisation de la somme cumulative

        # Lecture du reste des éléments et calcul des sommes ajustées
        for i in range(1, n):
            a[i] = int(input())  # Lecture de l'élément i
            s[i] = s[i-1] + a[i]  # Calcul de la somme cumulée jusqu'à i

            # Ajustement de la somme pour que s[i] représente la somme
            # d'un sous-tableau de taille k se terminant à i
            if i >= k:
                s[i] -= a[i-k]

        ans = 0  # Initialisation de la valeur maximale trouvée

        # Recherche de la somme maximale parmi les sous-tableaux de longueur k
        for i in range(k-1, n):
            if s[i] > ans:
                ans = s[i]

        print(ans)  # Affichage de la somme maximale trouvée

max_subarray_sum_with_length_k()