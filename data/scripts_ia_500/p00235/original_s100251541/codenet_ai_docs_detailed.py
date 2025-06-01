while True:
    # Lecture du nombre de noeuds dans l'arbre. Si n=0, fin du programme.
    n = int(input())
    if n == 0:
        break

    # Initialisation de la liste d'adjacence pour représenter l'arbre.
    # Chaque élément edges[i] contiendra une liste des voisins de i sous forme [voisin, poids_arête].
    edges = [[] for _ in range(n)]

    # Lecture des n-1 arêtes de l'arbre avec leurs poids t.
    for _ in range(n - 1):
        a, b, t = map(int, input().split())
        # Conversion en indices 0-based.
        a -= 1
        b -= 1
        # Ajout de l'arête dans les deux sens (arbre non orienté).
        edges[a].append([b, t])
        edges[b].append([a, t])

    # Liste pour marquer les noeuds visités lors du parcours en profondeur.
    used = [False] * n
    # Liste pour identifier les feuilles (noeuds avec un seul voisin sauf la racine).
    is_leaf = [False] * n
    for i in range(1, n):
        # Un noeud est une feuille s'il a exactement un voisin.
        if len(edges[i]) == 1:
            is_leaf[i] = True

    def check(x):
        """
        Fonction récursive qui calcule deux valeurs à partir du noeud x:
        - La somme totale des temps nécessaires pour visiter tous les sous-arbres non-feuilles descendants,
          en parcourant chaque arête aller-retour.
        - La plus longue distance aller simple sur un chemin descendant vers une feuille.

        Args:
            x (int): Le noeud courant depuis lequel on effectue la recherche.

        Returns:
            tuple: (total_time, max_path_length)
                total_time (int): Le temps cumulé des allers-retours sur les sous-arbres.
                max_path_length (int): La plus grande distance simple vers une feuille.
        """
        used[x] = True
        # Initialisation de la liste des temps avec 0 pour inclure la propre durée du noeud.
        times = [0]
        max_path = 0
        # Parcours des voisins du noeud x.
        for to, t in edges[x]:
            # On continue si le voisin n'a pas été visité et n'est pas une feuille.
            if not used[to] and not is_leaf[to]:
                # Appel récursif sur le sous-arbre voisin.
                time, path = check(to)
                # Ajout du temps d'aller-retour (t * 2) plus le temps du sous-arbre.
                times.append(time + t * 2)
                # Mise à jour de la plus longue distance simple.
                max_path = max(max_path, path + t)
        # On retourne la somme des temps et la plus longue distance simple.
        return sum(times), max_path

    # Calcul des résultats à partir de la racine (noeud 0).
    total_time, max_path = check(0)

    # Affiche le temps total moins la plus longue distance simple,
    # ce qui correspond au temps optimal en évitant le chemin le plus long en double.
    print(total_time - max_path)