from heapq import heappop, heappush, heapify  # Importation des fonctions utiles pour manipuler une file de priorité (heap)

MAX_MONEY = 2500  # Limite maximale d'argent qu'un état peut avoir, pour restreindre la taille des structures de données
INF = float("inf")  # Représente une valeur infiniment grande, utilisée pour initialiser les distances
n, m, s = map(int, input().split())  # Lecture des entiers n = nombre de sommets, m = nombre d'arêtes, s = argent initial

# Si l'argent de départ dépasse la limite, on le réduit à la limite autorisée
s = min(s, MAX_MONEY)

# Initialisation du graphe : une liste de n sous-listes vides
graph = [[] for _ in range(n)]
for _ in range(m):  # On boucle sur chaque arête du graphe
    u, v, a, b = map(int, input().split())  # u et v sont les extrémités, a le coût en argent, b le coût en temps
    u -= 1  # Conversion de l'indice vers 0-based (Python)
    v -= 1  # Idem pour v
    graph[u].append((v, a, b))  # Ajoute l'arête (voisin, coût en argent, coût en temps) dans la liste d'adjacence de u
    graph[v].append((u, a, b))  # Comme le graphe est non-orienté, ajoute aussi dans celle de v

# Lecture de la liste des options de change pour chaque sommet
# Pour chaque sommet i, cd[i] = (nombre de pièces qu'on peut ajouter, coût en temps associé)
cd = [tuple(map(int, input().split())) for _ in range(n)]

# Création et initialisation de la table dp :
# dp[v][money] contiendra le coût minimal pour atteindre le sommet v avec 'money' pièces
dp = [[INF] * (MAX_MONEY+10) for _ in range(n)]  # On ajoute un offset pour éviter tout débordement d'indice
dp[0][s] = 0  # Coût nul pour être au sommet 0 avec s pièces

# Initialisation de la file de priorité avec le point de départ :
# (coût accumulé, indice du sommet courant, nombre de pièces courantes)
q = [(0, 0, s)]

# Boucle principale : variante de Dijkstra prenant en compte l'argent comme seconde dimension d'état
while q:  # On continue tant qu'il existe des états à explorer
    dist, v, money = heappop(q)  # On récupère l'état avec le coût accumulé minimal (priorité la plus haute)
    
    # Si l'on trouve cet état avec un meilleur coût déjà enregistré, on saute
    if dp[v][money] < dist:
        continue
    
    # Parcours de tous les voisins du sommet courant
    for nv, fare, cost in graph[v]:  # nv = voisin, fare = pièces nécessaires, cost = coût en temps
        nm = money - fare  # On calcule le nouveau nombre de pièces après avoir payé
        if nm < 0:
            continue  # Si l'on n'a pas assez de pièces, on ignore cette transition
        # Si on améliore le coût pour atteindre (nv, nm), on met à jour et on empile ce nouvel état
        if dp[nv][nm] > dp[v][money] + cost:
            dp[nv][nm] = dp[v][money] + cost
            heappush(q, (dp[nv][nm], nv, nm))
    
    # On considère l'opération de change sur place
    # nm = min(number of pièces augmenté à cd[v][0], mais pas plus que MAX_MONEY)
    nm = min(money + cd[v][0], MAX_MONEY)
    # Si cette opération permet d'améliorer le coût pour rester sur place avec ce nouveau nombre de pièces
    if dp[v][nm] > dp[v][money] + cd[v][1]:
        dp[v][nm] = dp[v][money] + cd[v][1]
        heappush(q, (dp[v][nm], v, nm))  # On ajoute cet état à la file pour exploration future

# Après la terminaison de la boucle, pour chaque sommet excepté le sommet de départ
for i in range(1, n):  # On commence à 1 car 0 est le sommet de départ
    # On affiche la valeur minimale de dp pour ce sommet sur tous les montants d'argent possibles
    print(min(dp[i]))  # Cela donne le coût minimal (en temps) pour atteindre ce sommet, quelle que soit la quantité d'argent restante