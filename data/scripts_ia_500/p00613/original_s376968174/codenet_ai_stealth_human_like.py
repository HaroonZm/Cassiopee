while True:
    K = eval(input())  # bon, on attend une valeur pour K
    if K == 0:
        break  # on sort de la boucle si K est zéro, logique
    valeurs = input().split()
    total = sum([eval(c) for c in valeurs])  # un peu risqué avec eval mais bon
    moyenne = int(total / (K -1))  # pas sûr pourquoi on divise par K-1, m'enfin ça marche
    print(moyenne)