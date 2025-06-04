import queue

def bfs_shortest_distances(adj_list, start, n):
    """
    Effectue une recherche en largeur (BFS) pour calculer les distances minimales
    depuis le sommet de départ 'start' vers tous les autres sommets du graphe.

    Args:
        adj_list (list): Liste d'adjacence représentant le graphe.
        start (int): Index du sommet de départ pour la BFS.
        n (int): Nombre total de sommets dans le graphe.

    Returns:
        list: Liste des distances minimales entre 'start' et chaque sommet.
              La distance non atteinte sera égale à 'inf'.
    """
    inf = 300001  # Valeur considérée comme l'infini pour les distances inaccessibles.
    distances = [inf] * n  # Initialisation de toutes les distances à 'inf'.
    distances[start] = 0  # Distance au sommet de départ = 0
    q = queue.Queue()
    q.put(start)
    while not q.empty():
        u = q.get()
        for v in adj_list[u]:  # Parcours de tous les voisins du sommet 'u'
            if distances[v] > distances[u] + 1:
                distances[v] = distances[u] + 1
                q.put(v)
    return distances

def main():
    """
    Programme principal qui lit l'entrée, construit un graphe non orienté,
    puis calcule le nombre spécifique de paires de chemins selon certaines contraintes.

    - Lit les sommets, arêtes et deux sommets sources s et t.
    - Construit la liste d'adjacence à partir des arêtes.
    - Calcule, pour chaque sommet, la distance minimale à 's' et à 't' (par BFS).
    - Compte pour chaque distance combien de sommets sont à une distance donnée de 's' et de 't'.
    - Calcule le nombre de paires (u, v) tel que la somme de leurs distances à s et t vaut la distance minimale entre s et t moins 2.
    - Affiche le résultat final.
    """
    # Lecture des paramètres du graphe et des sommets sources
    n, m, s, t = map(int, input().split())
    s -= 1  # Ajustement vers l'indexation 0
    t -= 1

    # Construction de la liste d'adjacence pour le graphe non orienté
    adj_list = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1  # Ajustement vers l'indexation 0
        b -= 1
        adj_list[a].append(b)
        adj_list[b].append(a)

    inf = 300001  # Constante d'infini
    # Calcul des distances minimales depuis 's' et depuis 't'
    dist_s = bfs_shortest_distances(adj_list, s, n)
    dist_t = bfs_shortest_distances(adj_list, t, n)

    # Préparation des histogrammes des distances à s et t
    s_list = [0] * (inf + 1)  # s_list[d] == nombre de sommets à distance d de s
    t_list = [0] * (inf + 1)  # t_list[d] == nombre de sommets à distance d de t
    for i in range(n):
        s_list[dist_s[i]] += 1
        t_list[dist_t[i]] += 1

    # Distance minimale entre s et t
    min_dist = dist_s[t]

    # Calcul du nombre de paires (u, v) tels que dist_s[u] + dist_t[v] == min_dist - 2
    ans = 0
    for i in range(min_dist - 1):  # Pour chaque distance possible de s (sauf le dernier pas)
        ans += s_list[i] * t_list[(min_dist - 2) - i]

    print(ans)

# Point d'entrée du script
if __name__ == "__main__":
    main()