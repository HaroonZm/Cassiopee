import sys  # Importation du module sys, pour interagir avec l'entrée/sortie du système et modifier certaines limites système

input = sys.stdin.readline  # Redéfinition de la fonction 'input' pour utiliser la lecture rapide (bufferisée) depuis l'entrée standard
sys.setrecursionlimit(10**6)  # Augmente la limite maximale de récursion autorisée à 1 000 000 pour éviter une erreur 'RecursionError' lors de l'utilisation de fonctions récursives profondes
from collections import deque  # Importation de deque depuis 'collections', une structure de données qui agit comme une file double (FIFO/LIFO)

# Définition de la fonction dfs pour la recherche en profondeur (Depth-First Search)
def dfs(v, p):
    global pos  # On utilise une variable globale 'pos' pour retenir une information accessible hors de la fonction
    
    seen[v] = True  # On indique que le noeud courant 'v' a été visité
    hist.append(v)  # On enregistre le noeud courant 'v' dans la liste 'hist', qui stocke l'historique du chemin de visite

    # On parcourt tous les voisins du noeud courant 'v' en utilisant sa liste d'adjacence
    for nv in adj_list[v]:
        if nv == p:  # Si le voisin 'nv' est le noeud parent 'p' (pour éviter de remonter en arrière dans le graphe)
            continue  # On saute cette itération pour éviter de revenir sur ses pas

        if seen[nv]:  # Si le voisin 'nv' a déjà été vu, cela signifie qu'un cycle est détecté
            pos = nv  # On sauvegarde dans 'pos' le noeud où on a détecté le cycle
            return  # On quitte la fonction dfs immédiatement car le cycle est trouvé
        
        dfs(nv, v)  # On appelle récursivement dfs sur le nouveau voisin (nv), ce qui continue l'exploration

        if pos != -1:  # Si 'pos' a été modifié et n'est plus égal à -1, cela signifie qu'on a trouvé le cycle et qu'on souhaite propager l'arrêt
            return  # On quitte la fonction pour arrêter l'exploration inutile

    hist.pop()  # Si on termine l'exploration du noeud 'v' sans trouver de cycle, on l'enlève de l'historique

N = int(input())  # Lecture du nombre d'arêtes (ou de noeuds selon l'utilisation ; ici chaque arête est lue séparément), conversion en entier

adj_list = [[] for _ in range(N)]  # Création d'une liste d'adjacence contenant N listes vides, chaque liste représente les voisins d'un noeud donné

# On parcourt N fois pour lire chaque arête (relation entre deux noeuds)
for _ in range(N):
    ui, vi = map(int, input().split())  # On lit deux entiers qui représentent des indices de noeuds (ui et vi)
    adj_list[ui-1].append(vi-1)  # On ajoute vi-1 (on convertit de 1-indexé à 0-indexé) à la liste des voisins de ui-1
    adj_list[vi-1].append(ui-1)  # On ajoute ui-1 à la liste des voisins de vi-1, car le graphe est non orienté

seen = [False] * N  # Création d'une liste booléenne de taille N pour marquer les noeuds visités, initialisée à False pour tous au départ
hist = deque([])  # Création d'un objet deque vide pour stocker l'historique du chemin de visite lors de la dfs
pos = -1  # Initialisation de la variable 'pos' à -1, signifiant qu'aucun cycle n'a encore été trouvé

dfs(0, -1)  # On commence la recherche en profondeur depuis le noeud 0 (premier noeud, suivant l'indexation Python) et avec parent indéfini (-1)

cycle = set()  # Création d'un ensemble vide pour stocker les noeuds qui font partie du cycle détecté

# On retire les éléments de 'hist' 1 à 1 (de la fin) pour retrouver la séquence de noeuds qui forment le cycle
while hist:
    t = hist.pop()  # On enlève et récupère le dernier élément de 'hist'
    cycle.add(t)  # On ajoute cet élément à l'ensemble 'cycle'
    if t == pos:  # Dès qu'on arrive sur le noeud où le cycle a été détecté, on a ajouté tous les noeuds du cycle
        break  # On sort de la boucle car on a terminé de remplir l'ensemble 'cycle'

Q = int(input())  # Lecture du nombre de requêtes (Q), conversion en entier

# On traite chaque requête indépendamment
for _ in range(Q):
    ai, bi = map(int, input().split())  # Pour chaque requête, on lit deux entiers 'ai' et 'bi', qui sont des noeuds
    # On vérifie si les deux noeuds sont tous les deux dans le cycle (c'est-à-dire sont membres de l'ensemble 'cycle')
    if ai-1 in cycle and bi-1 in cycle:
        print(2)  # Si les deux sont dans le cycle, on affiche 2 (exemple : il existe 2 chemins simples entre eux)
    else:
        print(1)  # Sinon, on affiche 1 (par exemple il n'existe qu'un seul chemin simple entre eux)