def calculate_median_difference():
    """
    Lit un entier n et une liste d'entiers d depuis l'entrée utilisateur,
    trie la liste, puis calcule et affiche la différence entre les deux médianes.
    
    Si n est pair, la différence correspondra à d[n//2] - d[(n-1)//2].
    Si n est impair, les deux indices sont identiques, donc la différence sera 0.
    """
    # Lecture de la taille de la liste
    n = int(input())
    # Lecture des éléments de la liste, en les convertissant en entiers
    d = list(map(int, input().split()))
    # Tri de la liste pour faciliter la recherche des médianes
    d.sort()
    # Calcule de la différence entre la médiane haute et la médiane basse
    # Pour un tableau trié, d[n//2] est la médiane "haute", d[(n-1)//2] est la médiane "basse"
    result = d[n // 2] - d[(n - 1) // 2]
    # Affichage du résultat
    print(result)

# Appel de la fonction principale
calculate_median_difference()