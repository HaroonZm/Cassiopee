import heapq  # Importe le module heapq, utilisé pour créer et manipuler des files de priorité (tas binaire)

# Lit trois entiers séparés par des espaces depuis l'entrée standard.
# Ces trois entiers sont attribués respectivement à n, m, et K.
# n : nombre de sommets (noeuds) dans le graphe
# m : nombre d'arêtes (liens) dans le graphe
# K : nombre de noeuds spéciaux sources à considérer
n, m, K = map(int, raw_input().split())

# Crée une liste vide de listes pour représenter le graphe sous forme de liste d'adjacence.
# g[i] contiendra la liste des voisins du noeud i.
# La liste est initialisée pour chaque noeud, du noeud 0 jusqu'à n-1.
g = [[] for _ in xrange(n)]

# Initialise une matrice "cost" (n x n).
# cost[i][j] stockera le coût de l'arête entre les noeuds i et j.
# Pour l'instant, chaque coût est mis à 100000 (un nombre très grand arbitraire, ici utilisé comme "infini").
cost = [[10**5] * n for _ in xrange(n)]

# Ceci débute une boucle pour lire les informations des arêtes du graphe.
# Il y a exactement 'm' arêtes, donc la boucle s'exécute 'm' fois.
for i in xrange(m):
    # Lit trois entiers depuis l'entrée standard : a, b, l.
    # a : extrémité de l'arête
    # b : l'autre extrémité de l'arête
    # l : poids (coût) de l'arête
    a, b, l = map(int, raw_input().split())
    # On décrémente a et b de 1 car l'entrée est supposée 1-indexée (commence à 1), 
    # alors que les listes Python sont 0-indexées (commencent à 0).
    a -= 1
    b -= 1
    # On ajoute b à la liste des voisins de a, car il existe une arête de a à b.
    g[a].append(b)
    # On ajoute a à la liste des voisins de b, car la relation est symétrique (graphe non dirigé).
    g[b].append(a)
    # On enregistre le coût de l'arête entre a et b.
    cost[a][b] = l
    cost[b][a] = l

# On va utiliser une file de priorité (min-heap/tas binaire) pour Dijkstra, appelée pq ("priority queue").
pq = []
# On crée une liste de distances d pour stocker la distance minimale trouvée depuis n'importe quelle source spéciale
# vers chaque noeud du graphe. Elle est initialisée à l'infini (float('inf')) pour chaque noeud.
d = [float('inf')] * n

# Cette boucle lit K entiers correspondant aux points de départ spéciaux (sources de Dijkstra)
# et initialise la file de priorité à 0 pour ces sources.
for i in xrange(K):
    # Lit un entier c, l’identifiant d'une source. On décrémente de 1 pour passer à l'indexation 0.
    c = int(raw_input()) - 1
    # On ajoute un couple [0, c] à la file de priorité, 
    # 0 étant la distance initiale pour cette source à elle-même.
    heapq.heappush(pq, [0, c])
    # On met à jour la distance minimale pour ce sommet source à 0.
    d[c] = 0

# Boucle principale de l'algorithme de Dijkstra pour trouver les plus courts chemins depuis toutes les sources.
while len(pq) != 0:
    # Récupère l'élément ayant la plus faible distance actuellement dans la file (pop du tas binaire).
    # t : distance courante
    # u : sommet concerné
    t, u = heapq.heappop(pq)
    # Si la distance enregistrée est déjà plus petite que la distance actuellement examinée,
    # cela signifie que l'on a traité un chemin plus court auparavant, on ignore alors ce couple.
    if d[u] < t:
        continue
    # Parcourt tous les voisins v du noeud actuel u.
    for v in g[u]:
        # Si le chemin trouvé à travers u vers v est meilleur (plus court) que le meilleur connu jusque là
        # alors on met à jour la distance pour v.
        if d[u] + cost[u][v] < d[v]:
            d[v] = d[u] + cost[u][v]
            # On pousse ce nouveau couple distance-sommet dans la file de priorité pour exploration future.
            heapq.heappush(pq, [d[v], v])

# Après avoir calculé tous les plus courts chemins depuis les sources spéciales, 
# on cherche maintenant à trouver la valeur maximale demandée, stockée dans ans.
ans = 0
# On parcourt chaque noeud du graphe.
for i in xrange(n):
    # Pour chaque voisin j du noeud i (donc chaque arête plusieurs fois)
    for j in g[i]:
        # On calcule (1 + d[i] + d[j] + cost[i][j]) / 2.
        # Ce calcul suit la formule du problème pour le maximum cherché.
        # Note : d[i] correspond à la plus courte distance depuis n'importe quelle source jusqu'à i.
        # cost[i][j] est le coût de l'arête.
        # On ajoute 1, on somme, puis on fait une division entière par 2.
        ans = max(ans, (1 + d[i] + d[j] + cost[i][j]) / 2)
# Enfin, on affiche le résultat trouvé.
print(ans)