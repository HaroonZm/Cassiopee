# Importation du module bisect et en particulier la fonction bisect_right
# bisect_right permet de trouver l'indice où insérer un élément dans une liste triée de façon à conserver l'ordre
from bisect import bisect_right

# Lecture de deux entiers N et M à partir de l'entrée standard (généralement le clavier)
# split() sépare la ligne lue en fonction des espaces, et map(int, ...) convertit chaque élément en entier
# N : nombre de préfectures ; M : nombre de villes
N, M = map(int, input().split())

# Création d'une liste vide nommée PY, qui va contenir pour chaque ville, la préfecture et l'année d'établissement
# Par exemple : PY = [[préfecture1, année1], [préfecture2, année2], ...]
PY = []

# Création d'une liste de listes appelée 'record' pour stocker pour chaque préfecture, les années d'établissement de ses villes
# On utilise la compréhension de liste pour générer (N+1) listes vides, car les préfectures sont numérotées à partir de 1 jusqu'à N inclus
record = [[] for i in range(N + 1)]

# Boucle pour lire les informations relatives à chaque ville
for i in range(M):
    # Lecture de deux entiers P et Y: P est le numéro de la préfecture, Y l'année d'établissement de la ville
    P, Y = map(int, input().split())
    # Ajout de la paire [P, Y] à la liste PY (conservation de l'ordre d'entrée pour le traitement ultérieur)
    PY.append([P, Y])
    # Ajout de l'année Y à la liste des années pour la préfecture P dans 'record'
    record[P].append(Y)

# Boucle pour trier les années d'établissement pour chaque préfecture
# La numérotation va de 1 à N inclus car 0 n'est pas utilisé (aucune préfecture 0)
for i in range(1, N + 1):
    # Tri des années pour chaque préfecture i en ordre croissant (nécessaire pour le traitement avec bisect_right)
    record[i].sort()

# Nouvelle boucle pour traiter chaque ville dans l'ordre d'entrée (celui de PY)
for i in range(M):
    # Récupère p (le numéro de la préfecture) et y (l'année) pour la i-ème ville enregistrée
    p, y = PY[i][0], PY[i][1]
    # Calcule la position de y dans la liste triée record[p] (les années de la préfecture p)
    # bisect_right retourne l'indice après le dernier élément égal à y, soit le rang de la ville pour cette année
    order = bisect_right(record[p], y)
    # Préparation de l'identifiant de la ville : 
    # str(p).zfill(6) convertit p en chaîne et complète par des zéros à gauche pour obtenir une chaîne de 6 caractères
    # str(order).zfill(6) fait la même chose pour le rang order
    # La concaténation des deux donne l'identifiant unique demandé
    print(str(p).zfill(6) + str(order).zfill(6))