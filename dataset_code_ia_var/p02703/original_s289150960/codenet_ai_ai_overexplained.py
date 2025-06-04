import sys # Importation du module sys pour accéder aux objets liés au système, notamment les flux d'entrée/sortie
input = sys.stdin.readline # Redéfinition de la fonction input pour utiliser la méthode readline plus rapide sur l'entrée standard
import heapq # Importation du module heapq pour utiliser les files de priorité (tas binaire/min-heap)

def dijkstra(edge, start):
    # Cette fonction implémente l'algorithme de Dijkstra pour trouver les plus courts chemins depuis un sommet de départ
    n = len(edge) # On récupère le nombre de sommets du graphe (liste d'adjacence 'edge')
    dist = [float("inf")] * n # On crée une liste de distances, initialement remplies avec l'infini flottant, taille égale au nombre de sommets
    dist[start] = 0 # La distance du sommet de départ à lui-même est 0
    que = [(0, start)] # Initialisation d'une file de priorité (ici une liste contenant un tuple (distance, numéro de sommet)), utilisée pour explorer les sommets les plus proches en priorité
    while que: # Boucle principale tant que la file de priorité n'est pas vide
        d, v = heapq.heappop(que) # On retire de la file le sommet avec la plus petite distance courante, sous forme de tuple (d = distance, v = numéro du sommet)
        if dist[v] < d:
            continue # Si la distance mémorisée est déjà plus petite que celle qu'on traite, on ignore cette itération (chemin sous-optimal)
        for nv, nd in edge[v]: # Pour chaque sommet adjacent 'nv' accessible à partir de 'v', et le coût 'nd' du déplacement
            if dist[nv] > d + nd: # Si la distance vers 'nv' en empruntant ce nouvel arc est plus courte que celle qu'on connaît
                dist[nv] = d + nd # On met à jour la distance minimale vers 'nv'
                heapq.heappush(que, (dist[nv], nv)) # On ajoute ce nouveau couple distance/sommet dans la file de priorité afin de le traiter plus tard
    return dist # À la fin de la boucle, dist contenant la plus courte distance depuis 'start' vers chaque sommet est retournée

# Lecture des trois entiers n (nombre de sommets), m (nombre d'arêtes), et s (état initial ou départ spécifique)
n, m, s = map(int, input().split())
G = [[] for _ in range(n)] # Initialisation du graphe sous forme de liste d'adjacence : G[i] contiendra la liste des voisins de i

# Selon la valeur de s, le traitement diverge.
if s >= 2500:
    # Si le point de départ possède une valeur supérieure ou égale à 2500
    for _ in range(m): # Pour chaque arête, on la lit depuis l'entrée
        u, v, a, b = map(int, input().split()) # Lecture des informations de l'arête : deux sommets (u,v), coût associé a et b
        u -= 1 # Ajustement des indices des sommets en partant de 0 (en Python les listes sont indexées à partir de 0)
        v -= 1
        G[u].append((v, b)) # On ajoute à la liste d'adjacence de u un tuple (v, b) indiquant qu'il existe un arc de u à v de coût b
        G[v].append((u, b)) # Comme le graphe est non orienté, on ajoute aussi l'arc inverse dans G[v]
    L = dijkstra(G, 0) # On applique Dijkstra sur ce graphe à partir du sommet 0. Le résultat est stocké dans la liste L (distances minimales)

else:
    # Si s < 2500, version avancée du problème avec gestion d'états supplémentaires
    for _ in range(m):
        # On lit chaque arête du graphe, comme précédemment, mais potentiellement avec des informations supplémentaires
        u, v, a, b = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append((v, a, b)) # On stocke l'arc avec toutes ses informations (v, a, b)
        G[v].append((u, a, b))
    CD = [list(map(int, input().split())) for _ in range(n)] # Pour chaque sommet, on lit une paire d'entiers (c, d), stockés dans une liste CD
    edge = [[] for _ in range(n * 2500)] # On construit un graphe plus grand, où chaque état (sommet, montant d'argent) est représenté par un sommet virtuel distinct. Il y a 'n' sommets et 2500 valeurs d'argent différentes possible (états)
    for i in range(n): # Pour chaque sommet du graphe initial
        c, d = CD[i] # On récupère la paire (c, d) : coût d'augmentation d'argent, argent obtenu
        for k in range(2500): # Pour chaque valeur possible du montant d'argent détenu (de 0 à 2499)
            for v, a, b in G[i]:
                # Pour chaque voisin v de i, où a est le montant minimal nécessaire pour le déplacement, b le coût
                if k >= a: # On vérifie si on détient assez d'argent pour utiliser cette arête
                    edge[2500 * i + k].append((2500 * v + (k - a), b)) # On ajoute un arc de l'état (i,k) vers l'état (v,k-a) avec coût b
            if k + c < 2500:
                # On considère l'action d'augmenter son argent
                edge[2500 * i + k].append((2500 * i + (k + c), d)) # On peut passer de l'état (i, k) à (i, k+c) avec comme coût d
    dist = dijkstra(edge, s) # On lance Dijkstra sur le graphe des états, avec comme état de départ 's' (montant d'argent initial)
    L = [0] * n # Initialisation du résultat final : distances minimales pour atteindre chaque sommet
    for i in range(n):
        # Pour chaque sommet i, on cherche la plus petite distance parmi tous les états où ce sommet est atteint avec un montant d'argent quelconque
        L[i] = min(dist[2500 * i:2500 * (i + 1)]) # On prend le minimum des 2500 sous-distances associées à ce sommet
print(*L[1:], sep="\n") # Enfin, on affiche les distances finales pour tous les sommets sauf le premier (index 1 à n-1), chaque distance sur une ligne séparée (dépliage de la liste avec *)