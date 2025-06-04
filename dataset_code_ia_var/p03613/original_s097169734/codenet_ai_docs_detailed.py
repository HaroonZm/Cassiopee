def get_maximum_appearance():
    """
    Lecture des entrées depuis l'utilisateur, puis calcul du nombre maximal d'apparitions
    parmi chaque entier original et ses voisins (+1 et -1). 
    Affiche la valeur maximale d'apparition qu'on peut obtenir pour un nombre lorsque
    l'on considère chaque a_i, a_i+1 et a_i-1 pour chaque élément a_i de la liste d'entrée.

    Entrée:
        - la première ligne contient un entier n, la taille de la liste.
        - la deuxième ligne contient n entiers, séparés par des espaces.

    Sortie:
        - un entier : le nombre maximal d'apparitions obtenu (voir description ci-dessus).
    """
    # Lecture de la taille de la liste
    n = int(input())
    # Lecture de la liste d'entiers séparés par des espaces
    a = list(map(int, input().split()))

    # Dictionnaire pour compter les apparitions de chaque nombre
    # lors du passage sur a_i, a_i+1, a_i-1 pour chaque a_i.
    ans = {}
    for i in a:
        # On considère les nombres i-1, i, i+1
        for j in range(3):
            current = i + j - 1  # i-1, i, i+1 lors de j=0,1,2 respectivement
            if current not in ans:
                ans[current] = 1
            else:
                ans[current] += 1

    # On cherche le nombre dont la fréquence (selon la règle ci-dessus) est maximale
    print(max(ans.values()))

# Déclencher la fonction principale
get_maximum_appearance()