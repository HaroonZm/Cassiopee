def main():
    """
    Point d'entrée principale du programme.
    Lit des arbres pondérés depuis l'entrée utilisateur et affiche pour chacun
    la différence entre le temps total pour parcourir tous les bords deux fois
    et le temps maximal pour atteindre une feuille depuis la racine.
    """
    while True:
        # Lecture du nombre de sommets (noeuds) dans l'arbre courant
        n = int(input())
        # Condition d'arrêt : si n == 0, on quitte la boucle principale
        if n == 0:
            break

        # Initialisation de la liste des arêtes (voisins) pour chaque noeud
        edges = [[] for _ in range(n)]
        # Lecture des n-1 arêtes pour construire l'arbre
        for _ in range(n - 1):
            a, b, t = map(int, input().split())
            # On convertit en indices à base zéro
            a -= 1
            b -= 1
            # Ajout des voisins respectifs avec le poids de l'arête
            edges[a].append([b, t])
            edges[b].append([a, t])

        # Liste pour marquer si un noeud a été utilisé lors du parcours
        used = [False] * n
        # Liste pour identifier les feuilles de l'arbre (hors racine)
        is_leaf = [False] * n
        # On identifie les feuilles (degré 1) en ignorant la racine (noeud 0)
        for i in range(1, n):
            if len(edges[i]) == 1:
                is_leaf[i] = True

        def check(x):
            """
            Parcourt récursivement l'arbre à partir du noeud x afin de calculer :
            - le temps total pour parcourir toutes les arêtes depuis ce noeud, en allant et retour ;
            - le chemin le plus long (max_path) menant à une feuille (depuis x).

            Args:
                x (int): indice du noeud courant

            Returns:
                tuple: (somme totale des temps pour parcourir toutes les arêtes sous x,
                        temps du chemin le plus long depuis x jusqu'à une feuille)
            """
            used[x] = True  # Marque ce noeud comme visité
            times = [0]     # Liste des temps pour chaque sous-arbre. On commence à 0 pour inclure la racine.
            max_path = 0    # Maximum du chemin le plus long de x à une feuille

            for to, t in edges[x]:
                # On parcourt seulement les enfants non encore visités et qui ne sont pas une feuille
                if not used[to] and not is_leaf[to]:
                    # Appel récursif sur le sous-arbre de to
                    time, path = check(to)
                    # Pour faire l'aller-retour dans le sous-arbre, on multiplie le poids par 2
                    times.append(time + t * 2)
                    # On met à jour le chemin le plus long
                    max_path = max(max_path, path + t)
            # La somme totale correspond à la somme de tous les aller-retour vers les enfants non-feuilles
            return sum(times), max_path

        # On lance l'exploration depuis la racine (noeud 0)
        total_time, max_path = check(0)
        # Affichage de la différence (stratégie d'optimisation du parcours)
        print(total_time - max_path)

# Lancement du programme principal
if __name__ == "__main__":
    main()