from itertools import groupby

# Lecture du nombre d'entrées (N)
N = int(input())
# Lecture des valeurs d'entrée comme une liste d'entiers (D)
D = list(map(int, input().split()))

def dfs(lst, num):
    """
    Recherche récursive de la plus grande distance minimale atteignable sur un cercle de 24 unités.
    Pour chaque configuration possible d'ajout ou de retrait des décalages D[num], construit une liste de positions
    et évalue la solution finale lorsque tous les décalages ont été utilisés.

    Args:
        lst (list): Liste actuelle des positions considérées sur le cercle, initialisée avec [0] (position de départ).
        num (int): Index du décalage en cours de traitement dans la liste D.

    Effet de bord:
        Modifie la variable globale 'ans' pour conserver la meilleure solution trouvée.
    """
    global ans
    # Si tous les décalages ont été appliqués, évaluer la configuration actuelle
    if num == N:
        min_distance = 100  # Valeur suffisamment grande pour la minimisation
        # Examiner toutes les paires possibles de positions sur le cercle
        for i in range(0, N):
            for j in range(i + 1, N + 1):
                # Calcul de la distance sur le cercle modulo 24
                distance = abs(lst[i] - lst[j])
                # Prendre la plus courte distance sur le cercle (dans un sens ou dans l'autre)
                test = min(distance, 24 - distance)
                # Mise à jour de la distance minimale trouvée pour cette configuration
                min_distance = min(test, min_distance)
        # Mise à jour de la meilleure solution globale (distance minimale maximale)
        ans = max(ans, min_distance)
    else:
        # Option 1 : avancer de D[num] (dans le sens positif)
        dfs(lst + [D[num]], num + 1)
        # Option 2 : reculer de D[num] (dans le sens négatif, équivalent à 24 - D[num] sur le cercle)
        dfs(lst + [24 - D[num]], num + 1)

# Cas où le nombre de positions N est supérieur ou égal à 24
if N >= 24:
    # Avec au moins 24 positions sur un cercle de 24 unités, la distance minimale est forcément 0
    print(0)

# Cas intermédiaire : contraintes spécifiques pour N >= 12
elif N >= 12:
    # Tri de la liste des valeurs D pour faciliter le comptage des occurrences
    D.sort()
    # Groupement des valeurs identiques pour analyse des contraintes
    D_grouper = groupby(D)
    for key, group in D_grouper:
        g = len(list(group))  # Nombre d'occurrences du décalage key
        # Si l'un des décalages est 0, ce qui place deux positions au même endroit, la distance minimale est 0
        if key == 0:
            print(0)
            exit()
        # Si la valeur 12 apparaît plus d'une fois, alors deux positions sont diamétralement opposées (même distance)
        elif key == 12:
            if g > 1:
                print(0)
                exit()
        # Pour les autres valeurs, si elles apparaissent plus de deux fois, alors au moins 3 positions sont identiques modulo 24
        else:
            if g > 2:
                print(0)
                exit()
    # Si aucune des contraintes n'est violée, il est possible de placer les positions sans collision
    print(1)

# Cas général pour N < 12 : utilisation de la recherche exhaustive
else:
    ans = 0  # Initialisation du meilleur résultat
    # Démarrer la récursion avec la position de départ [0] et D[0] comme premier décalage à appliquer
    dfs([0], 0)
    print(ans)