from heapq import heappush, heappop  # Importation des fonctions pour gérer une file de priorité (tas) : heappush ajoute un élément, heappop enlève et retourne l'élément de plus petite valeur
INF = 10 ** 20  # Définition d'une constante 'INF' représentant une très grande valeur utilisée pour initialiser les distances comme infinies

# Lecture des entrées : n, m, k, s
# n : nombre de nœuds (sommets) dans le graphe
# m : nombre d'arêtes (connexions) dans le graphe
# k : nombre de nœuds initialement marqués ou particuliers (ex : stations Z)
# s : une distance seuil utilisée dans le calcul du coût
n, m, k, s = map(int, input().split())  # map applique int à chaque élément de la ligne d'entrée splittée en liste

# Lecture des coûts p et q
# p : coût normal de déplacement
# q : coût réduit ou spécifique lorsque la distance est inférieure ou égale à s
p, q = map(int, input().split())

# Initialisation d'une liste z_dist pour stocker la distance minimale de chaque nœud à un nœud spécial marqué (station Z)
# On initialise toutes les distances à INF pour signifier qu'elles sont inconnues/infinies au départ
z_dist = [INF] * n

# Initialisation d'une file de priorité vide, qui contiendra les nœuds à traiter
que = []  

# Pour chaque nœud marqué (station Z), on le lit, on note sa distance à 0 car c'est le point de départ,
# puis on l'ajoute dans la file de priorité pour traitement dans une prochaine étape
for _ in range(k):
  c = int(input()) - 1  # On soustrait 1 car l'indexation en Python commence à 0, alors que l'entrée est souvent à partir de 1
  z_dist[c] = 0  # Distance à soi-même est 0
  heappush(que, (0, c))  # On insère un tuple (distance, nœud) dans la file de priorité

# Construction du graphe sous forme de liste d'adjacence
# edges[i] contiendra la liste des nœuds adjacents au nœud i
edges = [[] for _ in range(n)]  # Création de n listes vides

# Lecture des arêtes du graphe (connexions)
for _ in range(m):
  a, b = map(int, input().split())
  a -= 1  # Ajustement de l'index pour aller de 1-based à 0-based
  b -= 1
  # Ajout du lien dans les deux sens car le graphe est non orienté (bidirectionnel)
  edges[a].append(b)
  edges[b].append(a)

# Maintenant, on va calculer les distances minimales de chaque nœud à une station Z en utilisant une recherche à coût uniforme (Dijkstra modifié)
while que:  # Tant que la file de priorité n'est pas vide
  total, node = heappop(que)  # Extraction du nœud avec la plus petite distance actuelle
  for to in edges[node]:  # Parcours des voisins du nœud courant
    # Si la distance minimale connue au voisin est supérieure à la distance actuelle + 1 (puisqu'on passe par node)
    if z_dist[to] > total + 1:
      z_dist[to] = total + 1  # Mise à jour de la distance minimale au voisin
      heappush(que, (total + 1, to))  # Ajout du voisin dans la file de priorité pour continuer l'exploration

# Après ce calcul, z_dist[i] donne la distance minimale du nœud i à la station Z la plus proche

# Initialisation d'une liste cost pour stocker le coût total minimum pour atteindre chaque nœud depuis le nœud 0
cost = [INF] * n  # Initialement, le coût de chacun est infini
cost[0] = 0  # Le coût pour atteindre le point de départ (nœud 0) est 0

# Réinitialisation de la file de priorité pour chercher le chemin minimal en prenant en compte les coûts variables
que = []

# On insère le point de départ dans la file de priorité avec un coût 0
heappush(que, (0, 0))

# Algorithme de Dijkstra classique modifié pour prendre en compte les coûts p ou q selon la distance à la station Z
while que:  # Tant que la file de priorité n'est pas vide
  total, node = heappop(que)  # Extraction du nœud avec le coût actuel minimal
  for to in edges[node]:  # Parcours des voisins du nœud courant

    # Cas particulier du nœud d'arrivée (n-1) : on vérifie s'il est possible d'améliorer son coût sans ajouter un coût supplémentaire
    if to == n - 1:
      if cost[to] > total:
        cost[to] = total  # Mise à jour du coût pour atteindre le dernier nœud
        continue  # On ne poursuit pas l'ajout du nœud dans la queue car c'est la fin

    # Si la distance à la station Z du voisin est 0, cela signifie que le voisin est lui-même une station Z
    # Dans ce cas, on ne doit pas passer par ce nœud (donc on le skip)
    if z_dist[to] == 0:
      continue

    # Selon la distance à la station Z, on choisit le coût du déplacement vers ce voisin
    if z_dist[to] <= s:
      price = q  # Coût réduit car le nœud est proche d'une station Z
    else:
      price = p  # Coût normal si le nœud est trop éloigné

    # Si le coût pour atteindre ce voisin via le nœud courant est meilleur que le coût précédemment connu,
    if cost[to] > total + price:
      cost[to] = total + price  # Mise à jour du coût minimal
      heappush(que, (total + price, to))  # Ajout dans la file de priorité pour exploration future

# À la fin, cost[n - 1] contient le coût minimal pour atteindre le dernier nœud depuis le premier
print(cost[n - 1])  # Affichage du résultat final au format attendu