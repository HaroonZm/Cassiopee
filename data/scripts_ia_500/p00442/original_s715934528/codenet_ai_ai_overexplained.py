from collections import deque  # Importation de la classe deque pour la gestion efficace d'une file d'attente

# Définition de la fonction TopoSort_cnt qui réalise un tri topologique avec un compteur spécifique
def TopoSort_cnt(n, cnt):
    # Création d'une file d'attente doublement terminée (deque) pour stocker les sommets avec degré entrant zéro
    start = deque()
    
    # Boucle qui parcourt chaque nœud de 0 à n-1 (xrange est utilisé pour Python 2, similaire à range en Python 3)
    for i in xrange(n):
        # Vérification si le degré entrant du nœud i est zéro, ce qui signifie qu'il n'a aucune dépendance préalable
        if indeg[i] == 0:
            # Ajout de ce nœud dans la file d'attente 'start' car il peut être traité immédiatement
            start.append(i)
            
    # Initialisation ou augmentation du compteur cnt par le nombre d'éléments initiaux dans 'start'
    cnt += len(start)
    
    # Tant que la file d'attente 'start' n'est pas vide, on continue à traiter les nœuds
    while len(start) > 0:
        # Suppression et récupération du premier élément de la file d'attente (traitement du sommet)
        i = start.popleft()
        # Ajout de ce nœud dans la liste 'ans' correspondant à l'ordre topologique des nœuds
        ans.append(i)
        
        # Initialisation d'un compteur temporaire à zéro pour compter les nouveaux nœuds ajoutés au cours de cette itération
        tmp = 0
        
        # Pour chaque nœud j adjacent au nœud i (tous les sommets accessibles directement depuis i)
        for j in g[i]:
            # Réduction du degré entrant du nœud j car le nœud i vient d'être traité/retiré
            indeg[j] -= 1
            # Si après décrément, le degré entrant de j est zéro, cela signifie qu'il n'a plus de dépendances non traitées
            if indeg[j] == 0:
                # Ajout de j dans la file d'attente pour traitement futur
                start.append(j)
                # Incrémentation du compteur temporaire pour ce noeud ajouté
                tmp += 1
        
        # Mise à jour du compteur cnt avec la valeur maximale entre cnt actuel et le produit cnt * tmp,
        # cela permet de compter les branches ou choix multiples pendant le tri topologique
        cnt = max(cnt, cnt * tmp)
    
    # Retour de la liste ans qui contient l'ordre topologique et du compteur cnt calculé
    return ans, cnt


# Définition de la fonction solve qui construit le graphe et applique la fonction TopoSort_cnt
def solve(n, m):
    # Boucle pour lire et traiter chacun des m arcs du graphe
    for i in xrange(m):
        # Lecture d'une ligne de l'entrée standard contenant deux entiers wt et lt représentant un arc wt -> lt
        wt, lt = map(int, raw_input().split())
        # Conversion des indices wt et lt en indices zéro-based (car listes Python commencent à 0)
        wt -= 1
        lt -= 1
        
        # Ajout du nœud lt dans la liste d'adjacence du nœud wt pour modéliser l'arc wt -> lt
        g[wt].append(lt)
        # Incrémentation du degré entrant du nœud lt car un nouvel arc entrant vers lt a été ajouté
        indeg[lt] += 1
    
    # Appel de la fonction TopoSort_cnt avec le nombre de nœuds n et un compteur initialisé à zéro
    ans, cnt = TopoSort_cnt(n, 0)
    
    # Condition pour déterminer si le compteur est strictement supérieur à 1,
    # ce qui indique qu'il existe plus d'une façon valide d'ordonner les tâches
    if cnt > 1:
        # Affichage de la solution finale en remettant les indices en base 1
        for i in xrange(n):
            print(ans[i] + 1)
        # Impression de 1 indiquant la multiplicité des solutions possibles
        print(1)
    else:
        # Sinon, réaffichage de la solution unique
        for i in xrange(n):
            print(ans[i] + 1)
        # Impression de 0 pour indiquer qu'il n'y a qu'une unique solution possible
        print(0)


# Lecture du nombre total de nœuds dans le graphe depuis l'entrée standard, conversion en entier
n = int(raw_input())
# Lecture du nombre total d'arcs dans le graphe depuis l'entrée standard, conversion en entier
m = int(raw_input())

# Initialisation d'une liste indeg contenant n entiers à zéro, représentant les degrés entrants de chaque nœud
indeg = [0] * n

# Initialisation de la liste g qui contiendra les listes d'adjacence de chacun des n nœuds,
# chaque élément est initialisé par une liste vide (aucune arête sortante au départ)
g = [[] for _ in xrange(n)]

# Initialisation de la liste ans vide qui contiendra l'ordre topologique des nœuds une fois calculé
ans = []

# Appel de la fonction solve avec les paramètres n (nombre de nœuds) et m (nombre d'arcs)
solve(n, m)