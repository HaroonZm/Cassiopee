import sys

# Augmente la limite de récursion pour gérer de grands arbres
sys.setrecursionlimit(114514)

# Lecture du nombre de sommets dans l'arbre
nombre_sommets = int(input())

# Création d'une liste d'adjacence pour représenter les connexions entre les sommets
graphe_adjacence = [[] for _ in range(nombre_sommets + 1)]

# Lecture et ajout des arêtes à la liste d'adjacence
for _ in range(nombre_sommets - 1):
    sommet_depart, sommet_arrivee = map(int, input().split())
    graphe_adjacence[sommet_depart].append(sommet_arrivee)
    graphe_adjacence[sommet_arrivee].append(sommet_depart)

# Initialisation des distances pour Fennec et Snuke à -1 (indiquant une non-visite)
distance_fennec_depuis_1 = [-1 for _ in range(nombre_sommets + 1)]
distance_snuke_depuis_N = [-1 for _ in range(nombre_sommets + 1)]

def calculer_distances(distance_array, sommet_courant, distance_actuelle):
    if distance_array[sommet_courant] == -1:
        distance_array[sommet_courant] = distance_actuelle
        for voisin in graphe_adjacence[sommet_courant]:
            calculer_distances(distance_array, voisin, distance_actuelle + 1)

# Calcul des distances pour Fennec depuis le sommet 1
calculer_distances(distance_fennec_depuis_1, 1, 0)

# Calcul des distances pour Snuke depuis le sommet N
calculer_distances(distance_snuke_depuis_N, nombre_sommets, 0)

# Décompte du nombre de sommets plus proches de Fennec ou de Snuke
nombre_sommets_proches_fennec = 0
nombre_sommets_proches_snuke = 0

for sommet in range(1, nombre_sommets + 1):
    if distance_snuke_depuis_N[sommet] < distance_fennec_depuis_1[sommet]:
        nombre_sommets_proches_snuke += 1
    else:
        nombre_sommets_proches_fennec += 1

# Affichage du gagnant
if nombre_sommets_proches_fennec > nombre_sommets_proches_snuke:
    print("Fennec")
else:
    print("Snuke")