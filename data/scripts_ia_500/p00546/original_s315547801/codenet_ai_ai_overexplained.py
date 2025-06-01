from heapq import heappush, heappop  # Importation des fonctions d'une file de priorité (tas binaire) pour gérer efficacement les éléments selon leur priorité numérique
INF = 10 ** 20  # Définition d'une constante très grande représentant l'infini pratique, utilisée pour initialiser des distances inconnues

# Lecture et séparation de la première ligne d'entrée standard en quatre entiers n, m, k et s
# n : nombre de sommets (noeuds), m : nombre d'arêtes, k : nombre de noeuds spéciaux, s : seuil de distance
n, m, k, s = map(int, input().split())

# Lecture de la deuxième ligne d'entrée standard en deux entiers p et q
# p et q représentent des coûts différents associés au déplacement sur certains noeuds
p, q = map(int, input().split())

# Initialisation d'une liste nommée z_dist de taille n remplie avec la valeur INF
# Cette liste servira à stocker la distance minimale entre chaque noeud et le noeud spécial le plus proche
z_dist = [INF] * n

# Initialisation d'une liste vide qui sera utilisée comme une file de priorité (tas binaire)
# pour stocker les noeuds à explorer, ordonnés par leur distance courante
que = []

# Boucle exécutée k fois pour lire les indices des noeuds spéciaux
for _ in range(k):
  c = int(input()) - 1  # Lecture de l'indice du noeud spécial, ajustement pour passage à l'indexation 0 basée en Python
  z_dist[c] = 0  # Mise à jour de la distance de ce noeud spécial à lui-même, distance nulle
  heappush(que, (0, c))  # Ajout de ce noeud avec une priorité égale à 0 dans la file de priorité

# Création d'une liste de liste appelée edges de taille n, initialement vide à chaque indice
# chaque sous-liste contiendra les noeuds adjacents (arêtes) du noeud correspondant
edges = [[] for _ in range(n)]

# Boucle exécutée m fois pour lire les arêtes entre les noeuds
for _ in range(m):
  a, b = map(int, input().split())  # Lecture des noeuds connectés par une arête
  a -= 1  # Passage à l'indexation 0
  b -= 1
  edges[a].append(b)  # Ajout du noeud b à la liste des voisins du noeud a
  edges[b].append(a)  # Ajout du noeud a à la liste des voisins du noeud b (graphe non orienté)

# Algorithmique classique de propagation de distances minimale depuis les noeuds spéciaux
while que:  # Tant que la file de priorité n'est pas vide
  total, node = heappop(que)  # Extraction de l'élément avec la plus petite distance stockée (total = distance, node = noeud)
  for to in edges[node]:  # Parcours de tous les noeuds adjacents au noeud actuel
    if z_dist[to] > total + 1:  # Si la distance actuelle au noeud adjacent peut être améliorée en passant par node
      z_dist[to] = total + 1  # Mise à jour de la distance minimale
      heappush(que, (total + 1, to))  # Ajout du noeud adjacent avec sa nouvelle distance dans la file de priorité

# Initialisation d'une liste des coûts minimale pour atteindre chaque noeud depuis le noeud de départ (indice 0)
cost = [INF] * n
cost[0] = 0  # Le coût pour atteindre le noeud de départ depuis lui-même est nul

# Ré-initialisation de la file de priorité vide
que = []

# Ajout du noeud de départ avec un coût total de zéro
heappush(que, (0, 0))

# Boucle de recherche du chemin minimal avec prise en compte des coûts p et q
while que:  # Tant que la file de priorité n'est pas vide
  total, node = heappop(que)  # Extraction du noeud avec le coût total minimal connu
  for to in edges[node]:  # Parcours des voisins du noeud courant
    if to == n - 1:  # Si le noeud voisin est le noeud destination (dernier noeud, index n-1)
      print(total)  # Afficher le coût total minimal pour atteindre ce noeud destination
      que = []  # Vider la file de priorité pour arrêter la boucle principale
      break  # Sortir du for car le chemin optimal est trouvé

    if z_dist[to] == 0:  # Ignorer les noeuds qui sont eux-mêmes spéciaux où la distance z_dist est nulle
      continue

    # Détermination du prix à payer pour atteindre ce noeud voisin
    # Si la distance au noeud spécial le plus proche est inférieure ou égale à s, le coût est q
    # Sinon, le coût est p
    if z_dist[to] <= s:
      price = q
    else:
      price = p

    # Mise à jour du coût pour atteindre le noeud voisin to si ce nouveau chemin est meilleur
    if cost[to] > total + price:
      cost[to] = total + price  # Mise à jour du coût minimum
      heappush(que, (total + price, to))  # Ajout dans la file de priorité avec le nouveau coût total calculé