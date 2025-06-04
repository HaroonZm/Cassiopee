# Importer la classe deque du module collections, utilisée pour créer une file efficace
from collections import deque

# Lire deux entiers séparés par un espace depuis l'entrée standard. 
# V représente le nombre de sommets (nodes/vertices) du graphe, 
# et E le nombre d'arêtes (edges). 
# map(int, input().split()) convertit chaque entrée en entier.
V, E = map(int, input().split())

# Initialiser un dictionnaire pour représenter la liste d'adjacence du graphe :
# - les clés sont les sommets de départ,
# - les valeurs sont des listes de sommets d'arrivée.
dic = {}

# Créer une liste pnum de taille V initialisée à 0 pour chaque index :
# Cette liste servira à stocker le nombre de prédecesseurs (in-degree) pour chaque sommet.
pnum = [0] * V

# Boucle pour lire chaque arête du graphe.
# On itère sur le nombre total d'arêtes E.
for i in range(E):

    # Lire deux entiers s et t depuis l'entrée standard :
    # s est le sommet de départ de l'arête, t est le sommet d'arrivée.
    s, t = map(int, input().split())

    # Incrémenter pnum[t] pour indiquer qu'un nouvel arc arrive sur t (t a un prédecesseur en plus).
    pnum[t] += 1
    
    # Si le sommet s n'est pas encore une clé du dictionnaire dic,
    # on initialise la valeur associée à s comme une liste vide.
    if s not in dic:
        dic[s] = []
    # Ajouter t à la liste des sommets accessibles à partir de s (arc s -> t).
    dic[s].append(t)

# Créer une file à double extrémité (deque) initialement vide.
# On l'utilisera pour la suppression efficace du premier élément.
q = deque([])

# Initialiser une liste vide 'ans', qui contiendra l'ordre topologique du graphe.
ans = []

# Parcourir tous les sommets numérotés de 0 à V-1.
for i in range(V):

    # Si le sommet i n'a aucun prédecesseur (in-degree de i == 0),
    # cela signifie qu'il peut être placé en premier dans l'ordre topologique.
    if pnum[i] == 0:
        # Ajouter le sommet i à la queue pour traitement ultérieur.
        q.append(i)
        # Ajouter le sommet i à la liste de l'ordre topologique final.
        ans.append(i)

# Traiter la file 'q' tant qu'elle n'est pas vide.
while len(q) > 0:

    # Supprimer et obtenir le premier élément actuellement dans la queue 'q'.
    now = q.popleft()

    # Vérifier si le sommet 'now' n'a pas de successeurs dans le dictionnaire dic.
    if now not in dic:
        # S'il n'a pas de successeurs, continuer directement à la prochaine itération.
        continue

    # Parcourir tous les successeurs du sommet actuel 'now'
    # (c'est-à-dire tous les sommets atteignables directement depuis 'now').
    for i in dic[now]:
        # Enlever 1 au nombre de prédecesseurs (in-degree) du sommet i,
        # car le sommet 'now' a déjà été placé dans l'ordre topologique.
        pnum[i] -= 1

        # Si i n'a plus aucun prédecesseur (in-degree == 0),
        # cela veut dire qu'il peut maintenant être traité à son tour.
        if pnum[i] == 0:
            # Ajouter le sommet i à la queue pour le traiter plus tard.
            q.append(i)
            # Ajouter le sommet i à la liste de l'ordre topologique.
            ans.append(i)

# Après avoir déterminé l'ordre topologique,
# parcourir tous les sommets pour afficher leur ordre d'apparition.
for i in range(V):
    # Afficher le i-ème élément de la liste 'ans', 
    # c'est-à-dire, l'ordre topologique du sommet portant le numéro ans[i].
    print(ans[i])