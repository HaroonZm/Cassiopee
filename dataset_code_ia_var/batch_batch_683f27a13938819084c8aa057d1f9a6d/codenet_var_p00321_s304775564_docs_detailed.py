def main():
    """
    Lit les données depuis l'entrée standard, traite des paires issues de groupes,
    puis sélectionne celles qui apparaissent au moins f fois. Affiche le nombre 
    de ces paires et liste les paires retenues avec un tri personnalisé.
    """
    # Lecture du nombre de groupes (n) et du seuil de fréquence (f)
    n, f = map(int, input().split())
    
    # Dictionnaire pour compter les occurrences de chaque paire
    pair_count = {}
    
    # Boucle sur chaque groupe
    for _ in range(n):
        # Lecture d'une ligne : premier élément = nombre d'éléments ; le reste, la liste des éléments
        values = input().split()
        m, *c = values  # m = nombre d'éléments, c = liste d'éléments (strings)
        m = int(m)
        
        # Parcourt toutes les paires possibles dans le groupe (sans doublon ni auto-paire)
        for i in range(m - 1):
            for j in range(i + 1, m):
                # Trie la paire pour éviter les permutations dans le comptage
                p = (min(c[i], c[j]), max(c[i], c[j]))
                # Incrémente le nombre de fois où cette paire apparaît
                if p in pair_count:
                    pair_count[p] += 1
                else:
                    pair_count[p] = 1
    
    # Liste pour stocker les paires apparaissant au moins 'f' fois, avec leur compte
    frequent_pairs = []
    for pair in pair_count:
        if pair_count[pair] >= f:
            frequent_pairs.append((pair, pair_count[pair]))
    
    # Tri des paires : d'abord sur le second élément, puis sur le premier (ordre lexicographique)
    frequent_pairs.sort(key=lambda x: x[0][1])
    frequent_pairs.sort(key=lambda x: x[0][0])
    
    # Affiche le nombre total de telles paires
    print(len(frequent_pairs))
    
    # Affiche chaque paire (deux éléments, sans leur nombre d'occurrences)
    for pair_info in frequent_pairs:
        print(*pair_info[0])

if __name__ == "__main__":
    main()