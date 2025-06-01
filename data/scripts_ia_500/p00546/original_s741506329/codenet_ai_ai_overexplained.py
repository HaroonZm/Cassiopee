from collections import deque  # Importation de deque pour une file à double extrémité, permettant des opérations FIFO efficaces
import heapq                 # Importation de heapq pour utiliser une file de priorité (tas) efficace dans le calcul de plus courts chemins

# lecture et décomposition des entrées : N, M, K, S respectivement le nombre de villes, routes, villes infectées par des zombies, et la distance maximale pour considérer une ville "dangereuse"
N, M, K, S = map(int, input().split())

# lecture des coûts P et Q où P est le coût pour une ville "non dangereuse" et Q pour une ville "dangereuse"
P, Q = map(int, input().split())

C = []  # Initialisation de la liste des villes infectées par des zombies
for _ in range(K):        # Boucle K fois pour récupérer les indices des villes zombies
    C.append(int(input()))  # Ajout de la ville zombie en int dans la liste C

# Construction de la liste d'adjacence pour représenter le graphe, avec N+1 listes vides (les villes sont numérotées de 1 à N)
adj = [[] for _ in range(N + 1)]
for _ in range(M):        # Pour chaque route donnée
    a, b = map(int, input().split())  # Lire les deux extrémités de la route (ville a et ville b)
    adj[a].append(b)                   # Ajouter b comme voisin de a
    adj[b].append(a)                   # Ajouter a comme voisin de b (graphe non orienté)

expensive_cities = set()  # Ensemble des villes qui seront considérées comme dangereuses (à coût Q)

# Pour chaque ville infectée par un zombie, on fait une recherche en largeur (BFS) pour marquer comme dangereuses les villes accessibles en <= S routes
for c in C:
    q = deque([c])            # File de parcours BFS initialisée avec la ville zombie c
    step = 0                  # Compteur de distance en nombre d'arêtes parcourues depuis la ville zombie
    visited = [False] * (N + 1)  # Liste pour marquer les villes visitées, false initialement

    # Boucle BFS qui continue tant que la file n'est pas vide et que la limite S n'est pas dépassée
    while q and step <= S:
        l = len(q)            # Nombre de villes dans la file à ce niveau de BFS (distance step)
        new_q = deque()       # Nouvelle file pour le niveau suivant

        for _ in range(l):     # Parcours des villes actuelles à cette distance step
            node = q.popleft()   # Extraction de la ville en tête de file
            visited[node] = True # Marquage de la ville courante comme visitée

            for nei in adj[node]:   # Pour chaque voisin (ville voisine) de la ville courante
                if visited[nei]:    # Si la ville voisine a déjà été visitée, on l'ignore pour éviter les cycles
                    continue
                if nei in q or nei in new_q:  # Si la ville voisine est déjà dans la file actuelle ou la nouvelle file, on évite la redondance
                    continue
                if nei in C:      # Si la ville voisine est une ville zombie, on ne la considère pas pour cette phase (car déjà dangereuse)
                    continue
                new_q.append(nei)  # Ajout de la ville voisine dans la file pour traitement au niveau suivant (step+1)

        q = new_q    # Passage au niveau suivant en remplaçant la file actuelle par la nouvelle
        step += 1    # Incrément du compteur de distance (nombre d'arêtes parcourues)

    # Toutes les villes marquées comme visitées dans ce BFS (sauf les villes zombies elles-mêmes) sont considérées dangereuses (coût Q)
    for i in range(1, N + 1):
        if visited[i] and i not in C:  # Condition pour exclure les villes zombies initiales
            expensive_cities.add(i)    # Ajout dans l'ensemble des villes dangereuses

# Construction d'une nouvelle liste d'adjacence adj2 où chaque voisin est associé à un coût P ou Q, selon que la ville est dangereuse ou non
adj2 = [[] for _ in range(N + 1)]  # Initialisation avec N+1 listes vides
for i in range(1, N + 1):           # Pour chaque ville i du graphe
    for city in adj[i]:             # Pour chaque ville voisine city de i
        if city in C:               # Si la ville voisine est une ville zombie, on ignore cette route ici (pas de coût défini explicitement)
            continue
        # Si la ville voisine est dangereuse (dans expensive_cities), le coût est Q, sinon P
        if city in expensive_cities:
            adj2[i].append((city, Q))  # Ajout d'un tuple (ville, coût) à la liste d'adjacence pondérée
        else:
            adj2[i].append((city, P))  # Ajout d'un tuple (ville, coût) à la liste d'adjacence pondérée

# Initialisation de la file de priorité (tas) avec la distance 0 au point de départ, ville 1
pq = [(0, 1)]    # Liste avec un tuple (distance courante, numéro de ville)
dist = [float('inf')] * (N + 1)  # Tableau des distances minimum connues, initialisé à l'infini pour toutes les villes sauf le départ
visited = [False] * (N + 1)       # Tableau pour savoir si on a déjà fixé la distance minimale d'une ville
dist[1] = 0                       # Distance du point de départ vers lui-même est nulle

# Boucle principale de l'algorithme de Dijkstra pour trouver le plus court chemin pondéré
while pq:                    # Tant que la file de priorité n'est pas vide
    d, n = heapq.heappop(pq)  # Extraction de la ville avec la plus petite distance estimée
    if n == N:               # Si on atteint la ville finale N, on peut sortir (distance minimale trouvée)
        break
    visited[n] = True        # Marquage de cette ville comme définitivement traitée (distance minimale connue)

    for nei, nd in adj2[n]:  # Pour chaque voisin et coût associé de la ville n
        if visited[nei]:     # Si on a déjà traité ce voisin, on ignore pour éviter de retravailler dessus
            continue
        if d + nd < dist[nei]:  # Si le chemin via n est plus court que la meilleure distance connue vers nei
            dist[nei] = d + nd  # Mise à jour de la distance la plus courte vers nei
            heapq.heappush(pq, (d + nd, nei))  # Ajout dans la file de priorité avec la nouvelle distance estimée

# Après avoir calculé la distance minimale vers la ville N, on fait un ajustement final :
d = dist[N]            # Distance minimale calculée vers la ville N
if N in expensive_cities:  # Si la ville finale N est dangereuse
    print(d - Q)         # On enlève Q car on ne paie pas le coût de la ville d'arrivée elle-même
else:
    print(d - P)         # Sinon on enlève P pour la même raison (cout non appliqué à la ville d'arrivée)