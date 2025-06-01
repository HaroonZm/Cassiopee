import sys

# Le module sys permet d'interagir avec l'interpréteur Python, notamment pour la gestion de la récursion.
# La fonction setrecursionlimit modifie la limite maximale d'appels récursifs pouvant être effectués dans le programme.
# Par défaut, Python limite le nombre de récursions pour éviter un dépassement de pile,
# ici on augmente cette limite à 100000 appels récursifs afin de permettre une profondeur de récursion très élevée.
sys.setrecursionlimit(100000)

# On lit deux entiers depuis l'entrée standard.
# int(input()) prend une entrée utilisateur, la transforme en entier, puis stocke dans la variable correspondante.
# V représente le nombre de sommets (ou nœuds) dans un graphe.
# E représente le nombre d'arêtes (connexions entre les sommets) dans ce graphe.
V, E = int(input()), int(input())

# L est une liste vide, elle sera utilisée pour stocker un ordre topologique des sommets.
L = []

# visited est une liste de taille V initialisée à zéro.
# Chaque élément correspond à un sommet ; 0 signifie que le sommet n'a pas encore été visité.
# On utilise une compréhension de liste pour créer cette liste efficace.
visited = [0 for i in range(V)]

# edges est une liste de listes de taille V.
# Chaque élément edges[i] est une liste qui contiendra les sommets vers lesquels il est possible d'aller à partir du sommet i.
# Cela représente la structure du graphe sous forme de liste d'adjacence.
edges = [[] for i in range(V)]

# Définition d'une fonction récursive appelée visit qui prend en paramètre un sommet x.
# Cette fonction explore les sommets du graphe à partir de x, en profondeur.
def visit(x):
    # La condition vérifie si le sommet x n'a pas encore été visité.
    # visited[x] == 0 signifie non visité, != 0 signifie visité.
    if not visited[x]:
        # On marque le sommet x comme visité en assignant la valeur 1.
        visited[x] = 1
        # Pour chaque sommet e accessible depuis x (dans edges[x]),
        # on appelle récursivement visit(e) pour explorer plus profondément.
        for e in edges[x]:
            visit(e)
        # Une fois tous les successeurs de x explorés, on ajoute x à la liste L.
        # Cela correspond à un traitement post-ordre dans la recherche en profondeur,
        # typique pour calculer un ordre topologique d'un graphe orienté.
        L.append(x)

# On lit ensuite E lignes d'entrée, représentant les arêtes du graphe.
# À chaque itération, s et t sont les extrémités d'une arête dirigée de s vers t.
# map(int, input().split()) lit deux entiers séparés par un espace.
for i in range(E):
    s, t = map(int, input().split())
    # On soustrait 1 aux sommets pour passer d'une numérotation 1-based à 0-based (commençant à 0),
    # ce qui est standard pour les indices en Python.
    # On ajoute ce sommet t-1 à la liste d'adjacence du sommet s-1,
    # pour indiquer qu'un arc existe de s-1 vers t-1.
    edges[s - 1].append(t - 1)

# Pour chaque sommet i dans la plage 0 à V-1,
# si ce sommet n'a pas été visité, on lance la fonction visit(i) pour l'explorer.
# Cela permet de couvrir tous les composantes du graphe même s'ils sont déconnectés.
for i in range(V):
    if not visited[i]:
        visit(i)

# Après la visite, L contient les sommets dans l'ordre inverse d'un ordre topologique.
# Pour obtenir l'ordre topologique correct, il faut inverser la liste L.
L.reverse()

# Initialisation d'un indicateur flag à 0.
# Ce flag permettra de détecter une condition spécifique sur les liens entre sommets dans L.
flag = 0

# On parcourt la liste L contenant l'ordre topologique des sommets.
for i in range(V):
    # Affichage du sommet i dans l'ordre topologique, en remettant à l'indexation 1-based avec +1.
    print(L[i] + 1)
    # On vérifie deux conditions uniquement si flag est encore 0 :
    # 1. On s'assure que i n'est pas le dernier indice (pour accéder à i+1).
    # 2. On vérifie si le sommet suivant dans la liste L (L[i+1]) n'est pas un successeur direct du sommet courant L[i].
    # Cette condition signifie que dans notre ordre topologique, les sommets successifs ne sont pas directement connectés.
    if not flag and i < V - 1 and (L[i + 1] not in edges[L[i]]):
        # Si cette condition est vraie, on positionne flag à 1.
        # Cela peut indiquer que la chaîne de successeurs dans l'ordre topologique n'est pas un chemin strict du graphe.
        flag = 1

# Enfin, on affiche la valeur de flag qui signalera si une telle discontinuité a été trouvée.
print(flag)