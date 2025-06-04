continuer = True
while continuer:
    n = int(input())  # nombre de noeuds
    m = int(input())  # nombre d'arêtes
    if n == 0 and m == 0:
        continuer = False
        break
    edges = []
    for _ in range(m):
        ligne = input()
        u, v = map(int, ligne.split())
        edges.append([u, v])

    # je trie histoire que ça soit plus facile après
    edges.sort(key=lambda item: item[0])
    part1 = []
    part2 = []

    for pair in edges:
        premier, second = pair
        # J'ajoute tous les voisins du sommet 1 dans une partition
        if premier == 1:
            part1.append(second)
        # Ok, là on construit la 2e partition tant bien que mal
        elif premier in part1 and second not in part1 and second not in part2:
            part2.append(second)
        elif second in part1 and premier not in part1 and premier not in part2:
            part2.append(premier)
        # Est-ce que j'ai tout géré ? J'sais pas. On verra.

    # Bon, je suppose que la réponse c'est ça...
    print(len(part1) + len(part2))  # Normalement c'est bon, à vérifier quand même