from collections import deque  # Importation du module collections pour utiliser deque, une file double.

# Définition de la fonction de tri topologique avec comptage spécial.
def TopoSort_cnt(n, cnt):
    start = deque()  # Création d'une nouvelle file double pour stocker les sommets de départ du tri topologique.
    # Parcours de chaque sommet de 0 à n-1 (chaque sommet est numéroté avec i).
    for i in xrange(n):
        # Vérifie si le degré entrant (indeg) du sommet i est égal à 0, c'est-à-dire qu'il n'a pas de précédence.
        if indeg[i] == 0:
            # Si le sommet n'a pas de précédence, on l'ajoute à la file 'start'.
            start.append(i)
    # Incrémente 'cnt' (le compteur total) par la longueur initiale de la file, c'est-à-dire le nombre de sources.
    cnt += len(start)
    # Boucle tant que la file 'start' contient au moins un élément.
    while len(start) > 0:
        # Retire et récupère le premier sommet de la file pour le traiter.
        i = start.popleft()
        # Ajoute ce sommet à la liste 'ans', qui stocke l'ordre du tri topologique.
        ans.append(i)
        tmp = 0  # Variable temporaire pour compter le nombre de sommets ajoutés à 'start' dans cette itération.
        # Parcours de tous les sommets voisins de i, c'est-à-dire de tous les sommets accessibles directement depuis i.
        for j in g[i]:
            # On décrémente le degré entrant du sommet voisin de 1, car on va supprimer le sommet i du graphe.
            indeg[j] -= 1
            # Si maintenant le degré entrant de ce voisin est 0, cela signifie qu'il peut être ajouté à 'start'.
            if indeg[j] == 0:
                # On ajoute ce sommet voisin à la file pour traitement.
                start.append(j)
                tmp += 1  # Incrémente le compte temporaire.
        # Met à jour le compteur spécial 'cnt'. 'cnt*tmp' calcule un produit, on garde la valeur maximale entre 'cnt' et ce calcul.
        cnt = max(cnt, cnt * tmp)
    # Renvoie deux variables : l'ordre topologique construit et la valeur finale du compteur spécial.
    return ans, cnt

# Définition de la fonction principale de résolution.
def solve(n, m):
    # On lit m lignes, chacune définissant une arête orientée du graphe.
    for i in xrange(m):
        # Récupère deux entiers par ligne : wt (origine) et lt (destination) de l'arête.
        wt, lt = map(int, raw_input().split())
        # Décrémente de 1 pour passer de l'indexation 1-based à 0-based (Python commence à zéro).
        wt -= 1
        lt -= 1
        # Ajoute 'lt' à la liste d'adjacence du sommet 'wt', c'est-à-dire qu'il y a une arête wt -> lt.
        g[wt].append(lt)
        # Incrémente le degré entrant du sommet 'lt', car il a une arête supplémentaire pointant vers lui.
        indeg[lt] += 1
    # Appelle la fonction de tri topologique avec comptage spécial, avec 'n' sommets et un compteur initial à 0.
    ans, cnt = TopoSort_cnt(n, 0)
    # Si le compteur spécial est strictement supérieur à 1, on considère qu'une propriété spéciale est satisfaite.
    if cnt > 1:
        # On parcourt tous les sommets dans l'ordre topologique et on imprime leur indice en repassant à 1-based.
        for i in xrange(n):
            print(ans[i] + 1)
        # On affiche 1 car la propriété spéciale est satisfaite.
        print(1)
    else:
        # Sinon, même affichage des sommets en 1-based.
        for i in xrange(n):
            print(ans[i] + 1)
        # On affiche 0 car la propriété spéciale n'est pas satisfaite.
        print(0)

# Lecture du nombre total de sommets : entrée utilisateur convertie en entier.
n = int(raw_input())
# Lecture du nombre total d'arêtes : entrée utilisateur convertie en entier.
m = int(raw_input())
# Initialisation de la liste des degrés entrants, un entier pour chaque sommet initialisé à zéro.
indeg = [0] * n
# Initialisation de la liste d'adjacence pour décrire le graphe : une liste vide pour chaque sommet.
g = [[] for _ in xrange(n)]
# Initialisation de la liste pour contenir la solution finale du tri topologique.
ans = []

# Appel de la fonction principale pour résoudre le problème en utilisant les données précédemment lues.
solve(n, m)