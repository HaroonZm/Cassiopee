import bisect

def main():
    """
    Point d'entrée principal du programme. Lit une liste d'entiers, puis exécute plusieurs requêtes de recherche
    utilisant la recherche binaire pour trouver les indices de début et de fin des occurrences d'un entier donné
    dans la liste triée.
    """
    # Lecture du nombre d'entiers dans la liste
    n = int(input())
    # Lecture de la liste des entiers, supposée déjà triée
    li = [int(a) for a in input().split()]
    # Lecture du nombre de requêtes
    q = int(input())

    # Traitement de chaque requête
    for _ in range(q):
        # Lecture de la valeur à rechercher
        k = int(input())
        # Recherche de l'indice du premier élément >= k
        l = bisect.bisect_left(li, k)
        # Recherche de l'indice du premier élément > k
        u = bisect.bisect_right(li, k)
        # Affichage des indices trouvés séparés par un espace
        print("{0} {1}".format(l, u))

if __name__ == "__main__":
    main()